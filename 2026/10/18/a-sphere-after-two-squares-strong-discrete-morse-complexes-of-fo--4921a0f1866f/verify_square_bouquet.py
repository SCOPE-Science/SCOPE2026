"""Reproduce the one-point square-cycle strong-matching decomposition.
Run: python3 verify_square_bouquet.py
Requires only Python 3 standard library. This is a separate finite check,
not a substitute for the all-parameter proof.
"""
from itertools import permutations
from collections import Counter


def downset(facets):
    result = {0}
    for facet in facets:
        mask = facet
        while mask:
            result.add(mask)
            mask = (mask - 1) & facet
    return result


def graph(p):
    n = 1 + 3*p
    neighbors = [set() for _ in range(n)]
    for i in range(p):
        a, b, c = 1+3*i, 2+3*i, 3+3*i
        for u, v in ((0,a),(a,b),(b,c),(c,0)):
            neighbors[u].add(v)
            neighbors[v].add(u)
    arcs = [(v,u) for v in range(n) for u in sorted(neighbors[v])]
    return neighbors, arcs


def order_faces(p):
    # Build all distinct states of the vertex-ordering automaton.
    neighbors, arcs = graph(p)
    n = len(neighbors)
    arc_index = {arc:j for j,arc in enumerate(arcs)}
    states = {(0,0)}
    for _ in range(n):
        next_states = set()
        for placed, matching in states:
            for v in range(n):
                if placed >> v & 1:
                    continue
                earlier = [u for u in neighbors[v] if placed >> u & 1]
                next_matching = matching
                if len(earlier) == 1:
                    next_matching |= 1 << arc_index[(v,earlier[0])]
                next_states.add((placed | (1<<v), next_matching))
        states = next_states
    full = (1<<n)-1
    return arcs, downset({f for s,f in states if s==full})


def local_classes():
    # Local order restrictions relative to a common center 0.
    local = [(1,0),(1,2),(2,1),(2,3),(3,0),(3,2)]
    neighbors, _ = graph(1)
    result = {}
    for name, cond in {
        'L': lambda pos: True,
        'U': lambda pos: pos[0]<pos[1] and pos[0]<pos[3],
        'Wa':lambda pos: pos[1]<pos[0]<pos[3],
        'Wc':lambda pos: pos[3]<pos[0]<pos[1],
    }.items():
        gen = set()
        for perm in permutations(range(4)):
            pos = {v:j for j,v in enumerate(perm)}
            if not cond(pos):
                continue
            matching=0
            for v in (1,2,3):
                smaller = [u for u in neighbors[v] if pos[u]<pos[v]]
                if len(smaller)==1:
                    matching |= 1 << local.index((v,smaller[0]))
            gen.add(matching)
        result[name] = downset(gen)
    return local, result


def join(families):
    acc = {0}
    offset = 0
    for width, faces in families:
        acc = {a | (b << offset) for a in acc for b in faces}
        offset += width
    return acc


def predicted_faces(p, arcs, classes):
    # Predicted description: base L^*p and a cone for each (center, petal endpoint).
    ids = {arc:i for i,arc in enumerate(arcs)}
    local = [(1,0),(1,2),(2,1),(2,3),(3,0),(3,2)]
    petal_bits = []
    for j in range(p):
        bits = [ids[(v+3*j, u+3*j)] if u else ids[(v+3*j,0)] for v,u in local]
        petal_bits.append(bits)
    def mapmask(mask, indices):
        return sum(1<<indices[i] for i in range(6) if mask >> i & 1)
    def product(names):
        masks = {0}
        for i, name in enumerate(names):
            masks = {a | mapmask(b,petal_bits[i]) for a in masks for b in classes[name]}
        return masks
    base = product(['L']*p)
    total = set(base)
    for j in range(p):
        for label, endpoint in [('Wa',1+3*j),('Wc',3+3*j)]:
            link = product(['U' if i!=j else label for i in range(p)])
            apex = 1 << ids[(0,endpoint)]
            total |= {f | apex for f in link}
    return base, total


def mod2_betti(faces):
    level = {}
    for face in faces:
        if face:
            d = face.bit_count()-1
            level.setdefault(d, []).append(face)
    for d in level:
        level[d].sort()
    index = {d:{f:i for i,f in enumerate(level[d])} for d in level}
    ranks = {}
    for d in sorted(level):
        if d == 0:
            continue
        basis = {}
        for simplex in level[d]:
            v = 0
            m = simplex
            while m:
                bit = m & -m
                m -= bit
                v ^= 1 << index[d-1][simplex^bit]
            while v:
                pivot = v.bit_length()-1
                if pivot not in basis:
                    basis[pivot] = v
                    break
                v ^= basis[pivot]
        ranks[d] = len(basis)
    return {d:len(level[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in sorted(level)}


def main():
    local, cl = local_classes()
    def maximal_edges(name):
        faces = cl[name]
        return sorted(tuple(local[i] for i in range(6) if x>>i&1) for x in faces if x and not any(y!=x and x&y==x for y in faces))
    assert len(cl['L']) == 13 and sum(f.bit_count()==1 for f in cl['L'])==6
    assert sum(f.bit_count()==2 for f in cl['L'])==6
    assert len(cl['U'])==8 and sum(f.bit_count()==2 for f in cl['U'])==3
    assert len(cl['Wa']) == len(cl['Wc']) == 4
    print('local L: six vertices, six edges, connected cycle')
    print('local U: four vertices, three edges, connected path')
    print('local Wa/Wc: three isolated vertices each')
    for p in (1,2,3):
        arcs, actual = order_faces(p)
        base, predicted = predicted_faces(p, arcs, cl)
        assert predicted == actual, (p,len(predicted),len(actual),len(predicted^actual))
        ranks = mod2_betti(actual)
        fv = dict(sorted(Counter(f.bit_count()-1 for f in actual if f).items()))
        assert ranks == ({0:1,1:5} if p==1 else {**{k:(1 if k==0 else 0) for k in range(2*p-1)},2*p-1:1})
        print(f'p={p}: faces={len(actual)-1} base_faces={len(base)-1} f_vector={fv} mod2_betti={ranks}, decomposition=exact')
    print('PASS: finite ordering enumeration, local factorization, mod-two boundaries')

if __name__=='__main__':
    main()
