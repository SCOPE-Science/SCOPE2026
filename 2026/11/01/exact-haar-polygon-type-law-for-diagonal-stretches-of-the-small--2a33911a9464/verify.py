"""Standalone checks for the rhombicuboctahedron central-section law.
Requires Python 3 standard library only; execute: python verify.py
Checks are finite diagnostics accompanying, not replacing, the analytic proof.
"""
from itertools import product, permutations
from math import sqrt, atan2, atan, pi, hypot, exp
from random import Random

R = 1 + sqrt(2)

def plus(a,b): return a[0]+b[0],a[1]+b[1]
def minus(a,b): return a[0]-b[0],a[1]-b[1]
def times(a,b): return a[0]*b[0]+2*a[1]*b[1], a[0]*b[1]+a[1]*b[0]
def scale(a,n): return a[0]*n,a[1]*n

def sgn(a):
    x,y=a
    if x==y==0:return 0
    if x>=0 and y>=0:return 1
    if x<=0 and y<=0:return -1
    d=x*x-2*y*y
    return (1 if d>0 else -1) * (1 if x>0 else -1)

ONE=(1,0); BIG=(1,1)
VERTICES=[]
for idx in range(3):
    for signs in product((-1,1),repeat=3):
        VERTICES.append(tuple(scale(BIG if k==idx else ONE,signs[k]) for k in range(3)))
assert len(set(VERTICES))==24

def square_distance(a,b):
    d=(0,0)
    for x,y in zip(a,b):
        t=minus(x,y)
        d=plus(d,times(t,t))
    return d

EDGES=[(i,j) for i in range(24) for j in range(i) if square_distance(VERTICES[i],VERTICES[j])==(4,0)]
assert len(EDGES)==48

def principal_index(v):
    return next(k for k,p in enumerate(v) if p[1] != 0)

EDGES_WITHIN=[(i,j) for i,j in EDGES if principal_index(VERTICES[i])==principal_index(VERTICES[j])]
EDGES_SWAPPED=[(i,j) for i,j in EDGES if principal_index(VERTICES[i])!=principal_index(VERTICES[j])]
assert len(EDGES_WITHIN)==len(EDGES_SWAPPED)==24

def dot_sign(v,u):
    return sgn(plus(plus(scale(v[0],u[0]),scale(v[1],u[1])),scale(v[2],u[2])))

def counts(u):
    signs=[dot_sign(v,u) for v in VERTICES]
    assert 0 not in signs
    return (sum(signs[i]*signs[j]<0 for i,j in EDGES_WITHIN),
            sum(signs[i]*signs[j]<0 for i,j in EDGES_SWAPPED))

def sign_pattern(u):
    a,b,c=u
    aa=sgn(minus(minus(scale(BIG,b),(a,0)),(c,0)))
    bb=sgn(plus(minus(scale(BIG,b),(a,0)),(c,0)))
    cc=sgn(minus(minus(scale(BIG,c),(a,0)),(b,0)))
    dd=sgn(plus(minus(scale(BIG,c),(a,0)),(b,0)))
    assert 0 not in (aa,bb,cc,dd)
    return ''.join('+' if t>0 else '-' for t in (aa,bb,cc,dd))

EXPECTED={
    '----':(8,0), '-+--':(8,4), '-+-+':(8,4),
    '++--':(4,8), '++-+':(4,8), '++++':(0,12),
}
REPRESENTATIVES={
    '----':(100,2,1), '-+--':(100,30,28), '-+-+':(100,30,29),
    '++--':(100,42,1), '++-+':(100,51,21), '++++':(100,73,72),
}
for pat,u in REPRESENTATIVES.items():
    assert sign_pattern(u)==pat, (pat,u,sign_pattern(u))
    assert counts(u)==EXPECTED[pat], (pat,counts(u))

cases=0
for b in range(1,90):
    for c in range(1,b):
        u=(101,b,c)
        try: pat=sign_pattern(u)
        except AssertionError: continue
        assert pat in EXPECTED
        n1,n2=counts(u)
        assert (n1,n2)==EXPECTED[pat],(u,pat,n1,n2)
        expected=8 if sgn(plus(minus(scale(BIG,b),(101,0)),(c,0)))<0 else 12
        assert n1+n2==expected
        cases+=1
assert cases>3800

def solid_angle(i,j,k,s):
    alpha=s[i]/s[j]; beta=s[i]/s[k]
    aa=R+sqrt(R*R+alpha*alpha)
    bb=R+1+sqrt((R+1)**2+alpha*alpha+beta*beta)
    return 2*atan(alpha*beta/(aa*bb+alpha*alpha))

def p8(s):
    return (2/pi)*sum(solid_angle(*ijk,s) for ijk in permutations(range(3)))

den=(R+hypot(R,1))*(R+1+sqrt((R+1)**2+2))+1
p_regular=(24/pi)*atan(1/den)
assert abs(p8([1,1,1])-p_regular)<1e-14

def simpson(f,a,b,n):
    assert n%2==0
    h=(b-a)/n
    return h/3*(f(a)+f(b)+4*sum(f(a+i*h) for i in range(1,n,2))+2*sum(f(a+i*h) for i in range(2,n,2)))

def integrand(x,branch):
    y=x if branch==0 else 1-R*x
    return y/((1+x*x)*sqrt(1+x*x+y*y))
area=simpson(lambda x:integrand(x,0),0,1/(R+1),6000)+simpson(lambda x:integrand(x,1),1/(R+1),1/R,6000)
assert abs((12/pi)*area-p_regular)<2e-12

rng=Random(173)
for s in ((1,1,1),(2,1,1),(1,3,5),(.5,1.2,2)):
    sample_n=80000
    hits=0
    for _ in range(sample_n):
        t=sorted((s[i]*abs(rng.gauss(0,1)) for i in range(3)),reverse=True)
        hits+=(t[0]>R*t[1]+t[2])
    empirical=hits/sample_n
    assert abs(empirical-p8(s))<.011,(s,empirical,p8(s))
    print('stretch',s,'analytic',round(p8(s),10),'simulation',round(empirical,6))

print('PASS: 24 exact vertices, 48 exact edges, 6 feasible sign chambers,',cases,'exact grid classifications')
print('PASS: spherical cone formula, independent gnomonic quadrature, Gaussian-normal simulations')
print('regular octagon probability=',format(p_regular,'.15f'))
print('regular dodecagon probability=',format(1-p_regular,'.15f'))
print('regular expected sides=',format(12-4*p_regular,'.15f'))
