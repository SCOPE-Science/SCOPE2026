#!/usr/bin/env python3
import math


def close(a, b, tol=1e-12):
    return abs(a-b) <= tol * max(1.0, abs(a), abs(b))

# One-step identity from native Model J and the published conjugacy.
for r0, h, p in [(5.0, 1.2, 0.3), (2.7, 0.4, 1.1), (7.0, 3.0, 0.05)]:
    x = r0*h/(1.0+h)
    h_next = math.exp(-p)*x
    assert close(x, math.exp(p)*h_next)

# Finite-cycle algebra: x_j = exp(p_j) h_{j+1}, with cyclic indexing.
h = [0.8, 1.1, 0.6, 1.4]
p = [0.2, 0.5, 0.1, 0.35]
alpha = 0.9
k = len(h)
x = [math.exp(p[j])*h[(j+1) % k] for j in range(k)]
Lambda_A = alpha**k * math.prod(h)
Lambda_J = alpha**k * math.prod(x)
assert close(Lambda_J, math.exp(sum(p))*Lambda_A)

pbar = sum(p)/k
alpha_A_c = math.prod(h)**(-1.0/k)
alpha_J_c = math.prod(x)**(-1.0/k)
assert close(alpha_J_c, math.exp(-pbar)*alpha_A_c)
assert alpha_J_c < alpha_A_c

print('VERIFY_OK')
