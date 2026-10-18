"""Reproducible exact-rational tests for mixed-spider greedy-output bias.
All graph enumerations are finite checks; the theorem relies on the written proof.
"""
from fractions import Fraction
from itertools import permutations
from collections import defaultdict
from functools import lru_cache
from math import comb


def formula(k,l):
    N=2**k
    p=Fraction(0)
    for j in range(k+1):
        p+=Fraction(comb(k,j),N*(l+2*j+1))
    q=[Fraction(l+2*j,N*(l+2*j+1)) for j in range(k+1)]
    tv=(abs(p-Fraction(1,N+1))+sum(comb(k,j)*abs(q[j]-Fraction(1,N+1)) for j in range(k+1)))/2
    return p,q,tv


def P_and_N(k,l):
    N=2**k
    positives=sum((Fraction(comb(k,j)*(l+2*j-N),l+2*j+1) for j in range(k+1) if l+2*j>N),Fraction())
    negatives=sum((Fraction(comb(k,j)*(N-l-2*j),l+2*j+1) for j in range(k+1) if l+2*j<N),Fraction())
    return positives,negatives


def graph(k,l):
    # center=0, each arm center-u_i-v_i, and l direct leaves.
    n=1+2*k+l
    adj=[0]*n
    for i in range(k):
        u=1+2*i;v=u+1
        for a,b in ((0,u),(u,v)):
            adj[a]|=1<<b;adj[b]|=1<<a
    for x in range(1+2*k,n):
        adj[0]|=1<<x;adj[x]|=1
    return adj


def exact_law_from_graph(k,l):
    adj=graph(k,l); n=len(adj)
    # Enumerate target MIS, then calculate greedy first-arrival recurrence on induced graphs.
    masks=[m for m in range(1<<n) if all(not (m&(1<<v) and m&adj[v]) for v in range(n)) and all((m>>v&1) or (m&adj[v]) for v in range(n))]
    @lru_cache(None)
    def rec(rest,target):
        if not rest:return Fraction(int(target==0))
        z=rest.bit_count()
        return sum((rec(rest&~(adj[v]|(1<<v)), target&~(1<<v)) for v in range(n) if target>>v&1),Fraction())/z
    return {m:rec((1<<n)-1,m) for m in masks}


def run():
    checks=0
    # Direct graph-based distribution recurrence for small k,l; no use of published formula.
    for k,l in [(0,1),(0,2),(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,4),(3,5),(3,6),(3,7)]:
        law=exact_law_from_graph(k,l)
        N=2**k
        assert len(law)==N+1
        p,q,b=formula(k,l)
        centerp=next(pv for mask,pv in law.items() if mask&1)
        assert centerp==p,(k,l,centerp,p)
        for mask,pv in law.items():
            if not mask&1:
                j=sum(bool(mask&(1<<(1+2*i))) for i in range(k))
                assert pv==q[j],(k,l,j,pv,q[j])
        assert b==sum(abs(x-Fraction(1,len(law))) for x in law.values())/2
        checks+=1
    # Derive exact global minimizer by monotone positive/negative deviations.
    for k in range(0,11):
        N=2**k
        for l in range(1, min(3*N+3,1000)):
            p,n=P_and_N(k,l)
            assert max(p,n)/Fraction(N*(N+1))==formula(k,l)[2]
        l0=N-k
        if k>=1:
            n0=P_and_N(k,l0)[1]
            p1=P_and_N(k,l0+1)[0]
            if k in (1,3):assert p1<n0
            else:assert p1>n0
        checks+=1
    print('VERIFICATION_OK independent_graph_cases=12 optimizer_parameter_checks=11 exact_fraction_checks=PASS')
    for k in range(0,10):
        lstar=2**k-k+(1 if k in (1,3) else 0)
        print('k',k,'unique_optimal_l',lstar,'exact_bias',formula(k,lstar)[2])

if __name__=='__main__':run()
