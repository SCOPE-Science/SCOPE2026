#!/usr/bin/env python3
"""Independent partial-injection enumeration and weighted-matching profile checks."""
from itertools import combinations,permutations
from collections import Counter

def partitions(n, cap=None):
    if n==0:
        yield ()
    else:
        for k in range(1,min(n,cap or n)+1):
            for rest in partitions(n-k,k): yield (k,)+rest

def alpha_from_parts(parts):
    a={};i=0
    for k in parts:
        for j in range(k-1): a[i+j]=i+j+1
        i+=k
    return a

def direct(parts):
    n=sum(parts); a=alpha_from_parts(parts); p=Counter()
    for k in range(n+1):
        for D in combinations(range(n),k):
            for I in combinations(range(n),k):
                for pi in permutations(I):
                    f=dict(zip(D,pi))
                    if all(f.get(a.get(x,-1),-1)==a.get(f.get(x,-1),-1) for x in range(n)):
                        p[k]+=1
    return p

def matching(parts):
    m=len(parts); result=Counter()
    def rec(i,mask,rank):
        if i==m:
            result[rank]+=1;return
        rec(i+1,mask,rank)
        for j in range(m):
            if not(mask>>j&1):
                for l in range(1,min(parts[i],parts[j])+1):
                    rec(i+1,mask | (1<<j),rank+l)
    rec(0,0,0)
    return result

if __name__=='__main__':
    total=0;seen={}
    for n in range(0,7):
        for parts in partitions(n):
            a=direct(parts);b=matching(parts)
            assert a==b,(parts,a,b)
            total+=sum(a.values())
            sig=tuple(a.get(i,0) for i in range(n+1))
            assert sig not in seen or seen[sig]==parts, (parts,seen.get(sig))
            seen[sig]=parts
    # triangular recovery c_j from coefficients by comparing with rank-truncated weighted matching profile
    for n in range(1,8):
        for parts in partitions(n):
            full=matching(parts); c=[]
            for j in range(1,n+1):
                trunc=tuple(min(k,j-1) for k in parts)
                low=matching(trunc).get(j,0)
                z=full.get(j,0)-low
                assert z>=0 and int(z**.5)**2==z,(parts,j,z)
                c.append(int(z**.5))
            assert [sum(k>=j for k in parts) for j in range(1,n+1)]==c,(parts,c)
    print('ALL_NILPOTENT_CENTRALIZER_RANK_CHECKS_PASSED',total)
