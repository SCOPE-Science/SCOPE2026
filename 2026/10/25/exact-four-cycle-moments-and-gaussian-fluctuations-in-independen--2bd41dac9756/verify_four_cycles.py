"""Finite, exact tests of four-cycle recursions for independently twisted cubes.
No finite computation is used to establish the limiting normal law.
"""
from fractions import Fraction
from itertools import permutations
from random import Random
from math import comb


def norm_edge(i,j):
    return (i,j) if i<j else (j,i)


def twist(edges1,edges2,m,pi):
    return set(edges1)|{(i+m,j+m) for i,j in edges2}|{norm_edge(i,m+pi[i]) for i in range(m)}


def overlap(edges1,edges2,pi):
    e2=set(edges2)
    return sum(norm_edge(pi[a],pi[b]) in e2 for a,b in edges1)


def cycle4_count(edges,n):
    neighbors=[set() for _ in range(n)]
    for i,j in edges:
        neighbors[i].add(j);neighbors[j].add(i)
    s=sum(comb(len(neighbors[i] & neighbors[j]),2)
          for i in range(n) for j in range(i+1,n))
    assert s%2==0
    return s//2


def constants(k):
    m=2**(k-1);d=k-1
    mu=Fraction(m*d*d,2*(m-1))
    var=Fraction(0) if k==2 else Fraction(m*d*d*(m-k)**2,2*(m-3)*(m-1)**2)
    return mu,var


def exact_match_moments(a,b,m):
    s1=s2=0
    count=0
    for pi in permutations(range(m)):
        y=overlap(a,b,pi)
        s1+=y;s2+=y*y;count+=1
    mu=Fraction(s1,count)
    var=Fraction(s2,count)-mu*mu
    return mu,var


def make(rng,k):
    if k==0: return set()
    m=2**(k-1)
    return twist(make(rng,k-1),make(rng,k-1),m,rng.sample(range(m),m))


def test():
    # The unique graph at level 2 is a 4-cycle.
    cube2=make(Random(1),2)
    assert cycle4_count(cube2,4)==1
    assert constants(2)==(Fraction(1),Fraction(0))
    # Exact enumeration at level 3, including direct four-cycle census.
    g3={}
    for pi in permutations(range(4)):
        out=twist(cube2,cube2,4,pi)
        cross=overlap(cube2,cube2,pi)
        assert cycle4_count(out,8)==2+cross
        g3[cross]=out
    assert set(g3)=={2,4}
    assert exact_match_moments(cube2,cube2,4)==constants(3)
    # For all 4 pairs of distinct lower-graph types, enumerate every
    # top-level perfect matching; the variance has no graph-shape parameter.
    for a in g3.values():
        for b in g3.values():
            assert exact_match_moments(a,b,8)==constants(4)
    # Repeated direct checks at larger levels ensure correct cycle geometry.
    r=Random(2317)
    checks=0
    for k in (3,4,5,6):
        for _ in range(35):
            m=2**(k-1)
            a,b=make(r,k-1),make(r,k-1)
            pi=r.sample(range(m),m)
            big=twist(a,b,m,pi)
            assert cycle4_count(big,2*m)==(cycle4_count(a,m)+cycle4_count(b,m)+overlap(a,b,pi))
            checks+=1
    assert checks==140
    for k in range(2,15):
        mu,v=constants(k)
        assert mu>0 and v>=0
    return {'exhaustive_n3_matchings':24,'exhaustive_n4_matchings':4*40320,
            'sampled_direct_identity_checks':checks,'mu3':str(constants(3)[0]),
            'v3':str(constants(3)[1]),'mu4':str(constants(4)[0]),
            'v4':str(constants(4)[1])}

if __name__=='__main__':
    print(test())
