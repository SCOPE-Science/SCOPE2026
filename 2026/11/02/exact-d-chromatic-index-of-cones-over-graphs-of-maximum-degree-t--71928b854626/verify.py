#!/usr/bin/env python3
"""Finite independent checks for the cone/degree-two D-coloring formula."""
from itertools import combinations


def components(n, H):
    adj=[[] for _ in range(n)]
    for a,b in H:
        adj[a].append(b);adj[b].append(a)
    seen=set(); result=[]
    for root in range(n):
        if root in seen:continue
        stack=[root];seen.add(root); verts=[]
        while stack:
            v=stack.pop();verts.append(v)
            for w in adj[v]:
                if w not in seen:seen.add(w);stack.append(w)
        result.append((verts,all(len(adj[v])==2 for v in verts)))
    return result


def expected(n, H):
    comps=components(n,H)
    c=any(cyc and len(v) in (3,4) for v,cyc in comps)
    p=any(len(v)>=3 for v,cyc in comps)
    e=bool(H)
    return max(n, 6 if c else 0, 5 if p else 0, 3 if e else 0)


def explicit(n,H):
    # Input is canonically labeled in consecutive path/cycle component blocks.
    adj=[[] for _ in range(n)]
    for a,b in H: adj[a].append(b);adj[b].append(a)
    comps=components(n,H)
    K=expected(n,H)
    spokes={v:i for i,v in enumerate(range(n))}
    paint={tuple(sorted((n,v))):i for v,i in spokes.items()}
    for verts,cyclic in comps:
        if cyclic:
            start=min(verts);ordered=[start];prev=-1
            while True:
                v=ordered[-1]
                opts=[w for w in adj[v] if w!=prev]
                nxt=opts[0]
                if nxt==start:break
                prev=v;ordered.append(nxt)
            m=len(ordered)
            if m==3:
                extra=[c for c in range(K) if c not in [spokes[v] for v in ordered]]
                assert len(extra)>=3
                for j in range(3):paint[tuple(sorted((ordered[j],ordered[(j+1)%3])))]=extra[j]
            elif m==4:
                extra=[c for c in range(K) if c not in [spokes[v] for v in ordered]]
                assert len(extra)>=2
                for j in range(4):paint[tuple(sorted((ordered[j],ordered[(j+1)%4])))]=extra[j%2]
            else:
                for j in range(m):
                    paint[tuple(sorted((ordered[j],ordered[(j+1)%m])))]=spokes[ordered[(j+3)%m]]
        else:
            ends=[v for v in verts if len(adj[v])<=1]
            ordered=[min(ends)]
            prev=-1
            while len(ordered)<len(verts):
                v=ordered[-1];nxt=next(w for w in adj[v] if w!=prev)
                prev=v;ordered.append(nxt)
            for j in range(len(ordered)-1):
                a,b=ordered[j:j+2]
                if K<5:
                    x=next(c for c in range(K) if c not in (spokes[a],spokes[b]))
                else:
                    x=(spokes[a]+3)%K
                paint[tuple(sorted((a,b)))]=x
    return paint


def canonical_order(n,H):
    # Relabel every component to a consecutive block, preserving adjacency.
    adj=[[] for _ in range(n)]
    for a,b in H: adj[a].append(b);adj[b].append(a)
    ordered=[]
    for verts,cyclic in components(n,H):
        if cyclic:
            start=min(verts); cur=start;prev=-1
            while cur not in ordered:
                ordered.append(cur)
                nexts=[w for w in adj[cur] if w!=prev]
                prev,cur=cur,nexts[0]
        else:
            start=min(v for v in verts if len(adj[v])<=1)
            cur=start;prev=-1
            while cur is not None:
                ordered.append(cur)
                nexts=[w for w in adj[cur] if w!=prev]
                prev,cur=cur,(nexts[0] if nexts else None)
    assert len(ordered)==n and len(set(ordered))==n
    trans={v:i for i,v in enumerate(ordered)}
    E={tuple(sorted((trans[a],trans[b]))) for a,b in H}
    return E


def conflicts(n,H):
    edges=[tuple(sorted((n,v))) for v in range(n)] + sorted(H)
    edge_lookup={e:i for i,e in enumerate(edges)}
    bad=set()
    for i,e in enumerate(edges):
        for j,f in enumerate(edges):
            if j>i and set(e)&set(f):bad.add((i,j))
    for four in combinations(range(n+1),4):
        present=[edge_lookup[e] for e in combinations(four,2) if e in edge_lookup]
        if len(present)>=5:
            bad|=set(combinations(present,2))
    return edges,bad


def valid(n,H,paint):
    edges,bad=conflicts(n,H)
    assert set(paint)==set(edges),('missing',set(edges)-set(paint))
    return all(paint[edges[i]]!=paint[edges[j]] for i,j in bad)


def kcolorable(vertices,bad,K):
    adj=[set() for _ in range(vertices)]
    for a,b in bad:adj[a].add(b);adj[b].add(a)
    color=[-1]*vertices
    def rec(used):
        left=[v for v in range(vertices) if color[v]<0]
        if not left:return True
        v=max(left,key=lambda i:(len({color[w] for w in adj[i] if color[w]>=0}),len(adj[i])))
        avoid={color[w] for w in adj[v] if color[w]>=0}
        for c in range(min(K,used+1)):
            if c not in avoid:
                color[v]=c
                if rec(max(used,c+1)):return True
        color[v]=-1
        return False
    return rec(0)


def make(n,segments):
    edges=set();i=0
    for typ,m in segments:
        for j in range(m-1):edges.add((i+j,i+j+1))
        if typ=='C':edges.add((i,i+m-1))
        i+=m
    assert i==n
    return edges


def partitions(n,maxk=None):
    if n==0:yield ();return
    if maxk is None:maxk=n
    for k in range(min(n,maxk),1-1,-1):
        for tail in partitions(n-k,k):yield (k,)+tail


def run():
    cases=0
    for n in range(1,6):
        pairs=list(combinations(range(n),2))
        for mask in range(1<<len(pairs)):
            H={pairs[i] for i in range(len(pairs)) if mask>>i&1}
            deg=[0]*n
            for a,b in H:deg[a]+=1;deg[b]+=1
            if max(deg)>2:continue
            H=canonical_order(n,H)
            K=expected(n,H)
            paint=explicit(n,H)
            assert valid(n,H,paint),(n,H,K,paint)
            edges,bad=conflicts(n,H)
            assert kcolorable(len(edges),bad,K),(n,H,K)
            if K>=2:assert not kcolorable(len(edges),bad,K-1),(n,H,K)
            cases+=1
    print('ALL_LABELED_DEGREE_TWO_GRAPHS_N_LE_5_OK',cases)
    iso=0
    for n in range(1,11):
        seen=set()
        for part in partitions(n):
            def possible(part):
                if not part:yield ();return
                m,*rest=part
                for tail in possible(rest):
                    yield (('P',m),)+tail
                    if m>=3:yield (('C',m),)+tail
            for segments in possible(part):
                H=make(n,segments)
                key=(n,tuple(sorted(segments)))
                if key in seen:continue
                seen.add(key)
                K=expected(n,H)
                paint=explicit(n,H)
                assert valid(n,H,paint),(n,segments,K)
                edges,bad=conflicts(n,H)
                if n<=7:
                    assert not kcolorable(len(edges),bad,K-1),(n,segments,K)
                iso+=1
    print('UNLABELED_COMPONENT_PROFILES_N_LE_10_OK',iso)
    print('VERIFY_OK')

if __name__=='__main__':run()
