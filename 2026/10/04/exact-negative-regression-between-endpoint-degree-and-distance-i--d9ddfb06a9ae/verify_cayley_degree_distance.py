#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from collections import Counter, defaultdict
import heapq, math

def prufer_tree(seq,n):
    deg=[1]*n
    for x in seq:
        deg[x]+=1
    leaves=[i for i,d in enumerate(deg) if d==1]
    heapq.heapify(leaves)
    adj=[[] for _ in range(n)]
    for x in seq:
        leaf=heapq.heappop(leaves)
        adj[leaf].append(x); adj[x].append(leaf)
        deg[leaf]-=1; deg[x]-=1
        if deg[x]==1:
            heapq.heappush(leaves,x)
    a=heapq.heappop(leaves); b=heapq.heappop(leaves)
    adj[a].append(b); adj[b].append(a)
    return adj

def distance(adj,u,v):
    stack=[(u,-1,0)]
    while stack:
        x,p,d=stack.pop()
        if x==v:
            return d
        for y in adj[x]:
            if y!=p:
                stack.append((y,x,d+1))
    raise AssertionError

def falling(a,r):
    z=1
    for j in range(r):
        z*=a-j
    return z

def cond_dist(n,k):
    if k==n-1:
        return {1:Fraction(1)}
    N=n-k-2
    out=defaultdict(Fraction)
    for b in range(N+1):
        pb=Fraction(math.comb(N,b)*(n-1)**(N-b), n**N)
        out[1+b]+=pb*Fraction(k,k+1)
        out[2+b]+=pb*Fraction(1,k+1)
    return dict(out)

def run():
    trees_enumerated=0
    distance_mass_checks=0
    conditional_probability_checks=0
    mean_checks=0
    stochastic_tail_checks=0
    covariance_checks=0

    for n in range(2,9):
        joint=defaultdict(Counter)
        dist_count=Counter()
        total=n**(n-2)
        for seq in product(range(n),repeat=n-2):
            adj=prufer_tree(seq,n)
            d=distance(adj,0,1)
            deg=len(adj[0])
            joint[d][deg]+=1
            dist_count[d]+=1
            trees_enumerated+=1

        for k in range(1,n):
            p=Fraction(dist_count[k],total)
            target=Fraction((k+1)*falling(n-2,k-1), n**k)
            assert p==target
            distance_mass_checks+=1

            law=cond_dist(n,k)
            obs={deg:Fraction(c,dist_count[k]) for deg,c in joint[k].items()}
            assert obs==law
            conditional_probability_checks+=len(law)

            mean=sum(Fraction(dg)*pr for dg,pr in law.items())
            target_mean=Fraction(2)-Fraction(k+2,n)+Fraction(1,k+1)
            assert mean==target_mean
            mean_checks+=1

        ED=sum(Fraction(k*dist_count[k],total) for k in dist_count)
        ED2=sum(Fraction(k*k*dist_count[k],total) for k in dist_count)
        Edeg=sum(Fraction(sum(deg*c for deg,c in joint[k].items()),total) for k in joint)
        EDdeg=sum(Fraction(k*sum(deg*c for deg,c in joint[k].items()),total) for k in joint)
        cov=EDdeg-ED*Edeg
        target_cov=Fraction(1)-Fraction(ED2+ED,n)
        assert cov==target_cov
        if n>=3:
            assert cov<0
        covariance_checks+=1

    for n in range(3,81):
        laws=[cond_dist(n,k) for k in range(1,n)]
        for k0 in range(len(laws)-1):
            a=laws[k0]; b=laws[k0+1]
            maxdeg=max(max(a),max(b))
            strict=False
            for t in range(1,maxdeg+1):
                ta=sum(p for d,p in a.items() if d>=t)
                tb=sum(p for d,p in b.items() if d>=t)
                assert ta>=tb
                strict |= ta>tb
                stochastic_tail_checks+=1
            assert strict

    print(
        "VERIFY_OK "
        f"trees_enumerated={trees_enumerated} "
        f"distance_mass_checks={distance_mass_checks} "
        f"conditional_probability_checks={conditional_probability_checks} "
        f"mean_checks={mean_checks} "
        f"stochastic_tail_checks={stochastic_tail_checks} "
        f"covariance_checks={covariance_checks}"
    )

if __name__=="__main__":
    run()
