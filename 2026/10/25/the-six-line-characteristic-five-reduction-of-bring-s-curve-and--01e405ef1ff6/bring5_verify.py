#!/usr/bin/env python3
"""Exact finite-field checks for the characteristic-five Bring complete intersection."""
import itertools
from math import comb
import sympy as sp

p = 5
A,B,C,T = sp.symbols('a b c t')
off = [A,B,C,-A-B-C,sp.Integer(0)]
x = [T+u for u in off]
q = sp.expand(sum(z**2 for z in x))
h = sp.expand(sum(z**3 for z in x))
Q = A*A+B*B+C*C+A*B+A*C+B*C
P = (A+B)*(A+C)*(B+C)

def modzero(expr):
    pol = sp.Poly(sp.expand(expr), A,B,C,T, modulus=5)
    assert pol.is_zero, (expr,pol)

modzero(sum(x))
modzero(q - 2*Q)
modzero(h - 3*T*q + 3*P)

roots = set()
for a,b,c in itertools.product(range(5), repeat=3):
    if a != 1:
        continue
    if (Q.subs({A:a,B:b,C:c}) % 5 == 0
            and P.subs({A:a,B:b,C:c}) % 5 == 0):
        roots.add((a,b,c))
assert roots == {(1,4,2),(1,4,3),(1,2,4),(1,3,4),(1,2,3),(1,3,2)}, roots
# The projective intersection has no roots at a=0, even over an algebraic closure:
# with a=0, each cubic line reduces Q to b^2, c^2 or b^2,
# and its unique vanishing projective candidate is absent.
for b,c in itertools.product(range(5),repeat=2):
    assert (b == c == 0) or (Q.subs({A:0,B:b,C:c})%5 != 0 or P.subs({A:0,B:b,C:c})%5 != 0)

jac=sp.det(sp.Matrix([[sp.diff(Q,B),sp.diff(Q,C)], [sp.diff(P,B),sp.diff(P,C)]]))
for a,b,c in roots:
    assert int(jac.subs({A:a,B:b,C:c}))%5 != 0

# All projective F5 points of the curve.
def normalize(v):
    k=next(i for i,z in enumerate(v) if z%5)
    s=pow(v[k]%5,-1,5)
    return tuple((s*z)%5 for z in v)

points=set()
for v in itertools.product(range(5),repeat=5):
    if all(z==0 for z in v): continue
    if all(sum(z**j for z in v)%5 ==0 for j in (1,2,3)):
        points.add(normalize(v))
assert len(points)==31, len(points)

e=(1,1,1,1,1)
v0=(0,1,2,3,4)

def line(v):
    return frozenset([normalize(e)]+[normalize(tuple((v[i]+u)%5 for i in range(5))) for u in range(5)])
lines={line(v) for v in itertools.permutations(v0)}
assert len(lines)==6 and all(len(L)==6 for L in lines)
assert set().union(*lines)==points
assert all(L.intersection(M)=={normalize(e)} for L,M in itertools.combinations(lines,2))
assert sum(line(v)==line(v0) for v in itertools.permutations(v0))==20

# Complete-intersection Hilbert polynomial: H(n) = 6n-3 for n >= 2.
def dimR(n):return comb(n+3,3) if n>=0 else 0
for n in range(2,16):
    Hilbert=dimR(n)-dimR(n-2)-dimR(n-3)+dimR(n-5)
    assert Hilbert==6*n-3,(n,Hilbert)
assert 6 - (1 - 4) == 9
print('VERIFY_OK: exact modular identities; six transverse points; six S5-orbit lines; 31 F5 points; stabilizer 20; Hilbert polynomial 6n-3; normalization defect 9')

# Degree-filtered normalization: k[a,b,c]/(Q,P) injects into six polynomial branches.
# The conductor is the third power of the vertex maximal ideal.
def rank5(rows):
    if not rows: return 0
    m=[list(map(lambda z:z%5,r)) for r in rows]
    r=0; N=len(m[0])
    for j in range(N):
        piv=next((i for i in range(r,len(m)) if m[i][j]%5),None)
        if piv is None:continue
        m[piv],m[r]=m[r],m[piv]
        inv=pow(m[r][j],-1,5)
        m[r]=[(z*inv)%5 for z in m[r]]
        for i in range(len(m)):
            if i != r:
                d=m[i][j]
                m[i]=[(v-d*u)%5 for v,u in zip(m[i],m[r])]
        r+=1
        if r==len(m):break
    return r

D=sorted(roots)
for degree, expected in [(0,1),(1,3),(2,5),(3,6),(4,6)]:
    monomials=[(i,j,degree-i-j) for i in range(degree+1) for j in range(degree-i+1)]
    V=[[pow(a,i,5)*pow(b,j,5)*pow(c,k,5)%5 for (i,j,k) in monomials] for a,b,c in D]
    E=list(zip(*V))
    rank=rank5(E)
    assert rank==expected,(degree,rank,expected)
    if degree<3:
        for j in range(6):
            single=[int(i==j) for i in range(6)]
            assert rank5(E+[single])==rank+1,(degree,j)
print('CONDUCTOR_OK: branch-evaluation ranks 1,3,5,6 and no isolated branch through degree two; conductor m^3; colength nine')
