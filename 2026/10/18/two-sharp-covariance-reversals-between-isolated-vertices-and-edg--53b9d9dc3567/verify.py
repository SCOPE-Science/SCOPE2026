#!/usr/bin/env python3
"""Independent exact-rational checks for the circular hard geometric graph sign theorem.
Run with Python 3 standard library only. Finite checks supplement, not replace, the proof.
"""
from fractions import Fraction as F
from math import comb
from itertools import product

checks = 0

def check(b, note):
    global checks
    assert b, note
    checks += 1

def circle_cov(n, r):
    assert n >= 2 and 0 < r < F(1,2)
    ell = 1-2*r
    if r >= ell:
        q = F(1)
    else:
        q = 2*r/ell-(r/ell)**2
    return F(n*(n-1),2)*ell**(n-1)*((n-2)*q-2*n*r)

def alternate_cov(n,r):
    ell = 1-2*r
    if r <= F(1,3):
        polynomial = n*r*(3-8*r)-(4-10*r)
        return F(n*(n-1),2)*ell**(n-3)*r*polynomial
    return F(n*(n-1),2)*ell**(n-1)*(n*ell-2)

def exact_grid_cov(n,m,k):
    # Locations iid uniformly on {0,...,m-1}; edge if circular grid steps <= k.
    allowed=[x for x in range(m) if min(x,m-x)>k]
    ell=F(len(allowed),m)
    p=F(2*k+1,m)
    hits=sum(min(abs(x-y),m-abs(x-y))<=k for x in allowed for y in allowed)
    q=F(hits,len(allowed)**2)
    # Direct joint probability: choose two remaining positions in the allowed set,
    # and all other n-3 positions there too. This does NOT assume the continuum Q formula.
    joint_independent_edge=F(hits,m*m)*ell**(n-3) if n>=3 else F(0)
    # (n-1 choose 2) nonincident edges, each with direct joint probability;
    # incident edges never coexist with isolation.
    joint=F(n*comb(n-1,2))*joint_independent_edge if n>=3 else F(0)
    return joint-n*ell**(n-1)*comb(n,2)*p

for n in range(2,35):
    for r in [F(1,20),F(1,10),F(1,5),F(1,4),F(3,10),F(1,3),F(7,20),F(2,5),F(49,100)]:
        check(circle_cov(n,r)==alternate_cov(n,r),('two formulae',n,r))
        # Complete sign diagram on representative rational radii.
        actual=(circle_cov(n,r)>0)-(circle_cov(n,r)<0)
        if n<=5:
            expected=-1
        elif n==6:
            expected=(r>F(1,4) and r<F(1,3))-(r<F(1,4) or r>F(1,3))
        else:
            # Compare n*r*(3-8*r)-(4-10*r) at radii <=1/3.
            signpoly=n*r*(3-8*r)-(4-10*r)
            signpart=signpoly if r<=F(1,3) else n*(1-2*r)-2
            expected=(signpart>0)-(signpart<0)
        check(actual==expected,('phase',n,r,actual,expected))

check(circle_cov(6,F(3,10))==F(72,3125),'n6 positive witness')
check(circle_cov(6,F(1,4))==0,'n6 left boundary')
check(circle_cov(6,F(1,3))==0,'n6 right boundary')
for n in range(6,35):
    upper=F(n-2,2*n)
    check(circle_cov(n,upper)==0,('upper',n))

# Independent discrete-circle conditional triple-counting check: as mesh is refined,
# covariances agree with continuum prediction to an absolute O(1/m) tolerance.
# Use rational r=(k+1/2)/m: grid edge cutoff k, removing discontinuity ambiguity.
for n,r_target in [(3,F(1,5)),(5,F(3,10)),(6,F(3,10)),(7,F(3,10)),(8,F(2,5))]:
    m=900
    k=(m*r_target.numerator//r_target.denominator)
    grid=exact_grid_cov(n,m,k)
    continuous=circle_cov(n,F(2*k+1,2*m))
    check(abs(grid-continuous)<F(1,20),('mesh convergence',n,r_target,grid,continuous))
    if n==6 and r_target==F(3,10):
        check(grid>0, 'independent finite-grid witness positive')

# Exact exhaustive circle-graph checks on a finite discrete torus.
# This is independent of the conditional-moment calculation.
for m in (5,7,11):
    for k in range(1,(m-1)//2):
        for n in (2,3,4):
            if m**n>20000: continue
            tot=0; sumi=0;sume=0;sumie=0
            for xs in product(range(m),repeat=n):
                deg=[0]*n;e=0
                for i in range(n):
                    for j in range(i+1,n):
                        dist=abs(xs[i]-xs[j]);dist=min(dist,m-dist)
                        if dist<=k:
                            deg[i]+=1;deg[j]+=1;e+=1
                isolated=sum(d==0 for d in deg)
                tot+=1;sumi+=isolated;sume+=e;sumie+=isolated*e
            exhaustive=F(sumie,tot)-F(sumi,tot)*F(sume,tot)
            analytic=exact_grid_cov(n,m,k)
            check(exhaustive==analytic,('full discrete enumeration',m,k,n,exhaustive,analytic))
print('OK: %d rational/checker assertions' % checks)
