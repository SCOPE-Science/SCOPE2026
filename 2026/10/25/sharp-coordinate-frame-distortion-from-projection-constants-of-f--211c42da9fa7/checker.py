"""Reproducible finite-dimensional checks for a hyperplane projection comparison.

Analytical proof, not this finite checker, establishes the universal theorem.
"""
from fractions import Fraction
from random import Random
from math import isclose
from scipy.optimize import linprog


def exact_invariants(weights):
    a = [Fraction(x) for x in weights]
    assert all(x >= 0 for x in a) and sum(a) == 1
    top = max(a)
    delta = max(Fraction(1), (1-top)/top)
    if top >= Fraction(1,2):
        projection = Fraction(1)
    else:
        projection = Fraction(1) + 1/sum(x/(1-2*x) for x in a if x)
    assert projection < 2
    assert delta <= projection/(2-projection)
    equal = top >= Fraction(1,2) or all(x == top for x in a if x)
    assert (delta == projection/(2-projection)) == equal
    return projection, delta


def lp_minimal_projection(weights):
    a = [float(v) for v in weights if v]
    n = len(a)
    if n == 1:
        return 1.0
    # Variables: projection factors t_i, their absolute values p_i,
    # absolute deviations q_i, and common row-norm upper bound L.
    size = 3*n+1
    rows, limits = [], []
    def impose(terms, limit):
        row = [0.0]*size
        for idx, coeff in terms:
            row[idx] += coeff
        rows.append(row)
        limits.append(limit)
    for i, ai in enumerate(a):
        impose([(i,1),(n+i,-1)],0)
        impose([(i,-1),(n+i,-1)],0)
        impose([(i,-1),(2*n+i,-1)],-1)
        impose([(i,1),(2*n+i,-1)],1)
        impose([(2*n+i,1),(n+i,(1-ai)/ai),(3*n,-1)],0)
    eq = [[1.0]*n+[0.0]*(2*n+1)]
    obj = [0.0]*(3*n)+[1.0]
    bounds = [(None,None)]*n + [(0,None)]*(2*n+1)
    out = linprog(obj,A_ub=rows,b_ub=limits,A_eq=eq,b_eq=[1],bounds=bounds,method='highs')
    assert out.success, out.message
    return float(out.fun)


def main():
    probes = 0
    for n in range(3,14):
        weights = [Fraction(1,n)]*n
        lam, delta = exact_invariants(weights)
        assert lam == 2-Fraction(2,n) and delta == n-1
        probes += 1
    r = Random(51471)
    for n in range(2,13):
        for _ in range(90):
            vals = [r.randint(0,35) for j in range(n)]
            if not sum(vals):
                vals[0] = 1
            weights = [Fraction(v,sum(vals)) for v in vals]
            lam, delta = exact_invariants(weights)
            numerical = lp_minimal_projection(weights)
            assert isclose(numerical,float(lam),rel_tol=1.e-9,abs_tol=1.e-9), (weights,numerical,lam)
            probes += 1
    print(f'Passed {probes} exact-inequality and LP-optimization checks.')

if __name__ == '__main__':
    main()
