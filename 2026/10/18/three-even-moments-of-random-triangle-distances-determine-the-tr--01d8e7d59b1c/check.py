"""Standalone exact-rational certificate for triangle pair-distance moments.
Run: python3 check.py; only Python standard library is required.
"""
from fractions import Fraction as F
from math import comb, factorial, sqrt
from random import Random
from collections import defaultdict


def mu(i, j):
    return F(2 * factorial(i) * factorial(j), factorial(i+j+2))


def diff_moment(i, j):
    return sum(((-1)**(i+j-a-b)) * comb(i,a)*comb(j,b)*mu(a,b)*mu(i-a,j-b)
               for a in range(i+1) for b in range(j+1))


# Multi-index: (power B, power C, power p, power q, power r).
Q = {(2,0,1,0,0):F(1), (1,1,1,0,0):F(1),
     (1,1,0,1,0):F(1), (1,1,0,0,1):F(-1),
     (0,2,0,1,0):F(1)}


def mul(a, b):
    out = defaultdict(F)
    for x,c in a.items():
        for y,d in b.items():
            out[tuple(s+t for s,t in zip(x,y))] += c*d
    return {x:y for x,y in out.items() if y}


def raw(k):
    z={(0,0,0,0,0):F(1)}
    for _ in range(k):
        z=mul(z,Q)
    out=defaultdict(F)
    for (i,j,a,b,c),v in z.items():
        out[(a,b,c)] += v*diff_moment(i,j)
    return {x:y for x,y in out.items() if y}


wanted={
 1:{(1,0,0):F(1,18),(0,1,0):F(1,18),(0,0,1):F(1,18)},
 2:{(2,0,0):F(1,60),(0,2,0):F(1,60),(0,0,2):F(1,60)},
 3:{(3,0,0):F(23,4200),(0,3,0):F(23,4200),(0,0,3):F(23,4200),
    (2,1,0):F(7,4200),(2,0,1):F(7,4200),(1,2,0):F(7,4200),
    (0,2,1):F(7,4200),(1,0,2):F(7,4200),(0,1,2):F(7,4200),
    (1,1,1):F(-28,4200)}
}
for k in (1,2,3):
    assert raw(k)==wanted[k], (k,raw(k))


def exact_moments(p,q,r):
    e1=p+q+r
    e2=p*q+p*r+q*r
    e3=p*q*r
    return (e1/F(18), (e1*e1-2*e2)/60,
            F(23,4200)*e1**3-F(31,2100)*e1*e2+e3/210)


def reconstruct(m):
    e1=18*m[0]
    e2=(e1**2-60*m[1])/2
    e3=210*m[2]-F(23,20)*e1**3+F(31,10)*e1*e2
    return e1,e2,e3

cases=[(F(1),F(4),F(4)), (F(2),F(2),F(5)),
       (F(1),F(1),F(1)), (F(4),F(9),F(16)),
       (F(3),F(4),F(5)), (F(7),F(9),F(11))]
for p,q,r in cases:
    a,b,c=map(lambda x:sqrt(float(x)),(p,q,r))
    assert a+b>c and a+c>b and b+c>a
    m=exact_moments(p,q,r)
    assert reconstruct(m)==(p+q+r,p*q+p*r+q*r,p*q*r)
assert exact_moments(*cases[0])[:2]==exact_moments(*cases[1])[:2]
assert exact_moments(*cases[1])[2]-exact_moments(*cases[0])[2]==F(2,105)

# Independent sampling in physical coordinates via exponential barycentrics.
rng=Random(20261016)
def bary():
    a,b,c=[rng.expovariate(1.0) for _ in range(3)]
    return b/(a+b+c),c/(a+b+c)
for p,q,r in cases:
    cross=float((p+q-r))
    sums=[0.,0.,0.]
    n=70000
    for _ in range(n):
        x1,x2=bary(); y1,y2=bary()
        B=x1-y1;C=x2-y2
        D=float(p)*B*B+cross*B*C+float(q)*C*C
        assert D>=-1e-12
        for k in range(3):sums[k]+=D**(k+1)
    exact=exact_moments(p,q,r)
    for k in range(3):
        assert abs(sums[k]/n-float(exact[k])) < 0.035*max(1.,float(exact[k])),(p,q,r,k,sums[k]/n,exact[k])
print('TRIANGLE_PAIR_DISTANCE_MOMENTS_OK exact_polynomial_orders=3 rational_cases=6 monte_carlo_samples=420000')
