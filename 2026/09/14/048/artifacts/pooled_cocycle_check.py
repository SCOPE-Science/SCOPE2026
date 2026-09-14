"""Support check: pooled C([0,1],T)-valued categorical 2-cocycle identity.

Model: single-vertex 2-graph degrees in N^2. Homotopy
  w_t(x, y) = exp(i * t * (x[1] * y[0])),  x=(m1,n1), y=(m2,n2),
i.e. phase n1*m2. This is a normalized 2-cocycle of the monoid N^2 for
every t, giving a categorical 2-cocycle c_t on any 2-graph via
c_t(lam, mu) = w_t(d(lam), d(mu)) with pointwise (in fact Lipschitz)
t-dependence. We verify:
  (a) 2-cocycle identity at every t on a grid, for random degree triples;
  (b) normalization; (c) pointwise continuity / Lipschitz bound in t;
  (d) pooled identity: for each triple, the C([0,1],T)-valued identity
      holds uniformly over the t-grid (sup norm of defect ~ 0).
Writes pooled_cocycle_check_results.json next to this script.
"""
import cmath
import json
import math
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))


def w(t, x, y):
    return cmath.exp(1j * t * (x[1] * y[0]))


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def cocycle_defect(t, x, y, z):
    lhs = w(t, x, y) * w(t, add(x, y), z)
    rhs = w(t, x, add(y, z)) * w(t, y, z)
    return abs(lhs - rhs)


def main():
    rng = random.Random(20260914)
    degs = [(rng.randint(0, 6), rng.randint(0, 6)) for _ in range(40)]
    tgrid = [k / 20.0 for k in range(21)]
    max_defect = 0.0
    for _ in range(4000):
        x, y, z = rng.choice(degs), rng.choice(degs), rng.choice(degs)
        t = rng.choice(tgrid)
        d = cocycle_defect(t, x, y, z)
        max_defect = max(max_defect, d)
        assert d < 1e-12, (t, x, y, z, d)
    # uniform over grid per triple (pooled identity)
    worst_pooled = 0.0
    for _ in range(1500):
        x, y, z = rng.choice(degs), rng.choice(degs), rng.choice(degs)
        worst_t = max(cocycle_defect(t, x, y, z) for t in tgrid)
        worst_pooled = max(worst_pooled, worst_t)
        assert worst_t < 1e-12
    # normalization
    for _ in range(500):
        x = rng.choice(degs)
        t = rng.choice(tgrid)
        assert abs(w(t, (0, 0), x) - 1.0) < 1e-12
        assert abs(w(t, x, (0, 0)) - 1.0) < 1e-12
    # Lipschitz continuity in t: |w_t - w_s| <= |phase| * |t - s|
    worst_lip = 0.0
    for _ in range(3000):
        x, y = rng.choice(degs), rng.choice(degs)
        t = rng.random()
        s = rng.random()
        phase = x[1] * y[0]
        quot = abs(w(t, x, y) - w(s, x, y)) / max(abs(t - s), 1e-12)
        assert quot <= phase + 1e-9, (x, y, t, s, quot)
        worst_lip = max(worst_lip, quot)
    results = {
        "model": "single-vertex 2-graph, c_t(lam,mu)=exp(i*t*n(lam)*m(mu))",
        "triples_checked": 4000,
        "pooled_triples_checked": 1500,
        "t_grid": tgrid,
        "max_cocycle_defect": max_defect,
        "worst_pooled_defect_over_grid": worst_pooled,
        "worst_lipschitz_quotient": worst_lip,
        "status": "PASS",
    }
    with open(os.path.join(HERE, "pooled_cocycle_check_results.json"), "w") as f:
        json.dump(results, f, indent=2)
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
