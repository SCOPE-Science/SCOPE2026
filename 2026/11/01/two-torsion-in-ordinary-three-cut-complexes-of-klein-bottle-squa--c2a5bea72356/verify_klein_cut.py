"""Independent finite tests for ordinary three-cut complexes of Klein square grids.
Run with Python 3 and SymPy installed. The all-parameter proof is in RESULT.md.
"""
from itertools import combinations
from math import comb
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def model(m, n):
    assert m >= 5 and n >= 5
    # Equivalence (x + m,y) ~ (x,-1-y), (x,y+n) ~ (x,y).
    def v(x, y):
        q, r = divmod(x, m)
        return r * n + ((-1-y if q % 2 else y) % n)
    vertices = list(range(m*n))
    edges = set()
    squares = []
    for i in range(m):
        for j in range(n):
            a,b,c,d = [v(x,y) for x,y in ((i,j),(i+1,j),(i+1,j+1),(i,j+1))]
            assert len({a,b,c,d}) == 4
            squares.append((a,b,c,d))
            for u,w in ((a,b),(a,d)):
                edges.add(tuple(sorted((u,w))))
    assert len(edges) == 2*m*n
    adj=[set() for _ in vertices]
    for u,w in edges:
        adj[u].add(w)
        adj[w].add(u)
    assert all(len(a)==4 for a in adj)
    return vertices,edges,squares,adj


def signed_surface_snf(V, edges, squares):
    elist=sorted(edges)
    # Spanning tree: use a graph-based queue so the graph geometry is not assumed.
    adj=[set() for _ in range(V)]
    for u,v in elist:
        adj[u].add(v);adj[v].add(u)
    seen={0};front=[0]; tree=set()
    for u in front:
        for v in sorted(adj[u]):
            if v not in seen:
                seen.add(v);front.append(v);tree.add(tuple(sorted((u,v))))
    assert len(seen)==V and len(tree)==V-1
    non_tree=[e for e in elist if e not in tree]
    assert len(non_tree)==len(edges)-V+1
    rows={e:i for i,e in enumerate(non_tree)}
    A=[[0]*len(squares) for _ in non_tree]
    for j,square in enumerate(squares):
        seq=(*square,square[0])
        for a,b in zip(seq,seq[1:]):
            e=tuple(sorted((a,b)))
            if e in rows: A[rows[e]][j] += 1 if a < b else -1
    S=smith_normal_form(Matrix(A),domain=ZZ)
    diag=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]!=0]
    return (len(non_tree),diag)


def check(m,n):
    vs,edges,squares,adj=model(m,n)
    N=len(vs); e3=[]
    for v in vs:
        for a,b in combinations(sorted(adj[v]),2):
            e3.append(tuple(sorted((a,v,b))))
    assert len(set(e3))==6*N
    sqsets={frozenset(s) for s in squares}
    assert len(sqsets)==N
    # Full enumeration of all 4-subsets that are dual simplices: test every triple.
    triple_set=set(e3)
    valid4={frozenset(t) for t in combinations(vs,4) if all(tuple(sorted(u)) in triple_set for u in combinations(t,3))}
    assert valid4==sqsets, (len(valid4),len(sqsets))
    # Among 2-step pairs, exactly N square diagonals per class and 2N straight pairs.
    dist2={tuple(sorted((a,b))) for v in vs for a,b in combinations(adj[v],2)}
    assert len(dist2)==4*N
    straight=[];corners=[]
    for e in sorted(dist2):
        common=adj[e[0]]&adj[e[1]]
        assert len(common) in (1,2)
        (straight if len(common)==1 else corners).append(e)
    assert len(straight)==2*N and len(corners)==2*N
    # Each square's two diagonal edges are exactly the two common-neighbor pairs.
    diag_coverage={}
    for s in squares:
        for e in (tuple(sorted((s[0],s[2]))),tuple(sorted((s[1],s[3])))):
            diag_coverage[e]=diag_coverage.get(e,0)+1
    assert set(diag_coverage)==set(corners) and all(k==1 for k in diag_coverage.values())
    # Reconstruct the full Alexander dual independently and replay all free-face
    # collapses. Each lower face must lie in exactly its specified upper face.
    F={frozenset((v,)) for v in vs}
    F.update(frozenset(e) for e in combinations(vs,2))
    F.update(frozenset(t) for t in triple_set)
    F.update(valid4)
    original_counts=[sum(len(f)==k for f in F) for k in range(1,5)]
    assert original_counts==[N,comb(N,2),6*N,N]
    def collapse(lower,upper):
        L,U=frozenset(lower),frozenset(upper)
        assert L in F and U in F and len(U)==len(L)+1 and L<U
        assert sum(L < a for a in F)==1,(m,n,L,U)
        F.remove(L);F.remove(U)
    for a,b,c,d in squares:
        collapse((a,b,c),(a,b,c,d))
    for a,b,c,d in squares:
        collapse((a,c),(a,c,d))
    for a,c in straight:
        v,=adj[a]&adj[c]
        collapse((a,c),(a,v,c))
    assert sum(len(f)==4 for f in F)==0
    target={frozenset((v,)) for v in vs}
    target.update(frozenset(e) for e in edges)
    for a,b,c,d in squares:
        target.add(frozenset((b,d)))
        target.update((frozenset((a,b,d)),frozenset((b,c,d))))
    long_pairs={frozenset(p) for p in combinations(vs,2)
                if tuple(p) not in edges and tuple(p) not in dist2}
    target.update(long_pairs)
    assert F==target,(len(F),len(target),len(F^target))
    # Smith normal form of the cellular square surface after contracting a spanning tree.
    cycle_rank,smith=signed_surface_snf(N,edges,squares)
    assert cycle_rank==N+1
    assert smith.count(2)==1 and smith.count(1)==N-1 and len(smith)==N, (m,n,smith)
    h=comb(N,2)-6*N
    assert h>=0
    # Record the cut-complex ranks inferred from the checked integral Smith factors.
    # Cellular H1(K;F2) has dimension 2, over any odd prime dimension 1.
    print(f"({m},{n}): V={N}, E={len(edges)}, 3faces={len(triple_set)}, 4faces={len(valid4)}, long_edges={h}, ")
    print(f"  elementary free pairs={4*N}; survivor faces={[sum(len(f)==k for f in F) for k in range(1,4)]}")
    print(f"  surface SNF=1^{smith.count(1)}*2^{smith.count(2)}; H1(Klein)=Z + Z/2;")
    print(f"  predicted Delta3: H_{{{N-5}}}=Z/2; H_{{{N-4}}}=Z^{h+1}; OK")

if __name__=='__main__':
    for mm,nn in ((5,5),(5,6),(6,6)):
        check(mm,nn)
    print('KLEIN_ORDINARY_THREE_CUT_INTEGRAL_DUAL_CHECKS_OK')
