"""Independent executable checks for the stated deletion-code construction and dual bound.
Requires Python 3.9 or later, standard library only.
"""
from itertools import combinations


def outputs(ones, n):
    w = ['0'] * n
    for i in ones:
        w[i] = '1'
    return {''.join(w[:i] + w[i + 1:]) for i in range(n)}


def proposed(n):
    left = [(i, i+1) for i in range(0, n-1, 2)]
    bridge = [(i+1, i+4) for i in range(0, n-4, 4)]
    return left + bridge


def chosen_adjacent_starts(n):
    # The n-1 adjacent input pairs form the vertices of a path.
    starts = list(range(0, n-2, 2))
    covered = {v for p in starts for v in (p, p+1)}
    if n-2 not in covered:
        starts.append(n-3)
    assert len(starts) == (n-1+1)//2
    assert {v for p in starts for v in (p,p+1)} == set(range(n-1))
    return starts


def dual_outputs(n):
    m = n-1
    chosen = set()
    for i in range(m):
        y = ['0'] * m
        y[i] = '1'
        chosen.add(''.join(y))
    for p in chosen_adjacent_starts(n):
        y = ['0'] * m
        y[p] = y[p+1] = '1'
        chosen.add(''.join(y))
    return chosen


def run():
    for n in range(3, 121):
        C = proposed(n)
        assert len(set(C)) == len(C)
        assert len(C) == (3*n-2)//4, (n,C)
        seen = {}
        for c in C:
            for s in outputs(c,n):
                assert s not in seen, (n, c, seen.get(s), s)
                seen[s] = c
        U = dual_outputs(n)
        assert len(U) == n-1 + n//2
        assert (len(U)//2) == (3*n-2)//4
        if n <= 65:
            for c in combinations(range(n),2):
                assert len(outputs(c,n) & U)>=2, (n,c,outputs(c,n)&U)
    print('PASS: construction n=3..120, dual cover n=3..65, exact bound every tested n')


if __name__ == '__main__':
    run()
