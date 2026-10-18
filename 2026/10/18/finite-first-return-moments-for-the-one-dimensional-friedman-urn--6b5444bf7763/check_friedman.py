"""Exact finite checks for the Friedman-walk first-return theorem.

Use Python >=3.9; no external libraries. This is supplementary finite
verification, not a certificate of the all-time survival theorem.
"""
from fractions import Fraction as F
from math import comb, sqrt

checks = 0

def verify(condition):
    global checks
    assert condition
    checks += 1

# Survivors at time 1: the initial white draw is deterministic.
alive = {1: F(1)}
survival = {1: F(1)}
weighted = {1: F(1)}
first_return = {}
for n in range(1, 21):
    nxt = {}
    hit = F(0)
    for x, mass in alive.items():
        plus = F(n + 2 - x, 2 * (n + 1))
        minus = 1 - plus
        verify(F(0) <= plus <= F(1, 2))
        verify(F(1, 2) <= minus <= 1)
        verify(plus - minus == F(1 - x, n + 1))
        nxt[x + 1] = nxt.get(x + 1, F(0)) + mass * plus
        if x == 1:
            hit += mass * minus
        else:
            nxt[x - 1] = nxt.get(x - 1, F(0)) + mass * minus
    alive = nxt
    survival[n + 1] = sum(alive.values(), F(0))
    weighted[n + 1] = sum(x * mass for x, mass in alive.items())
    first_return[n + 1] = hit
    verify((n + 1) * weighted[n + 1] == n * weighted[n] + survival[n])
    verify(n * weighted[n] == 1 + sum((survival[k] for k in range(1, n)), F(0)))
    verify(survival[n + 1] <= survival[n])
    verify(first_return[n + 1] == survival[n] - survival[n + 1])
    verify(sum(alive.values(), F(0)) + sum(first_return.values(), F(0)) == 1)

# A separate enumeration from urn draw counts, independent of the above
# time/position transition kernel.
paths = {(1, 0): F(1)}
for n in range(1, 11):
    verify(sum(paths.values(), F(0)) == survival[n])
    verify(sum((w-b) * p for (w,b),p in paths.items()) == weighted[n])
    new_paths = {}
    for (w, b), mass in paths.items():
        p_white = F(b + 1, w + b + 1)
        verify(p_white == F(n + 2 - (w - b), 2 * (n + 1)))
        new_paths[w + 1, b] = new_paths.get((w + 1, b), F(0)) + mass * p_white
        if w > b + 1:
            new_paths[w, b + 1] = new_paths.get((w, b + 1), F(0)) + mass * (1 - p_white)
    paths = new_paths

# Reflection identity for an absorbing symmetric walk.
def law_symmetric(m):
    return {2 * j - m: F(comb(m, j), 2 ** m) for j in range(m + 1)}

def q_absorbing(m, x):
    d = {x: F(1)}
    for _ in range(m):
        nd = {}
        for y, p in d.items():
            nd[y + 1] = nd.get(y + 1, F(0)) + p / 2
            if y > 1:
                nd[y - 1] = nd.get(y - 1, F(0)) + p / 2
        d = nd
    return sum(d.values(), F(0))
for m in range(1, 16):
    for x in range(1, 9):
        refl = sum((mass for y,mass in law_symmetric(m).items() if -x < y <= x), F(0))
        verify(q_absorbing(m, x) == refl)
        verify(float(refl) <= min(1, 2*x/sqrt(m)) + 1e-12)

# The exact survivor bound for the observed finite prefix.
def survival_from(time, initial_x, steps):
    law = {initial_x: F(1)}
    for n in range(time, time + steps):
        nxt = {}
        for x, mass in law.items():
            plus = F(n + 2 - x, 2 * (n + 1))
            nxt[x + 1] = nxt.get(x + 1, F(0)) + mass * plus
            if x > 1:
                nxt[x - 1] = nxt.get(x - 1, F(0)) + mass * (1 - plus)
        law = nxt
    return sum(law.values(), F(0))

for n in range(2, 11):
    # Compare from the start with the simple walk.
    verify(survival[n] <= q_absorbing(n-1, 1))
for time in range(1, 9):
    for x in range(1, time + 1, 2):
        for m in range(1, 9):
            verify(survival_from(time, x, m) <= q_absorbing(m, x))

print(f"PASS: {checks} exact/reproducible finite assertions")
print("First-return masses:", [(n, str(first_return[n])) for n in range(2, 11, 2)])
print("Survivals:", [(n, str(survival[n])) for n in range(1, 11)])
