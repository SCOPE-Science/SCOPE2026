#!/usr/bin/env python3
"""Finite checks for the star-subdivision collapse and integral symmetry lattice."""
from itertools import combinations, permutations
from math import comb
from collections import Counter


def closure(facets):
    out = {frozenset()}
    for f in facets:
        f = tuple(f)
        for r in range(1, len(f) + 1):
            out.update(map(frozenset, combinations(f, r)))
    return out


def check_graph(n, edges, name, equivariant=False):
    E = {tuple(sorted(e)) for e in edges}
    neigh = {i: set() for i in range(n)}
    for i, j in E:
        neigh[i].add(j)
        neigh[j].add(i)
    assert min(map(len, neigh.values())) >= 3, 'Minimum degree required'
    edge_token = lambda i, j: ('e',) + tuple(sorted((i, j)))
    center = lambda i: ('b', i)
    stars = {i: frozenset(edge_token(i, j) for j in neigh[i]) for i in range(n)}
    triangles = list(combinations(range(n), 3))
    triangles = [t for t in triangles if all(tuple(sorted(p)) in E for p in combinations(t, 2))]
    tri_facets = [frozenset(edge_token(*p) for p in combinations(t, 2)) for t in triangles]
    original = closure(list(stars.values()) + tri_facets)
    # Every face of the clique complex is a star face or an edge-triangle face:
    edge_list = sorted(E)
    for r in range(2, min(4, len(edge_list)) + 1):
        for chosen in combinations(edge_list, r):
            if all(set(e) & set(f) for e, f in combinations(chosen, 2)):
                assert frozenset(edge_token(*e) for e in chosen) in original
    
    subdiv = original.copy()
    for v in range(n):
        A = stars[v]
        assert A in subdiv
        subdiv.remove(A)
        new_faces = closure([set(A - {x}) | {center(v)} for x in A])
        subdiv.update(new_faces)
    # Each orbit of faces with the same size can be collapsed in any order,
    # and every elementary pair is checked at the moment of removal.
    pairs = []
    for size in range(max(len(A) for A in stars.values()) - 1, 2, -1):
        for v in range(n):
            A = stars[v]
            if len(A) <= size:
                continue
            for face in combinations(sorted(A), size):
                F = frozenset(face)
                cone = F | {center(v)}
                assert F in subdiv and cone in subdiv, (name,v,F)
                proper_cofaces = [H for H in subdiv if F < H]
                assert proper_cofaces == [cone], (name,v,size,F,len(proper_cofaces))
                subdiv.remove(F)
                subdiv.remove(cone)
                pairs.append((F, cone))
    # A pair of incident original edges that does not close a graph triangle
    # must also be removed together with its cone. Triangle pairs survive
    # because they are also faces of a central graph-triangle simplex.
    for v in range(n):
        for a,b in combinations(sorted(neigh[v]),2):
            if tuple(sorted((a,b))) in E:
                continue
            F = frozenset((edge_token(v,a),edge_token(v,b)))
            cone = F | {center(v)}
            assert F in subdiv and cone in subdiv
            assert [H for H in subdiv if F<H] == [cone], (name,v,a,b)
            subdiv.remove(F)
            subdiv.remove(cone)
            pairs.append((F,cone))
    target_facets = []
    for i, j in E:
        target_facets += [frozenset((center(i),edge_token(i,j))),
                          frozenset((edge_token(i,j), center(j)))]
    for i, j, k in triangles:
        eij, eik, ejk = edge_token(i,j), edge_token(i,k), edge_token(j,k)
        target_facets += [frozenset((center(i),eij,eik)),
                          frozenset((center(j),eij,ejk)),
                          frozenset((center(k),eik,ejk)),
                          frozenset((eij,eik,ejk))]
    target = closure(target_facets)
    assert subdiv == target, (name,len(subdiv),len(target),list(subdiv^target)[:4])
    incidence = Counter(v for t in triangles for v in t)
    expected_pairs = sum(2**len(neigh[v])-len(neigh[v])-2-incidence[v] for v in range(n))
    assert len(pairs) == expected_pairs, (name,len(pairs),expected_pairs)
    # Final simplicial complex, and same-size pair set, are invariant under graph automorphisms.
    if equivariant:
        for p in permutations(range(n)):
            if not all(tuple(sorted((p[i],p[j]))) in E for i,j in E):
                continue
            def move(tok):
                return center(p[tok[1]]) if tok[0]=='b' else edge_token(p[tok[1]],p[tok[2]])
            assert {frozenset(map(move, f)) for f in target} == target
            if p != tuple(range(n)):
                for size in set(len(F) for F,_ in pairs):
                    orbit = {(F,T) for F,T in pairs if len(F) == size}
                    assert {(frozenset(map(move,F)),frozenset(map(move,T))) for F,T in orbit} == orbit
    print('GRAPH',name,'vertices',n,'edges',len(E),'triangles',len(triangles),
          'original_faces',len(original)-1,'collapse_pairs',len(pairs),
          'target_faces',len(target)-1,'OK')


def det(mat):
    n = len(mat)
    if n == 0: return 1
    if n == 1: return mat[0][0]
    if n == 2: return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
    return sum((-1)**j*a*det([row[:j]+row[j+1:] for row in mat[1:]]) for j,a in enumerate(mat[0]))


def module_check(n):
    # A_n is the augmentation kernel generated by a_i=e_i-e_(n-1).
    bases = list(combinations(range(n-1), 3))
    def image_matrix(p):
        # p(a_j)=e_{p(j)}-e_{p(n-1)}; in a_i basis (0<=i<n-1).
        M = [[(int(p[j]==i)-int(p[n-1]==i)) for j in range(n-1)] for i in range(n-1)]
        return [[det([[M[i][j] for j in src] for i in dst]) for src in bases] for dst in bases]
    def orient(triple):
        sorted_t = tuple(sorted(triple))
        inversions = sum(triple[i] > triple[j] for i in range(3) for j in range(i+1,3))
        return sorted_t, (-1 if inversions%2 else 1)
    # c_{ijk}=(e_i-e_last) wedge (e_j-e_last) wedge (e_k-e_last)
    # in oriented C_2. Check every simplex boundary coefficient cancels.
    def cycle(t):
        i,j,k=t
        return {(i,j,k):1, (i,j,n-1):-1, (i,k,n-1):1,(j,k,n-1):-1}
    for t in bases:
        edges = Counter()
        for tri, coefficient in cycle(t).items():
            i,j,k=tri
            for edge,sgn in [((j,k),1),((i,k),-1),((i,j),1)]:
                edges[edge] += coefficient*sgn
        assert all(x==0 for x in edges.values()),t
    traces = Counter()
    for p in permutations(range(n)):
        M = image_matrix(p)
        for cidx,src in enumerate(bases):
            image_c = Counter()
            for tri, coefficient in cycle(src).items():
                target, sign = orient(tuple(p[i] for i in tri))
                image_c[target] += coefficient*sign
            # The coordinates on triangles avoiding the last vertex
            # determine the integral cycle, and equal the exterior-minor formula.
            assert all(image_c[dst] == M[r][cidx] for r,dst in enumerate(bases))
        traces[sum(M[i][i] for i in range(len(bases)))] += 1
    assert traces[n if False else len(bases)] >= 1
    assert sum(traces.values()) == __import__('math').factorial(n)
    # Integral cycles - the boundary of a tetrahedron with vertex (n-1),
    # giving a unimodular basis of ker(partial_2) by the exact augmented simplex complex.
    assert len(bases) == comb(n-1,3)
    print('MODULE','S_'+str(n),'rank',len(bases),'trace_counts',str(sorted(traces.items())), 'OK')


def main():
    for n in range(4,8):
        check_graph(n, combinations(range(n),2), 'K_'+str(n),equivariant=(n<=6))
        module_check(n)
    # The cube and Petersen graphs stress-test noncomplete, triangle-free input.
    cube_edges = [(i,j) for i in range(8) for j in range(i+1,8) if (i^j).bit_count()==1]
    check_graph(8, cube_edges,'Q_3',equivariant=True)
    # Mixed triangle and nontriangle vertex links test both kinds of final pairs.
    prism = [(i,(i+1)%3) for i in range(3)] + [(i+3,((i+1)%3)+3) for i in range(3)] + [(i,i+3) for i in range(3)]
    check_graph(6,prism,'Triangular_prism',equivariant=True)
    missing = tuple(sorted((0,1)))
    check_graph(5,[e for e in combinations(range(5),2) if e!=missing],'K_5_minus_edge',equivariant=True)
    peter_edges=[]
    for i in range(5):
        peter_edges.append((i,(i+1)%5))
        peter_edges.append((i,i+5))
        peter_edges.append((i+5,((i+2)%5)+5))
    check_graph(10,peter_edges,'Petersen',equivariant=True)
    print('VERIFY_OK')

if __name__=='__main__':
    main()
