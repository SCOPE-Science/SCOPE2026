"""Independent finite verification of p-morphisms of powerset-intersection frames."""
from itertools import product
from functools import reduce
from math import factorial


def subsets(n):
    return tuple(range(1, 1 << n))


def p_morphism(table, m, n):
    src, tgt = subsets(m), subsets(n)
    for i, s in enumerate(src):
        fs = table[i]
        for j, t in enumerate(src):
            if s & t and not (fs & table[j]):
                return False
        for y in tgt:
            if fs & y and not any((s & t) and table[j] == y
                                   for j, t in enumerate(src)):
                return False
    return True


def image_map(choice, m):
    return tuple(reduce(int.__or__, (1 << choice[i] for i in range(m) if s & (1 << i)), 0)
                 for s in subsets(m))


def onto(choice, n):
    return set(choice) == set(range(n))


def stirling(m, n):
    memo = {(0, 0): 1}
    def rec(a, b):
        if (a, b) not in memo:
            if a == 0 or b == 0:
                memo[a, b] = 0
            else:
                memo[a, b] = rec(a - 1, b - 1) + b * rec(a - 1, b)
        return memo[a, b]
    return rec(m, n)


def check_exhaustive(m, n):
    target = set(image_map(c, m) for c in product(range(n), repeat=m)
                 if onto(c, n))
    observed = set()
    for table in product(subsets(n), repeat=(1 << m) - 1):
        if p_morphism(table, m, n):
            observed.add(table)
    assert observed == target, (m, n, len(observed), len(target))
    assert len(target) == factorial(n) * stirling(m, n)
    return len(observed), len(subsets(n)) ** len(subsets(m))


def check_constructed():
    total = 0
    for m in range(1, 7):
        for n in range(1, min(m, 4) + 1):
            for choice in product(range(n), repeat=m):
                if not onto(choice, n):
                    continue
                assert p_morphism(image_map(choice, m), m, n)
                total += 1
    return total


def main():
    tests = [(1,1),(1,2),(2,1),(2,2),(2,3),(3,1),(3,2)]
    for m, n in tests:
        count, tested = check_exhaustive(m, n)
        print(f'exhaustive ({m},{n}): {count} bounded morphisms from {tested} maps')
    count = check_constructed()
    print(f'constructed surjections checked: {count}')
    print('ALL_CHECKS_OK')

if __name__ == '__main__':
    main()
