#!/usr/bin/env python3
from itertools import combinations, permutations


def compositions(n):
    return [(a, b, n-a-b) for a in range(n+1) for b in range(n-a+1)]


def inter(x, y):
    return sum(min(a, b) for a, b in zip(x, y))


def valid(fam):
    return all(inter(x, y) <= 2 for x, y in combinations(fam, 2))


def heavy(x):
    return {i for i, a in enumerate(x) if a >= 3}


def no_five(n):
    pts = compositions(n)
    for fam in combinations(pts, 5):
        if valid(fam):
            raise AssertionError(f"unexpected five-word code at n={n}: {fam}")


def main():
    w5 = [(5,0,0),(0,5,0),(0,0,5),(2,2,1)]
    w6 = [(6,0,0),(0,6,0),(0,0,6),(2,2,2)]
    assert valid(w5) and valid(w6)

    no_five(5)
    no_five(6)

    hf5 = {x for x in compositions(5) if not heavy(x)}
    expected5 = set(permutations((2,2,1)))
    assert hf5 == expected5
    assert all(inter(x,y) > 2 for x,y in combinations(hf5,2))

    hf6 = [x for x in compositions(6) if not heavy(x)]
    assert hf6 == [(2,2,2)]

    for n in range(7,31):
        assert all(heavy(x) for x in compositions(n))
        constants=[(n,0,0),(0,n,0),(0,0,n)]
        assert valid(constants)

    print('VERIFY_OK')


if __name__ == '__main__':
    main()
