"""Exact independent reproduction checks for an exchangeable star-outbreak model.

Run: python beta_star_verify.py
Standard library only. Enumerates all vaccination sets for representative graphs
and checks a wide rational parameter grid, independent of the symbolic proof.
"""
from fractions import Fraction as Q
from math import comb
from itertools import combinations

def rising(x,n):
    result=Q(1)
    for j in range(n): result*=x+j
    return result

def prob_exactly(n,k,a,b):
    if k<0 or k>n: return Q(0)
    return Q(comb(n,k))*rising(a,k)*rising(b,n-k)/rising(a+b,n)

def tail(n,r,a,b):
    return sum((prob_exactly(n,k,a,b) for k in range(r,n+1)),Q(0))

def risk_reduction(d,r,a,b,S):
    return tail(d,r,a,b)-tail(d-len(S),r,a,b)

def direct_submod(d,r,a,b):
    V=tuple(range(d))
    risks=[tail(d,r,a,b)-tail(d-s,r,a,b) for s in range(d+1)]
    for i in V:
        for j in range(i+1,d):
            other=tuple(v for v in V if v!=i and v!=j)
            for m in range(len(other)+1):
                for sub in combinations(other,m):
                    if risks[m+2]-2*risks[m+1]+risks[m]>0:
                        return False
    return True

def theorem(d,r,a,b):
    if r==1:return False
    if r==d:return True
    return (r-1)*b-(d-r)*a-(d-1)>=0

def second_difference(d,r,a,b,s):
    F=lambda z:tail(d,r,a,b)-tail(d-z,r,a,b)
    return F(s+2)-2*F(s+1)+F(s)

def beta_weighted_pair_difference(n,r,a,b):
    # The mixed Bernoulli step, computed independently by Beta moments.
    pos=Q(comb(n,r-2))*rising(a,r)*rising(b,n-r+2)/rising(a+b,n+2) if 0<=r-2<=n else Q(0)
    neg=Q(comb(n,r-1))*rising(a,r+1)*rising(b,n-r+1)/rising(a+b,n+2) if 0<=r-1<=n else Q(0)
    return pos-neg

cases=0
for d in range(2,9):
    for r in range(1,d+1):
        for a in (Q(1,3), Q(1,2), Q(1), Q(3,2), Q(2), Q(4)):
            for b in (Q(1,4), Q(1), Q(3,2), Q(3), Q(6), Q(10)):
                predicted=theorem(d,r,a,b)
                actual=direct_submod(d,r,a,b)
                assert predicted==actual,(d,r,a,b,predicted,actual)
                for s in range(d-1):
                    lhs=second_difference(d,r,a,b,s)
                    rhs=-beta_weighted_pair_difference(d-s-2,r,a,b)
                    assert lhs==rhs,(d,r,a,b,s,lhs,rhs)
                cases+=1
print('Exact complete vaccination-set checks:',cases)

# Explicit fixed-mean experiment on a five-neighbor star with overload r=3.
for a,b,expected in [(Q(5,4),Q(15,4),-Q(195,57344)),(Q(1),Q(3),Q(0)),(Q(1,2),Q(3,2),Q(3,256))]:
    assert a/(a+b)==Q(1,4)
    assert second_difference(5,3,a,b,0)==expected
    assert direct_submod(5,3,a,b)==(expected<=0)
    print('shape parameters:',a,b,'mean:',a/(a+b),'correlation:',1/(a+b+1),'second difference:',expected)

# Direct configuration enumeration for a separate independently calculated risk:
# beta-integrated probability of every infected-neighbor subset, summed by size.
for d,r,a,b in [(5,3,Q(1,2),Q(3,2)),(7,4,Q(2),Q(6)),(6,2,Q(1),Q(10))]:
    for s in range(d+1):
        keep=d-s
        explicit=Q(0)
        for bits in range(1<<keep):
            k=bits.bit_count()
            if k>=r:
                explicit+=rising(a,k)*rising(b,keep-k)/rising(a+b,keep)
        assert explicit==tail(keep,r,a,b)
print('Direct individual infection-configuration enumeration: PASS')
