"""Exhaustive finite verification of the matching-deleted biclique theorem.

Python 3 standard library only. No finite run substitutes for the general proof.
"""
from collections import Counter
from itertools import combinations
from math import comb


def zero_forces(a, b, t, I, J):
    """Direct implementation of the ordinary blue-vertex colour-change rule."""
    white_a, white_b = set(I), set(J)
    while True:
        gained_a, gained_b = set(), set()
        for i in range(a):
            if i not in white_a:
                seen = {j for j in white_b if not (i == j and i < t)}
                if len(seen) == 1:
                    gained_b |= seen
        for j in range(b):
            if j not in white_b:
                seen = {i for i in white_a if not (i == j and j < t)}
                if len(seen) == 1:
                    gained_a |= seen
        if not (gained_a or gained_b):
            return not white_a and not white_b
        white_a -= gained_a
        white_b -= gained_b


def characterization(t, I, J):
    if len(I) > 2 or len(J) > 2:
        return False
    i_star = set(I).intersection(range(t))
    j_star = set(J).intersection(range(t))
    if (len(I) == 2 and not i_star) or (len(J) == 2 and not j_star):
        return False
    return not (len(I) == len(J) == 2 and i_star == j_star)


def predicted_histogram(a, b, t):
    pa = comb(a, 2) - comb(a-t, 2)
    pb = comb(b, 2) - comb(b-t, 2)
    equal = t*(a-t)*(b-t) + comb(t, 2)
    order = a + b
    return {order: 1,
            order - 1: order,
            order - 2: a*b + pa + pb,
            order - 3: b*pa + a*pb,
            order - 4: pa*pb - equal}


def main():
    cases, examined = 0, 0
    for a in range(3, 8):
        for b in range(3, 8):
            if a+b > 14:
                continue
            for t in range(0, min(a, b)+1):
                observed = Counter()
                for x in range(a+1):
                    for I in combinations(range(a), x):
                        for y in range(b+1):
                            for J in combinations(range(b), y):
                                obtained = zero_forces(a, b, t, I, J)
                                expected = characterization(t, I, J)
                                assert obtained == expected, (a,b,t,I,J,obtained,expected)
                                examined += 1
                                if obtained:
                                    observed[a+b-x-y] += 1
                expected_counts = predicted_histogram(a, b, t)
                for k in range(a+b+1):
                    assert observed[k] == expected_counts.get(k, 0), (a,b,t,k,observed[k],expected_counts.get(k,0))
                cases += 1
    print(f"VERIFY_OK cases={cases} initial_colourings={examined} (3<=a,b<=7, a+b<=14, all t)")


if __name__ == '__main__':
    main()
