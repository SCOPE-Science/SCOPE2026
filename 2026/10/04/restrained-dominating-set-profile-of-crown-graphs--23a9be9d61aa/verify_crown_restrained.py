#!/usr/bin/env python3
from math import comb


def crown(n):
    nbr = [set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                nbr[i].add(n+j)
                nbr[n+j].add(i)
    return nbr


def is_restrained_dominating(nbr, D):
    D = set(D)
    C = set(range(len(nbr))) - D
    return all((nbr[v] & D) and (nbr[v] & C) for v in C)


def profile_criterion(n, D):
    D = set(D)
    I = {i for i in range(n) if i not in D}
    J = {j for j in range(n) if n+j not in D}
    if not I and not J:
        return True
    a, b = len(I), len(J)
    if not (1 <= a <= n-1 and 1 <= b <= n-1):
        return False
    universe = set(range(n))
    if a == 1 and next(iter(I)) in J:
        return False
    if a == n-1 and next(iter(universe-I)) in J:
        return False
    if b == 1 and next(iter(J)) in I:
        return False
    if b == n-1 and next(iter(universe-J)) in I:
        return False
    return True


def expected_profile(n, a, b):
    if (a, b) == (0, 0):
        return 1
    if not (1 <= a <= n-1 and 1 <= b <= n-1):
        return 0
    ba = a in (1, n-1)
    bb = b in (1, n-1)
    if not ba and not bb:
        return comb(n, a) * comb(n, b)
    if ba and not bb:
        return n * comb(n-1, b)
    if not ba and bb:
        return n * comb(n-1, a)
    if (a, b) == (1, 1):
        return n * (n-1)
    if (a, b) == (n-1, n-1):
        return n
    return 0


def main():
    subset_checks = criterion_checks = coefficient_checks = minimum_checks = 0
    valid_sets = 0
    for n in range(3, 10):
        nbr = crown(n)
        counts = {}
        by_size = {}
        minimum_sets = []
        for mask in range(1 << (2*n)):
            D = {v for v in range(2*n) if (mask >> v) & 1}
            actual = is_restrained_dominating(nbr, D)
            predicted = profile_criterion(n, D)
            subset_checks += 1
            criterion_checks += 1
            if actual != predicted:
                raise AssertionError((n, sorted(D), actual, predicted))
            if actual:
                valid_sets += 1
                a = sum(i not in D for i in range(n))
                b = sum(n+j not in D for j in range(n))
                counts[(a, b)] = counts.get((a, b), 0) + 1
                by_size[len(D)] = by_size.get(len(D), 0) + 1
        for a in range(n+1):
            for b in range(n+1):
                coefficient_checks += 1
                if counts.get((a, b), 0) != expected_profile(n, a, b):
                    raise AssertionError(('profile', n, a, b, counts.get((a,b),0), expected_profile(n,a,b)))
        gamma = min(by_size)
        minimum_checks += 1
        if gamma != 2 or by_size[2] != n:
            raise AssertionError(('minimum', n, gamma, by_size.get(2)))
        expected_min = {frozenset((i, n+i)) for i in range(n)}
        actual_min = set()
        for i in range(2*n):
            for j in range(i+1, 2*n):
                if is_restrained_dominating(nbr, {i, j}):
                    actual_min.add(frozenset((i, j)))
        if actual_min != expected_min:
            raise AssertionError(('minimum sets', n))
    print(f'VERIFY_OK n_range=3..9 subset_checks={subset_checks} criterion_checks={criterion_checks} valid_sets={valid_sets} coefficient_checks={coefficient_checks} minimum_checks={minimum_checks} max_order=18')


if __name__ == '__main__':
    main()
