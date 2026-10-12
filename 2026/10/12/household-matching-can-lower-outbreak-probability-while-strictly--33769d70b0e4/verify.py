"""Exact-rational checks for the two-type household-matching SIR example."""
from fractions import Fraction as Q
from math import exp

p = {"AA": Q(19, 20), "BB": Q(1, 100),
     "AB": Q(2, 5), "BA": Q(1, 100)}
beta = {"A": 1, "B": 5}

def pair_pg(a, z):
    """PGF coefficient dictionary for one initial source of type a, partner z."""
    t = p[a + z]
    return {beta[a]: 1 - t, beta[a] + beta[z]: t}

def avg(*d):
    result = {}
    for terms in d:
        for k, v in terms.items():
            result[k] = result.get(k, Q(0)) + v / len(d)
    return result

f0 = avg(pair_pg("A", "A"), pair_pg("B", "B"))
f1 = avg(pair_pg("A", "B"), pair_pg("B", "A"))
assert f0 == {1: Q(1, 40), 2: Q(19, 40),
              5: Q(99, 200), 10: Q(1, 200)}
assert f1 == {1: Q(3, 10), 6: Q(41, 200), 5: Q(99, 200)}
assert sum(f0.values()) == sum(f1.values()) == 1
mean = lambda f: sum(k*v for k, v in f.items())
assert mean(f0) == Q(7, 2)
assert mean(f1) == Q(801, 200)
assert mean(f1) - mean(f0) == Q(101, 200) > 0
assert (1 + Q(4, 5) + (Q(4, 5)**2)/2) == Q(53, 25) > 2
u = Q(1, 2)
upper0 = sum(v*u**k for k,v in f0.items())
upper1 = sum(v*u**k for k,v in f1.items())
assert upper0 == Q(30049, 204800) < Q(1, 5)
assert upper1 == Q(2159, 12800) < Q(1, 5)
# 200(F1-F0)/u == 55-95u+41u**5-u**9; bound on 0<u<=1/2.
poly = {0: Q(55), 1: Q(-95), 5: Q(41), 9: Q(-1)}
for k in set(f0) | set(f1):
    difference = f1.get(k, Q(0)) - f0.get(k, Q(0))
    assert difference == poly.get(k-1, Q(0)) / 200
assert Q(55) - Q(95, 2) - Q(1, 512) == Q(3839, 512) > 0

def f(s, b):
    u = exp(s-1)
    return (1-b)*sum(float(v)*u**k for k,v in f0.items()) + b*sum(float(v)*u**k for k,v in f1.items())

def extinction(b):
    lo, hi = 0.0, 0.2
    assert f(lo,b) > lo and f(hi,b) < hi
    for _ in range(90):
        mid = (lo+hi)/2
        if f(mid,b) > mid:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2

q0, qmid, q1 = extinction(0), extinction(0.5), extinction(1)
assert 0 < q0 < qmid < q1 < .2
print("ILLUSTRATIVE_ROOTS", "b=0", f"{q0:.12f}",
      "b=1/2", f"{qmid:.12f}", "b=1", f"{q1:.12f}")
print("VERIFY_OK")
