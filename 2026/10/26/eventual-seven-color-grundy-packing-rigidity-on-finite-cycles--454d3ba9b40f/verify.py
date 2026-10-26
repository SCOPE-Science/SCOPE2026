"""Standalone exact checks of cyclic first-fit packing colorings.

Run: python3 verify.py
Uses only the Python standard library.
"""

SEEDS = {
    22: (7,1,2,1,5,3,1,2,4,1,2,5,1,3,1,2,6,1,4,2,1,3),
    23: (7,1,2,3,1,5,2,1,4,3,1,2,5,1,3,2,1,6,1,4,2,1,3),
    24: (7,1,2,3,1,5,2,1,3,4,1,2,1,5,1,3,1,2,6,1,4,2,1,3),
    26: (7,2,1,3,5,1,2,4,1,3,2,1,4,2,1,5,1,3,2,1,6,3,1,2,4,1),
    27: (7,2,1,3,5,1,2,1,4,3,1,2,1,4,3,1,2,5,1,2,1,6,3,1,2,4,1),
    28: (7,3,1,2,4,1,6,1,2,3,1,5,2,1,4,2,1,3,1,4,1,2,1,5,3,1,2,1),
    29: (7,3,1,2,4,1,6,1,2,3,1,5,2,1,3,4,1,2,1,3,1,4,2,1,5,1,3,2,1),
    30: (7,1,2,3,1,5,1,2,1,4,2,1,3,2,1,4,3,1,2,5,1,3,1,2,6,1,4,2,1,3),
    31: (7,3,1,2,4,1,6,1,2,3,1,5,2,1,4,1,3,1,2,1,3,2,1,4,2,1,5,1,3,2,1),
}
CUTS = {28: 18, 29: 16, 30: 13, 31: 17}
BLOCK = (1, 2, 1, 3)


def dist(n, a, b):
    d = abs(a-b)
    return min(d, n-d)


def check_direct(word):
    """Test packing and lower-color witnesses by full pairwise comparisons."""
    n = len(word)
    assert min(word) == 1 and max(word) == 7
    for v, color in enumerate(word):
        for u in range(n):
            if u != v and word[u] == color:
                assert dist(n, u, v) > color, (n, u, v, color)
        for smaller in range(1, color):
            assert any(word[u] == smaller and dist(n, u, v) <= smaller
                       for u in range(n)), (n, v, color, smaller)
    # Independent reproduction by processing vertices in nondecreasing
    # output colors and evaluating the original first-fit rule at each vertex.
    already = []
    for v in sorted(range(n), key=lambda i: (word[i], i)):
        available = next(
            color for color in range(1, 8)
            if all(word[u] != color or dist(n, u, v) > color for u in already)
        )
        assert available == word[v], (n, v, available, word[v])
        already.append(v)


def extended(seed_length, k):
    w = SEEDS[seed_length]
    cut = CUTS[seed_length]
    return w[:cut] + BLOCK*k + w[cut:]


def main():
    for n, word in SEEDS.items():
        assert len(word) == n
        check_direct(word)
    cases = 0
    for n in CUTS:
        for k in (0, 1, 2, 3, 4, 5, 10, 25):
            check_direct(extended(n, k))
            cases += 1
    print('VERIFICATION_OK seeds=9 extension_cases=%d largest_length=%d direct_pairwise_and_first_fit=PASS' %
          (cases, max(len(extended(n, 25)) for n in CUTS)))


if __name__ == '__main__':
    main()
