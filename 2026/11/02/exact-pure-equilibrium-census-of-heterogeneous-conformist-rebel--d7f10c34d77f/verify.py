#!/usr/bin/env python3
"""Independent exact checks for the cycle equilibrium-census theorem."""
from itertools import product
from math import comb, prod


def segments(word):
    n = len(word)
    indices = [i for i, kind in enumerate(word) if kind == "R"]
    if not indices:
        raise ValueError("A rebel is required")
    return [((indices[(j+1) % len(indices)]-indices[j]-1) % n)
            for j in range(len(indices))]


def run_polynomial(length, z):
    if length == 0:
        return 1
    if length == 1:
        return 0
    return sum(comb(length-2-h, h)*z**h
               for h in range((length-2)//2+1))


def closed_count(word, m):
    assert len(word) >= 3 and m >= 3 and "R" in word
    runs = segments(word)
    if 1 in runs:
        return 0
    b = sum(1 if length == 0 else 2 for length in runs)
    q = m-1
    return q**b*prod(run_polynomial(length, q) for length in runs) + \
        (-1)**b*q*prod(run_polynomial(length, -1) for length in runs)


def direct_best_response(word, profile, m):
    n = len(word)
    for i, kind in enumerate(word):
        neighbours = (profile[(i-1) % n], profile[(i+1) % n])
        def payoff(choice):
            return sum((choice == x) if kind == "C" else (choice != x)
                       for x in neighbours)
        if any(payoff(other) > payoff(profile[i]) for other in range(m)):
            return False
    return True


def local_best_response(word, profile):
    n = len(word)
    return all((profile[i] in (profile[(i-1)%n], profile[(i+1)%n]))
               if kind == "C" else
               (profile[i] != profile[(i-1)%n]
                and profile[i] != profile[(i+1)%n])
               for i, kind in enumerate(word))


def run():
    direct_cases = 0
    local_cases = 0
    evaluated_direct_profiles = 0
    evaluated_local_profiles = 0
    for m, nmax in ((3, 8), (4, 6), (5, 5)):
        for n in range(3, nmax + 1):
            for word in product("CR", repeat=n):
                if "R" not in word:
                    continue
                predicted = closed_count(word, m)
                count = 0
                for profile in product(range(m), repeat=n):
                    count += direct_best_response(word, profile, m)
                    evaluated_direct_profiles += 1
                assert count == predicted, (word, m, count, predicted)
                direct_cases += 1
    for m, nmax in ((3, 9), (4, 7)):
        for n in range(3, nmax+1):
            for word in product("CR", repeat=n):
                if "R" not in word:
                    continue
                predicted = closed_count(word, m)
                count = sum(local_best_response(word, profile)
                            for profile in product(range(m), repeat=n))
                evaluated_local_profiles += m**n
                assert count == predicted, (word, m, count, predicted)
                local_cases += 1
    for r in range(1, 9):
        assert closed_count("RCCCC"*r, 3) == 12**r
    for left, right in [((0,2,3,4),(0,3,2,4)), ((2,2,3,4),(2,3,2,4))]:
        for m in range(3, 8):
            assert closed_count(''.join('R'+'C'*l for l in left),m) == \
                closed_count(''.join('R'+'C'*l for l in right),m)
    print('VERIFY_OK direct_cases=%d direct_profiles=%d local_cases=%d local_profiles=%d periodic_r=1..8 arrangement_pairs=2' %
          (direct_cases,evaluated_direct_profiles,local_cases,evaluated_local_profiles))

if __name__ == "__main__":
    run()
