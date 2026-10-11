#!/usr/bin/env python3
"""Reproducible finite check of the ordered two-point Abrams-surface classification.
All checks use only Python's standard library and enumerate every labeled graph
with at most six vertices; no imported math libraries or input data are needed.
"""
from itertools import combinations, permutations
from collections import defaultdict, deque
from hashlib import sha256


def edge_list(n):
    return list(combinations(range(n), 2))


def graph_from_mask(n, mask):
    adj=[set() for _ in range(n)]
    for i,(u,v) in enumerate(edge_list(n)):
        if mask>>i&1: adj[u].add(v);adj[v].add(u)
    return adj


def connected_adj(adj):
    n=len(adj);seen={0};stack=[0]
    while stack:
        for w in adj[stack.pop()]:
            if w not in seen:seen.add(w);stack.append(w)
    return len(seen)==n


def surface_link_good(adj,u,v):
    # Link vertices are movements of the first and second particles.
    left=[(0,w) for w in adj[u] if w!=v]
    right=[(1,w) for w in adj[v] if w!=u]
    nodes=left+right
    link={x:set() for x in nodes}
    for a in left:
        for b in right:
            if a[1]!=b[1]: link[a].add(b); link[b].add(a)
    if not nodes or any(len(link[x]) not in (1,2) for x in nodes):return False
    if sum(len(link[x])==1 for x in nodes) not in (0,2):return False
    seen={nodes[0]};stack=[nodes[0]]
    while stack:
        for w in link[stack.pop()]:
            if w not in seen:seen.add(w);stack.append(w)
    return len(seen)==len(nodes)


def surface_good(adj):
    return connected_adj(adj) and all(surface_link_good(adj,u,v) for u in range(len(adj)) for v in range(len(adj)) if u!=v)


def mask_from_edges(n,ed):
    ed={tuple(sorted(e)) for e in ed}
    return sum(1<<i for i,e in enumerate(edge_list(n)) if e in ed)


def iso_masks(n,ed):
    result=set()
    for perm in permutations(range(n)):
        mapped={tuple(sorted((perm[u],perm[v]))) for u,v in ed}
        result.add(mask_from_edges(n,mapped))
    return result


def expected(n):
    if n<5:return set()
    if n==5:
        cycle={(i,(i+1)%5) for i in range(5)}
        complete=set(edge_list(n))
        ans=iso_masks(n,cycle)
        for r in (0,1,2):ans|=iso_masks(n,complete-{(0,1),(2,3)} if r==2 else complete-{(0,1)} if r==1 else complete)
        return ans
    if n==6:
        cycle={(i,(i+1)%6) for i in range(6)}
        chords=[(0,3),(1,4),(2,5)]
        ans=set()
        for r in range(4):ans|=iso_masks(n,cycle|set(chords[:r]))
        return ans
    raise ValueError('expected only finite base cases')


def topology(n,ed):
    adj=[set() for _ in range(n)]
    for u,v in ed: adj[u].add(v);adj[v].add(u)
    assert surface_good(adj)
    e=sorted({tuple(sorted(uv)) for uv in ed});
    # Cubical 0-cells are ordered distinct vertex pairs.
    V=[(u,v) for u in range(n) for v in range(n) if u!=v]
    E=[(coord,edge,w) for edge in e for w in range(n) if w not in edge for coord in (0,1)]
    # coord=0: edge in first coordinate; coord=1: edge in second.
    F=[(a,b) for a in e for b in e if set(a).isdisjoint(b)]
    inc=defaultdict(list)
    for i,(a,b) in enumerate(F):
        x,y=a;p,q=b
        for one,sgn in [((0,a,p),1),((0,a,q),-1),((1,b,x),-1),((1,b,y),1)]:
            inc[one].append((i,sgn))
    assert set(E)==set(inc) and all(1<=len(inc[c])<=2 for c in E)
    edgeend={}
    graph={v:set() for v in V}
    for one in E:
        coord,edge,w=one;x,y=edge
        uv=((x,w),(y,w)) if coord==0 else ((w,x),(w,y))
        edgeend[one]=uv
        a,b=uv;graph[a].add(b);graph[b].add(a)
    def components(nodes, neigh):
        remain=set(nodes);comp=[]
        while remain:
            root=next(iter(remain));todo=[root];part={root};remain.remove(root)
            while todo:
                for y in neigh[todo.pop()]:
                    if y in remain:remain.remove(y);part.add(y);todo.append(y)
            comp.append(part)
        return comp
    comps=components(V,graph)
    bg=defaultdict(set)
    for one in E:
        if len(inc[one])==1:
            a,b=edgeend[one];bg[a].add(b);bg[b].add(a)
    assert all(len(v)==2 for v in bg.values())
    bcount=len(components(bg,bg))
    # Propagate signs of oriented squares across each interior 1-cell.
    orientation={}
    sqfaces=defaultdict(list)
    for one,arr in inc.items():
        if len(arr)==2:
            (i,si),(j,sj)=arr
            sqfaces[i].append((j,-si*sj));sqfaces[j].append((i,-si*sj))
    for start in range(len(F)):
        if start in orientation:continue
        orientation[start]=1;todo=[start]
        while todo:
            i=todo.pop()
            for j,sign in sqfaces[i]:
                candidate=orientation[i]*sign
                if j in orientation:assert orientation[j]==candidate
                else:orientation[j]=candidate;todo.append(j)
    chi=len(V)-len(E)+len(F)
    assert (2*len(comps)-bcount-chi)%2==0
    genus=(2*len(comps)-bcount-chi)//2
    return len(V),len(E),len(F),len(comps),chi,bcount,genus


def run():
    for n in (3,4,5,6):
        results={mask for mask in range(1<<(n*(n-1)//2)) if surface_good(graph_from_mask(n,mask))}
        exp=expected(n)
        assert results==exp, ('classification conflict',n, sorted(results-exp)[:8],sorted(exp-results)[:8])
        print('n=',n,'labeled_good=',len(results),'all_graphs=',1<<(n*(n-1)//2),'sha256_masks=',sha256(','.join(map(str,sorted(results))).encode()).hexdigest())
    for n,ed,label in [
        (5,{(i,(i+1)%5) for i in range(5)},'cycle5'),
        *( (5,set(edge_list(5))-{(0,1),(2,3)} if r==2 else set(edge_list(5))-{(0,1)} if r==1 else set(edge_list(5)),'K5 minus matching '+str(r)) for r in (0,1,2)),
        *( (6,{(i,(i+1)%6) for i in range(6)}|set([(0,3),(1,4),(2,5)][:r]),'C6 plus opposite chords '+str(r)) for r in (0,1,2,3)),
        (7,{(i,(i+1)%7) for i in range(7)},'cycle7'),
        (8,{(i,(i+1)%8) for i in range(8)},'cycle8')]:
        print(label,topology(n,ed))
    print('VERIFY_OK')
if __name__=='__main__':run()
