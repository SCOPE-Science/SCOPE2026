from math import comb, factorial, perm


def union_cover(t, s, m):
    counts = [1] + [0] * t
    orders = factorial(s)
    for _ in range(m):
        next_counts = [0] * (t + 1)
        for u, count in enumerate(counts):
            for j in range(max(0, s - u), min(s, t - u) + 1):
                next_counts[u + j] += count * comb(t - u, j) * comb(u, s - j) * orders
        counts = next_counts
    return counts[t]


def exclusion_cover(t, s, m):
    return sum((-1) ** j * comb(t, j) * perm(t - j, s) ** m for j in range(t + 1))


def main():
    comparisons = 0
    for r in range(3, 9):
        s = r - 1
        for m in range(2, 7):
            n = 1 + m * s
            for q in range(r + 1, n + 2):
                actual = union_cover(q - 1, s, m)
                assert actual == exclusion_cover(q - 1, s, m), (r, m, q)
                assert (actual > 0) == (q <= n), (r, m, q)
                if q == n:
                    assert q * actual == factorial(n), (r, m, q)
                comparisons += 1
    print(f"INTERMEDIATE_COVER_CHECK cases={comparisons} PASS")


if __name__ == "__main__":
    main()
