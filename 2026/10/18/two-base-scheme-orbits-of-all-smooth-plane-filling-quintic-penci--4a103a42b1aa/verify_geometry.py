"""Exact geometry certificates for smooth Tallini quintic pencils over F3.
Needs Python 3 with SymPy, and enumerate_pencils.py in the same directory.
"""
import sympy as sp
from enumerate_pencils import (smooth, lines, orbits, full, prod, norm, gens, trans, GL, T, P)
X,Y,Z=sp.symbols('X Y Z')
vars=(X,Y,Z)

def curve(v):
    A=full(v)
    v0=sp.Matrix(vars)
    v1=sp.Matrix([w**3 for w in vars])
    v2=sp.Matrix([sum(A[i][j]*vars[j] for j in range(3)) for i in range(3)])
    return sp.expand(sp.det(sp.Matrix.hstack(v0,v1,v2)))

def chart_polynomial(f,chart):
    vv=[w for w in vars if w!=chart]
    return sp.Poly(f.subs(chart,1),*vv,modulus=3).as_expr(),vv

assert len(smooth)==576
assert len(lines)==2016
assert sorted(len_orbit for _,len_orbit,_ in orbits)==[144,1872]
assert len(GL)==5616
assert all(len(P)==13 for _ in [0])
assert all(all(T[a][j]!=T[b][j] for j in range(13)) for penc in lines for a,b in [tuple(penc)[:2]])
# Exhaustively prove the indicated generators generate all of PGL_3(F3).
def key(A):
    first=next(x for row in A for x in row if x)
    return tuple(tuple((x*(1 if first==1 else 2))%3 for x in row) for row in A)
identity=((1,0,0),(0,1,0),(0,0,1))
group={identity};stack=[identity]
while stack:
    a=stack.pop()
    for g in gens:
        b=key(prod(a,g))
        if b not in group: group.add(b);stack.append(b)
assert len(group)==5616

# Under the proved full action, there are two orbits of smooth quintics.
S=set(smooth);seen=set();smoothsizes=[]
for v in smooth:
    if v in seen:continue
    orbit={v};stack=[v]
    while stack:
        a=stack.pop()
        for g in gens:
            b=trans(g,a)
            assert b in S
            if b not in orbit:orbit.add(b);stack.append(b)
    seen.update(orbit);smoothsizes.append((v,len(orbit)))
assert sorted(q for _,q in smoothsizes)==[144,432]
for v,n in smoothsizes:
    f=curve(v)
    for chart in vars:
        local,w=chart_polynomial(f,chart)
        gb=sp.groebner([local,sp.diff(local,w[0]),sp.diff(local,w[1])],*w,order='lex',modulus=3)
        assert list(gb)==[1],('singular geometric point',n,chart)
print('Exact geometric smoothness: 576 individual curves, 2 PGL orbits, verified on all affine charts')

irreducible_degree12=Z**12-Z**9+Z**8-Z**7+Z**6-Z**5+Z**4-Z**3+Z**2-Z+1
irreducible_degree3=Z**3-Z**2+Z+1
assert sp.Poly(irreducible_degree12,Z,modulus=3).is_irreducible
assert sp.Poly(irreducible_degree3,Z,modulus=3).is_irreducible
assert sp.gcd(sp.Poly(Z**3-Z,Z,modulus=3),sp.Poly(irreducible_degree3,Z,modulus=3)).degree()==0
assert sp.gcd(sp.Poly(Z**3-Z,Z,modulus=3),sp.Poly(irreducible_degree12,Z,modulus=3)).degree()==0
for seed,sz,_ in orbits:
    aa,bb=tuple(seed)[:2]
    f,g=curve(aa),curve(bb)
    for chart in vars:
        ff,vv=chart_polynomial(f,chart)
        gg,_=chart_polynomial(g,chart)
        gb=sp.groebner([ff,gg],*vv,order='lex',modulus=3)
        assert gb.is_zero_dimensional
        jac=sp.diff(ff,vv[0])*sp.diff(gg,vv[1])-sp.diff(ff,vv[1])*sp.diff(gg,vv[0])
        gr=sp.groebner([ff,gg,jac],*vv,order='lex',modulus=3)
        if sz==1872: assert list(gr)==[1],('not reduced',chart)
        else: assert list(gr)!=[1],('unexpectedly reduced',chart)
        if chart==X:
            univ=[h.as_expr() for h in gb.polys if h.as_expr().free_symbols<={Z}]
            assert len(univ)==1
            expected=Z*(Z-1)*(Z+1)*(irreducible_degree12 if sz==1872 else irreducible_degree3**4)
            assert sp.Poly(univ[0]-expected,Z,modulus=3).is_zero
            # On the degree-3 or degree-12 residual component, Y is uniquely determined
            # by the second Groebner polynomial as Z^3-Z is nonzero in either residue field.
            assert any(sp.Poly(h.as_expr(),Y,Z,modulus=3).degree(Y)==1 for h in gb.polys)
    print('Pencil orbit',sz, 'stabilizer',5616//sz,'base scheme:',
          '13 rational + one reduced degree-12 point' if sz==1872 else
          '13 rational + one degree-3 point of local multiplicity four')
print('All projective-orbit, Groebner, transversality, and base-scheme certificates passed')
