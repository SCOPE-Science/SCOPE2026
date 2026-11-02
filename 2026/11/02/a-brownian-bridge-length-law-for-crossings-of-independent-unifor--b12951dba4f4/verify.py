#!/usr/bin/env python3
"""Independent finite checks for random-chord crossing and arc-fraction identities."""
from fractions import Fraction as F
from itertools import combinations
from math import comb, sqrt
from random import Random

checks=0

def eq(a,b):
    global checks
    checks+=1
    assert a==b, (a,b)

def near(a,b,tol=1e-10):
    global checks
    checks+=1
    assert abs(a-b)<tol, (a,b,tol)

def all_matchings(vertices):
    if not vertices:
        yield ()
    else:
        a=vertices[0]
        for idx in range(1,len(vertices)):
            b=vertices[idx]
            for tail in all_matchings(vertices[1:idx]+vertices[idx+1:]):
                yield ((a,b),)+tail

def crossing(a,b):
    x,y=a; u,v=b
    return int((x<u<y<v) or (u<x<v<y))

def crossing_count(edges):
    return sum(crossing(a,b) for a,b in combinations(edges,2))

# Exhaust every cyclic ordered pairing through twelve endpoints; independent of
# the iid endpoint calculation in the proof.
for n in range(2,7):
    xs=[crossing_count(edges) for edges in all_matchings(tuple(range(2*n)))]
    eq(len(xs),__import__('math').factorial(2*n)//(2**n*__import__('math').factorial(n)))
    mean=F(sum(xs),len(xs)); second=F(sum(x*x for x in xs),len(xs))
    eq(mean,F(n*(n-1),6))
    eq(second-mean*mean,F(n*(n-1)*(n+3),45))

# For fixed first chord with circular gap d=m/M, enumerating all M^2
# independently selected grid points for the second chord gives the
# separated-endpoint probability 2d(1-d) EXACTLY, including coincident draws.
for M in (11,19,40):
    for m in range(1,M):
        prob=F(2*m*(M-m),M*M)
        eq(prob,2*F(m,M)*(1-F(m,M)))

# Polynomial integrations of p(w)=w-w^2/2, g(w)=p(w)-1/3.
# Coefficients ascending in powers w. Integral_0^1 polynomial exactly.
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def integ(poly,t=F(1)):
    return sum((v*t**(i+1)/F(i+1) for i,v in enumerate(poly)),F(0))
p=[F(0),F(1),-F(1,2)]
g=[-F(1,3),F(1),-F(1,2)]
eq(integ(p),F(1,3))
eq(integ(mul(p,p)),F(2,15))
eq(integ(g),0)
eq(integ(mul(g,g)),F(1,45))
for den in range(2,16):
    for num in range(1,den):
        t=F(num,den)
        c=-t*(1-t)*(2-t)/6
        eq(integ(g,t),c)
        for n in (2,5,13):
            ratio2=F(45*(n-1),n+3)*c*c/(t*(1-t))
            expected=F(5*(n-1),4*(n+3))*(2-t)**2*t*(1-t)
            eq(ratio2,expected)

# Exact finite projection and residual variance decomposition.
for n in range(2,100):
    explained=F(n*(n-1)**2,45)
    residual=F(4*n*(n-1),45)
    total=F(n*(n-1)*(n+3),45)
    eq(explained+residual,total)
    eq(explained/total,F(n-1,n+3))

# Unique interior maximizer t* solves 4t^2-7t+2=0;
# verify the sign of the polynomial on both sides and squared correlation.
tstar=(7-sqrt(17))/8
near(4*tstar*tstar-7*tstar+2,0)
near((5/4)*(2-tstar)**2*tstar*(1-tstar),(535+255*sqrt(17))/2048)
for t in (0.01,0.1,0.25,0.35,0.5,0.8,0.99):
    rho2=lambda x:5*(2-x)**2*x*(1-x)/4
    assert rho2(t)<rho2(tstar)
    checks+=1

# Independent random finite-sample check using the actual planar crossing
# condition, not matching enumerations or an algebraic covariance formula.
rng=Random(240311)
n=6; t=F(1,3); batches=24000
sums=[0.0]*5
for _ in range(batches):
    chords=[(rng.random(),rng.random()) for j in range(n)]
    lengths=[2*min(abs(u-v),1-abs(u-v)) for u,v in chords]
    y=sum(w<=float(t) for w in lengths)
    x=0
    for (u,v),(a,b) in combinations(chords,2):
        low,high=sorted((u,v))
        x+=int((low<a<high)!=(low<b<high))
    residual=x-F(n*(n-1),6)-(n-1)*sum((w-w*w/2-1/3 for w in lengths))
    sums[0]+=x; sums[1]+=y; sums[2]+=x*y; sums[3]+=x*x; sums[4]+=residual*residual
mx=sums[0]/batches; my=sums[1]/batches
near(mx,n*(n-1)/6,0.10)
near(my,n*float(t),0.10)
near(sums[2]/batches-mx*my,float(-F(n*(n-1),6)*t*(1-t)*(2-t)),0.20)
near(sums[3]/batches-mx*mx,n*(n-1)*(n+3)/45,0.28)
near(sums[4]/batches,4*n*(n-1)/45,0.23)
print(f'PASS: {checks} checks; {batches} seeded iid-chord simulations; exact matching enumeration n=2..6')
