#!/usr/bin/env python3
"""Exact integral-homotopy certificate for the Morse complex of the six-vertex three-sun graph.

Only Python 3 standard library. All nonempty faces and all Hasse arrows
are enumerated; the final assertion is a complete finite acyclicity test.
"""
from collections import Counter,defaultdict,deque

V=6
EDGES=sorted([(0,1),(0,2),(1,2),(0,3),(1,3),(1,4),(2,4),(0,5),(2,5)])
INCIDENCES=[(u,e) for e in EDGES for u in e]
INDEX={pair:i for i,pair in enumerate(INCIDENCES)}
ORDER=[13,0,9,17,5,3,4,15,6,2,14,16,12,8,1,11,10,7]
assert len(EDGES)==9 and len(INCIDENCES)==18 and sorted(ORDER)==list(range(18))


def creates_cycle(parents,source,target):
    node=target
    while node!=-1:
        if node==source:return True
        node=parents[node]
    return False


def by_vertices():
    options=[[] for _ in range(V)]
    for e in EDGES:
        for u in e:
            v=e[0]^e[1]^u
            options[u].append((v,INDEX[(u,e)]))
    found=set()
    parents=[-1]*V
    def rec(i,face):
        if i==V:
            if face:found.add(face)
            return
        rec(i+1,face)
        for v,j in options[i]:
            if creates_cycle(parents,i,v):continue
            parents[i]=v
            rec(i+1,face|(1<<j))
            parents[i]=-1
    rec(0,0)
    return found


def by_edges():
    found=set()
    parents=[-1]*V
    def rec(i,face):
        if i==len(EDGES):
            if face:found.add(face)
            return
        edge=EDGES[i]
        rec(i+1,face)
        for u in edge:
            if parents[u]!=-1:continue
            v=edge[0]^edge[1]^u
            if creates_cycle(parents,u,v):continue
            parents[u]=v
            rec(i+1,face|(1<<INDEX[(u,edge)]))
            parents[u]=-1
    rec(0,0)
    return found


def pivot_matching(faces):
    unmatched=set(faces)
    pairs={}
    for j in ORDER:
        bit=1<<j
        for a in sorted(unmatched):
            if a not in unmatched or a&bit:continue
            b=a|bit
            if b in unmatched:
                unmatched.remove(a)
                unmatched.remove(b)
                pairs[a]=b
    assert len(faces)==len(unmatched)+2*len(pairs)
    return unmatched,pairs


def verify_acyclic(faces,pairs):
    in_degree={f:0 for f in faces}
    arrows=defaultdict(list)
    h=0
    for b in faces:
        bits=b
        while bits:
            bit=bits&-bits
            bits^=bit
            a=b^bit
            if not a:continue
            source,dest=(a,b) if pairs.get(a)==b else (b,a)
            in_degree[dest]+=1
            arrows[source].append(dest)
            h+=1
    ready=deque(x for x,k in in_degree.items() if k==0)
    consumed=0
    while ready:
        x=ready.popleft()
        consumed+=1
        for y in arrows[x]:
            in_degree[y]-=1
            if in_degree[y]==0:ready.append(y)
    assert consumed==len(faces),f'gradient cycle detected: {consumed}/{len(faces)} vertices consumed'
    return h


def rank_mod2(faces,s):
    rows=sorted(f for f in faces if f.bit_count()==s-1)
    rowindex={f:i for i,f in enumerate(rows)}
    pivots={}
    for col in sorted(f for f in faces if f.bit_count()==s):
        bitmask=col
        vec=0
        while bitmask:
            bit=bitmask&-bitmask
            bitmask-=bit
            vec^=1<<rowindex[col^bit]
        while vec:
            lead=vec.bit_length()-1
            if lead not in pivots:
                pivots[lead]=vec
                break
            vec^=pivots[lead]
    return len(pivots)


def main():
    # The usual complete-source, dominating-pair and complete-multipartite
    # directed-tree shellability hypotheses do not hold for this graph.
    nbr=[set() for _ in range(V)]
    for u,v in EDGES:
        nbr[u].add(v);nbr[v].add(u)
    assert all(len(n)<V-1 for n in nbr)
    def dominant_pair(u,v):
        if nbr[u]|nbr[v]!=set(range(V)):return False
        left=nbr[u]-nbr[v]
        right=nbr[v]-nbr[u]
        return all(y in nbr[x] for x in left for y in right)
    assert not any(dominant_pair(u,v) for u in range(V) for v in range(u+1,V))
    # Nonadjacency is not transitive: 3~4 and 3~2 are nonedges, 2~4 is an edge.
    assert 4 not in nbr[3] and 2 not in nbr[3] and 4 in nbr[2]
    a=by_vertices()
    b=by_edges()
    assert a==b
    faces=a
    fvec=Counter(x.bit_count()-1 for x in faces)
    assert fvec==Counter({0:18,1:123,2:394,3:585,4:324}),fvec
    critical,pairs=pivot_matching(faces)
    assert len(pairs)==708
    assert Counter(x.bit_count()-1 for x in critical)==Counter({0:1,4:27})
    hasse=verify_acyclic(faces,pairs)
    ranks=[rank_mod2(faces,s) for s in (2,3,4,5)]
    assert ranks==[17,106,288,297],ranks
    chi=sum((-1)**k*v for k,v in fvec.items())
    assert chi==28
    # Matrix-forest identity is checked independently via the exact
    # determinant of I-L(G), using an integer fraction-free elimination.
    lap=[[0]*V for _ in range(V)]
    for u,v in EDGES:
        lap[u][u]+=1;lap[v][v]+=1
        lap[u][v]-=1;lap[v][u]-=1
    mat=[[int(i==j)-lap[i][j] for j in range(V)] for i in range(V)]
    previous=1
    sign=1
    for k in range(V-1):
        if mat[k][k]==0:
            pivot=next((i for i in range(k+1,V) if mat[i][k]),None)
            assert pivot is not None
            mat[k],mat[pivot]=mat[pivot],mat[k]
            sign=-sign
        p=mat[k][k]
        for i in range(k+1,V):
            for j in range(k+1,V):
                num=mat[i][j]*p-mat[i][k]*mat[k][j]
                assert num%previous==0
                mat[i][j]=num//previous
            mat[i][k]=0
        previous=p
    det=sign*mat[-1][-1]
    assert det==1-chi==-27
    print('THREE_SUN_MORSE_HOMOTOPY_VERIFIED')
    print('graph_edges=',EDGES)
    print('incidence_vertices=',len(INCIDENCES))
    print('face_vector=',tuple(fvec[k] for k in range(5)))
    print('nonempty_faces=',len(faces))
    print('independent_enumerations_equal=True')
    print('no_complete_source=True no_dominant_pair=True not_complete_multipartite=True')
    print('pivot_order=',ORDER)
    print('morse_pairs=',len(pairs))
    print('critical_cells=',dict(sorted(Counter(x.bit_count()-1 for x in critical).items())))
    print('oriented_hasse_arrows=',hasse,'acyclic=True')
    print('mod2_boundary_ranks=',ranks)
    print('euler_characteristic=',chi,'independent_matrix_forest_check=True')
    print('integral_homotopy_type=27 copies S4')

if __name__=='__main__':
    main()
