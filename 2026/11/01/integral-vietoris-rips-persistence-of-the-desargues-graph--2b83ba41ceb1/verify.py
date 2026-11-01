#!/usr/bin/env python3
"""Standalone finite verification of the Desargues graph Rips filtration.

Run from the directory containing certificates/: python3 verify.py
Python >= 3.9; no third-party packages.
The 20 vertices are u_0..u_9 (0..9) and v_0..v_9 (10..19).
"""
from collections import Counter, deque
from pathlib import Path
import json

N = 20

def graph_and_distances():
    adjacency = [set() for _ in range(N)]
    def edge(a,b):
        assert a != b
        adjacency[a].add(b)
        adjacency[b].add(a)
    for i in range(10):
        edge(i,(i+1)%10)
        edge(i,10+i)
        edge(10+i,10+(i+3)%10)
    assert all(len(s)==3 for s in adjacency)
    assert sum(map(len,adjacency))//2 == 30
    distances=[]
    for s in range(N):
        d=[-1]*N;d[s]=0
        q=deque([s])
        while q:
            u=q.popleft()
            for v in adjacency[u]:
                if d[v]<0:
                    d[v]=d[u]+1;q.append(v)
        assert all(t>=0 for t in d)
        distances.append(d)
    counts=Counter(distances[a][b] for a in range(N) for b in range(a+1,N))
    assert counts=={1:30,2:60,3:60,4:30,5:10},counts
    return adjacency,distances

def clique_faces(distances,r):
    neigh=[sum(1<<j for j in range(N) if i!=j and distances[i][j]<=r)
           for i in range(N)]
    faces=set()
    def visit(m,c):
        if m:faces.add(m)
        while c:
            b=c&-c;c^=b
            i=b.bit_length()-1
            visit(m|b,c&neigh[i])
    visit(0,(1<<N)-1)
    return faces

def bit_dimensions(faces):
    return dict(sorted(Counter(x.bit_count()-1 for x in faces).items()))

def check_certificate(faces,steps,scale):
    active=set(faces)
    matching={}
    critical=[]
    for step_number,step in enumerate(steps,1):
        if step[0]==0:
            assert len(step)==3,step_number
            f,g=step[1:]
            assert f in active and g in active, (step_number,'inactive')
            assert f&g==f and g.bit_count()==f.bit_count()+1,step_number
            # In the remaining simplicial complex, f belongs to precisely one
            # larger simplex, g. Consequently f is a free facet of g.
            cofaces=[h for h in active if h!=f and h&f==f]
            assert cofaces==[g],(step_number,'not free',len(cofaces))
            active.remove(f);active.remove(g)
            matching[f]=g
        elif step[0]==1:
            assert len(step)==2,step_number
            g=step[1]
            assert g in active,step_number
            assert all((h&g)!=g or h==g for h in active),(step_number,'not maximal')
            active.remove(g);critical.append(g)
        else:raise AssertionError((step_number,'invalid operation'))
    assert not active,('unprocessed',len(active))
    assert len(matching)*2+len(critical)==len(faces)
    expected={2:{0:1,2:19},3:{0:1,3:1}}[scale]
    assert bit_dimensions(critical)==expected,(scale,bit_dimensions(critical))
    # Independently check there is no directed cycle in the full reversed
    # face-poset Hasse diagram: each matching arrow is reversed.
    indeg={x:0 for x in faces};successors={x:[] for x in faces}
    for g in faces:
        if g.bit_count()<=1:continue
        t=g
        while t:
            bit=t&-t;t^=bit
            f=g^bit
            assert f in faces
            if matching.get(f)==g:src,dst=f,g
            else:src,dst=g,f
            successors[src].append(dst);indeg[dst]+=1
    q=deque(x for x in faces if indeg[x]==0);seen=0
    while q:
        a=q.popleft();seen+=1
        for b in successors[a]:
            indeg[b]-=1
            if indeg[b]==0:q.append(b)
    assert seen==len(faces),(scale,'nonacyclic matching',seen,len(faces))
    return len(matching),bit_dimensions(critical)

def mod2_ranks(faces):
    groups={}
    for x in faces:groups.setdefault(x.bit_count()-1,[]).append(x)
    ranks={0:0}
    for d in range(1,max(groups)+1):
        idx={x:i for i,x in enumerate(groups[d-1])}
        pivots={}
        for simplex in groups[d]:
            col=0;t=simplex
            while t:
                b=t&-t;t^=b;col ^= 1 << idx[simplex^b]
            while col:
                hi=col.bit_length()-1
                if hi in pivots:col^=pivots[hi]
                else:pivots[hi]=col;break
        ranks[d]=len(pivots)
    betti={d:len(group)-ranks[d]-ranks.get(d+1,0) for d,group in groups.items()}
    return ranks,betti

def check_girth_hexagons(adjacency):
    # Identify undirected simple hexagons modulo cyclic shifts and reversal.
    cycles=set()
    for root in range(N):
        def walk(path):
            if len(path)==6:
                if root in adjacency[path[-1]]:
                    a=tuple(path)
                    b=a[::-1]
                    candidates=[tuple(a[i:]+a[:i]) for i in range(6)]
                    candidates += [tuple(b[i:]+b[:i]) for i in range(6)]
                    cycles.add(min(candidates))
                return
            for nxt in adjacency[path[-1]]:
                if nxt>root and nxt not in path:
                    walk(path+[nxt])
        walk([root])
    assert len(cycles)==20,len(cycles)
    edge_counts=Counter()
    for cyc in cycles:
        for i in range(6):
            edge_counts[tuple(sorted((cyc[i],cyc[(i+1)%6])))]+=1
    assert len(edge_counts)==30 and set(edge_counts.values())=={4}
    # Verify girth six by looking for alternative paths after removing each edge.
    for u in range(N):
        for v in adjacency[u]:
            if v<=u:continue
            d={u:0}; q=deque([u])
            while q:
                x=q.popleft()
                for y in adjacency[x]:
                    if {x,y}=={u,v}:continue
                    if y not in d:
                        d[y]=d[x]+1;q.append(y)
            assert d[v]>=5
    print('girth 6: 20 undirected simple hexagons, four through every edge')

def main():
    adjacency,distances=graph_and_distances()
    check_girth_hexagons(adjacency)
    for r,expected_faces in ((2,260),(3,3200)):
        faces=clique_faces(distances,r)
        assert len(faces)==expected_faces
        expected_dimensions={2:{0:20,1:90,2:120,3:30},
                             3:{0:20,1:150,2:540,3:1000,4:960,5:450,6:80}}[r]
        assert bit_dimensions(faces)==expected_dimensions
        cert=json.loads((Path(__file__).parent/'certificates'/f'r{r}_steps.json').read_text(encoding='utf-8'))
        assert cert['scale']==r
        pairs,critical=check_certificate(faces,cert['steps'],r)
        ranks,betti=mod2_ranks(faces)
        assert betti==({0:1,1:0,2:19,3:0} if r==2
                      else {0:1,1:0,2:0,3:1,4:0,5:0,6:0})
        print('r',r,'faces',len(faces),'matching_pairs',pairs,
              'critical',critical,'boundary_ranks',ranks,'betti',betti)
    pairs=[(a,b) for a in range(N) for b in range(a+1,N) if distances[a][b]==5]
    assert len(pairs)==10
    assert sorted(v for pair in pairs for v in pair)==list(range(N))
    assert all(pairs[i][1]-pairs[i][0]==5 for i in range(10))
    print('r 4: ten disjoint forbidden pairs, join of ten 0-spheres = S^9')
    print('r 5: diameter five, full 19-simplex')
    print('VERIFY_OK')

if __name__=='__main__':main()
