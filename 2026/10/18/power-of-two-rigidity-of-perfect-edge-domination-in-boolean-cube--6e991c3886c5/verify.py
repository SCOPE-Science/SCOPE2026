"""Standalone finite checks for the perfect-edge-domination hypercube theorem.

No external dependencies. Usage: python3 verify.py
The mathematical proof, rather than this finite test, establishes all dimensions.
"""
from collections import Counter


def edges(n):
    return [(v, v ^ (1 << i)) for v in range(1 << n)
            for i in range(n) if v < (v ^ (1 << i))]


def peds(n, chosen, edge_list=None):
    if edge_list is None:
        edge_list = edges(n)
    degree = [0] * (1 << n)
    for u, v in chosen:
        degree[u] += 1
        degree[v] += 1
    return all((u, v) in chosen or degree[u] + degree[v] == 1
               for u, v in edge_list)


def exhaustive(n):
    e = edges(n)
    counts = Counter()
    for mask in range(1 << len(e)):
        chosen = {edge for k, edge in enumerate(e) if (mask >> k) & 1}
        if peds(n, chosen, e):
            counts[len(chosen)] += 1
    return dict(sorted(counts.items()))


def linear_code(n):
    assert n > 1 and n & (n - 1) == 0
    r = n.bit_length() - 1
    out = set()
    for v in range(1 << n):
        if v.bit_count() & 1:
            continue
        syndrome = 0
        for i in range(n):
            if (v >> i) & 1:
                syndrome ^= i
        if syndrome == 0:
            out.add(v)
    assert len(out) == (1 << (n - 1)) // n
    return out


def star_set(n, B, e=None):
    if e is None:
        e = edges(n)
    return {edge for edge in e if edge[0] in B or edge[1] in B}


def classify_by_codes(n):
    e = edges(n)
    assert n <= 4
    sols = set()
    for parity in (0, 1):
        part = [v for v in range(1 << n) if v.bit_count() % 2 == parity]
        for mask in range(1 << len(part)):
            B = {v for j, v in enumerate(part) if (mask >> j) & 1}
            if all(sum((v ^ (1 << i)) in B for i in range(n)) == 1
                   for v in range(1 << n) if v.bit_count() % 2 != parity):
                f = star_set(n, B, e)
                assert peds(n, f, e)
                sols.add(frozenset(f))
    return len(sols)


def main():
    assert exhaustive(2) == {2: 4, 4: 1}
    assert exhaustive(3) == {12: 1}
    assert classify_by_codes(2) == 4
    assert classify_by_codes(3) == 0
    assert classify_by_codes(4) == 8
    for n in (2, 4, 8):
        e = edges(n)
        B = linear_code(n)
        f = star_set(n, B, e)
        assert len(f) == 1 << (n - 1)
        assert peds(n, f, e)
        assert all(sum((v ^ (1 << i)) in B for i in range(n)) == 1
                   for v in range(1 << n) if v not in B and v.bit_count() & 1)
        print(f'Q_{n}: |V|={1 << n}, |E|={len(e)}, code_size={len(B)}, |F|={len(f)}, VALID')
    print('Q_2 exhaustive: 4 nontrivial, 1 trivial; Q_3 exhaustive: only trivial')
    print('Q_4 complete one-parity code enumeration: 8 nontrivial edge sets')
    print('All checks passed.')


if __name__ == '__main__':
    main()
