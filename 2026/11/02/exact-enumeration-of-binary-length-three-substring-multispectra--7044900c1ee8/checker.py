#!/usr/bin/env python3
"""Exact, standard-library verification of the binary three-gram profile theorem.
The finite calculation is a proof certificate only in conjunction with the
rational-denominator and degree bound proved in RESULT.md.
"""

from itertools import product

P = [1, 5, -6, 5, -1, 6, 3, 1, -1, -2, 2]
M = 40
EDGES = ((0, 1), (1, 2), (1, 3), (2, 0), (2, 1), (3, 2))


def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def connected_nonloop(b, c, d, e, f, g):
    weights = (b, c, d, e, f, g)
    seen_edges = [(u, v) for (u, v), weight in zip(EDGES, weights) if weight]
    if not seen_edges:
        return None
    active = {vertex for edge in seen_edges for vertex in edge}
    reached = {min(active)}
    while True:
        after = set(reached)
        for u, v in seen_edges:
            if u in reached:
                after.add(v)
            if v in reached:
                after.add(u)
        if after == reached:
            break
        reached = after
    if reached != active:
        return None
    return (int(0 in active), int(3 in active))


def count_by_flow(max_m):
    """Euler-trail feasibility, enumerated by three free integral parameters."""
    out = [1] + [2] * max_m  # Empty profile; isolated 000 and 111 loop profiles.
    deltas = [(0, 0, 0, 0)]
    for start in range(4):
        for end in range(4):
            if start != end:
                deltas.append(tuple((1 if v == start else -1 if v == end else 0)
                                    for v in range(4)))
    for d0, d1, d2, d3 in deltas:
        for b in range(max_m + 1):
            e = b - d0
            if e < 0:
                continue
            for d in range(max_m + 1):
                g = d + d3
                base = b + e + d + g
                if g < 0:
                    continue
                if base > max_m:
                    break
                for c in range(max_m - base + 1):
                    f = c + d - b - d1
                    if f < 0:
                        continue
                    nonloop_sum = base + c + f
                    if nonloop_sum > max_m:
                        break
                    if not nonloop_sum:
                        continue
                    visited = connected_nonloop(b, c, d, e, f, g)
                    if visited is None:
                        continue
                    loop_vertices = sum(visited)
                    for m in range(nonloop_sum, max_m + 1):
                        extra = m - nonloop_sum
                        if loop_vertices == 2:
                            out[m] += extra + 1
                        elif loop_vertices == 1 or extra == 0:
                            out[m] += 1
    return out


def count_by_words(n):
    """Independent enumeration: hash the 8 read multiplicities of actual words."""
    seen = set()
    for word in range(1 << n):
        counts = [0] * 8
        for i in range(n - 2):
            trigram = (word >> i) & 7
            counts[trigram] += 1
        seen.add(tuple(counts))
    return len(seen)


def main():
    a = count_by_flow(M)
    for n in range(3, 17):
        assert count_by_words(n) == a[n - 2], (n, count_by_words(n), a[n - 2])
    # D0 = (1-z)^3 (1-z^2)(1-z^3)(1-z^4)
    d0 = [1]
    for polynomial in ([1, -1],) * 3 + ([1, 0, -1],
                                          [1, 0, 0, -1],
                                          [1, 0, 0, 0, -1]):
        d0 = multiply(d0, polynomial)
    left = multiply(a, d0)
    right = multiply(P, [1, 0, -1])  # D0/Q = 1-z^2
    for k in range(M + 1):
        assert left[k] == (right[k] if k < len(right) else 0), (k, left[k])
    assert len(d0) - 1 == 12
    assert a[:21] == [1, 8, 15, 28, 52, 92, 151, 240, 363, 532, 757,
                      1048, 1416, 1880, 2449, 3140, 3971, 4960, 6123,
                      7484, 9060]
    print('PASS: word-level profile enumeration for lengths 3..16;')
    print('PASS: independent Euler-flow counts through m=40;')
    print('PASS: polynomial rational-identity coefficient certificate through degree 40.')
    print('First 12 nonempty spectrum counts:', a[1:13])


if __name__ == '__main__':
    main()
