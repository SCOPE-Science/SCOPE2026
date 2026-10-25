#!/usr/bin/env python3
"""Independent finite checks for cyclic-coordinate fixed loci of 3-letter Hamming Rips complexes.

Uses literal word-orbits and raw Hamming distances; checks an abstract
orbit-clique description, simplicial homology and symmetry Lefschetz traces.
No external Python packages are required.
"""
from itertools import combinations, permutations, product
from math import comb, factorial


def hamming(x, y):
    return sum(a != b for a, b in zip(x, y))


def word_orbits(q):
    seen = set()
    output = []
    for x in product(range(q), repeat=3):
        if x in seen:
            continue
        r1 = (x[1], x[2], x[0])
        r2 = (x[2], x[0], x[1])
        orbit = tuple(sorted({x, r1, r2}))
        seen.update(orbit)
        if all(hamming(y, z) <= 2 for y in orbit for z in orbit):
            output.append(orbit)
    return output


def label(orbit):
    if len(orbit) == 1:
        return ('C', orbit[0][0])
    w = orbit[0]
    for c in w:
        if w.count(c) == 2:
            return ('D', c, next(d for d in w if d != c))
    raise AssertionError('non-admissible orbit')


def raw_edges(orbits):
    return {(i, j) for i, j in combinations(range(len(orbits)), 2)
            if all(hamming(x, y) <= 2 for x in orbits[i] for y in orbits[j])}


def predicted_edge(a, b):
    if a[0] == b[0] == 'C':
        return False
    if a[0] == b[0] == 'D':
        return a[1] == b[1]
    c, d = (a, b) if a[0] == 'C' else (b, a)
    return c[1] in d[1:]


def faces(labels, edges):
    idx = {tag: i for i, tag in enumerate(labels)}
    q = len([tag for tag in labels if tag[0] == 'C'])
    out = set()
    for a in range(q):
        block = [idx[('C', a)]] + [idx[('D', a, b)] for b in range(q) if b != a]
        for count in range(1, len(block)+1):
            for f in combinations(sorted(block), count):
                out.add(f)
    for a in range(q):
        for b in range(q):
            if a != b:
                out.add(tuple(sorted([idx[('D', a, b)], idx[('C', b)]])))
    for f in out:
        for i, j in combinations(f, 2):
            assert tuple(sorted([i,j])) in edges
    return out


def mod2_rank(columns):
    pivots = {}
    for v in columns:
        while v:
            k = v.bit_length()-1
            if k in pivots:
                v ^= pivots[k]
            else:
                pivots[k] = v
                break
    return len(pivots)


def homology_mod2(face_set):
    dims = {}
    for f in face_set:
        dims.setdefault(len(f)-1, []).append(f)
    ranks = {0:0}
    for k in range(1, max(dims)+1):
        row = {f: i for i, f in enumerate(dims[k-1])}
        columns = []
        for f in dims[k]:
            mask = 0
            for g in combinations(f, len(f)-1):
                mask ^= 1 << row[g]
            columns.append(mask)
        ranks[k] = mod2_rank(columns)
    betti = {k: len(v)-ranks.get(k,0)-ranks.get(k+1,0)
             for k,v in dims.items()}
    betti[0] -= 1
    return {k:v for k,v in betti.items() if v}


def sign_of_permutation(seq):
    s=1
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if seq[i]>seq[j]: s=-s
    return s


def lefschetz(labels, face_set, sigma):
    index = {tag:i for i,tag in enumerate(labels)}
    mapping = []
    for tag in labels:
        moved = (tag[0],) + tuple(sigma[c] for c in tag[1:])
        mapping.append(index[moved])
    l = -1 # reduced Euler/Lefschetz correction from H_0
    for f in face_set:
        im = [mapping[i] for i in f]
        if sorted(im) == list(f):
            order = [f.index(i) for i in im]
            l += (-1)**(len(f)-1)*sign_of_permutation(order)
    return l


def check(q):
    orbits = word_orbits(q)
    labels = [label(o) for o in orbits]
    assert len(set(labels))==len(labels)==q*q
    edges = raw_edges(orbits)
    expected = {(i,j) for i,j in combinations(range(q*q),2)
                if predicted_edge(labels[i],labels[j])}
    assert edges==expected, ('edge difference',q,edges^expected)
    face_set=faces(labels,edges)
    counts={k:sum(len(f)==k+1 for f in face_set) for k in range(q)}
    for k in range(q):
        expected_count = q*q if k==0 else (q*comb(q,2)+q*(q-1) if k==1
                               else q*comb(q,k+1))
        assert counts[k]==expected_count, (q,k,counts[k],expected_count)
    betti = homology_mod2(face_set)
    assert betti == {1:(q-1)**2}, (q,betti)
    tested=0
    if q<=5:
        for sigma in permutations(range(q)):
            fixed = sum(sigma[a]==a for a in range(q))
            got=lefschetz(labels,face_set,sigma)
            assert got==-(fixed-1)**2,(q,sigma,got, fixed)
            tested+=1
    print('q=',q,'raw_orbits=',len(orbits),'raw_compatible_pairs=',len(edges),
          'f_vector=',[counts[k] for k in range(q)],
          'mod2_reduced_betti=',betti,'symmetries_checked=',tested)

if __name__=='__main__':
    for q in range(2,7):
        check(q)
    print('ALL CHECKS PASSED')
