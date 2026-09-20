from itertools import combinations


def parity_dot(a: int, u: int) -> int:
    return (a & u).bit_count() & 1


def prescribed_order(m: int):
    # Binary-coordinate vectors e1,e2,e1+e2,e3,e4,e3+e4.
    prefix = [1, 2, 3, 4, 8, 12]
    remaining = [v for v in range(1, 1 << m) if v not in prefix]
    return prefix + remaining


def verify(m: int):
    N = 1 << m
    n = N - 1
    vectors = prescribed_order(m)
    assert len(vectors) == n
    assert len(set(vectors)) == n

    rows = []
    for u in range(N):
        xs = [1 if parity_dot(v, u) == 0 else -1 for v in vectors]
        s = 0
        max_abs = 0
        for x in xs:
            s += x
            max_abs = max(max_abs, abs(s))
        rows.append((xs, s, max_abs))

    # Symmetric Rademacher marginals.
    for i in range(n):
        assert sum(xs[i] for xs, _, _ in rows) == 0

    # Exact pairwise independence: each sign pair occurs N/4 times.
    for i, j in combinations(range(n), 2):
        table = {(a, b): 0 for a in (-1, 1) for b in (-1, 1)}
        for xs, _, _ in rows:
            table[(xs[i], xs[j])] += 1
        assert set(table.values()) == {N // 4}

    maximal_count = sum(max_abs >= 2 for _, _, max_abs in rows)
    terminal_count = sum(abs(s) >= 2 for _, s, _ in rows)
    terminal_values = sorted(s for _, s, _ in rows)

    assert maximal_count == N
    assert terminal_count == 1
    assert terminal_values == [-1] * (N - 1) + [n]

    return n, maximal_count, terminal_count


if __name__ == "__main__":
    print("m n maximal_count/2^m terminal_count/2^m ratio")
    for m in range(4, 10):
        n, a, b = verify(m)
        print(f"{m} {n} {a}/{1<<m} {b}/{1<<m} {a//b}")
