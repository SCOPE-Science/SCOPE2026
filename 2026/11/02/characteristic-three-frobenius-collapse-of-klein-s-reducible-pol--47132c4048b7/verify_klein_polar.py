#!/usr/bin/env python3
"""Exact Klein-polar reduction and finite-field incidence certificate.

Requires Python 3.10+ and sympy (tested with sympy 1.13+).
Run: python verify_klein_polar.py
All arithmetic is exact; no files or network connections are required.
"""
from itertools import combinations
from collections import Counter, defaultdict
import sympy as sp

x,y,z=sp.symbols('x y z')
V=(x,y,z)
F=x**3*y+y**3*z+z**3*x
H=x*y**5+y*z**5+z*x**5-5*x**2*y**2*z**2
hess=sp.hessian(F,V)
cols=sp.Matrix([sp.diff(H,v) for v in V])
border=hess.row_join(cols).col_join(sp.Matrix([[*cols,0]]))
B=sp.Poly(sp.expand(border.det(method='berkowitz')), *V,domain='ZZ')
assert all(int(c)%9==0 for c in B.coeffs())
Phi14=B.as_expr()/9
J=sp.Poly(sp.expand(sp.Matrix([[sp.diff(t,v) for v in V]
                             for t in (F,H,Phi14)]).det(method='berkowitz')),*V,domain='ZZ')
assert all(int(c)%14==0 for c in J.coeffs())
P=sp.Poly(J.as_expr()/14,*V,domain='ZZ')
assert P.total_degree()==21 and P.coeff_monomial(x**21)==1
assert sp.Poly(P.as_expr()-P.as_expr().xreplace({x:y,y:z,z:x}),*V).is_zero
T=(sp.diff(F,x),sp.diff(F,y),sp.diff(F,z))
Q=sp.Poly(sp.expand(P.as_expr().subs(dict(zip(V,T)),simultaneous=True)),*V,domain='ZZ')
Quot,Rem=sp.div(Q,P,domain='ZZ')
assert Rem.is_zero and Quot.total_degree()==42
assert all(int(c)%3==0 for c in sp.Poly(Quot.as_expr()-P.as_expr()**2,*V,domain='ZZ').coeffs())
assert all(int(c)%3==0 for c in sp.Poly(Q.as_expr()-P.as_expr()**3,*V,domain='ZZ').coeffs())
# T modulo 3 is (z**3,x**3,y**3), so cyclic invariance implies
# P(T**k) mod 3 = P**(3**k) for every integer k>=0.

# The monic degree-six modulus is irreducible over F_3. Checking that every
# nonzero element has multiplicative order dividing 728 independently proves
# the quotient has no zero divisors (hence is F_729).
MOD=(1,2,0,1,1,1,1) # 1 - T + T**3 + T**4 + T**5 + T**6
DIG=[tuple(n//3**i%3 for i in range(6)) for n in range(729)]
def enc(t): return sum((int(u)%3)*3**i for i,u in enumerate(t))
def add(a,b):return enc((DIG[a][i]+DIG[b][i] for i in range(6)))
def neg(a):return enc((-DIG[a][i] for i in range(6)))
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    if not a or not b:return 0
    p=[0]*11
    for i in range(6):
        for j in range(6):p[i+j]=(p[i+j]+DIG[a][i]*DIG[b][j])%3
    for k in range(10,5,-1):
        t=p[k]
        for j in range(6):p[k-6+j]=(p[k-6+j]-t*MOD[j])%3
    return enc(p[:6])
def power(a,n):
    if n<0:
        assert a!=0
        return power(power(a,727),-n)
    r=1
    while n:
        if n&1:r=mul(r,a)
        a=mul(a,a);n//=2
    return r
assert all(power(a,728)==1 for a in range(1,729))
tt=sp.symbols('t')
assert sorted(f.degree() for f,e in sp.factor_list(sp.Poly(tt**21-tt**7+1,tt,modulus=3))[1] for _ in range(e))==[3,6,6,6]
roots=[a for a in range(729) if add(sub(power(a,21),power(a,7)),1)==0]
assert len(roots)==21 and len(set(roots))==21
lines=[(1,neg(t),sub(power(t,12),power(t,-2))) for t in roots]
assert len(set(lines))==21

# Recover the entire degree-21 polynomial, not just values at 729 points.
prod={(0,0,0):1}
for ell in lines:
    nxt={}
    for mon,a in prod.items():
        for i,b in enumerate(ell):
            e=list(mon);e[i]+=1;e=tuple(e)
            nxt[e]=add(nxt.get(e,0),mul(a,b))
    prod={e:a for e,a in nxt.items() if a}
target={m:int(c)%3 for m,c in P.terms() if int(c)%3}
assert prod==target, 'All 21 linear factors form precisely the primitive Klein polynomial mod 3.'

def cross(u,v):
    return (sub(mul(u[1],v[2]),mul(u[2],v[1])),
            sub(mul(u[2],v[0]),mul(u[0],v[2])),
            sub(mul(u[0],v[1]),mul(u[1],v[0])))
def norm(p):
    a=next(c for c in p if c)
    return tuple(mul(c,power(a,727)) for c in p)
def field_degree(p):
    for d in (1,2,3,6):
        if norm(tuple(power(a,3**d) for a in p))==p:return d
    raise AssertionError('Unexpected field degree')
points=defaultdict(set)
for i,j in combinations(range(21),2):points[norm(cross(lines[i],lines[j]))].update((i,j))
assert len(points)==49 and sum(len(v)*(len(v)-1)//2 for v in points.values())==210
assert Counter(map(len,points.values()))==Counter({3:28,4:21})
assert Counter(field_degree(norm(line)) for line in lines)==Counter({3:3,6:18})
assert Counter((len(indices),field_degree(p)) for p,indices in points.items())==Counter({(3,1):1,(3,3):3,(3,6):24,(4,3):3,(4,6):18})
assert all(a==0 or a==1 or a==2 for a in norm((1,1,1)))
assert len(points[norm((1,1,1))])==3
print('KLEIN_POLAR_CHAR3_FROBENIUS_TOWER_AND_F729_ARITHMETIC_CERTIFICATE_PASS')
print('lines: 21 (degree-3 Frobenius 3; degree-6 Frobenius 18)')
print('points: 28 triples (degrees 1:1, 3:3, 6:24); 21 quadruples (degrees 3:3, 6:18)')
