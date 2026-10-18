#!/usr/bin/env python3
"""Finite checks for Rips/Cech equality and explicit elementary collapse.
Only standard Python is required. Each tested graph is checked directly.
"""
from itertools import combinations, product
from collections import deque, Counter


def normalize(edges):
    return sorted(set(tuple(sorted((int(u), int(v)))) for u, v in edges))


def prufer(seq):
    n = len(seq) + 2
    degree = [1]*n
    for i in seq: degree[i] += 1
    out=[]
    for x in seq:
        leaf = min(i for i in range(n) if degree[i]==1)
        out.append((leaf,x));degree[leaf]-=1;degree[x]-=1
    a,b = [i for i in range(n) if degree[i]==1]
    out.append((a,b))
    return normalize(out)


def cycle(n): return normalize((i,(i+1)%n) for i in range(n))

def theta(a,b,c):
    edges=[]; nextvertex=2
    for l in (a,b,c):
        path=[0]+list(range(nextvertex,nextvertex+l-1))+[1]
        nextvertex+=l-1
        edges += list(zip(path,path[1:]))
    return normalize(edges)


def barbell7():
    edges=cycle(7)+[(u+7,v+7) for u,v in cycle(7)]+[(0,7)]
    return normalize(edges)


def line_distance_le2(edges,i,j):
    a,b=edges[i],edges[j]
    if set(a)&set(b): return True
    es=set(edges)
    return any(tuple(sorted((x,y))) in es for x in a for y in b)


def faces_of_supports(supports):
    ans={frozenset()}
    for support in supports:
        ss=tuple(sorted(support))
        for n in range(1,len(ss)+1):
            ans.update(map(frozenset,combinations(ss,n)))
    return ans


def test_graph(graph, name):
    edges=normalize(graph)
    m=len(edges)
    if m<1:return 0,0
    verts=sorted(set(v for e in edges for v in e))
    stars={v:{i for i,e in enumerate(edges) if v in e} for v in verts}
    balls=[stars[u]|stars[v] for (u,v) in edges]
    C=faces_of_supports(balls)
    Y=faces_of_supports(stars.values())
    # Construct every Rips face by direct pairwise distance tests, not by Cech supports.
    sq={i:set(j for j in range(m) if j!=i and line_distance_le2(edges,i,j)) for i in range(m)}
    # backtracking enumerates each clique once using ordered search.
    R={frozenset()}
    def grow(chosen,remaining):
        for pos,v in enumerate(remaining):
            nxt=chosen+(v,)
            R.add(frozenset(nxt))
            grow(nxt, [w for w in remaining[pos+1:] if w in sq[v]])
    grow((),list(range(m)))
    if R!=C:
        bad=next(iter(R^C))
        raise AssertionError(f'{name}: Rips-Cech mismatch: {sorted(bad)}')
    if not Y<=C:raise AssertionError(f'{name}: flag complex not a subcomplex')
    outside=C-Y
    lower_to_upper={}
    for face in outside:
        generators=[i for i,b in enumerate(balls) if face<=b]
        if len(generators)!=1:
            raise AssertionError(f'{name}: nonunique ball generator on {face}: {generators}')
        center=generators[0]
        if center not in face:
            mate=face|{center}
            if mate not in outside:raise AssertionError(f'{name}: partner not outside')
            lower_to_upper[face]=mate
    if len(lower_to_upper)*2!=len(outside):raise AssertionError(f'{name}: unpaired outside face')
    paired=set(lower_to_upper)|set(lower_to_upper.values())
    if paired!=outside:raise AssertionError(f'{name}: matching does not partition outside')
    live=set(C)
    # descending dimension, verify each pair is an actual simplicial free face
    for lo,hi in sorted(lower_to_upper.items(),key=lambda a:(-len(a[0]),tuple(sorted(a[0])))):
        if lo not in live or hi not in live:raise AssertionError(f'{name}: already removed')
        one_step=[t for t in live if len(t)==len(lo)+1 and lo<t]
        if one_step!=[hi]:raise AssertionError(f'{name}: not free: {sorted(lo)}; cofaces={len(one_step)}')
        live.remove(lo);live.remove(hi)
    if live!=Y:raise AssertionError(f'{name}: wrong final target')
    # target flag-complex nerve has graph homotopy type, so Euler chi=V-E.
    chi=sum((-1)**(len(s)-1) for s in Y if s)
    assert chi == len(verts)-m, (name,chi,len(verts),m)
    return len(R)-1,len(lower_to_upper)


def main():
    tests=[]
    for n in range(2,7):
        for seq in product(range(n),repeat=n-2):
            tests.append((prufer(seq),f'prufer_n{n}_{seq}'))
    for n in range(7,13):
        tests.append((cycle(n),f'cycle_n{n}'))
    for n in range(2,11):
        tests.append(([(i,i+1) for i in range(n-1)],f'path_n{n}'))
    for n in range(3,11):
        tests.append(([(0,i) for i in range(1,n)],f'star_n{n}'))
    tests.extend([(theta(4,4,4),'theta444'),(theta(3,4,4),'theta344'),(barbell7(),'barbell7')])
    counts=Counter()
    max_faces=max_pairs=0
    for g,name in tests:
        nf,np=test_graph(g,name)
        counts[name.split('_')[0].rstrip('0123456789')]+=1
        max_faces=max(max_faces,nf);max_pairs=max(max_pairs,np)
    print('PASS: Rips/Cech equality and literal elementary collapses for',len(tests),'graph cases.')
    print('Case breakdown:',', '.join(f'{k}={v}' for k,v in sorted(counts.items())))
    print('Largest tested Rips nonempty-face count:',max_faces)
    print('Largest tested collapse-pair count:',max_pairs)
    # Minimal girth-six obstruction: opposite points of C6 form the Rips-only triangle.
    e=cycle(6); M=len(e)
    s={i:set(j for j in range(M) if j!=i and line_distance_le2(e,i,j)) for i in range(M)}
    R6={frozenset()}
    for n in range(1,M+1):
        R6.update(frozenset(p) for p in combinations(range(M),n) if all(b in s[a] for a,b in combinations(p,2)))
    stars={v:{i for i,x in enumerate(e) if v in x} for v in range(6)}
    C6=faces_of_supports([stars[u]|stars[v] for u,v in e])
    assert R6!=C6
    assert len(R6-C6)==2 and all(len(t)==3 for t in R6-C6) and not set.intersection(*(set(t) for t in R6-C6))
    assert Counter(len(t) for t in R6 if t) == {1:6,2:12,3:8}
    print('PASS: six-cycle is the sharp failure; Rips-only faces are the two disjoint triangles.')
    print('VERIFY_OK')

if __name__=='__main__':main()
