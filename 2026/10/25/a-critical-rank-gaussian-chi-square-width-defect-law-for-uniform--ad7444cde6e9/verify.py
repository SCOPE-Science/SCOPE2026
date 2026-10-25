#!/usr/bin/env python3
"""Finite support checks and diagnostics for Gaussian spherical widths.

Run with: python3 verify.py
Only Python standard library required. Random tests are finite diagnostics,
not substitutes for the all-dimensional proof.
"""
from itertools import combinations
import math
import random

ROOT = math.sqrt(2 / math.pi)


def support_fast(g, rank):
    return sum(sorted((z for z in g if z > 0), reverse=True)[:rank])


def support_vertices(g, rank):
    n = len(g)
    return max(sum(g[i] for i in inds)
               for r in range(rank + 1)
               for inds in combinations(range(n), r))


def widths_and_defect(g, rank):
    norm = math.sqrt(sum(x*x for x in g))
    pos = sorted(x for x in g if x > 0)
    neg = sorted(-x for x in g if x < 0)
    surplus_pos = max(0, len(pos) - rank)
    surplus_neg = max(0, len(neg) - rank)
    defect = (sum(pos[:surplus_pos]) + sum(neg[:surplus_neg])) / norm
    full_width = sum(abs(x) for x in g) / norm
    rank_width = (support_fast(g,rank) + support_fast([-x for x in g],rank)) / norm
    return full_width, rank_width, defect, len(pos)


def predicted(n, rank, count):
    c = (rank - n/2) / math.sqrt(n)
    z = (2*count-n) / math.sqrt(n)
    return ((max(0,z/2-c)**2 + max(0,-z/2-c)**2) / ROOT)


def run():
    rng = random.Random(20261020)
    exact = 0
    for n in range(2, 9):
        for k in range(1, n+1):
            for _ in range(40):
                g = [rng.gauss(0, 1) for __ in range(n)]
                a = support_fast(g, k)
                b = support_vertices(g, k)
                assert abs(a-b) < 1e-11, (n,k,a,b)
                wc, wp, loss, count = widths_and_defect(g,k)
                assert abs(wc-wp-loss)<1e-10
                assert (loss < 1e-13) == (n-k <= count <= k)
                exact += 1
    print('EXACT_SUPPORT_PASS', 'cases=', exact)
    for c in (0.0, 0.75, -0.75):
        errors = []
        for n in (256, 1024, 4096):
            k = max(1, min(n, round(n/2 + c * math.sqrt(n))))
            es=[]
            for _ in range(120):
                g=[rng.gauss(0,1) for __ in range(n)]
                wc,wp,defect,b=widths_and_defect(g,k)
                assert defect>=-1e-12
                es.append(abs(math.sqrt(n)*defect-predicted(n,k,b)))
            errors.append(sum(es)/len(es))
        print('ASYMPTOTIC_DIAGNOSTIC', 'c=', c,
              'MAE_256_1024_4096=', [round(x,6) for x in errors])
        assert errors[-1] < 0.25, (c,errors)
    assert abs((1 - 3/math.pi)-0.04507034144862795)<1e-12
    print('CHECKER_PASS cube_variance=', round(1 - 3/math.pi,12),
          'balanced_defect_mean_limit=',round(1/(4*ROOT),12))

if __name__ == '__main__':
    run()
