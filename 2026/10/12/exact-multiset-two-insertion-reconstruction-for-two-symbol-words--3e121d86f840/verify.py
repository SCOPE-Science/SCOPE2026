"""Exact finite-alphabet symbol-pattern certificate for two-insertion multiset intersections.

Run: python3 verify.py. Python standard library only.
All infinite-alphabet assertions in the accompanying proof reduce to 13 symbolic
patterns; the q=2,...,6 direct checks are independent finite spot checks.
"""
from itertools import combinations, product

EXPECTED = {
    (0, 0, 0, 1): (2, 11, 8),
    (0, 0, 1, 0): (2, 11, 8),
    (0, 0, 1, 1): (2, 6, 0),
    (0, 0, 1, 2): (3, 6, 0),
    (0, 1, 0, 0): (2, 11, 8),
    (0, 1, 0, 2): (3, 18, 8),
    (0, 1, 1, 0): (2, 10, 8),
    (0, 1, 1, 1): (2, 11, 8),
    (0, 1, 1, 2): (3, 12, 4),
    (0, 1, 2, 0): (3, 12, 4),
    (0, 1, 2, 1): (3, 18, 8),
    (0, 1, 2, 2): (3, 6, 0),
    (0, 1, 2, 3): (4, 6, 0),
}


def patterns(n):
    if not n:
        yield ()
        return
    for previous in patterns(n-1):
        for k in range(max(previous, default=-1)+2):
            yield previous + (k,)


def multiplicity(center, word):
    return sum(tuple(word[i] for i in ij) == tuple(center)
               for ij in combinations(range(4), 2))


def intersection(x, z, q):
    return sum(min(multiplicity(x, y), multiplicity(z, y))
               for y in product(range(q), repeat=4))


def main():
    all_patterns = [p for p in patterns(4) if p[:2] != p[2:]]
    assert len(all_patterns) == len(EXPECTED) == 13
    assert set(all_patterns) == set(EXPECTED)
    for p in all_patterns:
        s, expected_c, expected_e = EXPECTED[p]
        assert s == max(p)+1
        center_x, center_z = p[:2], p[2:]
        c = intersection(center_x, center_z, s)
        # Exactly one outside letter, represented by the new symbol s.
        e = sum(min(multiplicity(center_x, y), multiplicity(center_z, y))
                for y in product(range(s+1), repeat=4)
                if y.count(s) == 1)
        assert (c, e) == (expected_c, expected_e), (p,c,e)
        for q in (s, s+1, s+2, s+4):
            assert intersection(center_x,center_z,q) == c+(q-s)*e, (p,q)

    for q in range(2,7):
        centers = list(product(range(q), repeat=2))
        top, winners = -1, []
        for x, z in combinations(centers, 2):
            score = intersection(x,z,q)
            if score > top:
                top,winners = score,[(x,z)]
            elif score == top:
                winners.append((x,z))
        assert top == 8*q-5, (q,top)
        assert len(winners) == 2*q*(q-1), (q,len(winners))
        for x,z in winners:
            assert (x[0]==x[1] and z[0]!=z[1] and x[0] in z) or \
                   (z[0]==z[1] and x[0]!=x[1] and z[0] in x), (q,x,z)
    print('VERIFY_OK: 13 complete equality patterns, symbolic one-outsider coefficients, q=2..6 direct pair census')


if __name__ == '__main__':
    main()
