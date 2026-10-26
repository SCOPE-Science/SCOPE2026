"""Standalone exact checks for 0-or-2 public-goods equilibria on squared cycles."""
from math import comb


def transitions():
    out = {}
    for state in range(16):
        a, b, c, d = ((state >> shift) & 1 for shift in (3, 2, 1, 0))
        out[state] = tuple(
            ((state << 1) & 15) | e
            for e in (0, 1)
            if c == int(a + b + d + e in (0, 2))
        )
    return out


EDGES = transitions()
CYCLES = [
    (0b0000, 0b0001, 0b0010, 0b0100, 0b1000),
    (0b0011, 0b0111, 0b1110, 0b1100, 0b1001),
]
BRANCH_EDGES = {
    0b0110: (0b1101,),
    0b1101: (0b1010, 0b1011),
    0b1010: (0b0101,),
    0b0101: (0b1011,),
    0b1011: (0b0110,),
}
expected = {v: () for v in range(16)}
for cyc in CYCLES:
    for i, v in enumerate(cyc):
        expected[v] = (cyc[(i + 1) % 5],)
expected.update(BRANCH_EDGES)
assert expected == EDGES


def count_formula(n):
    total = 10 if n % 5 == 0 else 0
    for a in range(n // 3 + 1):
        if (n - 3 * a) % 5:
            continue
        b = (n - 3 * a) // 5
        if a + b:
            numerator = n * comb(a + b, a)
            assert numerator % (a + b) == 0
            total += numerator // (a + b)
    return total


def brute(n):
    neighbors = [tuple(sorted({(i + j) % n for j in (-2, -1, 1, 2)})) for i in range(n)]
    assert all(len(v) == 4 for v in neighbors)
    total = 0
    for mask in range(1 << n):
        valid = True
        for i in range(n):
            neighbors_active = sum((mask >> j) & 1 for j in neighbors[i])
            if ((mask >> i) & 1) != int(neighbors_active in (0, 2)):
                valid = False
                break
        total += valid
    return total


def trace_counts(limit):
    # Exact integer closed-walk enumeration by recurrence on the 16-state graph.
    counts = [1 if s == t else 0 for s in range(16) for t in range(16)]
    traces = []
    for n in range(1, limit + 1):
        nxt = [0] * 256
        for s in range(16):
            for mid in range(16):
                w = counts[16 * s + mid]
                if w:
                    for t in EDGES[mid]:
                        nxt[16 * s + t] += w
        counts = nxt
        traces.append(sum(counts[17 * s] for s in range(16)))
    return traces


def run():
    # Reconstruct the whole directed graph from the local rule.
    assert len(EDGES) == 16
    assert sum(len(v) for v in EDGES.values()) == 16
    traces = trace_counts(120)
    for n, value in enumerate(traces, start=1):
        assert value == count_formula(n), (n, value, count_formula(n))
    for n in range(5, 18):
        observed = brute(n)
        assert observed == count_formula(n), (n, observed, count_formula(n))
    assert count_formula(7) == 0
    assert all(count_formula(n) > 0 for n in range(8, 121))
    assert [count_formula(n) for n in range(5, 16)] == [15, 3, 0, 8, 3, 15, 11, 3, 13, 14, 18]
    print('PASS: 16-state adjacency, closed-walk count through 120, brute-force squared cycles 5..17')


if __name__ == '__main__':
    run()
