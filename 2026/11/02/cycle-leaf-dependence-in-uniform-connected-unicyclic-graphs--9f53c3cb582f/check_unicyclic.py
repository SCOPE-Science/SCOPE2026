#!/usr/bin/env python3
"""Reproducible finite checks for leaf–girth dependence in uniform simple unicyclic graphs."""
from math import comb, factorial, exp, sqrt, pi
from fractions import Fraction
from collections import Counter
from itertools import combinations

def predicted_count(n,c,l):
    m=n-c
    if m==0:
        return factorial(n)//(2*n) if l==0 else 0
    if not 0<=l<=m:
        return 0
    # Forest leaf-pattern inclusion exclusion, with a fixed unique cycle.
    num=sum((-1)**h*comb(m-l,h)*(n-l-h)**(m-1) for h in range(m-l+1))
    count=Fraction(factorial(n)*comb(m,l)*num,2*factorial(m))
    assert count.denominator==1, (n,c,l,count)
    return int(count)

def cycle_length_and_leaves(n,edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v);adj[v].add(u)
    seen={0}; queue=[0]
    for u in queue:
        for v in adj[u]:
            if v not in seen:
                seen.add(v);queue.append(v)
    if len(seen)!=n:
        return None
    leaves=sum(len(a)==1 for a in adj)
    degree=list(map(len,adj));queue=[i for i,d in enumerate(degree) if d==1]
    for u in queue:
        degree[u]=0
        for v in adj[u]:
            if degree[v]>0:
                degree[v]-=1
                if degree[v]==1:
                    queue.append(v)
    cycle=sum(d>0 for d in degree)
    assert 3<=cycle<=n, (n,edges,cycle)
    return cycle,leaves

def enumerate_graphs(n):
    table=Counter()
    all_edges=list(combinations(range(n),2))
    for edges in combinations(all_edges,n):
        x=cycle_length_and_leaves(n,edges)
        if x is not None:
            table[x]+=1
    return table

def check():
    tests=0
    for n in range(3,8):
        exact=enumerate_graphs(n)
        for c in range(3,n+1):
            for l in range(n+1):
                got=predicted_count(n,c,l)
                assert exact.get((c,l),0)==got,(n,c,l,exact.get((c,l),0),got)
                tests+=1
            m=n-c
            ctotal=sum(exact.get((c,l),0) for l in range(n+1))
            expected=Fraction(factorial(n)*n**m, 2*factorial(m)*n)
            assert ctotal==expected
            tests+=1
            if m:
                mu=Fraction(m*(n-1)**(m-1),n**(m-1))
                gotmu=Fraction(sum(l*exact.get((c,l),0) for l in range(n+1)),ctotal)
                assert mu==gotmu,(n,c,mu,gotmu)
                tests+=1
        # Check exact cycle, leaf, and mixed-moment identities as rational numbers.
        total=sum(exact.values())
        ec=Fraction(sum(c*v for (c,l),v in exact.items()),total)
        el=Fraction(sum(l*v for (c,l),v in exact.items()),total)
        ecl=Fraction(sum(c*l*v for (c,l),v in exact.items()),total)
        s=sum(Fraction(n**m,factorial(m)) for m in range(n-2))
        assert ec==Fraction(n**(n-2),factorial(n-3))/s
        assert el==n*sum(Fraction((n-1)**m,factorial(m)) for m in range(n-3))/s
        assert ecl==Fraction(n*(n-1)**(n-3),factorial(n-4))/s if n>=4 else ecl==0
        tests+=3
        for c in range(3,n):
            m=n-c
            mu=lambda m: Fraction(m*(n-1)**(m-1),n**(m-1)) if m else Fraction(0)
            assert mu(m)>mu(m-1)
            tests+=1
        print(f'n={n}: {sum(exact.values())} connected unicyclic labeled graphs; exact joint table verified')
    # Discrete truncated-Poisson conditional mean and covariance, then asymptotic constant.
    for n in (20,50,100,200,500,1000):
        # avoid overflows by taking recursive Poisson probabilities instead
        import math
        w=[math.exp(math.lgamma(n+1)-math.lgamma(m+1)+(m-n)*math.log(n)) for m in range(n-2)]
        wsum=sum(w);w=[x/wsum for x in w]
        meanC=sum(w[m]*(n-m) for m in range(n-2))
        means=[m*((n-1)/n)**(m-1) if m else 0 for m in range(n-2)]
        meanL=sum(w[m]*means[m] for m in range(n-2))
        cov=sum(w[m]*(n-m-meanC)*(means[m]-meanL) for m in range(n-2))
        assert cov<0
        print(f'n={n}: E[L]-n/e={meanL-n/exp(1):+.6f}; covariance/sqrt(n)={cov/sqrt(n):+.9f}')
        tests+=3
    print('limit covariance coefficient',-1/(exp(1)*sqrt(2*pi)))
    print('PASS',tests,'families of exact/asymptotic numerical checks')

if __name__=='__main__':check()
