"""Finite independent checks of a priced one-way-cycle hitting-time theorem.

Only standard-library modules are used. The universal assertion relies on the
proof, not on these finite tests.
"""
from fractions import Fraction as F
from math import sqrt, isclose
from random import Random


def exact_threshold(costs):
    costs = sorted(F(c) for c in costs)
    n = len(costs)
    for k in range(2, n+1):
        theta = sum(costs[:k], F(0)) / (k-1)
        if costs[k-1] < theta and (k == n or theta <= costs[k]):
            return theta
    raise AssertionError('threshold not found')


def optimized(costs):
    theta = float(exact_threshold(costs))
    lengths = [sqrt(max(float(c), theta)) for c in costs]
    z = sum(float(c) / s for c, s in zip(costs, lengths))
    rates = [1.0 / (z*s) for s in lengths]
    probs = [max(0., 1. - float(c)/theta) for c in costs]
    return theta, z, rates, probs


def hitting_formula(rates):
    n = len(rates)
    return [[0 if a == b else sum(1/rates[i] for i in _range(a,b,n))
             for b in range(n)] for a in range(n)]


def _range(a,b,n):
    i = a
    while i != b:
        yield i
        i = (i+1) % n


def hitting_poisson_exact(rates):
    n = len(rates)
    out = [[F(0) for j in range(n)] for i in range(n)]
    for target in range(n):
        inds = [i for i in range(n) if i != target]
        mat = []
        for i in inds:
            row = []
            for j in inds:
                row.append((rates[i] if i == j else F(0)) -
                           (rates[i] if j == (i+1) % n else F(0)))
            mat.append(row + [F(1)])
        for p in range(n-1):
            q = next(j for j in range(p,n-1) if mat[j][p] != 0)
            mat[p], mat[q] = mat[q], mat[p]
            div = mat[p][p]
            mat[p] = [x/div for x in mat[p]]
            for j in range(n-1):
                if j == p: continue
                mul = mat[j][p]
                mat[j] = [x-mul*y for x,y in zip(mat[j],mat[p])]
        for i,j in enumerate(inds): out[j][target] = mat[i][-1]
    return out


def run():
    rng = Random(91024)
    n_exact = n_poisson = n_random = 0
    for n in range(3, 10):
        for _ in range(55):
            costs = [F(rng.randint(1, 45), rng.randint(1, 8)) for i in range(n)]
            theta = exact_threshold(costs)
            assert sum((max(F(0), F(1)-c/theta) for c in costs), F(0)) == F(1)
            active = [i for i,c in enumerate(costs) if c < theta]
            assert len(active)>=2
            assert all(c/(F(1)-max(F(0),F(1)-c/theta))==theta for c in costs if c<theta)
            assert all(c>=theta for c in costs if c>=theta)
            n_exact += 1
    for n in range(3, 8):
        for _ in range(20):
            c = [F(rng.randint(1, 12)) for i in range(n)]
            arbitrary = [F(rng.randint(1, 15), rng.randint(1, 6)) for i in range(n)]
            budget = sum((a*b for a,b in zip(c,arbitrary)),F(0))
            rates=[a/budget for a in arbitrary]
            hit = hitting_poisson_exact(rates)
            closed = hitting_formula(rates)
            assert hit == closed
            assert max(max(row) for row in hit) == sum(1/x for x in rates) - min(1/x for x in rates)
            n_poisson += 1
    ex_costs=[F(1),F(3),F(100)]
    theta,z,r,q=optimized(ex_costs)
    assert theta==4.0 and z==12.0
    assert r == [1/24,1/24,1/120]
    assert abs(max(max(row) for row in hitting_formula(r))-144)<1e-9
    for n in range(3, 14):
        for _ in range(165):
            c = [10**rng.uniform(-2,2) for i in range(n)]
            theta,z,r,q=optimized(c)
            budget=sum(x*y for x,y in zip(c,r))
            val=sum(1/x for x in r)-min(1/x for x in r)
            assert isclose(budget,1,rel_tol=2e-12)
            assert isclose(val,z*z,rel_tol=2e-12)
            assert isclose(sum(q),1,rel_tol=2e-12)
            assert all(0<=t<1 for t in q)
            # Feasible randomized price reallocations, not a global proof.
            perturb=[x*10**rng.uniform(-0.8,0.8) for x in r]
            scale=sum(a*b for a,b in zip(c,perturb))
            perturb=[p/scale for p in perturb]
            test=sum(1/p for p in perturb)-min(1/p for p in perturb)
            assert test + 2e-10 >= val
            n_random+=1
    print('VERIFY_OK',n_exact,'exact dual KKT threshold systems;',n_poisson,
          'independent exact Markov hitting systems;',n_random,
          'normalized feasible price comparisons; proof remains analytic')


if __name__=='__main__': run()
