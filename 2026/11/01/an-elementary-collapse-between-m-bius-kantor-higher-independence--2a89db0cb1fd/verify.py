#!/usr/bin/env python3
"""Exact simplicial-collapse certificate for two adjacent higher-independence complexes.

Use ``python verify.py --emit`` once to generate collapse_pairs.txt.
Use ``python verify.py`` to independently reconstruct and replay the certificate.
Only the Python standard library is required.
"""
import hashlib
import heapq
import itertools
import pathlib
import sys
from collections import Counter

N = 16
HERE = pathlib.Path(__file__).resolve().parent
CERT = HERE / 'collapse_pairs.txt'


def graph():
    neighbors = [0] * N
    for i in range(8):
        for u, v in ((i, (i + 1) % 8), (i, i + 8), (i + 8, 8 + (i + 3) % 8)):
            neighbors[u] |= 1 << v
            neighbors[v] |= 1 << u
    return neighbors


def component_legal(mask, r, adj):
    rem = mask
    while rem:
        frontier = rem & -rem
        seen = frontier
        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            new = (adj[bit.bit_length() - 1] & rem) & ~seen
            seen |= new
            frontier |= new
            if seen.bit_count() > r:
                return False
        rem &= ~seen
    return True


def forbidden_connected(adj, size):
    ans = []
    for vertices in itertools.combinations(range(N), size):
        mask = sum(1 << i for i in vertices)
        if component_legal(mask, size - 1, adj) is False:
            # A size-k set exceeds cutoff k-1 exactly if it is connected.
            ans.append(mask)
    return ans


def forbidden_legal(mask, forbidden):
    return not any((mask & pattern) == pattern for pattern in forbidden)


def independent_faces():
    adj = graph()
    assert sum(x.bit_count() for x in adj) == 48
    assert all(adj[i] & (1 << i) == 0 for i in range(N))
    assert all((adj[i] >> j) & 1 == (adj[j] >> i) & 1 for i in range(N) for j in range(N))
    bad3 = forbidden_connected(adj, 3)
    bad4 = forbidden_connected(adj, 4)
    f2, f3 = set(), set()
    for mask in range(1 << N):
        x2 = component_legal(mask, 2, adj)
        x3 = component_legal(mask, 3, adj)
        assert x2 == forbidden_legal(mask, bad3)
        assert x3 == forbidden_legal(mask, bad4)
        # The cutoff-two condition has an independent local characterization.
        deg_ok = all((adj[i] & mask).bit_count() <= 1
                     for i in range(N) if mask & (1 << i))
        assert x2 == deg_ok
        if x2:
            f2.add(mask)
        if x3:
            f3.add(mask)
    assert f2 <= f3
    assert len(f2) == 6813 and len(f3) == 15197
    assert len(f3 - f2) == 8384
    return f2, f3, bad3, bad4


def cofaces_one(mask, faces):
    return [mask | (1 << v) for v in range(N)
            if (mask & (1 << v)) == 0 and (mask | (1 << v)) in faces]


def produce_pairs(relative):
    remaining = set(relative)
    # Counts are maintained independently of the later verifier's direct scan.
    count = {m: len(cofaces_one(m, remaining)) for m in remaining}
    candidates = []
    for m in remaining:
        if count[m] == 1:
            heapq.heappush(candidates, (m.bit_count(), m))
    pairs = []
    while candidates:
        _, low = heapq.heappop(candidates)
        if low not in remaining or count[low] != 1:
            continue
        high = cofaces_one(low, remaining)
        assert len(high) == 1
        high = high[0]
        pairs.append((low, high))
        for m in (low, high):
            remaining.remove(m)
            for v in range(N):
                if m & (1 << v):
                    parent = m ^ (1 << v)
                    if parent in remaining:
                        count[parent] -= 1
                        assert count[parent] >= 0
                        if count[parent] == 1:
                            heapq.heappush(candidates, (parent.bit_count(), parent))
    assert not remaining
    return pairs


def replay_pairs(large, small, pairs):
    remaining = set(large)
    used = set()
    for step, (low, high) in enumerate(pairs):
        assert low not in small and high not in small
        assert low in remaining and high in remaining
        assert low not in used and high not in used
        assert low.bit_count() + 1 == high.bit_count()
        assert low & high == low
        # The complete, currently remaining complex, not just a relative chain,
        # is searched for every codimension-one coface.
        assert cofaces_one(low, remaining) == [high], (step, low, high)
        # A unique codimension-one coface forces that coface to be maximal.
        assert not cofaces_one(high, remaining), (step, high)
        remaining.remove(low)
        remaining.remove(high)
        used.update((low, high))
    assert remaining == small
    assert len(used) == len(large - small)
    return Counter(low.bit_count() - 1 for low, _ in pairs)


def face_vector(faces):
    return dict(sorted(Counter(m.bit_count() - 1 for m in faces).items()))


def euler(faces):
    return sum((-1 if m.bit_count() % 2 == 0 else 1)
               for m in faces if m)


def main():
    f2, f3, bad3, bad4 = independent_faces()
    pairs = produce_pairs(f3 - f2)
    encoded = ''.join(f'{a} {b}\n' for a, b in pairs).encode('ascii')
    if '--emit' in sys.argv:
        CERT.write_bytes(encoded)
    assert CERT.is_file()
    assert CERT.read_bytes() == encoded
    parsed = []
    for line in CERT.read_text(encoding='ascii').splitlines():
        assert len(line.split()) == 2
        parsed.append(tuple(map(int, line.split())))
    assert parsed == pairs
    histogram = replay_pairs(f3, f2, parsed)
    assert len(pairs) == 4192
    assert euler(f2) == euler(f3) == 4
    print('GRAPH_VERTICES', N)
    print('GRAPH_EDGES', 24)
    print('CONNECTED_FORBIDDEN_TRIPLES', len(bad3))
    print('CONNECTED_FORBIDDEN_QUADRUPLES', len(bad4))
    print('FACES_R2', len(f2), 'F_VECTOR', face_vector(f2))
    print('FACES_R3', len(f3), 'F_VECTOR', face_vector(f3))
    print('RELATIVE_FACES', len(f3 - f2))
    print('ELEMENTARY_COLLAPSE_PAIRS', len(pairs))
    print('PAIRS_BY_LOWER_DIMENSION', dict(sorted(histogram.items())))
    print('FIRST_PAIR', *pairs[0])
    print('LAST_PAIR', *pairs[-1])
    print('COLLAPSE_CERTIFICATE_SHA256', hashlib.sha256(encoded).hexdigest())
    print('EULER_CHARACTERISTIC_BOTH', euler(f2))
    print('FINAL_RETAINED_COMPLEX_IS_INDEPENDENCE_2', True)
    print('MOBIUS_KANTOR_RELATIVE_COLLAPSE_VERIFIED')


if __name__ == '__main__':
    main()
