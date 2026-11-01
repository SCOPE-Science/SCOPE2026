#!/usr/bin/env python3
"""Finite, independent tests for perfect-matching complexes of two-layer graphs.

No packages beyond the Python standard library are needed.  This checks finite
instances; the proof for all even-cycle-free graphs is mathematical, not an
extrapolation from the tests.
"""
from collections import Counter, deque
from itertools import combinations
import random


def edge_norm(edges):
    return tuple(sorted(tuple(sorted(e)) for e in edges))


def graph_matchings(n, edges):
    """All disjoint-edge selections, as edge-index tuples."""
    result = []
    def walk(i, occupied, chosen):
        if i == len(edges):
            result.append(tuple(chosen))
            return
        walk(i + 1, occupied, chosen)
        u, v = edges[i]
        if not (occupied & (1 << u | 1 << v)):
            chosen.append(i)
            walk(i + 1, occupied | 1 << u | 1 << v, chosen)
            chosen.pop()
    walk(0, 0, [])
    return result


def prism_edges(n, edges):
    return tuple(edges) + tuple((u+n, v+n) for u, v in edges) + tuple((i,i+n) for i in range(n))


def perfect_matchings(n, edges):
    inc = [[] for _ in range(n)]
    for k,(u,v) in enumerate(edges):
        inc[u].append((k,v)); inc[v].append((k,u))
    out=[]
    def walk(left,mask):
        if not left:
            out.append(mask);return
        x = (left & -left).bit_length() - 1
        for k,y in inc[x]:
            if left & (1<<y):
                walk(left & ~(1<<x) & ~(1<<y), mask | (1<<k))
    walk((1<<n)-1,0)
    return tuple(sorted(out))


def has_even_cycle(n,edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
    def dfs(start,current,visited,depth):
        for w in adj[current]:
            if w == start and depth >= 4 and depth % 2 == 0:
                return True
            if w > start and w not in visited and dfs(start,w,visited | {w},depth+1):
                return True
        return False
    for a in range(n):
        for b in adj[a]:
            if b>a and dfs(a,b,{a,b},2):
                return True
    return False


def faces_from_facets(facets):
    fs={0}
    for f in facets:
        sub=f
        while sub:
            fs.add(sub)
            sub=(sub-1)&f
    return fs


def predicted_perfect_matchings(n,edges):
    q=len(edges); facets=[]
    for mm in graph_matchings(n,edges):
        covered=0;mask=0
        for j in mm:
            u,v=edges[j]
            covered |= (1<<u)|(1<<v)
            mask |= (1<<j)|(1<<(q+j))
        for v in range(n):
            if not(covered>>v&1):
                mask |= (1<<(2*q+v))
        facets.append(mask)
    return tuple(sorted(facets))


def predicted_faces(n,edges):
    q=len(edges); result=set()
    for facet in predicted_perfect_matchings(n,edges):
        sub=facet
        while True:
            result.add(sub)
            if sub==0: break
            sub=(sub-1)&facet
    return result


def projection(n,edges,face):
    q=len(edges); chosen=0;cover=0
    for j,(u,v) in enumerate(edges):
        if (face>>j)&1 or (face>>(q+j))&1:
            if cover&(1<<u | 1<<v):
                raise AssertionError('horizontal projection fails to be a matching')
            chosen |= 1<<j
            cover |= 1<<u | 1<<v
    return chosen,cover


def morse_pairs(n,edges,fs):
    q=len(edges);full=(1<<n)-1
    done=set(); pairs=[];critical=[]
    for s in sorted(fs):
        if s in done:continue
        hor,cover=projection(n,edges,s)
        if cover!=full:
            v=((full^cover)&-(full^cover)).bit_length()-1
            mate=s^(1<<(2*q+v))
        else:
            k=next((j for j in range(q) if (s>>(q+j))&1),None)
            if k is None:
                critical.append(s);done.add(s);continue
            mate=s^(1<<k)
        assert mate in fs and mate not in done and (s^mate).bit_count()==1
        lo,hi=sorted((s,mate),key=int.bit_count)
        pairs.append((lo,hi))
        done.add(s);done.add(mate)
    assert len(done)==len(fs)
    return pairs,critical


def verify_acyclic(fs,pairs):
    pairset=set(pairs);succ={x:[] for x in fs};indeg={x:0 for x in fs}
    for s in fs:
        t=s
        while t:
            bit=t & -t
            sub=s^bit
            if (sub,s) in pairset: src,dst=sub,s
            else:src,dst=s,sub
            succ[src].append(dst);indeg[dst]+=1
            t-=bit
    q=deque(x for x,d in indeg.items() if d==0)
    seen=0
    while q:
        x=q.popleft();seen+=1
        for y in succ[x]:
            indeg[y]-=1
            if indeg[y]==0:q.append(y)
    assert seen==len(fs),('cycle in matching',seen,len(fs))
    return sum(map(len,succ.values()))


def betti_mod2(fs):
    bydim={}
    for s in fs:
        bydim.setdefault(s.bit_count()-1,[]).append(s)
    ranks={}
    for d in sorted(k for k in bydim if k>=1):
        row={s:i for i,s in enumerate(bydim[d-1])}; basis={}
        for s in bydim[d]:
            col=0;t=s
            while t:
                bit=t&-t;col^=1<<row[s^bit];t-=bit
            while col:
                j=col.bit_length()-1
                if j in basis:col ^= basis[j]
                else:basis[j]=col;break
        ranks[d]=len(basis)
    return {d:len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0)-(d==0)
            for d in bydim if d>=0 and len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0)-(d==0)}


def test(n, edges, do_acyclic=True, do_betti=True):
    edges=edge_norm(edges)
    assert not has_even_cycle(n,edges)
    real=perfect_matchings(2*n,prism_edges(n,edges))
    predicted=predicted_perfect_matchings(n,edges)
    assert real==predicted,('wrong facet characterization',n,edges)
    fs=faces_from_facets(real)
    assert fs==predicted_faces(n,edges)
    pairs,crit=morse_pairs(n,edges,fs)
    pm=perfect_matchings(n,edges)
    assert len(pm)<=1
    if pm:
        assert len(crit)==1 and crit[0].bit_count()==n//2
    else:
        assert not crit
    arcs=verify_acyclic(fs,pairs) if do_acyclic else None
    betti=betti_mod2(fs) if do_betti else None
    if do_betti:
        expected={} if not pm else {n//2-1:1}
        assert betti==expected,(n,edges,betti,expected)
    return len(fs),len(pairs),len(crit),arcs


def main():
    checked=0;totalfaces=0;totalarcs=0;withpm=0
    for n in range(1,6):
        all_edges=list(combinations(range(n),2))
        for mask in range(1<<len(all_edges)):
            edges=[e for j,e in enumerate(all_edges) if mask>>j&1]
            if has_even_cycle(n,edges):continue
            fs,pairs,crit,arcs=test(n,edges)
            checked+=1;totalfaces+=fs;totalarcs+=arcs
            if crit:withpm+=1
    print('Exhaustive labeled even-cycle-free graphs on 1..5 vertices:',checked,
          'perfect-matching base graphs:',withpm,'faces checked:',totalfaces,
          'oriented incidences checked:',totalarcs)
    samples={
      'path6':(6,[(i,i+1) for i in range(5)]),
      'odd_cycle7':(7,[(i,(i+1)%7) for i in range(7)]),
      'bowtie':(5,[(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)]),
      'two_triangles_bridge':(6,[(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(2,3)]),
      'triangle_with_leaf':(4,[(0,1),(1,2),(2,0),(0,3)]),
      'disconnected_edges':(6,[(0,1),(2,3),(4,5)]),
      'star7':(7,[(0,i) for i in range(1,7)]),
    }
    for name,(n,e) in samples.items():
        f,p,c,a=test(n,e)
        print('sample',name,'n',n,'faces',f,'pairs',p,'critical',c,'incidences',a)
    # Deliberate hypothesis boundary: H=C4 has an even cycle.
    ring=edge_norm([(i,(i+1)%4) for i in range(4)])
    assert has_even_cycle(4,ring)
    real=perfect_matchings(8,prism_edges(4,ring));faces=faces_from_facets(real)
    bb=betti_mod2(faces)
    assert bb=={1:4},bb
    print('even-cycle boundary C4: reduced mod-2 Betti vector',bb,
          '(not the single-circle case)')
    print('EVEN_CYCLE_FREE_PRISM_PERFECT_MATCHING_MORSE_OK')

if __name__=='__main__':main()
