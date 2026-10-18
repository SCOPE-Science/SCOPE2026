from itertools import product
from math import comb, factorial
from functools import lru_cache
from collections import Counter


def rook_edges(m,n):
    N=m*n; adj=[0]*N
    for a in range(N):
        i,j=divmod(a,n)
        adj[a]=sum(1<<b for b in range(N) if b!=a and (b//n==i or b%n==j))
    return adj

def acyclic(S, adj):
    # Direct adjacency-based DFS with explicit parent: catches any cycle of any length.
    seen=0
    while q:= S & ~seen:
        v=(q&-q).bit_length()-1
        stack=[(v,-1)]
        while stack:
            v,parent=stack.pop()
            if seen>>v&1: continue
            seen|=1<<v
            nb=adj[v]&S
            while nb:
                bit=nb&-nb; nb-=bit
                w=bit.bit_length()-1
                if w==parent: continue
                if seen>>w&1:return False
                # Beware duplicate stack entries of same w: this simple traversal still detects cycle via its other incident edges.
                stack.append((w,v))
    return True

@lru_cache(None)
def all_lf_poly(m,n):
    if m==0 or n==0: return (1,)
    P=Counter({k:v for k,v in enumerate(all_lf_poly(m-1,n))})
    for l in range(1,m+1):
        for r in range(1,n+1):
            if abs(l-r)>1: continue
            count=factorial(l)*factorial(r)//(2 if l!=r else 1)
            if l==r: count=factorial(l)*factorial(r)
            mult=comb(m-1,l-1)*comb(n,r)*count
            for k,v in enumerate(all_lf_poly(m-l,n-r)):
                P[k+l+r-1]+=mult*v
    return tuple(P.get(k,0) for k in range(max(P)+1))

@lru_cache(None)
def ordinary_lf_poly(n):
    if not n:return (1,)
    P=Counter({k:v for k,v in enumerate(ordinary_lf_poly(n-1))})
    for s in range(2,n+1):
        mult=comb(n-1,s-1)*factorial(s)//2
        for k,v in enumerate(ordinary_lf_poly(n-s)):
            P[k+s-1]+=mult*v
    return tuple(P.get(k,0) for k in range(max(P)+1))

def predicted_max(m,n):
    if m>n:m,n=n,m
    return (m+n-1,factorial(m)**2) if m==n else (2*m,factorial(m)*ordinary_lf_poly(n)[m])

def inspect(m,n):
    adj=rook_edges(m,n); N=m*n
    forest=[False]*(1<<N)
    bysize=Counter(); max_by_size=Counter(); count=0
    for S in range(1<<N):
        ok=acyclic(S,adj)
        forest[S]=ok
        if ok:
            count+=1
            bysize[S.bit_count()]+=1
    for S,ok in enumerate(forest):
        if not ok:continue
        if all(not forest[S|(1<<j)] for j in range(N) if not S>>j&1):
            max_by_size[S.bit_count()]+=1
    P=all_lf_poly(m,n)
    assert all(bysize[k]==P[k] for k in range(max(len(P),max(bysize,default=0)+1))), (m,n,bysize,P)
    size,cnt=predicted_max(m,n)
    assert max_by_size==Counter({size:cnt}), (m,n,max_by_size,size,cnt)
    print('OK',m,n,'subsets',1<<N,'forests',count,'max',dict(max_by_size),'Fpoly',P)
    return 1<<N

if __name__=='__main__':
    tot=0; profiles=0
    for m,n in [(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(4,4),(3,6)]:
        tot+=inspect(m,n); profiles+=1
    print('VERIFICATION_OK', 'profiles',profiles,'total_subsets',tot)
