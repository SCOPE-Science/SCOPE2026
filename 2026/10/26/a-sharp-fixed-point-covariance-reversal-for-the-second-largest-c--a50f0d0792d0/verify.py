#!/usr/bin/env python3
"""Exact rational tests for second-cycle fixed-point covariance."""
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial
from itertools import permutations

@lru_cache(None)
def partitions(n, maximum=None):
    if maximum is None: maximum=n
    if n==0:
        return ((),)
    ans=[]
    for j in range(min(n,maximum),1-1,-1):
        for p in partitions(n-j,j): ans.append((j,)+p)
    return tuple(ans)

def parts_distribution(n):
    mean=Q(0); mixed=Q(0); prob=Q(0)
    for p in partitions(n):
        denom=1; fixed=0; counts={}
        for v in p: counts[v]=counts.get(v,0)+1
        for v,c in counts.items():
            denom *= v**c * factorial(c)
        w=Q(1,denom)
        b=p[1] if len(p)>1 else 0
        mean+=w*b; mixed+=w*b*counts.get(1,0);prob+=w
    assert prob==1
    return mean,mixed

def independent_mean(n):
    total=Q(0)
    for t in range(1,n+1):
        a=[Q(0)]*(n+1);a[0]=Q(1)
        for k in range(1,n+1):
            a[k]=sum((a[k-j] for j in range(1,min(k,t-1)+1)),Q(0))/k
        p_ge=Q(1)-a[n]-sum((a[n-j]/j for j in range(t,n+1)),Q(0))
        assert 0<=p_ge<=1
        total+=p_ge
    return total

def sample(perm):
    n=len(perm)
    out=[0]*n
    for i in range(n):
        if out[i]:continue
        j=i; seq=[]
        while not out[j]:
            seq.append(j);out[j]=1;j=perm[j]
        yield len(seq)

def run():
    vals={}; total=0
    for n in range(1,15):
        mean,mixed=parts_distribution(n)
        assert mean==independent_mean(n), n
        vals[n]=mean
        if n>=2:
            cov=mixed-mean
            assert cov==vals[n-1]+Q(1,n-1)-vals[n]
            assert (cov>0 if n<=5 else cov<0), (n,cov)
            print('cycle_class',n,'mean',mean,'cov',cov)
        total+=1
    brute_count=0
    for n in range(2,9):
        moment=0; fm=0; denom=factorial(n)
        for perm in permutations(range(n)):
            l=sorted(sample(perm),reverse=True)
            b=l[1] if len(l)>1 else 0
            f=sum(perm[i]==i for i in range(n))
            moment+=b*f;fm+=f
            brute_count+=1
        assert Q(fm,denom)==1
        assert Q(moment,denom)-vals[n]==vals[n-1]+Q(1,n-1)-vals[n]
    assert brute_count==46232,brute_count
    def bound(m):
        t=Q(0)
        for b in range(1,(m-1)//2+1): t+=Q(1,m-b)
        for b in range(2,(m-3)//2+1): t+=Q(1,m-b-1)
        return t
    assert bound(9)>1 and bound(14)>1
    for parity in (0,1):
        lo=14 if parity==0 else 9
        for m in range(lo,301,2):
            assert bound(m)>1 and bound(m+2)>bound(m)
    # Enumerate T_m independently and check incremental moment identity and lower bound.
    for m in range(1,15):
        t=Q(0)
        for p in partitions(m):
            if len(p)<2 or p[0]==p[1]:continue
            counts={}
            for v in p:counts[v]=counts.get(v,0)+1
            denom=1
            for v,c in counts.items():denom*=v**c*factorial(c)
            t+=Q(p[1]*counts[p[1]],denom)
        assert Q(m+1)*(independent_mean(m+1)-independent_mean(m))==Q(1,m)+t
        if m>=9:assert t>=bound(m)
    print('PASS:',total,'cycle type consistency checks,',brute_count,'enumerated permutations, exact growth and harmonic bounds.')
if __name__=='__main__':run()
