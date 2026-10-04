#!/usr/bin/env python3
import math

TARGET_A = 0.15547370036108804519
TARGET_F = 0.79393344459717058364

def li2(z):
    assert 0.0 <= z < 1.0
    total = 0.0
    power = z
    for n in range(1, 20000):
        add = power / (n*n)
        total += add
        if abs(add) < 1e-17:
            return total
        power *= z
    raise RuntimeError("dilog series did not converge")

def kkt_residual_b(b):
    z = 2*b/(1+b)
    f = li2(z)/(2*b)
    derivative_value = math.log((1+b)/(1-b))/(2*b*(1+b))
    return f - derivative_value

def solve_b():
    lo, hi = 0.80, 0.90
    flo, fhi = kkt_residual_b(lo), kkt_residual_b(hi)
    assert flo > 0 and fhi < 0
    for _ in range(100):
        mid = (lo+hi)/2
        fm = kkt_residual_b(mid)
        if fm > 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2

def limiting_integral(a):
    # t = 1-exp(-s), so -log(1-t) = s and dt = exp(-s) ds.
    # The remaining tail after S is bounded by a constant times (S+1)e^{-S}.
    S = 40.0
    N = 200000
    if N % 2:
        N += 1
    h = S/N
    b = 1-a
    def integrand(s):
        e = math.exp(-s)
        return s*e/(a + 2*b*(1-e))
    acc = integrand(0.0) + integrand(S)
    for i in range(1, N):
        acc += (4 if i % 2 else 2) * integrand(i*h)
    return acc*h/3

def finite_expectation(k, a):
    beta = 2*(1-a)
    lam = beta/(k-1)
    total = 0.0
    for j in range(1, k+1):
        A = a*j + lam*(j*(j-1)/2 + j*(k-j))
        if j == 1:
            term = 1.0/A
        else:
            # log of C(k-1,j-1) * j^(j-2) * lam^(j-1) * (j-1)! / A^j
            logterm = (
                math.lgamma(k) - math.lgamma(k-j+1)
                + (j-2)*math.log(j)
                + (j-1)*math.log(lam)
                - j*math.log(A)
            )
            term = math.exp(logterm)
        total += term
    return total

b = solve_b()
a = 1-b
f_from_kkt = li2(2*b/(1+b))/(2*b)
f_from_integral = limiting_integral(a)

assert abs(a - TARGET_A) < 2e-13, (a, TARGET_A)
assert abs(f_from_kkt - TARGET_F) < 2e-13, (f_from_kkt, TARGET_F)
assert abs(f_from_integral - TARGET_F) < 2e-9, (f_from_integral, TARGET_F)

ks = [20, 50, 100, 200, 500]
vals = [finite_expectation(k, a) for k in ks]
assert all(vals[i] > vals[i+1] for i in range(len(vals)-1))
assert all(v > TARGET_F for v in vals)
assert abs(vals[-1] - TARGET_F) < 0.0010

print("a_star=%.15f" % a)
print("F_star=%.15f" % f_from_integral)
for k, v in zip(ks, vals):
    print("k=%d E_k=%.15f gap=%.15f" % (k, v, v-TARGET_F))
print("VERIFY_OK")
