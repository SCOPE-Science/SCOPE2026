#!/usr/bin/env python3
"""Independent finite checks for a priced directed-cycle first-passage theorem.

The theorem itself is proved analytically in RESULT.md; these finite tests do not
certify all dimensions and prices. No external data or service is required.
"""
import math
import random


def candidate(prices, budget):
    if len(prices) < 3 or min(prices) <= 0 or budget <= 0:
        raise ValueError('Requires at least three strictly positive prices and budget')
    low, high = min(prices), sum(prices)
    for _ in range(110):
        c = (low + high) / 2
        if sum(max(0.0, 1.0 - p / c) for p in prices) < 1.0:
            low = c
        else:
            high = c
    c = (low + high) / 2
    mass = sum(p / math.sqrt(max(p, c)) for p in prices)
    rates = [budget / (mass * math.sqrt(max(p, c))) for p in prices]
    return c, mass, rates, mass * mass / budget


def worst_pair_hitting(rates):
    h = [1 / r for r in rates]
    return sum(h) - min(h)


def verify():
    rng = random.Random(20261030)
    assertions = 0
    examples = [([1., 1., 1.], 1.), ([1., 1., 2.], 1.),
                ([1., 1., 3.], 1.), ([1., 1., 9.], 1.),
                ([1., 1., 100.], 1.), ([1., 2., 3., 4.], 10.),
                ([1., 2., 3., 20.], 0.5),
                ([1., 1., 1., 1.], 2.),
                ([1., 1., 1., 3.], 3.),
                ([1., 1., 1., 4.], 3.),
                ([1., 1., 1., 100.], 3.),
                ([1., 100., 10000., 1e8], 1.)]
    for n in range(3, 11):
        for trial in range(45):
            prices = [10 ** rng.uniform(-1.5, 2) for _ in range(n)]
            if trial % 5 == 0:
                prices[:2] = [1., 1.]
            if trial % 9 == 0:
                prices = [1.] * n
            examples.append((prices, 10 ** rng.uniform(-1, 1)))
    for prices, budget in examples:
        n = len(prices)
        c, mass, rates, goal = candidate(prices, budget)
        assert abs(sum(max(0., 1-p/c) for p in prices) - 1) < 2e-12
        assertions += 1
        assert abs(sum(p*r for p, r in zip(prices, rates))/budget-1) < 2e-11
        assertions += 1
        assert abs(worst_pair_hitting(rates)/goal-1) < 3e-10
        assertions += 1
        lambdas = [max(0, 1-p/c) for p in prices]
        assert abs(sum(lambdas)-1) < 2e-12
        assertions += 1
        h = [1/r for r in rates]
        assert abs(sum((1-l)*t for l,t in zip(lambdas,h))/goal-1) < 3e-10
        assertions += 1
        for j in range(12):
            allocations = [math.exp(rng.uniform(-5,5)) for _ in prices]
            scale = budget / sum(p*r for p,r in zip(prices,allocations))
            competitor = [scale*r for r in allocations]
            assert worst_pair_hitting(competitor) >= goal*(1-2e-10)
            assertions += 1
    assert abs(candidate([1,1,1],1)[3]-6) < 1e-12
    assertions += 1
    assert abs(candidate([1,1,2],1)[3]-8) < 1e-12
    assertions += 1
    assert abs(candidate([1,1,9],1)[3]-(11+6*math.sqrt(2))) < 1e-12
    assertions += 1
    try:
        from scipy.optimize import minimize
    except ImportError:
        print(f'PASS {assertions} deterministic checks; scipy unavailable for optional optimizer comparisons')
        return
    successes = 0
    for trial in range(36):
        n = 3 + trial % 6
        prices = [math.exp(rng.uniform(-1.5,1.5)) for _ in range(n)]
        if trial % 3 == 0:
            prices[0] = prices[1] = min(prices)
        c, mass, rates, value = candidate(prices, 1.)
        h0 = [1/(r*value) for r in rates]
        def objective(h):
            return sum(p/a for p,a in zip(prices,h))
        def derivative(h):
            return [-p/(a*a) for p,a in zip(prices,h)]
        constraints = []
        for k in range(n):
            constraints.append({'type':'ineq',
              'fun':lambda h,k=k:1-sum(h)+h[k],
              'jac':lambda h,k=k:[0. if i==k else -1. for i in range(n)]})
        start = [h*math.exp(rng.uniform(-0.1,0.1)) for h in h0]
        normalization = max(sum(start)-min(start), 1e-15)
        start = [h/normalization*.98 for h in start]
        result = minimize(objective, start, jac=derivative, method='SLSQP',
          constraints=constraints, bounds=[(1e-10,None)]*n,
          options={'maxiter':800,'ftol':1e-10})
        if result.success:
            assert min(1-sum(result.x)+result.x[i] for i in range(n)) > -1e-7
            assert abs(result.fun/(mass*mass)-1)<1e-5
            successes += 1
            assertions += 2
    print(f'PASS {assertions} deterministic checks; {successes}/36 successful independent SLSQP comparisons; non-success flags not treated as impossibility')


if __name__ == '__main__':
    verify()
