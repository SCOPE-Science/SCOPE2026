"""Exact finite checks of the perfect-matching / optimal-committee correspondence.

Usage: python3 CHECK.py
Requires only the Python 3 standard library. Finite checks supplement the proof.
"""
from fractions import Fraction
from itertools import combinations, permutations
from math import comb


def graph(n, shifts):
    assert len(set(shifts)) == 3
    assert all(0 <= s < n for s in shifts)
    return tuple(sorted((i, (i + s) % n) for i in range(n) for s in shifts))


def score(n, edges, selected, rule):
    deg = [0] * (2*n)
    for idx in selected:
        i, j = edges[idx]
        deg[i] += 1
        deg[n+j] += 1
    return sum((rule[d] for d in deg), Fraction())


def permanent_by_permutations(n, edges):
    allowed = set(edges)
    return sum(all((i,p[i]) in allowed for i in range(n)) for p in permutations(range(n)))


def run():
    total_checked = 0
    graphs = 0
    reports = []
    rules = (
        ('PAV', (Fraction(0), Fraction(1), Fraction(3,2), Fraction(11,6))),
        ('coverage', (Fraction(0), Fraction(1), Fraction(1), Fraction(1))),
        ('strict-sublinear-1', (Fraction(0), Fraction(1), Fraction(3,2), Fraction(5,2))),
        ('strict-sublinear-2', (Fraction(0), Fraction(3), Fraction(5), Fraction(17,2))),
    )
    assert all(rule[0] == 0 and rule[1] > 0 and
               rule[2] < 2*rule[1] and rule[3] < 3*rule[1]
               for _, rule in rules)
    for n in range(3, 7):
        patterns = [(0, 1, 2)]
        if n >= 4:
            patterns += [(0,1,3),(0,2,3)]
        if n >= 5:
            patterns += [(0,1,n-1)]
        for shifts in patterns:
            edges = graph(n, shifts)
            assert len(edges) == 3*n
            assert len(set(edges)) == 3*n
            assert all(sum(i==a for i, _ in edges) == 3 for a in range(n))
            assert all(sum(j==b for _, j in edges) == 3 for b in range(n))
            winners = 0
            maxima = {name: Fraction(-1) for name, _ in rules}
            for subset in combinations(range(len(edges)), n):
                perfect = len({edges[e][0] for e in subset}) == n and len({edges[e][1] for e in subset}) == n
                for name, rule in rules:
                    actual = score(n, edges, subset, rule)
                    bound = 2*n*rule[1]
                    assert (actual == bound) == perfect, (name, n, shifts, subset, actual)
                    assert actual <= bound
                    maxima[name] = max(maxima[name], actual)
                winners += perfect
                total_checked += 1
            permanent = permanent_by_permutations(n, edges)
            assert winners == permanent, (n, shifts, winners, permanent)
            assert all(maxima[name] == 2*n*rule[1] for name,rule in rules)
            reports.append((n, shifts, winners, comb(3*n, n)))
            graphs += 1
    assert reports[0][:3] == (3,(0,1,2),6)
    print('PASS exact-combinatorial-score check')
    print('graphs', graphs, 'committees', total_checked, 'exact rule evaluations', total_checked*len(rules))
    for report in reports:
        print('size, shifts, PAV-winner/permanent count, committees:',*report)

if __name__ == '__main__':
    run()
