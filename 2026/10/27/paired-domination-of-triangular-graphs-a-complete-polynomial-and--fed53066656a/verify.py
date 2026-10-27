"""Reproducible finite tests for paired domination of triangular graphs.
No external packages or network access needed.
"""
from itertools import combinations
from math import comb, factorial
from collections import Counter

def brute(n):
    E = list(combinations(range(n), 2))
    m = len(E)
    adjacency = [0]*m
    for i, (a,b) in enumerate(E):
        for j,(c,d) in enumerate(E):
            if i != j and ({a,b} & {c,d}):
                adjacency[i] |= 1 << j
    dom = [False] * (1<<m)
    for s in range(1<<m):
        covered=s
        for i in range(m):
            if s & (1<<i): covered |= adjacency[i]
        dom[s] = covered==(1<<m)-1
    paired=[False]*(1<<m)
    paired[0]=True
    for s in range(1,1<<m):
        if s.bit_count() & 1: continue
        bit=s & -s
        i=bit.bit_length()-1
        r= s ^ bit
        possibles=r & adjacency[i]
        while possibles:
            b=possibles & -possibles
            if paired[r^b]:
                paired[s]=True
                break
            possibles ^= b
    brute_count=Counter()
    structural_count=Counter()
    for s in range(1<<m):
        if dom[s] and paired[s]:
            brute_count[s.bit_count()]+=1
        if s==0: continue
        deg=[0]*n
        for i,(u,v) in enumerate(E):
            if (s>>i)&1:
                deg[u]+=1
                deg[v]+=1
        isolated=deg.count(0)
        # Connected components of selected-edge spanning subgraph.
        parent=list(range(n))
        def find(u):
            while parent[u]!=u: u=parent[u]
            return u
        for i,(u,v) in enumerate(E):
            if (s>>i)&1: parent[find(u)]=find(v)
        sizes=Counter()
        for i,(u,v) in enumerate(E):
            if (s>>i)&1: sizes[find(u)]+=1
        prediction=(isolated<=1 and all(k%2==0 for k in sizes.values()))
        actual=dom[s] and paired[s]
        assert prediction==actual, (n,s,prediction,actual)
        if prediction: structural_count[s.bit_count()]+=1
    assert brute_count==structural_count
    first=min(brute_count) if brute_count else None
    # floor((n+1)/3) equals ceil((n-1)/3) for integers n.
    assert first==2*((n+1)//3)
    if n%3==1:
        t=(n-1)//3
        assert brute_count[first]==factorial(n)//(2**t*factorial(t))
    if n%3==0:
        t=n//3
        expected=factorial(n)//(2**t*factorial(t))
        if t>=2:
            expected+=n*comb(n-1,5)*125*factorial(n-6)//(2**(t-2)*factorial(t-2))
        assert brute_count[first]==expected, (n,brute_count[first],expected)
    print('n=',n,'subsets=',1<<m,'minimum=',first,'minimum_count=',brute_count[first],
          'coefficients=',sorted(brute_count.items()))
    return brute_count

if __name__=='__main__':
    for n in range(3,7): brute(n)
    print('ALL INDEPENDENT CHECKS PASSED')
