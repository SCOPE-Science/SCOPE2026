"""Exact finite validation of signed cellular traces for wheel two-particle spaces.

Reconstructs the unordered two-particle cubical graph configuration complex,
its boundary operators mod 2, and the signed action of every dihedral element.
This verifies finite instances of, but does not replace, the uniform proof.
"""
from itertools import combinations


def rank_binary(columns):
    pivots = {}
    for v in columns:
        while v:
            b = v.bit_length() - 1
            if b not in pivots:
                pivots[b] = v
                break
            v ^= pivots[b]
    return len(pivots)


def model(n):
    assert n >= 4
    vertices = tuple(range(n + 1))
    hub = n
    edges = tuple(sorted({tuple(sorted(edge)) for i in range(n)
                          for edge in ((i, (i + 1) % n), (i, hub))}))
    eid = {e: i for i, e in enumerate(edges)}
    zero = tuple(combinations(vertices, 2))
    one = tuple((v, j) for v in vertices for j, e in enumerate(edges)
                if v not in e)
    two = tuple((i, j) for i, e in enumerate(edges)
                for j in range(i + 1, len(edges))
                if set(e).isdisjoint(edges[j]))
    z_id = {z: i for i, z in enumerate(zero)}
    o_id = {c: i for i, c in enumerate(one)}
    b1 = []
    for v, j in one:
        a, b = edges[j]
        b1.append((1 << z_id[tuple(sorted((v, a)))]) ^
                  (1 << z_id[tuple(sorted((v, b)))]))
    b2 = []
    for i, j in two:
        a, b = edges[i]
        c, d = edges[j]
        w = 0
        for pair in ((a, j), (b, j), (c, i), (d, i)):
            w ^= 1 << o_id[pair]
        b2.append(w)
    assert len(zero) == n * (n + 1) // 2
    assert len(one) == 2 * n * (n - 1)
    assert len(two) == n * (3 * n - 7) // 2
    assert rank_binary(b1) == len(zero) - 1
    assert rank_binary(b2) == len(two)
    for w in b2:
        boundary = 0
        while w:
            z = w & -w
            w -= z
            boundary ^= b1[z.bit_length() - 1]
        assert boundary == 0
    return vertices, edges, zero, one, two, eid


def character(n, is_reflection, k, data):
    vertices, edges, zero, one, two, eid = data
    def gv(v):
        return ((k - v) % n if is_reflection else (v + k) % n) if v < n else n
    pem = [eid[tuple(sorted(map(gv, e)))] for e in edges]
    edge_sign = [1 if gv(a) < gv(b) else -1 for a, b in edges]
    t0 = sum(1 for a, b in zero if set((gv(a), gv(b))) == {a, b})
    t1 = sum(edge_sign[j] for v, j in one if gv(v) == v and pem[j] == j)
    t2 = sum(edge_sign[i] * edge_sign[j] * (1 if pem[i] < pem[j] else -1)
             for i, j in two if {pem[i], pem[j]} == {i, j})
    return (t0, t1, t2, 1 - t0 + t1 - t2)


def expected(n, reflection, k):
    if not reflection:
        if k == 0:
            return (n * (n + 1) // 2, 2 * n * (n - 1),
                    n * (3 * n - 7) // 2, n + 1)
        if n % 2 == 0 and k == n // 2:
            return (n // 2, 0, -n // 2, 1)
        return (0, 0, 0, 1)
    if n % 2 == 1:
        return ((n + 1) // 2, -2, -(n - 1) // 2, -2)
    if k % 2 == 0:
        return ((n + 4) // 2, 2, 2 - n // 2, -1)
    return (n // 2, -2, 2 - n // 2, -3)


def main():
    total = 0
    for n in range(4, 41):
        data = model(n)
        for refl in (False, True):
            for k in range(n):
                observed = character(n, refl, k, data)
                assert observed == expected(n, refl, k), (n, refl, k, observed)
                total += 1
        chars = [character(n, False, k, data)[-1] for k in range(n)]
        chars += [character(n, True, k, data)[-1] for k in range(n)]
        assert sum(chars) == 0  # no full dihedral invariants
        assert sum(chars[:n]) == 2 * n  # two rotational invariant lines
    print('WHEEL_CONFIG_CHAR_VERIFY_OK')
    print('Checked rim lengths 4..40, signed traces for', total,
          'dihedral elements, and exact mod-two boundary ranks.')
    print('Checked every dimension, all three cellular traces, and invariant counts.')


if __name__ == '__main__':
    main()
