#!/usr/bin/env python3
"""Independent numeric consistency tests for two-boundary-zero Hardy approximation.

Only standard-library arithmetic is required. Finite tests are not a proof of
uniqueness or of the continuum asymptotic statements.
"""
import cmath
import math

passed = 0

def check(condition, description):
    global passed
    if not condition:
        raise AssertionError(description)
    passed += 1

def finite_scaled_error(N, c):
    if c == 0:
        return 2 * (2 * N - 1) / (N + 1)
    theta = c / N
    if not (0 < theta <= math.pi):
        raise ValueError("Outside angular domain")
    # Geometric sum, phase-centered to reduce cancellation.
    S = cmath.exp(0.5j * (N - 1) * theta) * math.sin(0.5 * N * theta) / math.sin(0.5 * theta)
    x = S / N
    return 2 * (1 - x.real) / (1 - abs(x)**2)

def limiting_error(c):
    if c == 0:
        return 4.0
    return 2 * c * (c - math.sin(c)) / (c*c - 2 + 2 * math.cos(c))

def critical_derivative_numerator(c):
    return (-c**3*math.cos(c) + 3*c*c*math.sin(c)
            + 6*c*math.cos(c) - 6*c + 2*math.sin(c) - math.sin(2*c))

def solve(A, b):
    n = len(b)
    A = [list(row) + [b[i]] for i,row in enumerate(A)]
    for j in range(n):
        pivot = max(range(j,n), key=lambda i: abs(A[i][j]))
        A[j],A[pivot] = A[pivot],A[j]
        div = A[j][j]
        for k in range(j,n+1):
            A[j][k] /= div
        for i in range(n):
            if i != j:
                v = A[i][j]
                for k in range(j,n+1):
                    A[i][k] -= v*A[j][k]
    return [A[i][-1] for i in range(n)]

def direct_squared_error(n, theta):
    a = cmath.exp(-1j * theta)
    f = [1, -(1+a), a]
    N = n + 3
    C = [[f[k-j] if 0 <= k-j <= 2 else 0j for j in range(n+1)]
         for k in range(N)]
    gram = [[sum(C[k][i].conjugate()*C[k][j] for k in range(N))
             for j in range(n+1)] for i in range(n+1)]
    rhs = [C[0][i].conjugate() for i in range(n+1)]
    p = solve(gram,rhs)
    r = [(1 if k == 0 else 0) - sum(C[k][j]*p[j] for j in range(n+1))
         for k in range(N)]
    return sum(abs(v)**2 for v in r)

for n in range(0,8):
    N=n+3
    for theta in (0,0.09,0.3,0.8,1.4,2.5,math.pi):
        expected = finite_scaled_error(N,N*theta)/N
        measured = direct_squared_error(n,theta)
        check(abs(expected-measured) < 2e-8,
              f"finite Gram vs direct inverse: n={n}, theta={theta}")

for N in (100,300,1000,3000):
    for c in (0.0,0.4,1.0,2.0,math.pi,5.5,2*math.pi,7.54031418959,
              8.7,3*math.pi,4*math.pi,17.0):
        check(abs(finite_scaled_error(N,c)-limiting_error(c)) < 24/N,
              f"critical limit N={N}, c={c}")

lo,hi=7.0,8.2
for _ in range(90):
    mid=(lo+hi)/2
    if critical_derivative_numerator(mid)<0:
        lo=mid
    else:
        hi=mid
cstar=(lo+hi)/2
check(abs(critical_derivative_numerator(cstar))<1e-9,"stationary root")
check(abs(cstar-7.5403141895947865)<2e-11,"root location")
check(abs(limiting_error(cstar)-1.7912691607609164)<2e-11,"minimum value")

for k in range(1,10001):
    c=k/100
    check(limiting_error(c)>=limiting_error(cstar)-5e-13,
          f"grid lower bound at {c}")

for m in range(1,7):
    tlo=m*math.pi+1e-7
    thi=(m+0.5)*math.pi-1e-7
    for _ in range(65):
        tmid=(tlo+thi)/2
        if math.tan(tmid)-tmid<0:tlo=tmid
        else:thi=tmid
    root=2*(tlo+thi)/2
    for frac in (.1,.3,.5,.7,.9):
        left=2*m*math.pi+frac*(root-2*m*math.pi)
        right=root+frac*(2*(m+1)*math.pi-root)
        check(limiting_error(left)<2,"beating window")
        check(limiting_error(right)>2,"outside beating window")

print(f"PASS: {passed} finite consistency assertions")
print(f"c_star={cstar:.15f}; F(c_star)={limiting_error(cstar):.15f}")
