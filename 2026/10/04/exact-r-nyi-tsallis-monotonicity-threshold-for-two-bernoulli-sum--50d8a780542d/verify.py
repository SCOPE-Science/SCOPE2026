#!/usr/bin/env python3
import math

def probs(p1, p2):
    return (
        (1.0-p1)*(1.0-p2),
        p1*(1.0-p2)+(1.0-p1)*p2,
        p1*p2,
    )

def power_sum(p1, p2, q):
    return sum(x**q for x in probs(p1, p2))

def renyi(p1, p2, q):
    p = probs(p1, p2)
    if q == 1.0:
        return -sum(x*math.log(x) for x in p if x > 0.0)
    return math.log(sum(x**q for x in p))/(1.0-q)

def phi(u, v, r):
    return (1.0-u)*(u+v)**r + u*(u*v)**r

def rhs_log_derivative(u, v, q):
    r = q - 1.0
    num = phi(u, v, r) - 1.0
    den = (1.0+v)*(1.0 + (u+v)**q + (u*v)**q)
    return q*num/den

def p_from_odds(x):
    return x/(1.0+x)

# Check the exact differentiated formula numerically.
for u in (0.07, 0.2, 0.55, 0.91):
    for v in (0.09, 0.3, 0.7, 0.97):
        p1 = p_from_odds(u)
        for q in (0.25, 0.7, 1.2, 1.6, 2.0):
            h = 1e-6
            p2m = p_from_odds(v-h)
            p2p = p_from_odds(v+h)
            pm = power_sum(p1, p2m, q)
            pp = power_sum(p1, p2p, q)
            numeric = (math.log(pp)-math.log(pm))/(2.0*h)
            exact = rhs_log_derivative(u, v, q)
            assert abs(numeric-exact) < 2e-6, (u, v, q, numeric, exact)

# Check the two convexity regimes on a deterministic grid.
grid = [i/40.0 for i in range(1, 41)]
for u in grid:
    for v in grid:
        for r in (0.0, 0.1, 0.4, 0.75, 1.0):
            assert phi(u, v, r) <= 1.0 + 2e-14
        for r in (-0.9, -0.6, -0.2, -0.05):
            assert phi(u, v, r) >= 1.0 - 2e-14

# Check entropy monotonicity on a p-grid.
for q in (0.15, 0.5, 0.9, 1.0, 1.1, 1.5, 1.9, 2.0):
    for i in range(1, 25):
        p1 = i/50.0
        prev = renyi(p1, 0.01, q)
        for j in range(2, 26):
            p2 = j/50.0
            cur = renyi(p1, p2, q)
            assert cur + 2e-13 >= prev, (q, p1, p2, prev, cur)
            prev = cur

# Representative failures above q=2 near the fair boundary.
for q in (2.1, 2.5, 3.0, 4.0):
    eps = 1e-4
    p1 = 0.5-eps
    h = 2e-7
    left = renyi(p1, 0.5-h, q)
    edge = renyi(p1, 0.5, q)
    assert edge < left, (q, left, edge)

print("VERIFY_OK")
