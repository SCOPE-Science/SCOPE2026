#!/usr/bin/env python3
"""Exhaustively verify ordered total domination sequence counts on K_m x K_n.

Uses only the defining open-neighborhood rule and direct graph adjacency.
Run: python total_sequence_checker.py [maximum_dim]. Default: 6.
"""
import itertools
import json
import math
import sys
from fractions import Fraction
from functools import lru_cache


def pred(m, n):
    v = [(r, c) for r in range(m) for c in range(n)]
    masks = []
    for r, c in v:
        mask = 0
        for j, (rr, cc) in enumerate(v):
            if rr != r and cc != c:
                mask |= 1 << j
        masks.append(mask)
    return v, masks


def expected(m, n):
    a = m*n*(m-1)*(n-1)*(m-2)*(n-2)
    b = 3*m*n*(m-1)**2*(n-1)**2*(m+n-2)
    c = (math.comb(m,2)*math.comb(n,2)**2
         + math.comb(n,2)*math.comb(m,2)**2
         - math.comb(m,2)*math.comb(n,2))
    d = 3*m*n*(m-1)*(n-1)*(m-2)*(n-2)*(m+n)
    return a, b, c, d


def test(m, n):
    v, masks = pred(m,n)
    size = len(v)
    full = (1 << size) - 1
    totals = {}
    maximal_4_minimal = 0
    maximal_4_nonminimal = 0

    def is_total(ids):
        cover = 0
        for i in ids:
            cover |= masks[i]
        return cover == full

    def explore(path, dominated):
        nonlocal maximal_4_minimal, maximal_4_nonminimal
        legal_extensions = []
        for i in range(size):
            bit = 1 << i
            if (dominated | masks[i]) != dominated:
                assert i not in path
                legal_extensions.append((i, dominated | masks[i]))
        if dominated == full:
            totals[len(path)] = totals.get(len(path), 0) + 1
            if len(path) == 4:
                minimal = all(not is_total(path[:j] + path[j+1:]) for j in range(4))
                if minimal:
                    maximal_4_minimal += 1
                else:
                    maximal_4_nonminimal += 1
            assert not legal_extensions
            return
        if not legal_extensions:
            raise AssertionError(('incomplete maximal sequence', m,n,path))
        for i, new_dominated in legal_extensions:
            explore(path + (i,), new_dominated)

    explore((), 0)
    minfour_count = 0
    for c in itertools.combinations(range(size), 4):
        if is_total(c) and all(not is_total(c[:j] + c[j+1:]) for j in range(4)):
            minfour_count += 1
    @lru_cache(None)
    def online_probability(dom, length):
        if dom == full:
            return Fraction(1 if length == 3 else 0)
        choices = [dom | mask for mask in masks if (dom | mask) != dom]
        assert choices
        return sum((online_probability(new, length + 1) for new in choices), Fraction(0)) / len(choices)

    p3_online = online_probability(0, 0)
    a,b,c,d = expected(m,n)
    p3_formula = Fraction((m-1)*(n-1)*(m-2)*(n-2),(m*n-1)*(m*n-2))
    assert p3_online == p3_formula, (m,n,p3_online,p3_formula)
    assert totals == ({4:b} if not a else {3:a,4:b}), (m,n,totals,a,b)
    assert minfour_count == c, (m,n,minfour_count,c)
    assert maximal_4_minimal == 24*c, (m,n,maximal_4_minimal,24*c)
    assert maximal_4_nonminimal == d, (m,n,maximal_4_nonminimal,d)
    return {'m':m,'n':n,'n_vertices':size,'terminal_3':totals.get(3,0),
            'terminal_4':totals.get(4,0),'minimal_4_sets':minfour_count,
            'ordered_4_minimal':maximal_4_minimal,
            'ordered_4_nonminimal':maximal_4_nonminimal, 'p3_online':str(p3_online), 'p3_uniform_completions':str(Fraction(a,a+b))}


def main():
    maximum = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    allresults = []
    for m in range(2,maximum+1):
        for n in range(m,maximum+1):
            allresults.append(test(m,n))
    print(json.dumps({'tested_unordered_dimensions':len(allresults),
                      'total_terminal_sequences':sum(x['terminal_3']+x['terminal_4'] for x in allresults),
                      'total_ordered_4_sequences':sum(x['terminal_4'] for x in allresults),
                      'cases':allresults},indent=2))

if __name__=='__main__':
    main()
