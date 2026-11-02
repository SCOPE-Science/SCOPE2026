"""Independent finite tests for a sparse-seed zero-forcing theorem on path powers."""
from collections import Counter
from itertools import product
from math import exp


def actually_forces(n, k, seed):
    colored = {i for i in range(n) if seed >> i & 1}
    while True:
        target = None
        for i in sorted(colored):
            white = [j for j in range(max(0, i-k), min(n, i+k+1))
                     if j not in colored]
            if len(white) == 1:
                target = white[0]
                break
        if target is None:
            return len(colored) == n
        colored.add(target)


def first_force_or_total(n, k, seed):
    colored = {i for i in range(n) if seed >> i & 1}
    if len(colored) == n:
        return True
    for i in colored:
        if sum(j not in colored for j in range(max(0, i-k), min(n, i+k+1))) == 1:
            return True
    return False


def motif_count(n, k):
    motifs = set()
    for center in range(k, n-k):
        whole = set(range(center-k, center+k+1))
        for omitted in whole - {center}:
            motifs.add(frozenset(whole - {omitted}))
    return len(motifs)


def bad_probability_for_square(n, p):
    # A second method: a weighted finite-state scan of seed strings.
    def left(s):
        return not ((s[0] == 1 and s[1]+s[2] == 1) or
                    (s[1] == 1 and s[0]+s[2]+s[3] == 2))
    def right(s):
        return not ((s[2] == 1 and s[0]+s[1]+s[3] == 2) or
                    (s[3] == 1 and s[1]+s[2] == 1))
    states = {s: p**sum(s)*(1-p)**(4-sum(s))
              for s in product((0, 1), repeat=4) if left(s)}
    for length in range(5, n+1):
        update = {}
        for s, weight in states.items():
            for bit in (0, 1):
                # Test the newly completed interior radius-two neighborhood.
                if s[2] == 1 and s[0]+s[1]+s[3]+bit == 3:
                    continue
                successor = s[1:] + (bit,)
                update[successor] = update.get(successor, 0.0) + weight*(p if bit else 1-p)
        states = update
    return sum(value for s, value in states.items() if right(s))


def main():
    comparisons = 0
    for k in (1, 2, 3, 4):
        for n in range(k+2, 13 if k <= 2 else 12):
            for seed in range(1 << n):
                assert actually_forces(n, k, seed) == first_force_or_total(n, k, seed), (n, k, seed)
                comparisons += 1
    print('INITIAL_FORCE_EQUIVALENCE_OK', comparisons)
    tests = 0
    for k in (1, 2, 3, 4, 5):
        for n in (2*k+1, 2*k+2, 3*k+7, 4*k+13):
            target = (2*k-1)*(n-2*k)+1
            assert motif_count(n,k) == target, (n,k)
            tests += 1
    print('DISTINCT_MOTIF_CENSUS_OK', tests)
    for n in (500, 2000, 10000):
        p = n**(-.25)
        exact = 1.0 - bad_probability_for_square(n, p) + p**n
        print('SQUARE_RANDOM_PROBABILITY', n, round(exact, 7),
              'limiting', round(1-exp(-3), 7))
        assert 0 < exact < 1
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
