#!/usr/bin/env python3
"""Independent exact checks for 1-limited domination of cyclic clique cylinders.

The verifier is self-contained and needs Python 3.9 or later.
A vertex is 1-limited dominated when it is selected or adjacent to selected,
and each selected vertex has at most one nonselected neighbour.
"""
from itertools import product


def prediction(n, m):
    assert n >= 3 and m >= 3
    q, r = divmod(n, 3)
    return m * (n // 2 + int(n % 4 != 0))


def valid_vertexwise(n, m, fiber_masks):
    full = (1 << m) - 1
    for i in range(n):
        b = fiber_masks[i]
        a = fiber_masks[(i - 1) % n]
        c = fiber_masks[(i + 1) % n]
        inside = b.bit_count()
        for j in range(m):
            bit = 1 << j
            if b & bit:
                outside = (m - inside) + int(not(a & bit)) + int(not(c & bit))
                if outside > 1:
                    return False
            elif inside == 0 and not (a & bit or c & bit):
                return False
    return True


def full_subset_exact(n, m):
    """Exhaustive labelled vertex-subset enumeration with no fiber pruning."""
    N = n * m
    neighbors = []
    for i in range(n):
        for j in range(m):
            verts = [i*m+k for k in range(m) if k != j]
            verts += [((i - 1) % n)*m+j, ((i + 1) % n)*m+j]
            neighbors.append(sum(1 << k for k in verts))
    best = N + 1
    found = 0
    for mask in range(1 << N):
        s = mask.bit_count()
        if s > best:
            continue
        if all(((mask >> v) & 1 and (neighbors[v] & ~mask).bit_count() <= 1)
               or ((mask >> v) & 1 == 0 and (neighbors[v] & mask) != 0)
               for v in range(N)):
            if s < best:
                best, found = s, 1
            else:
                found += 1
    return best, found


def triple_valid(m, a, b, c):
    inside = b.bit_count()
    for j in range(m):
        bit = 1 << j
        if b & bit:
            if m - inside + int(not(a & bit)) + int(not(c & bit)) > 1:
                return False
        elif inside == 0 and not(a & bit or c & bit):
            return False
    return True


def transfer_exact(n, m):
    """Independent exact cyclic triple constraint / min-plus transfer."""
    full = (1 << m) - 1
    states = [0, full] + [full ^ (1 << j) for j in range(m)]
    triple = {(a, b, c): triple_valid(m, a, b, c)
              for a in states for b in states for c in states}
    best = m * n + 1
    for a in states:
        for b in states:
            cur = {(a,b): a.bit_count()+b.bit_count()}
            for _ in range(2, n):
                nxt = {}
                for (u, v), val in cur.items():
                    for c in states:
                        if not triple[u, v, c]:
                            continue
                        key = (v, c)
                        vv = val + c.bit_count()
                        if vv < nxt.get(key, n*m+1):
                            nxt[key] = vv
                cur = nxt
            for (u, v), val in cur.items():
                if triple[u, v, a] and triple[v, a, b]:
                    best = min(best, val)
    return best


def constructive_masks(n, m):
    q, r = divmod(n, 4)
    blocks = {0: '1100' * q,
              1: '11100' + '1100' * (q - 1) if q >= 1 else None,
              2: '111100' + '1100' * (q - 1) if q >= 1 else None,
              3: '110' + '1100' * q}
    binary = blocks[r]
    full = (1 << m) - 1
    assert binary and len(binary) == n
    return [full if x == '1' else 0 for x in binary]


def main():
    tests = 0
    for m in range(3, 7):
        for n in range(3, 7):
            if m*n > 18:
                continue
            observed, number = full_subset_exact(n, m)
            expected = prediction(n, m)
            assert observed == expected, (n, m, observed, expected)
            tests += 1
            print(f'FULL_SUBSET n={n} m={m} optimum={observed} minimum_sets={number}')
    print(f'FULL_SUBSET_OK {tests}')
    triples = 0
    for m in range(3, 9):
        for n in range(3, 43):
            observed = transfer_exact(n, m)
            expected = prediction(n, m)
            assert observed == expected, (n, m, observed, expected)
            triples += 1
    print(f'CYCLIC_TRANSFER_OK {triples} instances (m=3..8,n=3..42)')
    certificates = 0
    for m in range(3, 31):
        for n in range(3, 161):
            masks = constructive_masks(n, m)
            assert valid_vertexwise(n, m, masks), (n, m, masks)
            assert sum(b.bit_count() for b in masks) == prediction(n, m), (n, m)
            certificates += 1
    print(f'CONSTRUCTION_OK {certificates} instances (m=3..30,n=3..160)')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
