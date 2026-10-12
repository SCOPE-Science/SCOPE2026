#!/usr/bin/env python3
import math

def simpson(f, a, b, n):
    if n % 2:
        n += 1
    h = (b-a)/n
    total = f(a) + f(b)
    for i in range(1, n):
        total += (4.0 if i % 2 else 2.0) * f(a+i*h)
    return total*h/3.0

def entropy_binary(w):
    ans = 0.0
    if w > 0.0:
        ans -= w*math.log(w)
    if w < 1.0:
        ans -= (1.0-w)*math.log(1.0-w)
    return ans

# d=2,p=2.  W=sin^2(theta) turns the Beta(1/2,1/2) law
# into a uniform angular integral with density 2/pi.
N = 120000
def kappa_integrand(theta):
    w = math.sin(theta)**2
    return math.sqrt(entropy_binary(w)/2.0)

kappa = (2.0/math.pi)*simpson(kappa_integrand, 0.0, math.pi/2.0, N)
assert abs(kappa - 0.40611684414) < 3e-10, kappa

# Here R^2~Beta(1,1/2), so P(R^2>1-z)=sqrt(z) exactly.
def one_obs_tail(t):
    q = 2.0-t
    def integrand(theta):
        w = math.sin(theta)**2
        u1 = math.sqrt(w)
        u2 = math.sqrt(1.0-w)
        A = u1**q + u2**q
        r2 = A**(-2.0/q)
        z = max(0.0, 1.0-r2)
        return math.sqrt(z)
    return (2.0/math.pi)*simpson(integrand, 0.0, math.pi/2.0, N)

ratios = []
for t in (1e-2, 1e-3, 1e-4):
    ratios.append(one_obs_tail(t)/math.sqrt(t))
assert abs(ratios[-1]-kappa) < 2e-5, (ratios, kappa)
assert abs(ratios[-1]-kappa) < abs(ratios[0]-kappa)

# Deterministic checks of z_t/t -> H(W)/p for general directions.
tests = [
    (3.0, [0.2, 0.3, 0.5]),
    (4.5, [0.1, 0.2, 0.3, 0.4]),
    (2.7, [0.55, 0.45]),
]
for p, W in tests:
    t = 1e-7
    alpha = 1.0-t/p
    A = sum(w**alpha for w in W)
    z = 1.0 - A**(-p/(p-t))
    H = -sum(w*math.log(w) for w in W)
    target = H/p
    assert abs(z/t-target) < 3e-7, (p,W,z/t,target)

print(
    "VERIFY_OK "
    f"kappa_2_2={kappa:.10f} "
    f"tail_ratios={ratios[0]:.10f},{ratios[1]:.10f},{ratios[2]:.10f}"
)
