"""Reproduce rectangular templates and optimal two-adjacent-deletion covers.

Only the Python standard library is required. A codeword (a,b,c,d) yields
exactly (c,d), (a,d), (a,b) on deleting two consecutive positions.
The universal lower bound is the elementary three-output counting bound;
this script checks the constructive upper bound, not the abstract proof.
"""
from collections import Counter

TEMPLATES = {
    (2, 2): [(0, 1, 1, 0), (1, 1, 0, 0)],
    (2, 3): [(0, 0, 1, 2), (1, 0, 0, 1)],
    (3, 2): [(0, 1, 2, 0), (1, 0, 2, 1)],
    (3, 3): [(0, 2, 1, 1), (1, 0, 2, 2), (2, 1, 0, 0)],
    (3, 4): [(0, 2, 1, 0), (0, 1, 2, 3), (1, 3, 2, 1), (2, 0, 1, 2)],
    (4, 3): [(0, 1, 2, 0), (1, 1, 3, 0), (2, 1, 1, 2), (3, 1, 0, 2)],
    (4, 4): [(0, 1, 2, 2), (0, 3, 2, 0), (1, 3, 3, 1),
             (2, 1, 1, 3), (3, 3, 1, 0), (3, 3, 1, 2)],
}


def blocks(q):
    assert isinstance(q, int) and q >= 2
    r = q % 3
    if r == 0:
        sizes = [3] * (q // 3)
    elif r == 1:
        sizes = [3] * ((q - 4) // 3) + [4]
    else:
        sizes = [3] * ((q - 2) // 3) + [2]
    result, start = [], 0
    for size in sizes:
        result.append(tuple(range(start, start + size)))
        start += size
    assert start == q
    return result


def code(q):
    out = []
    for rows in blocks(q):
        for cols in blocks(q):
            template = TEMPLATES[len(rows), len(cols)]
            for a, b, c, d in template:
                out.append((rows[a], cols[b], rows[c], cols[d]))
    return out


def outputs(word):
    a, b, c, d = word
    return ((c, d), (a, d), (a, b))


def check():
    for (m, n), template in TEMPLATES.items():
        counts = Counter(w for x in template for w in outputs(x))
        assert len(template) == (m*n + 2)//3
        assert set(counts) == {(i, j) for i in range(m) for j in range(n)}
        assert all(a != c and b != d for a, b, c, d in template)
        assert sum(counts.values()) == 3 * len(template)
        if 3 in (m, n):
            assert set(counts.values()) == {1}
        else:
            assert sorted(counts.values()).count(2) == 2
            assert set(counts.values()) == {1, 2}
    for q in range(2, 101):
        words = code(q)
        assert len(words) == (q*q + 2)//3
        assert len(words) == len(set(words))
        counts = Counter(pair for w in words for pair in outputs(w))
        assert len(counts) == q*q
        assert min(counts.values()) == 1
        assert all(a != c and b != d for a,b,c,d in words)
        if q % 3 == 0:
            assert set(counts.values()) == {1}
        else:
            assert sorted(counts.values()).count(2) == 2
            assert set(counts.values()) == {1, 2}
    print('VERIFY_OK templates=7 q=2..100; exact counts and two-overlap certificates')
    print('SAMPLE', [(q, len(code(q))) for q in range(2, 13)])


if __name__ == '__main__':
    check()
