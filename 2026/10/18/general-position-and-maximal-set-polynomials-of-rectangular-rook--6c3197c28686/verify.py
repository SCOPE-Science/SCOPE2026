#!/usr/bin/env python3
"""Independent direct geodesic enumeration and exact labelled-star-forest recurrence.
Standard-library only; no external data or package dependencies.
"""
from math import comb, factorial
from functools import lru_cache
from collections import Counter, deque

@lru_cache(None)
def forest(m,n):
    # z-polynomial for edge-labelled bipartite star forests in K_{m,n}.
    if m==0 or n==0: return (1,)
    out=Counter()
    for k,c in enumerate(forest(m-1,n)):out[k]+=c
    # component involving first left vertex: isolated edge or left-centered star
    for d in range(1,n+1):
        for k,c in enumerate(forest(m-1,n-d)):
            out[k+d]+=comb(n,d)*c
    # component with first left vertex a leaf of a right-centered star of >=2 edges
    for d in range(2,m+1):
        for k,c in enumerate(forest(m-d,n-1)):
            out[k+d]+=n*comb(m-1,d-1)*c
    return tuple(out[k] for k in range(max(out)+1))

@lru_cache(None)
def restricted_stirling(n,p):
    if n==0:return int(p==0)
    if p==0:return 0
    return sum(comb(n-1,s-1)*restricted_stirling(n-s,p-1) for s in range(2,n+1))

def fall(x,p):
    v=1
    for i in range(p):v*=x-i
    return v

def A(m,n):
    return sum(fall(m,p)*restricted_stirling(n,p) for p in range(1,min(m-1,n//2)+1))

def maximal_pred(m,n):
    out=Counter()
    for a in range(m+1):
        for b in range(n+1):
            for k,c in enumerate(forest(m-a,n-b)):
                out[k]+=((-1)**(a+b))*comb(m,a)*comb(n,b)*c
    out[n]+=A(m,n)
    out[m]+=A(n,m)
    assert all(v>=0 for v in out.values()),(m,n,out)
    return tuple(out[i] for i in range(max(out)+1))

def geodesic_trip_masks(m,n):
    vs=[(i,j) for i in range(m) for j in range(n)]
    NN=len(vs)
    adj=[[int(i!=h and (i[0]==h[0] or i[1]==h[1])) for h in vs] for i in vs]
    dist=[]
    for s in range(NN):
        d=[None]*NN;d[s]=0; queue=deque([s])
        while queue:
            v=queue.popleft()
            for w in range(NN):
                if adj[v][w] and d[w] is None:
                    d[w]=d[v]+1;queue.append(w)
        dist.append(d)
    triples=[]
    for a in range(NN):
      for b in range(a+1,NN):
       for c in range(b+1,NN):
        if (dist[a][b]+dist[b][c]==dist[a][c] or
            dist[a][c]+dist[c][b]==dist[a][b] or
            dist[b][a]+dist[a][c]==dist[b][c]):
            triples.append((1<<a)|(1<<b)|(1<<c))
    return triples

def enumerate_direct(m,n):
    NN=m*n; allmask=(1<<NN)-1; invalid=geodesic_trip_masks(m,n)
    by_size=Counter(); maximal=Counter()
    validmask=[False]*(1<<NN)
    for mask in range(1<<NN):
        if not any(mask & tri==tri for tri in invalid):
            validmask[mask]=True
            by_size[mask.bit_count()]+=1
    for mask in range(1<<NN):
        if not validmask[mask]:continue
        rem=(~mask)&allmask
        if not any(validmask[mask | (1<<i)] for i in range(NN) if rem & (1<<i)):
            maximal[mask.bit_count()]+=1
    return tuple(by_size.get(i,0) for i in range(NN+1)),tuple(maximal.get(i,0) for i in range(NN+1))

def pad(p,N): return tuple(p)+(0,)*(N-len(p))

def main():
    profiles=[(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(3,6),(4,4)]
    total=0
    for m,n in profiles:
        gp,mgp=enumerate_direct(m,n)
        f=forest(m,n);g=maximal_pred(m,n)
        assert gp==pad(f,m*n+1),(m,n,'GP',gp,f)
        assert mgp==pad(g,m*n+1),(m,n,'MAX',mgp,g)
        assert min(k for k,v in enumerate(g) if v)>0 and max(k for k,v in enumerate(g) if v)==m+n-2
        possible={k for k,v in enumerate(g) if v}
        assert possible==({min(m,n)}|set(range(max(m,n),m+n-1))),(m,n,possible)
        total+=(1<<(m*n))
        print(f'board={m}x{n} gp_total={sum(gp)} maximal_total={sum(mgp)} top={mgp[m+n-2]}')
    for m in range(2,9):
      for n in range(m,11):
        f=forest(m,n);g=maximal_pred(m,n)
        assert f[0]==1 and f[1]==m*n and f[2]==comb(m*n,2)
        assert set(k for k,v in enumerate(g) if v)==({m}|set(range(n,m+n-1)))
        if m>=3 and n>=3:assert f[m+n-2]==m*n
    print('VERIFICATION_OK', 'direct_boards='+str(len(profiles)), 'direct_subsets='+str(total), 'symbolic_boards='+str(sum(11-m for m in range(2,9))))

if __name__=='__main__':main()
