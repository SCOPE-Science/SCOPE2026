#!/usr/bin/env python3
"""Exact arithmetic verification of a characteristic-seven Hessian intersection.
Requires SymPy 1.14 (or compatible). Run: python verify.py.
The computations use integers and the prime field F_7 only.
"""
import sympy as s

p=7
x,y,z,u,v=s.symbols('x y z u v')
F=x**3*y+y**3*z+z**3*x
G=x**5*z-5*x**2*y**2*z**2+x*y**5+y*z**5
assert s.expand(s.hessian(F,(x,y,z)).det()+54*G)==0
f=s.expand(F.subs(z,1));g=s.expand(G.subs(z,1))
A=s.Poly(s.resultant(f,g,y),x,modulus=7)
assert s.Poly(A.as_expr()-s.Poly(x*(x-2)**21,x,modulus=7).mul_ground(-1).as_expr(),x,modulus=7).is_zero or s.rem(A.as_expr(),x*(x-2)**21,x,modulus=7)==0
assert s.factor_list(A)[1]==[(s.Poly(x,x,modulus=7),1),(s.Poly(x-2,x,modulus=7),21)]
print('Resultant in x:',s.factor_list(A))

ff=s.Poly(s.expand(f.subs({x:u+2,y:v+4})),u,v,modulus=7).as_expr()
gg=s.Poly(s.expand(g.subs({x:u+2,y:v+4})),u,v,modulus=7).as_expr()
I=s.groebner([ff,gg],u,v,order='lex',modulus=7)
assert [tuple(m) for m in (poly.monoms()[0] for poly in I.polys)]==[(2,0),(1,7),(0,15)]
assert s.Poly(I.polys[-1].as_expr() - v**14*(v-3),u,v,modulus=7).is_zero
print('Affine Gröbner leading monomials:',[p.monoms()[0] for p in I.polys])
J=s.groebner([ff,gg,v**14],u,v,order='lex',modulus=7)
assert [tuple(m) for m in (poly.monoms()[0] for poly in J.polys)]==[(2,0),(1,7),(0,14)]
print('Local Gröbner leading monomials:',[p.monoms()[0] for p in J.polys])
B=[v**i for i in range(14)]+[u*v**i for i in range(7)]
assert len(B)==21

def vec(a):
    rem=J.reduce(s.expand(a))[1]
    pp=s.Poly(rem,u,v,modulus=7)
    return [int(pp.coeff_monomial(mon))%7 for mon in B]

def rank(vectors):
    if not vectors: return 0
    rows=[list(c) for c in zip(*vectors)]
    m,n=len(rows),len(rows[0]); i=0
    for j in range(n):
        t=next((k for k in range(i,m) if rows[k][j]%7),None)
        if t is None: continue
        rows[i],rows[t]=rows[t],rows[i]
        a=pow(rows[i][j],-1,7)
        rows[i]=[(a*w)%7 for w in rows[i]]
        for h in range(m):
            if h!=i and rows[h][j]:
                a=rows[h][j]
                rows[h]=[(aa-a*bb)%7 for aa,bb in zip(rows[h],rows[i])]
        i+=1
        if i==m:break
    return i

allmon={(a,b):vec(u**a*v**b) for a in range(22) for b in range(22-a)}
mdims=[rank([t for (a,b),t in allmon.items() if a+b>=d]) for d in range(22)]
assert mdims[:15]==[21,20,18,16,14,12,10,8,6,5,4,3,2,1,0]
H=[mdims[d]-mdims[d+1] for d in range(14)]
assert H==[1]+[2]*7+[1]*6
print('Local Hilbert-Samuel function:',H, 'length:',sum(H))

# Exact projective support, its three transverse points, and the exceptional point.
coords=((1,0,0),(0,1,0),(0,0,1),(2,4,1))
for point in coords:
    subs=dict(zip((x,y,z),point))
    assert int(F.subs(subs))%7==int(G.subs(subs))%7==0
for point in coords[:3]:
    # At each coordinate vertex the two gradients are linearly independent.
    vals=[[int(s.diff(poly,t).subs(dict(zip((x,y,z),point))))%7 for t in (x,y,z)] for poly in (F,G)]
    assert any((vals[0][i]*vals[1][j]-vals[0][j]*vals[1][i])%7 for i in range(3) for j in range(i+1,3))
print('Projective support: three transverse coordinate vertices plus the unique [2:4:1] fat point.')

# Finite affine support follows from v^14(v-3), with unique u above v=0 and v=3.
for v0 in (0,3):
    polynomials=[s.Poly(poly.as_expr().subs(v,v0),u,modulus=7) for poly in I.polys]
    common=polynomials[0]
    for qq in polynomials[1:]:common=s.gcd(common,qq)
    if v0==0:
        assert common.monic()==s.Poly(u**2,u,modulus=7)
    if v0==3:
        assert common.monic()==s.Poly(u+2,u,modulus=7)

print('VERIFY_OK')
