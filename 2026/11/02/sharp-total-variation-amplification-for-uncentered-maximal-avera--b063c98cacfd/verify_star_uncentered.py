"""Exact checks for finite-star uncentered ball maximal variation.

All assertions are integer or rational, and graph balls are enumerated independently
in the direct definition check.  The unrestricted theorem has an analytic proof.
Run: python verify_star_uncentered.py
"""
from fractions import Fraction
from itertools import product


def fast_scaled(t):
    """Return uncentered maximal values relative to the hub in scale 2(k+1)."""
    k = len(t)
    d = 2 * (k + 1)
    whole = 2 * sum(t)
    hub = max(0, (k + 1) * max(t), whole)
    leaf = [max(d*x, (k + 1)*x, whole) for x in t]
    return hub, leaf


def graph_balls(k):
    n = k+1
    def dist(i,j):
        if i == j: return 0
        if i == 0 or j == 0: return 1
        return 2
    balls = {tuple(u for u in range(n) if dist(v,u) <= r)
             for v in range(n) for r in range(3)}
    return [tuple(sorted(b)) for b in balls]


def direct_maximal(f):
    k = len(f)-1
    candidates = graph_balls(k)
    return [max(sum((Fraction(abs(f[u])) for u in b), Fraction(0)) / len(b)
                for b in candidates if v in b)
            for v in range(k+1)]


def exact_grid():
    checked = 0
    witnesses = 0
    for k in range(1,9):
        for t in product((-2,-1,0,1,2), repeat=k):
            h, leaf = fast_scaled(t)
            abs_sum = sum(map(abs, t))
            lhs = sum(abs(x-h) for x in leaf)
            assert lhs <= (k*k-k+2)*abs_sum, (k,t,'global')
            for i,x in enumerate(leaf):
                edge_bound = (k+1)*abs(t[i]) + (k-1)*(abs_sum-abs(t[i]))
                assert abs(x-h) <= edge_bound, (k,t,i,'local')
            checked += 1
        hub, leaves = fast_scaled((1,) + (0,)*(k-1))
        assert sum(abs(x-hub) for x in leaves) == k*k-k+2
        witnesses += 1
    return checked, witnesses


def direct_grid():
    checked = 0
    for k in range(1,7):
        for f in product((0,1,2), repeat=k+1):
            exact = direct_maximal(f)
            d = 2*(k+1)
            h, leaf = fast_scaled(tuple(f[i]-f[0] for i in range(1,k+1)))
            reconstructed = [Fraction(f[0]) + Fraction(h,d)] + [Fraction(f[0]) + Fraction(u,d) for u in leaf]
            assert exact == reconstructed, (k,f,exact,reconstructed)
            checked += 1
    return checked


def rational_witnesses():
    checked = 0
    for k in range(1,101):
        h, leaves = fast_scaled((3,) + (0,)*(k-1))
        assert sum(abs(v-h) for v in leaves) == 3*(k*k-k+2)
        checked += 1
    return checked


if __name__ == '__main__':
    a,b=exact_grid()
    c=direct_grid()
    d=rational_witnesses()
    print(f'PASS: {a} exhaustive normalized configurations (k=1..8), {b} sharp leaf witnesses,')
    print(f'      {c} independent graph-ball evaluations, and {d} further exact witnesses (k=1..100).')
    print('All edgewise and global inequalities were checked using exact integer arithmetic.')
