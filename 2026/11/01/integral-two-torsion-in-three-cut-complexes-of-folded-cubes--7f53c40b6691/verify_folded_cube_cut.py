#!/usr/bin/env python3
"""Independent finite checks for three-cut complexes of folded cubes.

The proof for all dimensions uses cubical covering spaces and Alexander duality.
The calculations here exhaustively test the face/collapse models in dimensions 5, 6.
Only Python's standard library is required.
"""

from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
from math import comb, gcd


def graph(d):
    n = 1 << (d - 1)
    steps = [1 << i for i in range(d - 1)] + [n - 1]
    assert len(set(steps)) == d
    neighbors = [set(v ^ s for s in steps) for v in range(n)]
    assert all(len(x) == d for x in neighbors)
    return neighbors


def is_connected_triple(s, adj):
    a, b, c = s
    return ((b in adj[a]) + (c in adj[a]) + (c in adj[b])) >= 2


def squares(adj):
    n = len(adj)
    found = set()
    for a in range(n):
        for b, d in combinations(sorted(adj[a]), 2):
            for c in adj[b] & adj[d]:
                if c == a or c in adj[a]:
                    continue
                found.add(tuple(sorted((a, b, c, d))))
    return sorted(found)


def dual_faces(adj):
    n = len(adj)
    faces = set((v,) for v in range(n))
    faces.update(combinations(range(n), 2))
    for t in combinations(range(n), 3):
        if is_connected_triple(t, adj):
            faces.add(t)
    for quad in combinations(range(n), 4):
        if all(is_connected_triple(t, adj) for t in combinations(quad, 3)):
            faces.add(quad)
    return faces


def local_collapse(d):
    adj = graph(d)
    n = len(adj)
    assert all(x in adj[y] for x in range(n) for y in adj[x])
    assert all(not (adj[a] & adj[b]) for a in range(n) for b in adj[a])
    assert all(len(adj[a] & adj[b]) in (0, 2)
               for a in range(n) for b in range(a + 1, n) if b not in adj[a])
    if d == 5:
        assert all(len(adj[a] & adj[b]) == 2
                   for a in range(n) for b in range(a + 1, n) if b not in adj[a])
    sq = squares(adj)
    q = n * comb(d, 2) // 4
    assert len(sq) == q
    faces = dual_faces(adj)
    expected_initial = Counter({1:n, 2:comb(n, 2), 3:n * comb(d, 2), 4:q})
    assert Counter(map(len, faces)) == expected_initial
    retained = set(faces)
    pairs = []

    def upper_cofaces(f):
        return {x for x in retained if len(x) == len(f) + 1 and set(f).issubset(x)}

    for square in sq:
        a = square[0]
        b, d_ = sorted(x for x in square if x in adj[a])
        c = next(x for x in square if x not in (a, b, d_))
        assert b in adj[c] and d_ in adj[c] and c not in adj[a]
        tri1 = tuple(sorted((a,b,c)))
        tet = square
        assert upper_cofaces(tri1) == {tet}
        retained.remove(tri1)
        retained.remove(tet)
        pairs.append((tri1,tet))
        diagonal = tuple(sorted((a,c)))
        tri2 = tuple(sorted((a,c,d_)))
        assert upper_cofaces(diagonal) == {tri2}
        assert not any(len(x) >= 4 and set(diagonal).issubset(x) for x in retained)
        retained.remove(diagonal)
        retained.remove(tri2)
        pairs.append((diagonal,tri2))
    # Every removed pair is an elementary simplicial collapse.
    # Two residual triangles triangulate each square using its other diagonal.
    long_edges = {e for e in retained if len(e) == 2 and e[1] not in adj[e[0]]
                  and len(adj[e[0]] & adj[e[1]]) == 0}
    L = n * (n - 1 - d - comb(d, 2)) // 2
    assert len(long_edges) == L
    assert Counter(map(len,retained)) == Counter({1:n,2:n*d//2+q+L,3:2*q})
    return adj, sq, faces, retained, pairs, L


def mod_rank(columns, p):
    piv = {}
    for col in columns:
        w = dict(col)
        while w:
            k = min(w)
            if k not in piv:
                inv = pow(w[k], -1, p)
                piv[k] = {j: (c * inv) % p for j,c in w.items() if c * inv % p}
                break
            multiple = w[k]
            for j,c in piv[k].items():
                z = (w.get(j,0) - multiple*c) % p
                if z:
                    w[j] = z
                else:
                    w.pop(j,None)
    return len(piv)


def square_complex_ranks(adj, sq, p):
    edges = sorted((a,b) for a in range(len(adj)) for b in adj[a] if a < b)
    index = {e:i for i,e in enumerate(edges)}
    columns = []
    for s in sq:
        a = s[0]
        b, d_ = sorted(x for x in s if x in adj[a])
        c = next(x for x in s if x not in (a,b,d_))
        ring = (a,b,c,d_,a)
        col = defaultdict(int)
        for x,y in zip(ring,ring[1:]):
            key = (min(x,y),max(x,y))
            col[index[key]] = (col[index[key]] + (1 if x<y else -1)) % p
        columns.append({k:v for k,v in col.items() if v})
    return mod_rank(columns,p)


def clebsch_morse(adj, faces):
    # An explicit element-matching order on the 16-vertex Alexander dual.
    order = (13,14,2,3,15,9,8,12,1,6,10,4,11,7,0,5)
    remaining = set(faces)
    pairs = []
    for v in order:
        for f in sorted(faces,key=lambda t:(len(t),t)):
            if v in f: continue
            upper = tuple(sorted(f+(v,)))
            if f in remaining and upper in remaining:
                remaining.remove(f)
                remaining.remove(upper)
                pairs.append((f,upper))
    critical = {k:sorted(f for f in remaining if len(f)==k+1) for k in range(4)}
    assert [len(critical[k]) for k in range(4)] == [1,1,16,0]
    matched = set(pairs)
    indeg = {f:0 for f in faces}
    arrows = defaultdict(list)
    inc = 0
    for big in faces:
        for i in range(len(big)):
            small = big[:i]+big[i+1:]
            if not small: continue
            src,dst = (small,big) if (small,big) in matched else (big,small)
            arrows[src].append(dst)
            indeg[dst]+=1
            inc+=1
    todo = deque(f for f in faces if indeg[f]==0)
    visited=0
    while todo:
        f=todo.popleft();visited+=1
        for nxt in arrows[f]:
            indeg[nxt]-=1
            if indeg[nxt]==0:todo.append(nxt)
    assert visited == len(faces), 'Morse matching contains a gradient cycle'
    matched_edge_to_triangle={f:g for f,g in pairs if len(f)==2}

    @lru_cache(None)
    def reduce_edge(edge):
        if edge not in matched_edge_to_triangle:
            return {edge:1}
        triangle = matched_edge_to_triangle[edge]
        pivot = next(i for i in range(3) if triangle[:i]+triangle[i+1:] == edge)
        out = defaultdict(int)
        for i in range(3):
            subedge=triangle[:i]+triangle[i+1:]
            if subedge == edge: continue
            for other, coefficient in reduce_edge(subedge).items():
                out[other] -= (-1)**(pivot+i)*coefficient
        return {e:v for e,v in out.items() if v}

    only_edge = critical[1][0]
    degrees=[]
    for triangle in critical[2]:
        coeff = defaultdict(int)
        for i in range(3):
            for edge,number in reduce_edge(triangle[:i]+triangle[i+1:]).items():
                coeff[edge] += (-1)**i*number
        degrees.append(coeff[only_edge])
    assert gcd(*degrees) == 2 and max(map(abs,degrees)) == 2
    return critical, degrees, inc


def direct_dual_check_d5(adj, faces):
    # Compare every subset with the complement-of-disconnected-triples
    # definition of the ordinary three-cut complex.
    n = len(adj)
    assert n == 16
    good = {sum(1 << i for i in f) for f in faces} | {0}
    bad = [sum(1 << i for i in t) for t in combinations(range(n),3)
           if not is_connected_triple(t,adj)]
    assert len(bad) == 400
    count = 0
    for mask in range(1 << n):
        in_dual = all((mask & b) != b for b in bad)
        assert in_dual == (mask in good)
        count += in_dual
    assert count == 337
    return len(bad), count


def main():
    for d in (5,6):
        adj,sq,faces,left,pairs,L=local_collapse(d)
        n = len(adj)
        ranks={p:square_complex_ranks(adj,sq,p) for p in (2,3,5)}
        edge_count = n*d//2
        assert ranks[2] == edge_count-n
        assert ranks[3] == ranks[5] == edge_count-n+1
        beta=2**(d-4)*(d*d-5*d+8)-1
        assert len(sq)-ranks[3] == beta
        assert len(sq)-ranks[2] == beta+1
        print(f'd={d}: N={n}, squares={len(sq)}, dual_faces={len(faces)}, '
              f'elementary_collapse_pairs={len(pairs)}, long_edges={L}, '
              f'square_boundary_ranks_mod_2_3_5={ranks[2]},{ranks[3]},{ranks[5]}, '
              f'beta={beta}')
        if d==5:
            bad, good = direct_dual_check_d5(adj,faces)
            print(f'd=5 direct_complement_check: disconnected_triples={bad}, dual_faces_with_empty={good}')
            crit,degrees,inc = clebsch_morse(adj,faces)
            assert inc == 880
            print('d=5 Morse critical counts:', [len(crit[k]) for k in range(4)])
            print('d=5 Morse attaching degrees:', degrees)
    print('FOLDED_CUBE_THREE_CUT_TORSION_CHECKS_OK')

if __name__=='__main__':
    main()
