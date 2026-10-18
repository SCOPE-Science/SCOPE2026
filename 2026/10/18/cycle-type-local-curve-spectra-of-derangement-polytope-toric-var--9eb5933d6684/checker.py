#!/usr/bin/env python3
"""Independent finite checks of cycle-type curve degrees for derangement polytopes."""
from collections import defaultdict, Counter
from itertools import combinations, permutations
from math import comb, factorial

def partitions_no_ones(n, limit=None):
    if limit is None:
        limit=n
    if n == 0:
        yield ()
    for k in range(min(n,limit),1,-1):
        for rem in partitions_no_ones(n-k,k):
            yield (k,)+rem

def cycles_polygon(l):
    out={(0,0):1}
    for k in range(1,l):
        for h in range(1,min(k,l-k)+1):
            ways=l*comb(k-1,h-1)*comb(l-k-1,h-1)//h
            assert ways*h==l*comb(k-1,h-1)*comb(l-k-1,h-1)
            out[(k+h,h)]=out.get((k+h,h),0)+(-1)**k*ways
    return out

def run_polynomial(lam):
    n=sum(lam)
    C={(0,0):1}
    for length in lam:
        local=cycles_polygon(length)
        nxt=defaultdict(int)
        for (v,h),a in C.items():
            for (dv,dh),b in local.items():
                nxt[(v+dv,h+dh)]+=a*b
        C=dict(nxt)
    coeff=defaultdict(int)
    for (v,h),a in C.items():
        for m in range(n-v+1):
            if v+m<2 or h+m<1:
                continue
            coeff[v+m]+=a*comb(n-v,m)*factorial(h+m-1)
    for l in lam:
        coeff[l]+=(-1)**l
    return {k:v for k,v in sorted(coeff.items()) if v}

def canonical_sigma(lam):
    n=sum(lam); s=list(range(n));a=0
    for length in lam:
        for j in range(length): s[a+j]=a+(j+1)%length
        a+=length
    return s

def independent_cycle_count(lam):
    n=sum(lam);sigma=canonical_sigma(lam)
    inv=[0]*n
    for i,j in enumerate(sigma):inv[j]=i
    degrees=Counter()
    for k in range(2,n+1):
        for S in combinations(range(n),k):
            for order in permutations(S[1:]):
                arr=(S[0],)+order
                if all(arr[(idx+1)%k]!=inv[arr[idx]] for idx in range(k)):
                    degrees[k]+=1
    return dict(sorted(degrees.items()))

def independent_graph_degree(lam):
    n=sum(lam)
    if n>6:
        return None
    s=canonical_sigma(lam)
    count=Counter()
    for tau in permutations(range(n)):
        if any(tau[i]==i for i in range(n)) or list(tau)==s:
            continue
        inv=[0]*n
        for i,j in enumerate(s):inv[j]=i
        relative=[inv[tau[i]] for i in range(n)]
        changed={i for i in range(n) if relative[i]!=i}
        if not changed:
            continue
        first=next(iter(changed));seen={first};at=relative[first]
        while at not in seen:
            seen.add(at);at=relative[at]
        if at==first and seen==changed:
            count[len(changed)]+=1
    return dict(sorted(count.items()))

def type_multiplicity(lam):
    n=sum(lam);m=Counter(lam);z=1
    for l,c in m.items():z*=l**c*factorial(c)
    return factorial(n)//z

if __name__=='__main__':
    graph=[]
    for n in range(3,9):
        edge_end_sum=0;degree_profile=[]
        for lam in partitions_no_ones(n):
            formula=run_polynomial(lam)
            direct=independent_cycle_count(lam)
            if formula != direct:
                raise AssertionError((n,lam,'inclusion-exclusion',formula,'direct',direct))
            graphdegree=independent_graph_degree(lam)
            if graphdegree is not None and graphdegree != direct:
                raise AssertionError((n,lam,'adjacency',graphdegree,'direct',direct))
            edges_here=sum(formula.values())
            count=type_multiplicity(lam)
            edge_end_sum+=count*edges_here
            degree_profile.append((lam,edges_here))
        assert edge_end_sum%2==0
        graph.append((n,edge_end_sum//2))
        print('n=',n,'dimension=',n*n-3*n+1,'types=',degree_profile,'edges=',edge_end_sum//2)
    print('GRAPH_EDGE_COUNTS:',graph)
    print('VERIFY_OK')
