#!/usr/bin/env python3
from itertools import product
from collections import Counter, deque


def det3(m):
    a,b,c,d,e,f,g,h,i = m
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def rank3(m):
    if all(x == 0 for x in m):
        return 0
    if det3(m) != 0:
        return 3
    M = [m[0:3], m[3:6], m[6:9]]
    for r1 in range(3):
        for r2 in range(r1+1,3):
            for c1 in range(3):
                for c2 in range(c1+1,3):
                    if M[r1][c1]*M[r2][c2] - M[r1][c2]*M[r2][c1] != 0:
                        return 2
    return 1


def build_model(p, q, missing=frozenset()):
    lower = tuple(f"a{i}" for i in range(p))
    upper = tuple(f"b{j}" for j in range(q))
    vertices = lower + upper
    edges = tuple((a,b) for i,a in enumerate(lower) for j,b in enumerate(upper) if (i,j) not in missing)
    return vertices, edges


def spanning_basis(vertices, edges):
    parent = {v:v for v in vertices}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x,y):
        rx,ry = find(x),find(y)
        if rx == ry:
            return False
        parent[ry] = rx
        return True

    tree, chords = [], []
    for e in edges:
        (tree if union(*e) else chords).append(e)
    assert len(tree) == len(vertices)-1
    assert len(chords) == len(edges)-len(vertices)+1 == 3

    edge_index = {e:k for k,e in enumerate(edges)}
    adj = {v:[] for v in vertices}
    for e in tree:
        u,v = e
        adj[u].append((v,e))
        adj[v].append((u,e))

    basis = []
    for chord in chords:
        u,v = chord
        # Fundamental cycle: chord u->v, then unique tree path v->u.
        prev = {v:(None,None)}
        Q = deque([v])
        while Q:
            x = Q.popleft()
            if x == u:
                break
            for y,e in adj[x]:
                if y not in prev:
                    prev[y] = (x,e)
                    Q.append(y)
        path = []
        cur = u
        while cur != v:
            px,e = prev[cur]
            path.append((px,cur,e))
            cur = px
        path.reverse()

        vec = [0]*len(edges)
        vec[edge_index[chord]] = 1
        for x,y,e in path:
            eu,ev = e
            vec[edge_index[e]] += 1 if (x,y)==(eu,ev) else -1
        basis.append(tuple(vec))

    # basis is list of 3 E-vectors. Each chord is the identity coordinate selector.
    for j,ch in enumerate(chords):
        ci=edge_index[ch]
        for k,z in enumerate(basis):
            assert z[ci] == (1 if j==k else 0)

    # boundary check
    vidx={v:i for i,v in enumerate(vertices)}
    for z in basis:
        bd=[0]*len(vertices)
        for coeff,(u,v) in zip(z,edges):
            bd[vidx[u]] -= coeff
            bd[vidx[v]] += coeff
        assert all(x==0 for x in bd)
    return tuple(tree), tuple(chords), tuple(basis)


def enumerate_model(p,q,missing=frozenset()):
    vertices, edges = build_model(p,q,missing)
    edge_set=set(edges)
    edge_index={e:i for i,e in enumerate(edges)}
    tree,chords,basis=spanning_basis(vertices,edges)
    chord_indices=[edge_index[e] for e in chords]

    matrices=Counter()
    map_rank=Counter()
    homeomorphisms=0
    homology_isomorphisms=0
    total=0

    def is_monotone(vals):
        f=dict(zip(vertices,vals))
        for u,v in edges:
            fu,fv=f[u],f[v]
            if fu != fv and (fu,fv) not in edge_set:
                return False
        return True

    for vals in product(vertices, repeat=len(vertices)):
        if not is_monotone(vals):
            continue
        total += 1
        f=dict(zip(vertices,vals))
        cols=[]
        for z in basis:
            img=[0]*len(edges)
            for coeff,(u,v) in zip(z,edges):
                if coeff == 0:
                    continue
                fu,fv=f[u],f[v]
                if fu == fv:
                    continue
                assert (fu,fv) in edge_set
                img[edge_index[(fu,fv)]] += coeff
            coords=tuple(img[i] for i in chord_indices)
            # Reconstruct from the basis and check exact equality.
            rec=[0]*len(edges)
            for c,bz in zip(coords,basis):
                for i,x in enumerate(bz):
                    rec[i] += c*x
            assert tuple(rec) == tuple(img)
            cols.append(coords)

        # Flatten row-major from columns.
        m=(cols[0][0],cols[1][0],cols[2][0],
           cols[0][1],cols[1][1],cols[2][1],
           cols[0][2],cols[1][2],cols[2][2])
        matrices[m] += 1
        r=rank3(m)
        map_rank[r] += 1
        if abs(det3(m)) == 1:
            homology_isomorphisms += 1

        # A finite-poset homeomorphism is exactly a bijection whose inverse is monotone.
        if len(set(vals)) == len(vertices):
            inv={vals[i]:vertices[i] for i in range(len(vertices))}
            inverse_ok=True
            for u,v in edges:
                iu,iv=inv[u],inv[v]
                if iu != iv and (iu,iv) not in edge_set:
                    inverse_ok=False
                    break
            if inverse_ok:
                homeomorphisms += 1
                assert abs(det3(m)) == 1

    distinct_rank=Counter(rank3(m) for m in matrices)
    # Every integral H1-isomorphism found must be a homeomorphism.
    assert homology_isomorphisms == homeomorphisms
    return {
        "total":total,
        "distinct":len(matrices),
        "map_rank":dict(sorted(map_rank.items())),
        "distinct_rank":dict(sorted(distinct_rank.items())),
        "homeomorphisms":homeomorphisms,
        "homology_isomorphisms":homology_isomorphisms,
        "tree":tree,
        "chords":chords,
    }


B24=enumerate_model(2,4)
B42=enumerate_model(4,2)
D=enumerate_model(3,3,frozenset({(2,2)}))

assert B24["total"] == 1782
assert B24["distinct"] == 421
assert B24["map_rank"] == {0:1278,1:168,2:288,3:48}
assert B24["distinct_rank"] == {0:1,1:84,2:288,3:48}
assert B24["homeomorphisms"] == B24["homology_isomorphisms"] == 48

assert B42["total"] == 1782
assert B42["distinct"] == 421
assert B42["map_rank"] == B24["map_rank"]
assert B42["distinct_rank"] == B24["distinct_rank"]
assert B42["homeomorphisms"] == B42["homology_isomorphisms"] == 48

assert D["total"] == 646
assert D["distinct"] == 113
assert D["map_rank"] == {0:362,1:232,2:48,3:4}
assert D["distinct_rank"] == {0:1,1:60,2:48,3:4}
assert D["homeomorphisms"] == D["homology_isomorphisms"] == 4

print("VERIFY_OK")
print("K2,4_self_maps=1782")
print("K2,4_distinct_H1_actions=421")
print("K2,4_distinct_rank_profile=1,84,288,48")
print("K2,4_H1_isomorphism_maps=48=homeomorphisms")
print("K4,2_opposite_same_counts=yes")
print("K3,3_minus_edge_self_maps=646")
print("K3,3_minus_edge_distinct_H1_actions=113")
print("K3,3_minus_edge_distinct_rank_profile=1,60,48,4")
print("K3,3_minus_edge_H1_isomorphism_maps=4=homeomorphisms")
print("direct_H1_action_count_depends_on_minimal_model=yes")
