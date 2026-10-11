"""Independent finite checks of the line-graph radius-one Cech collapse."""
from itertools import combinations
from collections import Counter


def generalized_petersen(n, k):
    return sorted({tuple(sorted(e)) for i in range(n) for e in
                   ((i, (i+1)%n), (i, n+i), (n+i, n+(i+k)%n))})


def heawood_edges():
    return sorted((i, 7+j) for i in range(7) for j in range(7)
                  if (i-j)%7 in (0, 1, 3))


def all_faces(facets):
    faces = set()
    for F in facets:
        vs = [j for j in range(F.bit_length()) if F>>j & 1]
        for k in range(1, len(vs)+1):
            for tup in combinations(vs, k):
                faces.add(sum(1 << v for v in tup))
    return faces


def check(edges, title):
    edges=sorted({tuple(sorted(e)) for e in edges})
    m=len(edges)
    assert m and all(u!=v for u,v in edges)
    # For each original edge e, its line-graph closed neighborhood.
    fac=[]
    for u,v in edges:
        fac.append(sum(1<<j for j,(a,b) in enumerate(edges)
                       if u in (a,b) or v in (a,b)))
    complex_faces=all_faces(fac)
    vertices=set(u for e in edges for u in e)
    star=[sum(1<<i for i,e in enumerate(edges) if u in e)
          for u in sorted(vertices)]
    spine=all_faces(star)
    assert spine<=complex_faces
    excess=complex_faces-spine
    match={}
    for s in excess:
        contained=[j for j,f in enumerate(fac) if s & f==s]
        assert len(contained)==1, (title, s, contained)
        j=contained[0]
        if not s>>j&1:
            assert s|(1<<j) in excess
            match[s]=s|(1<<j)
    assert set(match)|set(match.values())==excess
    assert len(match)*2==len(excess)
    active=set(complex_faces)
    for low in sorted(match,key=lambda x:(-x.bit_count(),x)):
        high=match[low]
        assert low in active and high in active
        other=[c for c in active if c!=low and c & low==low]
        assert other==[high], (title,low,other)
        active.remove(low); active.remove(high)
    assert active==spine
    fv=Counter(s.bit_count()-1 for s in complex_faces)
    fs=Counter(s.bit_count()-1 for s in spine)
    n=len(vertices)
    beta1=m-n+1
    d=Counter(u for e in edges for u in e)
    total_line_graph_edges=sum(k*(k-1)//2 for k in d.values())
    local_kernel_rank=sum((k-1)*(k-2)//2 for k in d.values() if k>=2)
    assert total_line_graph_edges-m+1-beta1==local_kernel_rank
    assert sum((-1)**d*x for d,x in fs.items())==1-beta1
    assert sum((-1)**d*x for d,x in fv.items())==1-beta1
    print(title, 'vertices',n,'edges',m,'Cech_faces',len(complex_faces),
          'spine_faces',len(spine),'collapse_pairs',len(match),
          'H1_rank',beta1,'Cech_fvector',sorted(fv.items()))


def c4_boundary_check():
    edges=sorted((i,(i+1)%4) if i<3 else (0,3) for i in range(4))
    fac=[]
    for i,(u,v) in enumerate(edges):
        fac.append(sum(1<<j for j,(a,b) in enumerate(edges)
                       if u in (a,b) or v in (a,b)))
    F=all_faces(fac)
    assert len(F)==14 and sum(f.bit_count()==3 for f in F)==4
    assert not any(f.bit_count()==4 for f in F)
    print('C4_boundary_S2',len(F),'faces')

if __name__=='__main__':
    check([(i,i+1) for i in range(6)],'path_P7')
    check([(i,(i+1)%5) for i in range(5)],'cycle_C5')
    check([(0,i) for i in range(1,6)],'star_K1_5')
    check(generalized_petersen(5,2),'Petersen')
    check(heawood_edges(),'Heawood')
    check(generalized_petersen(10,2),'Dodecahedron')
    check([(i,(i+1)%5) for i in range(5)]+[(0,5),(5,6),(6,7),(7,8),(8,0)], 'two_C5_one_vertex_wedge')
    c4_boundary_check()
    print('VERIFY_OK')
