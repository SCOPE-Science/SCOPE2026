#!/usr/bin/env python3
import math

L = math.log(2.0)

def forcing(n):
    return sum(math.lgamma(math.comb(n, j) + 1.0) for j in range(n))

def kappa(terms=70):
    s = 0.0
    term_power = 1.0
    fact = 1.0
    for n in range(terms):
        if n > 0:
            term_power *= L
            fact *= n
        s += forcing(n) * term_power / fact
    return s

# Exact small automorphism orders for the recursively defined forests H_n.
h = [1]
for n in range(1, 5):
    value = 1
    for j in range(n):
        c = math.comb(n, j)
        value *= math.factorial(c) * h[j]**c
    h.append(value)
assert h[:4] == [1, 1, 2, 288]
assert h[4] == 182601737180282880

K = kappa()
assert abs(K - 0.5656527950551603) < 2e-15

# Logarithmic recurrence and normalized convergence check.
a = [0.0] * 13
rows = []
for n in range(1, 13):
    a[n] = forcing(n) + sum(math.comb(n, j) * a[j] for j in range(n))
    log_aut_free_godel = 2.0 * a[n]
    normalized = (L**(n+1) / math.factorial(n)) * log_aut_free_godel
    rows.append((n, normalized))
assert abs(rows[-1][1] - K) < 5e-9

print('kappa_70 = %.16f' % K)
print('H_orders_n0_to_n4 =', h)
print('normalized_n8_to_n12 =')
for n, value in rows[7:]:
    print('%d %.16f' % (n, value))
print('VERIFY_OK')
