"""Exact joint law of two binary16 long-time basin labels."""

from fractions import Fraction


Q, N = 2**24, 0x3c01
q = [j if j < 1024 else (1024 + j % 1024) << (j // 1024 - 1)
     for j in range(N)]


def round_scaled(p, d):
    assert 0 <= p <= Q * d and d > 0
    a, b = 0, N - 1
    while b - a > 1:
        c = (a + b) // 2
        if d * q[c] <= p:
            a = c
        else:
            b = c
    da, db = p - d * q[a], d * q[b] - p
    return a if da < db or (da == db and a % 2 == 0) else b


def classify(edge, nonfixed):
    known = [-1] * N
    histogram, sums = [0] * 3, [0] * 3
    for start in range(N):
        if known[start] != -1:
            continue
        order, seen = [], {}
        j = start
        while known[j] == -1 and j not in seen:
            seen[j] = len(order)
            order.append(j)
            j = edge[j]
        label = known[j]
        if label == -1:
            cycle = order[seen[j]:]
            if cycle == [0]:
                label = 0
            elif cycle == [0x3a00]:
                label = 1
            else:
                assert len(cycle) == nonfixed
                label = 2
            histogram[label] += 1
            sums[label] = sum(q[k] for k in cycle)
        for k in order:
            known[k] = label
    assert histogram == [1, 1, 1]
    assert all(known[k] >= 0 and known[k] == known[edge[k]] for k in range(N))
    return known, [Fraction(sums[k], Q * (nonfixed if k == 2 else 1))
                   for k in range(3)]


def main():
    F = [round_scaled(4 * x * (Q - x), Q) for x in q]
    G = [round_scaled(4 * q[round_scaled(x * q[round_scaled(Q - x, 1)], Q)], 1)
         for x in q]
    a, ca = classify(F, 5)
    b, cb = classify(G, 40)
    weight = [[0] * 3 for _ in range(3)]
    for i in range(N):
        weight[a[i]][b[i]] += q[min(i + 1, N - 1)] - q[max(i - 1, 0)]
    assert sum(map(sum, weight)) == 2 * Q
    assert weight == [[11335435, 0, 21950155], [2730, 22528, 0], [2602, 0, 240982]]
    assert ca == [0, Fraction(3, 4), Fraction(8837, 16384)]
    assert cb == [0, Fraction(3, 4), Fraction(533001, 1048576)]
    ef = sum(ca[j] * sum(weight[j]) for j in range(3)) / (2 * Q)
    eg = sum(cb[j] * sum(row[j] for row in weight) for j in range(3)) / (2 * Q)
    assert ef == Fraction(19241579, 4294967296)
    assert eg == Fraction(11845614952233, 35184372088832)
    assert eg - ef == Fraction(11687987937065, 35184372088832)
    print(weight)


if __name__ == '__main__':
    main()
