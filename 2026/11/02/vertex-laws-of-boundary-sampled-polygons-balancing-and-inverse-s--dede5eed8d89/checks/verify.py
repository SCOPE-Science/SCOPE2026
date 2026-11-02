"""Exact finite occupancy and geometric tests for boundary-sampled polygons."""
from fractions import Fraction as F
from math import comb, factorial
from itertools import product
from collections import defaultdict


def distributions(p, n):
    m=len(p)
    # Direct multinomial summation in exact rational arithmetic.
    out=defaultdict(F)
    def visit(i,left,counts,weight):
        if i==m-1:
            counts=counts+[left]
            prob=weight*p[i]**left/F(factorial(left))
            out[sum(min(2,k) for k in counts)]+=prob*factorial(n)
            return
        for k in range(left+1):
            visit(i+1,left-k,counts+[k],weight*p[i]**k/F(factorial(k)))
    visit(0,n,[],F(1))
    assert sum(out.values(),F(0)) == 1
    return dict(out)

def distribution_from_exponential_gf(p,n):
    # Polynomial in t of degree at most n, coefficient in z indexed by vertex number.
    table={(0,0):F(1)}
    for prob in p:
        factors=[(0,0,F(1)),(1,1,prob)]
        for k in range(2,n+1):
            factors.append((k,2,prob**k/F(factorial(k))))
        new=defaultdict(F)
        for (t,v),c in table.items():
            for k,w,a in factors:
                if t+k <= n: new[(t+k,v+w)] += c*a
        table=new
    return {v:c*factorial(n) for (t,v),c in table.items() if t==n and c}

def stoch_dominance(a,b):
    assert all(sum(p for k,p in a.items() if k>=t)<=sum(p for k,p in b.items() if k>=t) for t in range(2,max(max(a),max(b))+2))

def expect_formula(p,n):
    if n == 0: return F(0)
    return sum(2*(1-(1-x)**n)-n*x*(1-x)**(n-1) for x in p)

samples=[([F(2,5),F(7,20),F(1,4)], [F(3,8),F(3,8),F(1,4)]),
         ([F(7,20),F(3,10),F(1,5),F(3,20)], [F(13,40),F(13,40),F(1,5),F(3,20)]),
         ([F(3,10),F(1,4),F(1,5),F(3,20),F(1,10)], [F(11,40),F(11,40),F(1,5),F(3,20),F(1,10)])]
for p,q in samples:
    assert sum(p)==sum(q)==1
    for n in range(0,11):
        dp=distributions(p,n); dq=distributions(q,n)
        assert dp==distribution_from_exponential_gf(p,n)
        assert dq==distribution_from_exponential_gf(q,n)
        stoch_dominance(dp,dq)
        assert sum(F(k)*v for k,v in dp.items())==expect_formula(p,n)
        assert sum(F(k)*v for k,v in dq.items())==expect_formula(q,n)
        if n>=3: assert expect_formula(p,n)<expect_formula(q,n)
print('EXACT_MULTINOMIAL_GFs_AND_PAIR_BALANCING_PASSED')

# Test arbitrary symmetric central binomial intervals, the basis of the full stochastic-order proof.
for k in range(1,31):
    for a in range(0,k//2+1):
        def interval(q):
            return sum(F(comb(k,j))*q**j*(1-q)**(k-j) for j in range(a,k-a+1))
        assert interval(F(1,8)) <= interval(F(1,4)) <= interval(F(3,8)) <= interval(F(1,2))
print('CENTRAL_BINOMIAL_INTERVAL_MONOTONICITY_PASSED')

# Direct convex-hull vertex count comparison for rhombi with different interior angles.
try:
    import numpy as np
    from scipy.spatial import ConvexHull
    rng=np.random.default_rng(11023)
    for angle in (0.55, 1.05, 1.57, 2.1):
        x,y=np.cos(angle),np.sin(angle)
        vertices=np.array([[0,0],[1,0],[1+x,y],[x,y]],float)
        for i in range(800):
            N=int(rng.integers(3,35)); sides=rng.integers(0,4,N); loc=rng.uniform(0.01,0.99,N)
            pts=vertices[sides]*(1-loc[:,None])+vertices[(sides+1)%4]*loc[:,None]
            if np.linalg.matrix_rank(pts-pts[0])<2: continue
            hull=ConvexHull(pts)
            expected=sum(min(2,int(np.sum(sides==j))) for j in range(4))
            assert len(hull.vertices)==expected,(len(hull.vertices),expected,sides)
    print('DIRECT_NONCONGRUENT_RHOMBUS_GEOMETRY_PASSED')
except ImportError:
    print('GEOMETRY_SCIPY_UNAVAILABLE_EXACT_TESTS_PASSED')

print('ALL_CHECKS_PASSED')
