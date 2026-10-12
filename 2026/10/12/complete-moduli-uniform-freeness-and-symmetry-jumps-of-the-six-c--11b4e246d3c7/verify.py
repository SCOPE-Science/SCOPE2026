"""Exact symbolic consistency checks for a family of conic--line arrangements.
Run: python3 verify.py (Python standard library only).
These computations supplement, but do not replace, the geometric proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import gcd

# Multivariate polynomials over the integers in variables x,y,z,l,
# stored as exponent tuples with integer coefficients.
Z = (0, 0, 0, 0)

def var(k):
    e = list(Z); e[k] = 1
    return {tuple(e): 1}

def const(k):
    return {Z: int(k)} if k else {}

def add(*ps):
    ans = {}
    for p in ps:
        for e, c in p.items():
            ans[e] = ans.get(e, 0) + c
            if not ans[e]: del ans[e]
    return ans

def scale(p, a):
    return {e: c*a for e, c in p.items() if c*a}

def neg(p): return scale(p, -1)

def sub(p,q): return add(p,neg(q))

def mul(*ps):
    ans = const(1)
    for p in ps:
        nxt={}
        for e, c in ans.items():
            for f,d in p.items():
                k=tuple(e[i]+f[i] for i in range(4))
                nxt[k]=nxt.get(k,0)+c*d
        ans={e:c for e,c in nxt.items() if c}
    return ans

def deriv(p, k):
    ans={}
    for e,c in p.items():
        if e[k]:
            f=list(e);f[k]-=1;f=tuple(f)
            ans[f]=ans.get(f,0)+c*e[k]
    return {e:c for e,c in ans.items() if c}

def evaluate(p, values):
    return sum(c * __import__('functools').reduce(lambda u,v:u*v,
             (values[i]**e[i] for i in range(4)),1) for e,c in p.items())

x,y,z,l=(var(i) for i in range(4))
S=add(x,y,z)
L=mul(x,y,z,sub(x,y),sub(x,z),sub(y,z))
Q=add(mul(x,y),neg(mul(l,x,z)),mul(sub(l,const(1)),y,z))
F=mul(L,Q)
# D=sum x_i^2 d/dx_i, E=sum x_i d/dx_i, all lambda-independent.
D=lambda p:add(mul(x,x,deriv(p,0)),mul(y,y,deriv(p,1)),mul(z,z,deriv(p,2)))
E=lambda p:add(mul(x,deriv(p,0)),mul(y,deriv(p,1)),mul(z,deriv(p,2)))
assert D(L)==scale(mul(S,L),3)
assert D(Q)==mul(S,Q)
assert E(F)==scale(F,8)
assert add(scale(D(F),2),neg(mul(S,E(F))))=={}
T=[sub(scale(mul(v,v),2),mul(v,S)) for v in (x,y,z)]
assert add(*(mul(T[k],deriv(F,k)) for k in range(3)))=={}

# Conic equation and complete-quadrangle lines in a projective plane.
pts=[(1,0,0),(0,1,0),(0,0,1),(1,1,1)]
lines=[(1,0,0),(0,1,0),(0,0,1),(1,-1,0),(1,0,-1),(0,1,-1)]

def norm(v):
    g=0
    for q in v: g=gcd(g,abs(q))
    v=tuple(q//g for q in v)
    for q in v:
        if q: return v if q>0 else tuple(-t for t in v)
    raise ValueError('zero vector')

def cross(u,v):
    return norm((u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]))

inc={}
for a,b in combinations(lines,2):
    p=cross(a,b)
    inc.setdefault(p,set()).update(i for i,v in enumerate(lines) if sum(v[j]*p[j] for j in range(3))==0)
assert Counter(map(len,inc.values()))==Counter({3:4,2:3})
assert set(p for p,I in inc.items() if len(I)==3)==set(pts)
assert set(p for p,I in inc.items() if len(I)==2)=={(1,1,0),(1,0,1),(0,1,1)}
for p,I in inc.items():
    qp=add(mul(x,y),neg(mul(l,x,z)),mul(sub(l,const(1)),y,z))
    val=evaluate(qp,tuple(p)+(Fraction(3),))
    assert (val==0)==(len(I)==3)

# Anharmonic orbit and the classical quotient invariant.
def orbit(a):
    return {a,1-a,1/a,1/(1-a),a/(a-1),(a-1)/a}
def j(a): return 256*(1-a+a*a)**3/(a*a*(1-a)**2)
for a in map(Fraction,[3,4,5,7]):
    assert len(orbit(a))==6
    assert all(j(b)==j(a) for b in orbit(a))
for a in [Fraction(-1),Fraction(1,2),Fraction(2)]:
    assert len(orbit(a))==3 and j(a)==1728
assert len(orbit(Fraction(3)))==6
print('VERIFY_OK universal_syzygy=True singularities=4_ordinary_quadruples+3_nodes mdr_upper=2 generic_anharmonic_orbit=6 harmonic_orbit=3 j_harmonic=1728')
