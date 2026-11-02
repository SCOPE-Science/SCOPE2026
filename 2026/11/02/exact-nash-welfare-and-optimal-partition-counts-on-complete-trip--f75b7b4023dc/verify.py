#!/usr/bin/env python3
"""Exact independent dynamic enumeration of clique partitions in complete tripartite friend graphs."""
from functools import lru_cache
from math import factorial
from itertools import product

@lru_cache(None)
def independent_partition_counts(a,b,c):
    # Map numbers of 3-agent coalitions to counts of distinct partitions
    if a+b+c == 0:
        return {0:1}
    v=[a,b,c]
    i=next(j for j,x in enumerate(v) if x)
    v[i]-=1
    outcome={}
    # All possible coalitions containing one fixed distinguished agent
    for j in range(3):
        if j==i or v[j]==0:
            continue
        t=v.copy(); mult=t[j];t[j]-=1
        for q,z in independent_partition_counts(*t).items():
            outcome[q]=outcome.get(q,0)+mult*z
    j,k=[j for j in range(3) if j!=i]
    if v[j] and v[k]:
        t=v.copy();mult=t[j]*t[k];t[j]-=1;t[k]-=1
        for q,z in independent_partition_counts(*t).items():
            outcome[q+1]=outcome.get(q+1,0)+mult*z
    return outcome

def formula(a,b,c):
    n=a+b+c
    if n<2 or 2*max(a,b,c)>n:
        return None
    t=n-2*max(a,b,c)
    assert 0<=t<=min(a,b,c) and (n-t)%2==0
    residual=(a-t,b-t,c-t)
    x=(residual[0]+residual[1]-residual[2])//2
    y=(residual[0]+residual[2]-residual[1])//2
    z=(residual[1]+residual[2]-residual[0])//2
    assert min(x,y,z)>=0 and sum(residual)==2*(x+y+z)
    count=factorial(a)*factorial(b)*factorial(c)//(factorial(t)*factorial(x)*factorial(y)*factorial(z))
    return t,count,(x,y,z)

def audit():
    tested=positive=zero=0
    for a,b,c in product(range(9),repeat=3):
        n=a+b+c
        if not 2<=n<=21:continue
        tested+=1
        counts=independent_partition_counts(a,b,c)
        out=formula(a,b,c)
        if out is None:
            zero+=1
            assert not counts,(a,b,c,counts)
        else:
            positive+=1
            t,num,_=out
            assert counts and max(counts)==t,(a,b,c,t,counts)
            assert counts[t]==num,(a,b,c,t,num,counts)
            assert all(n-3*q>=0 and (n-3*q)%2==0 for q in counts)
    # Short closed-form witnesses capturing parity and imbalance.
    cases=[(1,1,1),(2,2,1),(3,3,1),(3,2,1),(4,3,2),(5,4,4),(7,7,0),(7,6,0)]
    for abc in cases:
        print('EXAMPLE',abc,'formula=',formula(*abc),'independent=',independent_partition_counts(*abc))
    print('VERIFY_OK tested=%d positive=%d zero=%d cached_states=%d' % (tested,positive,zero,independent_partition_counts.cache_info().currsize))

if __name__=='__main__':audit()


def all_partitions(elements):
    if not elements:
        yield ()
        return
    first,*tail=elements
    for blocks in all_partitions(tail):
        yield ((first,),)+blocks
        for i in range(len(blocks)):
            yield blocks[:i]+((first,)+blocks[i],)+blocks[i+1:]


def brute_payoff_audit():
    checked=instances=0
    for n in range(2,9):
        for a in range(n+1):
            for b in range(n-a+1):
                c=n-a-b
                roles=([0]*a)+([1]*b)+([2]*c)
                best=0
                winners=0
                for partition in all_partitions(list(range(n))):
                    checked+=1
                    utilities=[]
                    for coalition in partition:
                        for i in coalition:
                            utility=sum(1 if roles[i]!=roles[j] else -n for j in coalition if i!=j)
                            utilities.append(utility)
                    if min(utilities)<0:continue
                    prod=1
                    for u in utilities:prod*=u
                    if prod>best:
                        best=prod
                        winners=1
                    elif prod==best and prod>0:
                        winners+=1
                f=formula(a,b,c)
                if f is None:
                    assert best==0,(a,b,c,best)
                else:
                    assert (best,winners)==(2**(3*f[0]),f[1]),(a,b,c,best,winners,f)
                instances+=1
    print('BRUTE_OK literal_game_partitions=%d labeled_compositions=%d' %(checked,instances))

if __name__=='__main__':brute_payoff_audit()
