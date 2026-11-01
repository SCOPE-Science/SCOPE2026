#!/usr/bin/env python3
"""Exact integral homology of doubles of six-dimensional cyclic-polytope boundaries.
Run: python3 verify.py  (requires SymPy). All assertions use exact arithmetic.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

# m, facet count, (f0,f1,f2), critical (c0,c1,c2), Morse rank,
# free first Betti, nontrivial integral elementary divisors, second Betti.
EXPECTED = {
 7:(7,(21,105,105),(1,7,27),7,0,(3,),20),
 8:(16,(28,204,240),(1,23,86),8,15,(),78),
 9:(30,(36,351,450),(1,33,167),33,0,(),134),
 10:(50,(45,555,750),(1,47,286),23,24,(2,),263),
 11:(77,(55,825,1155),(1,63,447),63,0,(),384),
 12:(112,(66,1170,1680),(1,81,656),46,35,(3,),610),
 13:(156,(78,1599,2340),(1,101,919),101,0,(),818),
 14:(210,(91,2121,3150),(1,123,1242),75,48,(4,),1167),
 15:(275,(105,2745,4125),(1,147,1631),147,0,(),1484),
 16:(352,(120,3480,5280),(1,173,2092),110,63,(5,),1982),
}

def cyclic_facets(m):
    """Gale evenness characterizes all boundary facets of C(m,6)."""
    for facet in combinations(range(m),6):
        outside=[v for v in range(m) if v not in facet]
        if all(sum(a<v<b for v in facet)%2==0 for a,b in combinations(outside,2)):
            yield facet

def all_pairings(points):
    if not points:
        yield (); return
    a=points[0]
    for j in range(1,len(points)):
        for rest in all_pairings(points[1:j]+points[j+1:]):
            yield ((a,points[j]),)+rest

def double_faces(m):
    facets=tuple(cyclic_facets(m))
    edge_vertices=tuple(combinations(range(m),2))
    index={e:i for i,e in enumerate(edge_vertices)}
    faces=set()
    for facet in facets:
        for k in (1,2,3):
            for subset in combinations(facet,2*k):
                for matching in all_pairings(subset):
                    faces.add(tuple(sorted(index[e] for e in matching)))
    faces=tuple(sorted(faces,key=lambda f:(len(f),f)))
    assert len(faces)==len(set(faces))
    return facets,edge_vertices,faces

def discrete_matching(faces,nverts):
    free=set(faces); pairs={}
    for v in range(nverts):
        for face in sorted((f for f in free if v not in f),key=lambda f:(len(f),f)):
            coface=tuple(sorted(face+(v,)))
            if face in free and coface in free:
                free.remove(face);free.remove(coface);pairs[face]=coface
    assert 2*len(pairs)+len(free)==len(faces)
    return free,pairs

def dag_check(faces,pairs):
    """Orient unmatched Hasse edges down, matched edges up; Kahn-sort all."""
    index={face:i for i,face in enumerate(faces)}
    adj=[[] for _ in faces]; indegree=[0]*len(faces);incidences=0
    for coface in faces:
        if len(coface)==1: continue
        for j in range(len(coface)):
            face=coface[:j]+coface[j+1:]
            assert face in index
            if pairs.get(face)==coface:
                u,v=index[face],index[coface]
            else:
                u,v=index[coface],index[face]
            adj[u].append(v);indegree[v]+=1;incidences+=1
    queue=deque(i for i,v in enumerate(indegree) if v==0);done=0
    while queue:
        v=queue.popleft();done+=1
        for w in adj[v]:
            indegree[w]-=1
            if indegree[w]==0: queue.append(w)
    assert done==len(faces),(done,len(faces))
    return incidences

def morse_columns(free,pairs):
    critical_edges=tuple(sorted(f for f in free if len(f)==2))
    critical_triangles=tuple(sorted(f for f in free if len(f)==3))
    edge_ix={e:i for i,e in enumerate(critical_edges)}
    edge_triangle={f:g for f,g in pairs.items() if len(f)==2}
    @lru_cache(None)
    def project(edge):
        if edge in edge_ix: return {edge_ix[edge]:1}
        if edge not in edge_triangle: return {}
        triangle=edge_triangle[edge]
        k=next(k for k in range(3) if triangle[:k]+triangle[k+1:]==edge)
        pivot=(-1)**k
        answer=Counter()
        for j in range(3):
            if j==k: continue
            other=triangle[:j]+triangle[j+1:]
            for i,val in project(other).items():
                answer[i]-=(-1)**j*pivot*val
        return {i:v for i,v in answer.items() if v}
    columns=[]
    for triangle in critical_triangles:
        col=Counter()
        for j in range(3):
            face=triangle[:j]+triangle[j+1:]
            for i,v in project(face).items(): col[i]+=(-1)**j*v
        columns.append({i:v for i,v in col.items() if v})
    return critical_edges,critical_triangles,columns

def modular_rank(columns,p):
    pivots={}
    for col in columns:
        c={i:z%p for i,z in col.items() if z%p}
        while c:
            k=max(c)
            if k not in pivots:
                pivots[k]=c;break
            fac=c[k]*pow(pivots[k][k],-1,p)%p
            for i,v in pivots[k].items():
                t=(c.get(i,0)-fac*v)%p
                if t:c[i]=t
                else:c.pop(i,None)
    return len(pivots)

def raw_boundary_rank_mod2(faces):
    """Independent unreduced simplicial-chain rank, not using Morse columns."""
    edges=[f for f in faces if len(f)==2]
    pos={f:i for i,f in enumerate(edges)}; pivots={}
    for triangle in (f for f in faces if len(f)==3):
        bits=0
        for j in range(3):
            bits ^= 1 << pos[triangle[:j]+triangle[j+1:]]
        while bits:
            j=bits.bit_length()-1
            if j in pivots:bits^=pivots[j]
            else: pivots[j]=bits;break
    return len(pivots)

def verify(m):
    facets,edges,faces=double_faces(m)
    counts=Counter(len(f)-1 for f in faces)
    fvec=tuple(counts[i] for i in range(3))
    assert fvec[0]==len(edges)
    assert fvec[1]>0 and fvec[2]>0
    free,pairs=discrete_matching(faces,len(edges))
    critical=Counter(len(f)-1 for f in free)
    cc=tuple(critical[i] for i in range(3))
    incidence=dag_check(faces,pairs)
    ce,ct,columns=morse_columns(free,pairs)
    assert len(ce)==cc[1] and len(ct)==cc[2]
    mat=Matrix([[col.get(i,0) for col in columns] for i in range(len(ce))])
    H=hermite_normal_form(mat)
    S=smith_normal_form(H,domain=ZZ)
    inv=tuple(abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i])
    rank=len(inv)
    b1=len(ce)-rank;b2=len(ct)-rank
    answer=(len(facets),fvec,cc,rank,b1,tuple(i for i in inv if i>1),b2)
    assert answer==EXPECTED[m],(m,answer,EXPECTED[m])
    # Every critical vertex is the unique zero-dimensional CW cell, so d1=0;
    # all other chain groups outside degrees 0,1,2 vanish.
    assert cc[0]==1
    # Independent mod-two elimination on the FULL simplicial boundary.
    # The extra mod-two first Betti is the number of even Smith invariants.
    raw_rank=raw_boundary_rank_mod2(faces)
    assert raw_rank==fvec[1]-(fvec[0]-1)-b1-sum(i%2==0 for i in inv)
    # Euler identity cross-check, independent of integer matrix reduction.
    assert fvec[0]-fvec[1]+fvec[2]==1-b1+b2
    if m in (7,10,12,14,16):
        ranks={p:modular_rank(columns,p) for p in (2,3,5,7,11)}
        assert ranks[11]==rank
        assert ranks[3 if m in (7,12) else (5 if m==16 else 2)]==rank-1
    else: ranks={}
    print(f'VERIFY_OK m={m} facets={len(facets)} f={fvec} matched={len(pairs)} incidences={incidence} critical={cc} smith_nonunit={[i for i in inv if i>1]} rank={rank} H1=Z^{b1}+torsion H2=Z^{b2} modular={ranks}',flush=True)

if __name__=='__main__':
    for m in range(7,17):verify(m)
    print('ALL_VERIFY_OK exact_homology_and_acyclicity m=7..16',flush=True)
