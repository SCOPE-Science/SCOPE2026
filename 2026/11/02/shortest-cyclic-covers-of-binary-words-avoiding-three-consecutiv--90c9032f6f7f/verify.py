#!/usr/bin/env python3
"""Exact integer primal/dual certificate checker for restricted circular word covers.
Only Python's standard library is required. Run beside CERT.json.
"""
import base64
import json
from pathlib import Path
import struct
import zlib


def permitted(w, n):
    return all((w >> j) & 7 for j in range(n - 2))


def verify_case(row):
    n = row['n']
    assert 3 <= n <= 16
    V = 1 << (n - 1)
    E = 1 << n
    mask = V - 1
    extra = list(zlib.decompress(base64.b64decode(row['augmentation_zlib_b64'])))
    pbytes = zlib.decompress(base64.b64decode(row['potential_i16le_zlib_b64']))
    p = struct.unpack('<' + 'h' * V, pbytes)
    assert len(extra) == E
    assert len(pbytes) == 2 * V
    original = [int(permitted(w, n)) for w in range(E)]
    assert sum(original) == row['required']
    assert sum(extra) == row['additional']
    assert all(extra[w] == 0 for w in range(E) if not original[w])
    assert min(extra) >= 0

    indeg = [0] * V
    outdeg = [0] * V
    in_plus = [0] * V
    out_plus = [0] * V
    for w in range(E):
        u, v = w >> 1, w & mask
        outdeg[u] += original[w]
        indeg[v] += original[w]
        out_plus[u] += extra[w]
        in_plus[v] += extra[w]
        # Full de Bruijn graph: even a forbidden extra edge is allowed
        # in a hypothetical alternative covering cycle.
        assert p[v] - p[u] <= 1, ('dual edge inequality', n, w)
        if extra[w]:
            assert p[v] - p[u] == 1, ('complementarity', n, w)
    for v in range(V):
        assert out_plus[v] - in_plus[v] == indeg[v] - outdeg[v]
    # Under the constraints, the dual potential lower bound for the
    # number of extra windows is the exact dot product below.
    dual = sum(p[v] * (outdeg[v] - indeg[v]) for v in range(V))
    assert dual == row['additional'], (n, dual, row['additional'])

    w = row['witness']
    assert set(w) <= {'0', '1'}
    assert len(w) == row['required'] + row['additional'] == row['length']
    # Check *every indexed cyclic window*, including wraps, against
    # the complete prescribed multiset of n-word traversals.
    occurrences = [0] * E
    extended = w + w[:n - 1]
    for i in range(len(w)):
        edge = int(extended[i:i + n], 2)
        occurrences[edge] += 1
    assert occurrences == [original[e] + extra[e] for e in range(E)]
    # In particular the optimum itself avoids the forbidden triple.
    assert '000' not in (w + w[:2])
    return n, row['required'], row['additional'], row['length']


def check_tiny_exhaustive(n, optimum):
    # Independent brute-force check for n=3,4: a circular binary word
    # of period m is represented by all indexed m-bit strings.
    must = {u for u in range(1 << n) if permitted(u, n)}
    for m in range(n, optimum):
        for x in range(1 << m):
            w = format(x, '0%db' % m)
            cyclic = w + w[:n - 1]
            got = {int(cyclic[j:j+n], 2) for j in range(m)}
            assert not must.issubset(got), (n,m,w)


def main():
    data = json.loads((Path(__file__).parent / 'CERT.json').read_text('utf-8'))
    assert data['schema_version'] == 1
    cases = data['cases']
    assert [x['n'] for x in cases] == list(range(3,17))
    for row in cases:
        n, requested, added, length = verify_case(row)
        print(f'order={n} required={requested} extra={added} minimum={length}')
        if n in (3,4):
            check_tiny_exhaustive(n, length)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
