"""Independent finite checks of wheel geodesic transversals against a cyclic transfer formula."""
from collections import Counter
from itertools import combinations
from math import ceil


def shortest_paths(G,a,b):
    paths=[]
    q=[(a,)]
    seen={a:0}
    while q:
        path=q.pop(0)
        u=path[-1]
        if paths and len(path)>len(paths[0]):
            break
        if u==b:
            paths.append(path)
            continue
        for v in G[u]:
            if v in path: continue
            if len(path) <= seen.get(v, 10000):
                seen[v]=len(path)
                q.append(path+(v,))
    return paths


def maximal_geodesics(n):
    # The center is vertex n; rim vertices are 0,...,n-1.
    G={i:{(i-1)%n,(i+1)%n,n} for i in range(n)}
    G[n]=set(range(n))
    shortest=[]
    for a in G:
        for b in G:
            if a<b:
                shortest.extend(shortest_paths(G,a,b))
    maximal=[]
    for p in shortest:
        if not any(len(q)>len(p) and any(q[j:j+len(p)]==p or q[j:j+len(p)]==p[::-1] for j in range(len(q)-len(p)+1)) for q in shortest):
            maximal.append(frozenset(p))
    return {frozenset(p) for p in maximal}


def exact_minimal(n):
    geo=maximal_geodesics(n)
    masks=[sum(1<<j for j in p) for p in geo]
    def cover(bits):return all(bits&m for m in masks)
    out=Counter()
    full=Counter()
    for bits in range(1<<(n+1)):
        if cover(bits):
            full[bits.bit_count()]+=1
            if all(not cover(bits^(1<<i)) for i in range(n+1) if bits&(1<<i)):
                out[bits.bit_count()]+=1
    return out,full,geo


def transfer_coeff(n,k):
    allowed={(0,2),(1,1),(1,2),(2,0),(2,1),(2,2)}
    # Independent explicit gap-sequence enumeration is fine for small checks.
    from itertools import product
    t=0
    for a in product(range(3),repeat=k):
        if sum(a)==n-k and all((a[i-1],a[i]) in allowed for i in range(k)):
            t+=1
    assert (n*t)%k==0
    return n*t//k


def predicted(n):
    d=Counter({n-2:n})
    for k in range(ceil(n/3),n//2+1):
        d[k+1]+=transfer_coeff(n,k)
    return d


def full_predicted(n):
    from itertools import product
    d=Counter({n:1,n-1:n,n-2:n})
    # Enumerate all gap vectors explicitly; comparison code does not assume minimality.
    for k in range(ceil(n/3),n+1):
        t=0
        for g in product(range(3),repeat=k):
            if sum(g)==n-k:t+=1
        assert (n*t)%k==0
        d[k+1]+=n*t//k
    return d

def verify():
    for n in range(6,13):
        got,full,paths=exact_minimal(n)
        want=predicted(n)
        assert got==want,(n,got,want)
        if n<=10:
            full_want=full_predicted(n)
            assert full==full_want,(n,full,full_want)
        assert all(len(p)==3 for p in paths)
        print('n=',n,'minimal=',dict(sorted(got.items())),'maximal_geodesics=',len(paths))
    for n in range(6,14):
        k=ceil(n/3)
        count=transfer_coeff(n,k)
        if n%3==0: expect=3
        elif n%3==1: expect=n*(k+1)//2
        else: expect=n
        assert count==expect,(n,count,expect)
    print('VERIFY_OK')

if __name__=='__main__':verify()
