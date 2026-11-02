"""Independent exact enumeration: Groebner smoothness and finite-field factorization.
Requires Python 3 and SymPy 1.14. No external files or network.
"""
from collections import Counter
from itertools import product
import sympy as sp

P=5
x,y,z,t=sp.symbols('x y z t')
mon=[x**4,y**4,z**4,x*x*y*y,x*x*z*z,y*y*z*z]
pts=[(1,a,b) for a in range(P) for b in range(P)]+[(0,1,a) for a in range(P)]+[(0,0,1)]

def norm(v):
    lam=pow(next(a for a in v if a%P),-1,P)
    return tuple((lam*a)%P for a in v)

def basis(line):
    a,b,c=line
    if c:
        return (1,0,-a*pow(c,-1,P)%P),(0,1,-b*pow(c,-1,P)%P)
    if b:
        return (1,-a*pow(b,-1,P)%P,0),(0,0,1)
    return (0,1,0),(0,0,1)

line_rows=[]
for line in sorted(set(map(norm,pts))):
    u,v=basis(line)
    rows=[]
    for m in mon:
        expr=sp.expand(m.subs({x:u[0]+v[0]*t,y:u[1]+v[1]*t,z:u[2]+v[2]*t},simultaneous=True))
        rows.append(tuple(int(sp.Poly(expr,t,modulus=P).nth(i))%P for i in range(5)))
    line_rows.append(rows)
assert len(line_rows)==31

def smooth(coeff):
    F=sum(a*m for a,m in zip(coeff,mon))
    for one,other in ((x,(y,z)),(y,(x,z)),(z,(x,y))):
        G=sp.expand(F.subs(one,1))
        ideals=[G,*[sp.diff(G,u) for u in other]]
        if list(sp.groebner(ideals,*other,modulus=P)) != [1]:return False
    return True

def contact(coeff,rows):
    values=[sum(a*R[i] for a,R in zip(coeff,rows))%P for i in range(5)]
    assert any(values)
    polynomial=sp.Poly(sum(values[i]*t**i for i in range(5)),t,modulus=P)
    if (4-polynomial.degree())%2:return None
    scalar,factors=sp.factor_list(polynomial, modulus=P)
    if any(m%2 for f,m in factors):return None
    # The square root's homogenization has degree 2, with a zero at infinity if needed.
    h=sp.Poly(1,t,modulus=P)
    for f,m in factors:
        h=h*f**(m//2)
    h0,h1,h2=[int(h.nth(i))%P for i in range(3)]
    disc=(h1*h1-4*h0*h2)%P
    if disc==0:return 0
    if disc in (1,4):return 1
    return 2

count=Counter();total=0;bc=Counter()
for a,b,c,d,e,f in product(range(P),repeat=6):
    coeff=(a,b,c,d,e,f)
    if not any(coeff) or next(v for v in coeff if v)!=1:continue
    if not smooth(coeff):continue
    total+=1
    sig=[0,0,0]
    for rows in line_rows:
        ctype=contact(coeff,rows)
        if ctype is not None:sig[ctype]+=1
    count[tuple(sig)]+=1;bc[sum(sig)]+=1
expected={
(0,0,0):126,(0,0,2):120,(0,2,0):168,(2,0,0):72,
(0,0,4):28,(0,2,2):48,(0,4,0):72,(2,0,2):24,
(4,0,0):30,(2,0,4):36,(2,2,2):24,(2,4,0):12,
(0,2,6):24,(8,0,0):9,(0,0,16):7}
print('SMOOTH',total,'SIGNATURES',sorted(count.items()))
print('RATIONAL_BITANGENTS',sorted(bc.items()))
assert total==800 and count==expected
print('INDEPENDENT_VERIFY_OK')
