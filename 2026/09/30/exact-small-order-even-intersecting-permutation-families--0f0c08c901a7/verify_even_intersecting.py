#!/usr/bin/env python3
from itertools import permutations

def agreements(p,q): return sum(a==b for a,b in zip(p,q))

def graph_normalized(n):
    ident=tuple(range(n))
    cand=[p for p in permutations(range(n)) if p!=ident and agreements(p,ident)%2==0]
    N=len(cand); adj=[0]*N
    for i in range(N):
        for j in range(i):
            if agreements(cand[i],cand[j])%2==0:
                adj[i]|=1<<j; adj[j]|=1<<i
    return ident,cand,adj

def max_clique_exact(adj):
    N=len(adj); best=[]
    def color_sort(P):
        order=[]; bounds=[]; c=0; rem=P
        while rem:
            c+=1; avail=rem
            while avail:
                bit=avail & -avail; v=bit.bit_length()-1
                order.append(v); bounds.append(c)
                rem ^= bit; avail ^= bit; avail &= ~adj[v]
        return order,bounds
    def expand(P,C):
        nonlocal best
        if not P:
            if len(C)>len(best): best=C[:]
            return
        order,bounds=color_sort(P)
        for k in range(len(order)-1,-1,-1):
            if len(C)+bounds[k] <= len(best): return
            v=order[k]; bit=1<<v
            if P & bit:
                expand(P & adj[v], C+[v]); P ^= bit
    expand((1<<N)-1,[])
    return best

def n5_max_cliques():
    ident,cand,adj=graph_normalized(5); target=12; sols=[]
    def pc(x): return x.bit_count()
    def pick_pivot(U,P):
        best=-1; score=-1
        while U:
            b=U & -U; u=b.bit_length()-1; U^=b
            s=pc(P & adj[u])
            if s>score: best,score=u,s
        return best
    def bronk(R,P,X):
        if len(R)+pc(P)<target: return
        if not P and not X:
            if len(R)==target: sols.append(tuple(sorted(R)))
            return
        U=P|X; u=pick_pivot(U,P) if U else -1
        Q=P if u<0 else P & ~adj[u]
        while Q:
            b=Q & -Q; v=b.bit_length()-1; Q^=b
            bronk(R+[v], P & adj[v], X & adj[v])
            P ^= b; X |= b
    bronk([], (1<<len(cand))-1, 0)
    fams=[frozenset([ident]+[cand[i] for i in S]) for S in sols]
    assert len(fams)==26 and len(set(fams))==26
    return fams

def compose(a,b): return tuple(a[b[i]] for i in range(len(a)))

def classify_n5(fams):
    P=list(permutations(range(5)))
    # Left translates of the 26 normalized families yield all labeled maxima.
    allf=set()
    for F in fams:
        for a in P:
            allf.add(frozenset(compose(a,x) for x in F))
    assert len(allf)==240
    F=next(iter(allf)); orbit=set()
    for a in P:
        for b in P:
            orbit.add(frozenset(compose(compose(a,x),b) for x in F))
    assert orbit==allf
    return len(allf)

Ms={}
for n in range(3,7):
    ident,cand,adj=graph_normalized(n)
    C=max_clique_exact(adj)
    F=[ident]+[cand[i] for i in C]
    assert all(agreements(a,b)%2==0 for i,a in enumerate(F) for b in F[i+1:])
    Ms[n]=len(F)
    print(f'n={n} normalized_candidates={len(cand)} M={len(F)}')
assert Ms=={3:3,4:8,5:13,6:48}
fams=n5_max_cliques(); total=classify_n5(fams)
print('n=5 normalized_maximum_families=26')
print(f'n=5 labeled_maximum_families={total}')
print('n=5 left-right_orbits=1')
print('n=5 representative (1-based):')
for p in sorted(next(iter(fams))): print(' '+' '.join(str(x+1) for x in p))
print('VERIFY_OK')
