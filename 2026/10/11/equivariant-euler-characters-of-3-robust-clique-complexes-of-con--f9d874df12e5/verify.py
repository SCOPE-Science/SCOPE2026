#!/usr/bin/env python3
"""Finite checks for a rational equivariant Euler-character identity.

Builds the simplices independently from their defining independence condition;
counts signed setwise-fixed faces and compares them with cycle-space traces.
Finite checks do not replace the all-graph proof.
"""
from itertools import combinations, permutations, product
from math import factorial


def edges_from_mask(a, b, mask):
    return frozenset(frozenset((i, a + j)) for i in range(a) for j in range(b)
                     if mask & (1 << (i * b + j)))


def connected(n, edges):
    adj = [set() for _ in range(n)]
    for e in edges:
        u, v = tuple(e); adj[u].add(v); adj[v].add(u)
    seen = {0}; todo = [0]
    for u in todo:
        for v in adj[u] - seen:
            seen.add(v); todo.append(v)
    return len(seen) == n


def perm_sign(seq):
    return -1 if sum(x > y for i, x in enumerate(seq)
                     for y in seq[i+1:]) % 2 else 1


def complex_faces(n, edges):
    out = []
    for k in range(1, min(4, n)+1):
        for s in combinations(range(n), k):
            if k < 3:
                out.append(s)
            elif k == 3:
                if any(frozenset(e) in edges for e in combinations(s, 2)):
                    out.append(s)
            elif any(frozenset(e1) in edges and frozenset(e2) in edges
                     for e1 in combinations(s, 2)
                     for e2 in combinations(s, 2)
                     if set(e1).isdisjoint(e2)):
                out.append(s)
    return out


def squares(n, edges):
    return [s for s in combinations(range(n), 4)
            if sum(frozenset(e) in edges for e in combinations(s, 2)) == 4
            and all(sum(frozenset((v, w)) in edges for w in s if w != v) == 2
                    for v in s)]


def automorphisms(a, b, edges):
    n = a+b
    E = edges
    allp = list(permutations(range(a)))
    allq = list(permutations(range(a, n)))
    for lp, rp in product(allp, allq):
        p = lp + rp
        if all(frozenset((p[u], p[v])) in E for u, v in map(tuple, E)):
            yield p
    if a == b:
        for lp, rp in product(permutations(range(a, n)), permutations(range(a))):
            p = lp + rp
            if all(frozenset((p[u], p[v])) in E for u, v in map(tuple, E)):
                yield p


def signed_edge_trace(n, edges, p):
    ret = 0
    for e in edges:
        x, y = sorted(e)
        if {p[x], p[y]} == {x, y}:
            ret += 1 if (p[x], p[y]) == (x, y) else -1
    return ret


def identity_for_graph(n, edges, ps, faces=None, sq=None):
    if faces is None: faces = complex_faces(n, edges)
    if sq is None: sq = squares(n, edges)
    for p in ps:
        tr = [0] * 4
        for s in faces:
            moved = tuple(p[x] for x in s)
            if set(s) == set(moved):
                tr[len(s)-1] += perm_sign(moved)
        lhs = tr[0] - tr[1] + tr[2] - tr[3] - 1
        p2 = tuple(p[p[i]] for i in range(n))
        h1 = signed_edge_trace(n, edges, p) - sum(p[i] == i for i in range(n)) + 1
        h12 = signed_edge_trace(n, edges, p2) - sum(p2[i] == i for i in range(n)) + 1
        assert (h1*h1+h12) % 2 == 0
        cyc = sum(set(s) == {p[i] for i in s} for s in sq)
        rhs = cyc - (h1*h1+h12)//2
        if lhs != rhs:
            raise AssertionError((n, sorted(map(sorted,edges)), p, lhs, rhs, tr, h1, h12, cyc))
        yield 1


def grids(m,n):
    vertices=[(i,j) for i in range(m) for j in range(n)]
    mp={v:k for k,v in enumerate(vertices)}
    E=frozenset(frozenset((mp[(i,j)],mp[(x,y)]))
                for i,j in vertices for x,y in vertices if abs(i-x)+abs(j-y)==1)
    return len(vertices), E


def cube():
    verts=list(product((0,1),repeat=3))
    ix={v:i for i,v in enumerate(verts)}
    E=frozenset(frozenset((ix[x],ix[y])) for x in verts for y in verts
                if sum(a!=b for a,b in zip(x,y))==1)
    ps=[]
    for perm in permutations(range(3)):
        for flips in product((0,1),repeat=3):
            ps.append(tuple(ix[tuple(v[perm[j]]^flips[j] for j in range(3))] for v in verts))
    return len(verts),E,ps


def main():
    graphs = tests = 0
    for a in range(1,4):
        for b in range(a,4):
            for mask in range(1, 1<<(a*b)):
                E=edges_from_mask(a,b,mask)
                if not connected(a+b,E): continue
                graphs += 1
                tests += sum(identity_for_graph(a+b,E,automorphisms(a,b,E)))
    extras = []
    for m,n in ((2,5),(3,4),(4,4)):
        N,E=grids(m,n)
        vertices=[(i,j) for i in range(m) for j in range(n)]
        ix={v:i for i,v in enumerate(vertices)}
        fs=[lambda i,j:(i,j), lambda i,j:(m-1-i,j),
            lambda i,j:(i,n-1-j), lambda i,j:(m-1-i,n-1-j)]
        if m==n:
            fs.extend([lambda i,j:(j,i),lambda i,j:(n-1-j,n-1-i),
                       lambda i,j:(j,n-1-i),lambda i,j:(n-1-j,i)])
        ps=[tuple(ix[f(*v)] for v in vertices) for f in fs]
        tests += sum(identity_for_graph(N,E,ps)); extras.append(f'grid_{m}x{n}')
    N,E,ps=cube()
    tests += sum(identity_for_graph(N,E,ps)); extras.append('cube_all_48')
    print(f'VERIFY_OK connected_bipartite_graphs={graphs} automorphism_character_comparisons={tests} special_cases={",".join(extras)}')

if __name__=='__main__': main()
