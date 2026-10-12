#!/usr/bin/env python3
"""Finite corroboration for the matching-deleted-biclique sequence-b theorem."""

def make_graph(m,n,t):
    adj=[set() for _ in range(m+n)]
    for i in range(m):
        for j in range(n):
            if i < t and i == j:
                continue
            a=i; b=m+j
            adj[a].add(b); adj[b].add(a)
    return adj

def connected(adj):
    seen={0}; stack=[0]
    while stack:
        v=stack.pop()
        for w in adj[v]:
            if w not in seen:
                seen.add(w); stack.append(w)
    return len(seen)==len(adj)

def maximum_realized_color_count(adj,q):
    N=len(adj)
    color=[0]*N
    best=0
    tested=0
    # Restricted-growth strings enumerate set partitions once, i.e. proper
    # colorings up to a permutation of color names.
    def rec(v,max_color):
        nonlocal best,tested
        if v==N:
            k=max_color+1
            cdv=[0]*k
            for x in range(N):
                seen={color[x]}
                seen.update(color[y] for y in adj[x])
                if len(seen)==k:
                    cdv[color[x]] += 1
            tested += 1
            if min(cdv) >= q:
                best=max(best,k)
            return
        for c in range(max_color+2):
            if any(color[u]==c for u in adj[v] if u<v):
                continue
            color[v]=c
            rec(v+1,max(max_color,c))
    color[0]=0
    rec(1,0)
    return best,tested

def main():
    profiles=0
    colorings=0
    for m in range(2,5):
        for n in range(m,6):
            if m+n>9:
                continue
            for t in range(1,m+1):
                if m==n==t:
                    continue
                adj=make_graph(m,n,t)
                assert connected(adj)
                for q in range(2,m+2):
                    got,count=maximum_realized_color_count(adj,q)
                    want=2 if q<=m else 0
                    assert got==want,(m,n,t,q,got,want)
                    profiles += 1
                    colorings += count
    print(f"ALL CHECKS PASSED; profiles={profiles}; canonical_colorings_checked={colorings}; max_order=9")

if __name__=='__main__':
    main()
