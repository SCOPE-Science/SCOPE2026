#!/usr/bin/env python3
import math

def simpson(f, a, b, n):
    if n % 2:
        n += 1
    h = (b-a)/n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4.0 if i % 2 else 2.0) * f(a+i*h)
    return s*h/3.0

def A(w):
    return 1.0 + w*math.expm1(w)

N = 200000
L = simpson(lambda w: 1.0/A(w), 0.0, 1.0, N)
target = 0.7323592996919
assert abs(L-target) < 5e-13, (L,target)
assert L < math.pi/4.0 < 0.8

for j in range(1001):
    w = j/1000.0
    a = A(w)
    assert 1.0 - 1e-15 <= a <= math.e + 1e-15

# Check the exact finite-n upper-strip integral against numerical x-integration.
for w in (0.0, 0.17, 0.51, 0.83, 1.0):
    a = A(w)
    for n in (1, 2, 5, 20, 100):
        exact = (1.0 - (1.0-a/math.e)**n)/a
        # Integrate after u=e^{-x}: n * int_0^{1/e} (1-a*u)^{n-1} du.
        numeric = simpson(
            lambda u: n*((1.0-a*u)**(n-1)),
            0.0, 1.0/math.e, 20000
        )
        assert abs(exact-numeric) < 2e-11, (w,n,exact,numeric)

print(f"VERIFY_OK limit={L:.12f} pi_over_4={math.pi/4:.12f}")
