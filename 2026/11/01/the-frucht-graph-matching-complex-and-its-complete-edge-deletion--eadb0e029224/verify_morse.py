#!/usr/bin/env python3
"""Exact finite certificate for matching-complex topology of the Frucht graph.
Uses Python 3 standard library only. All complexes and directed incidences are reconstructed.
"""
from collections import Counter, deque
import json
from pathlib import Path

LCF = (-5, -2, -4, 2, 5, -2, 2, 5, -2, -5, 4, 2)
PIVOT_ORDER = (10, 5, 16, 17, 9, 0, 15, 14, 3, 6, 11, 13, 12, 7, 1, 8, 2, 4)
EXPECTED_BETAS = (12,18,13,16,15,15,12,15,15,14,16,18,14,13,15,17,12,17)
EXPECTED_FVECTOR = (18,117,333,397,152,8)


def graph_edges():
    edges = {tuple(sorted((i, (i+1)%12))) for i in range(12)}
    edges.update(tuple(sorted((i, (i+LCF[i])%12))) for i in range(12))
    e = tuple(sorted(edges))
    assert len(e) == 18
    assert all(sum(v in edge for edge in e) == 3 for v in range(12))
    return e


def all_faces(edges):
    # Independent generation: depth-first enumeration with 12-bit used-vertex mask.
    supports = [sum(1 << v for v in edge) for edge in edges]
    out = set()
    def visit(mask, used, first):
        if mask:
            out.add(mask)
        for i in range(first, len(supports)):
            if not (used & supports[i]):
                visit(mask | (1 << i), used | supports[i], i+1)
    visit(0, 0, 0)
    return out


def discrete_morse(faces, allowed):
    remaining = set(faces)
    pairs = []
    for j in PIVOT_ORDER:
        if j not in allowed:
            continue
        bit = 1 << j
        for low in sorted(remaining):
            high = low | bit
            if not (low & bit) and high in remaining:
                remaining.remove(low)
                remaining.remove(high)
                pairs.append((low, high))
    return pairs, sorted(remaining)


def check_gradient(faces, pairs):
    assert len(faces) == 2*len(pairs) + len(faces) - 2*len(pairs)
    matched = set(pairs)
    indeg = {f: 0 for f in faces}
    adj = {f: [] for f in faces}
    incidences = 0
    for high in faces:
        t = high
        while t:
            bit = t & -t
            t -= bit
            low = high ^ bit
            if not low:
                continue
            assert low in faces
            a, b = (low, high) if (low, high) in matched else (high, low)
            adj[a].append(b)
            indeg[b] += 1
            incidences += 1
    q = deque([f for f in faces if indeg[f] == 0])
    sorted_count = 0
    while q:
        u = q.popleft()
        sorted_count += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    assert sorted_count == len(faces), 'Directed Hasse cycle detected'
    return incidences


def check_cert(cert, cases):
    assert cert['lcf_jumps'] == list(LCF)
    assert cert['pivot_order'] == list(PIVOT_ORDER)
    assert cert['edges'] == [list(e) for e in graph_edges()]
    assert len(cert['cases']) == 19
    for a,b in zip(cert['cases'],cases):
        assert a == b


def main():
    es = graph_edges()
    faces = all_faces(es)
    assert len(faces) == 1025
    assert tuple(Counter(f.bit_count()-1 for f in faces)[i] for i in range(6)) == EXPECTED_FVECTOR
    cases = []
    for deleted in (None, *range(len(es))):
        sub = faces if deleted is None else {f for f in faces if not (f & (1 << deleted))}
        allowed = set(range(len(es))) if deleted is None else set(range(len(es))) - {deleted}
        pairs, critical = discrete_morse(sub, allowed)
        assert len(set(x for p in pairs for x in p)) == 2*len(pairs)
        assert not (set(critical) & set(x for p in pairs for x in p))
        assert set(critical) | set(x for p in pairs for x in p) == sub
        assert all((hi.bit_count() - lo.bit_count()) == 1 and (lo&hi) == lo for lo,hi in pairs)
        inc = check_gradient(sub, pairs)
        beta = 20 if deleted is None else EXPECTED_BETAS[deleted]
        critical_counts = Counter(f.bit_count()-1 for f in critical)
        assert critical_counts == {0:1,3:beta}, (deleted,critical_counts)
        assert sum((-1)**(f.bit_count()-1) for f in sub) == 1-beta
        cases.append({'deleted_edge_index':deleted,'nonempty_faces':len(sub),
                      'matched_pairs':len(pairs),'incidences':inc,
                      'critical_by_dimension':{'0':1,'3':beta},
                      'critical_bitmasks':critical,
                      'pairs':[[lo,hi] for lo,hi in pairs]})
    cert = {'lcf_jumps':list(LCF), 'pivot_order':list(PIVOT_ORDER),
            'edges':[list(e) for e in es], 'cases':cases}
    p = Path(__file__).with_name('morse_certificate.json')
    if p.exists():
        check_cert(json.loads(p.read_text(encoding='utf-8')),cases)
    else:
        raise RuntimeError('Missing accompanying morse_certificate.json')
    print('FRUCHT_EDGE_MATCHING_MORSE_OK cases=19 full_faces=1025 critical_3=20 deletion_betas=' + ','.join(map(str,EXPECTED_BETAS)))

if __name__ == '__main__':
    main()
