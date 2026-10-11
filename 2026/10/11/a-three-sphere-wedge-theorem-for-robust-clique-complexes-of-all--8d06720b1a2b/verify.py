"""Independent finite checks for the homology theorem on bounded-independence complexes.

Only elementary Python is used; the symbolic general proof is in RESULT.md.
"""
from itertools import combinations
from math import comb
from collections import deque


def rank_mod(columns, p):
    basis = {}
    for raw in columns:
        vec = dict(raw)
        while vec:
            pivot = max(vec)
            if pivot not in basis:
                inverse = pow(vec[pivot], -1, p)
                basis[pivot] = {k: (v*inverse)%p for k,v in vec.items() if (v*inverse)%p}
                break
            factor=vec[pivot]
            for k,v in basis[pivot].items():
                new=(vec.get(k,0)-factor*v)%p
                if new: vec[k]=new
                else: vec.pop(k,None)
    return len(basis)


def connected(n,edges):
    nbr=[set() for _ in range(n)]
    for u,v in edges: nbr[u].add(v);nbr[v].add(u)
    seen={0};q=deque([0])
    while q:
        for w in nbr[q.popleft()]:
            if w not in seen: seen.add(w);q.append(w)
    return len(seen)==n


def faces(n,edges):
    E={tuple(sorted(e)) for e in edges}
    fs=[list((i,) for i in range(n)), list(combinations(range(n),2)), [], []]
    for t in combinations(range(n),3):
        if any(e in E for e in combinations(t,2)): fs[2].append(t)
    for t in combinations(range(n),4):
        if any(e in E and f in E and set(e).isdisjoint(f)
               for e,f in combinations(combinations(t,2),2)):
            fs[3].append(t)
    return fs


def boundary_columns(fs,dim,p):
    dest={face:i for i,face in enumerate(fs[dim-1])}
    cols=[]
    for face in fs[dim]:
        col={dest[sub]: (1 if j%2==0 else p-1) for j in range(len(face))
             for sub in [face[:j]+face[j+1:]]}
        cols.append(col)
    return cols


def fourcycles(n,edges):
    E={tuple(sorted(e)) for e in edges}
    return sum(sum(int(tuple(sorted(pair)) in E) for pair in combinations(t,2))==4
               for t in combinations(range(n),4))


def verify(n, edges):
    assert connected(n,edges)
    fs=faces(n,edges)
    b=len(edges)-n+1
    c4=fourcycles(n,edges)
    expected=comb(b+1,2)-c4
    assert expected>=0
    assert len(fs[2]) == len(edges)*(n-2)-sum(comb(sum(v in e for e in edges),2) for v in range(n))
    assert len(fs[3]) == comb(len(edges),2)-sum(comb(sum(v in e for e in edges),2) for v in range(n))-c4
    for p in (2,3):
        r2=rank_mod(boundary_columns(fs,2,p),p)
        r3=rank_mod(boundary_columns(fs,3,p),p)
        h1=len(fs[1])-(n-1)-r2
        h2=len(fs[2])-r2-r3
        h3=len(fs[3])-r3
        assert (h1,h2,h3)==(0,0,expected), (n,len(edges),p,(h1,h2,h3),expected)
    return (len(fs[2]),len(fs[3]),expected)


def mask_to_edges(a,b,mask):
    return [(i,a+j) for i in range(a) for j in range(b) if (mask>>(i*b+j))&1]


def verify_relative_insertions(a,b):
    tested=0
    n=a+b
    for mask in range(1<<(a*b)):
        E=set(mask_to_edges(a,b,mask))
        if not connected(n,E): continue
        oldfaces=faces(n,E)
        for aa in range(a):
            for bb in range(a,n):
                if (aa,bb) in E: continue
                updated=faces(n,E|{(aa,bb)})
                U=[v for v in range(n) if v not in (aa,bb) and
                   tuple(sorted((aa,v))) not in E and tuple(sorted((bb,v))) not in E]
                triangles=[f for f in updated[2] if f not in set(oldfaces[2])]
                assert set(triangles)=={tuple(sorted((aa,bb,v))) for v in U}
                tindex={v:i for i,v in enumerate(U)}
                oldtetra=set(oldfaces[3])
                columns=[]
                for face in updated[3]:
                    if face in oldtetra: continue
                    projected={}
                    for j in range(4):
                        sub=face[:j]+face[j+1:]
                        if sub in triangles:
                            v=next(v for v in sub if v not in (aa,bb))
                            projected[tindex[v]]=1 if j%2==0 else -1
                    columns.append(projected)
                assert rank_mod([{i:v%2 for i,v in col.items()} for col in columns],2)==len(U)
                assert rank_mod([{i:v%3 for i,v in col.items()} for col in columns],3)==len(U)
                tested+=1
    return tested


def main():
    count=0
    for a,b in [(1,1),(2,2),(2,3),(3,3)]:
        for mask in range(1<<(a*b)):
            edges=mask_to_edges(a,b,mask)
            if connected(a+b,edges):
                verify(a+b,edges)
                count+=1
    # Larger, structurally different graphs, including a square-free 14-vertex cubic graph.
    cube=[(i,j) for i in range(8) for j in range(i+1,8) if (i^j).bit_count()==1]
    verify(8,cube);count+=1
    # Heawood incidence graph of points and lines of the Fano plane.
    lines=[(0,1,3),(1,2,4),(2,3,5),(3,4,6),(4,5,0),(5,6,1),(6,0,2)]
    heawood=[(i,7+j) for j,L in enumerate(lines) for i in L]
    verify(14,heawood);count+=1
    # Long cycles (no four-cycles), dense bicliques and a pair of linked cycles.
    for n in (6,8,10,12):
        verify(n,[(i,(i+1)%n) for i in range(n)]);count+=1
    for a,b in ((2,5),(3,4),(4,4)):
        verify(a+b,[(i,a+j) for i in range(a) for j in range(b)]);count+=1
    verify(10, [(0,1),(1,2),(2,3),(3,0),(3,4),(4,5),(5,6),(6,3),(6,7),(7,8),(8,9),(9,6)])
    count+=1
    steps=verify_relative_insertions(3,3)
    print('VERIFY_OK',count,'connected graphs and',steps,'edge insertions; mod 2/3 exact ranks')

if __name__=='__main__': main()
