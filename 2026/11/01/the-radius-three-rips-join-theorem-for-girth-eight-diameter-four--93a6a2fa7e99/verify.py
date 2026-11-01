#!/usr/bin/env python3
"""Exact finite structural cross-checks for bipartite diameter-four Rips theorem.
The mathematical proof is uniform; these finite tests are not its substitute.
"""
from itertools import product, combinations
from collections import deque
from math import comb


def gf2rank(cols):
    basis = {}
    for x in cols:
        while x:
            k = x.bit_length()-1
            if k in basis: x ^= basis[k]
            else:
                basis[k]=x
                break
    return len(basis)


def wq(q):
    def norm(v):
        k=next(i for i,x in enumerate(v) if x%q)
        inv=pow(v[k],-1,q)
        return tuple(x*inv%q for x in v)
    P=sorted({norm(v) for v in product(range(q),repeat=4) if any(v)})
    I={v:i for i,v in enumerate(P)}
    def pairing(a,b):
        return (a[0]*b[2]-a[2]*b[0]+a[1]*b[3]-a[3]*b[1])%q
    lines=set()
    for i,j in combinations(range(len(P)),2):
        if pairing(P[i],P[j]): continue
        l=frozenset(I[norm(tuple((a*P[i][k]+b*P[j][k])%q for k in range(4)))]
                    for a,b in product(range(q),repeat=2) if a or b)
        assert len(l)==q+1
        lines.add(l)
    return len(P), [tuple(sorted(x)) for x in sorted(lines,key=lambda x: tuple(sorted(x)))]


def grid(a,b):
    # a by b grid points, with a row-lines and b column-lines.
    pts=a*b
    lines=[tuple(i*b+j for j in range(b)) for i in range(a)]
    lines += [tuple(i*b+j for i in range(a)) for j in range(b)]
    return pts,lines


def cycle(n):
    assert n%2==0 and n>=8
    # Bipartite incidence graph of cycle C_n: n/2 points and n/2 lines
    h=n//2
    return h,[tuple(sorted((j,(j+1)%h))) for j in range(h)]


def complexes_of_side(neighbors):
    # Return all faces in dimension k, including only those from neighborhood facets.
    faces={}
    for block in neighbors:
        for size in range(1,len(block)+1):
            faces.setdefault(size-1,set()).update(combinations(sorted(block),size))
    return [sorted(faces[k]) for k in sorted(faces)]


def check(label, Pn, lines, expected_b=None):
    L=len(lines); N=Pn+L
    adj=[set() for _ in range(N)]
    for j,line in enumerate(lines):
        for i in line:
            assert 0<=i<Pn
            adj[i].add(Pn+j);adj[Pn+j].add(i)
    E=sum(map(len,adj))//2
    distances=[]
    for src in range(N):
        d=[None]*N;d[src]=0;Q=deque([src])
        while Q:
            v=Q.popleft()
            for w in adj[v]:
                if d[w] is None: d[w]=d[v]+1;Q.append(w)
        assert None not in d
        distances.append(d)
    diameter=max(max(x) for x in distances)
    assert diameter==4,(label,diameter)
    # For both parts, the 2-distance graph has its maximal cliques
    # among the neighbor-set simplices. Verify all triangles have a common center.
    side_facets=[]
    for group,other in [(range(Pn),range(Pn,N)),(range(Pn,N),range(Pn))]:
        vertices=list(group)
        neigh=[set(adj[j]) for j in other]
        edge_to_centers={}
        for y in other:
            for u,v in combinations(sorted(adj[y]),2):
                edge_to_centers.setdefault((u,v),[]).append(y)
        assert all(len(c)==1 for c in edge_to_centers.values()),label+' C4'
        for u,v,w in combinations(vertices,3):
            if all(tuple(sorted(edge)) in edge_to_centers for edge in [(u,v),(u,w),(v,w)]):
                assert set(edge_to_centers[tuple(sorted((u,v)))]) & set(edge_to_centers[tuple(sorted((u,w)))]) & set(edge_to_centers[tuple(sorted((v,w)))]) ,label+' C6'
        facets=[tuple(sorted(x)) for x in neigh]
        side_facets.append(facets)
        # Distances 2 within each part = sharing a neighbor;
        # distances across parts are always odd and at most 3.
        for u,v in combinations(vertices,2):
            assert (distances[u][v]==2) == (tuple(sorted((u,v))) in edge_to_centers)
    for u in range(Pn):
        for v in range(Pn,N):assert distances[u][v] in (1,3)
    b=E-N+1
    if expected_b is not None: assert b==expected_b,(label,b,expected_b)
    # All clique faces of distance-two within the parts are represented by
    # neighborhood facets. Reconstruct the actual integral chain ranks mod 2.
    for side, facets in enumerate(side_facets):
        # relabel each side to 0..size-1 for readability
        start=0 if side==0 else Pn
        fs=complexes_of_side([[x-start for x in f] for f in facets])
        ranks=[0]*(len(fs)+1)
        for k in range(1,len(fs)):
            lower_index={f:i for i,f in enumerate(fs[k-1])}
            cols=[sum(1<<lower_index[face[:j]+face[j+1:]] for j in range(len(face)))
                  for face in fs[k]]
            ranks[k]=gf2rank(cols)
        betti=[len(fs[k])-ranks[k]-ranks[k+1] for k in range(len(fs))]
        assert betti==[1,b]+[0]*(len(fs)-2),(label,side,betti,b)
        print(label,'side',side,'f-vector',tuple(len(x) for x in fs),'GF2_Betti',betti)
    print(label,'vertices',N,'edges',E,'diameter',diameter,
          'first_betti',b,'predicted_H3_rank',b*b,
          'predicted_H0_bars',N-1,'predicted_H1_bars',b)
    return b

if __name__=='__main__':
    assert check('C8',*cycle(8),expected_b=1)==1
    assert check('grid_3x3',*grid(3,3),expected_b=4)==4
    assert check('W2',*wq(2),expected_b=16)==16
    assert check('W3',*wq(3),expected_b=81)==81
    print('GENERALIZED_QUADRANGLE_RIPS_STRUCTURAL_CHECKS_OK')
