"""Independent arithmetic checks for the finite-parameter Radon-plane envelope.

Run with Python 3 (standard library only). This checks representative identities,
scalar inequalities, and a hexagonal witness; the analytic proof is in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt, log

CHECKS = 0

def check(pred, tag):
    global CHECKS
    CHECKS += 1
    if not pred:
        raise AssertionError(f"{tag} (check {CHECKS})")


def hn(a, b):
    return max(abs(a), abs(b), abs(a - b))


def root(t):
    low, high = 0.5, 1.0
    for _ in range(100):
        mid = (low + high) / 2
        d = (1-mid)*(1+mid)**(t-1)-mid
        if d > 0:
            low = mid
        else:
            high = mid
    return (low+high)/2


def profile(t, tau):
    return ((1+(1+tau)**t)/2)**(2/t)/(1+tau*tau)


# The exact hexagonal pair x=(1,0), y=(0,1) has chord lengths (1,1+tau).
for i in range(1001):
    tau = F(i, 1000)
    check(hn(F(1), tau) == 1, "hex positive chord")
    check(hn(F(1), -tau) == 1+tau, "hex negative chord")
    check(hn(F(1), F(i-500, 100)) >= 1, "Birkhoff orthogonality")

# Explicit sample of the convex majorization used in the theorem, exactly rational
# for four integer powers and many possible chord pairs (A,B).
for i in range(21):
    tau = F(i,20)
    for j in range(21):
        a = F(1)+tau*F(j,20)
        b = F(2)+tau-a
        for order in (1,2,3,4,5):
            check(a**order+b**order <= 1+(1+tau)**order,
                  "power-mean endpoint majorization")

# Critical equation and sampled global uniqueness of the scalar maximum.
for t in (1, 1.5, 2, 3, 4, 8, 16):
    tau = root(t)
    check(abs((1-tau)*(1+tau)**(t-1)-tau)<1e-12,
          "critical equation")
    check(profile(t,tau)>=profile(t,0)-1e-12 and
          profile(t,tau)>=profile(t,1)-1e-12, "boundary maximum")
    for i in range(101):
        check(profile(t,tau)+1e-12>=profile(t,i/100),
              "grid consistency of scalar maximum")

# Exact t=2 golden-ratio algebra.
g = (sqrt(5)-1)/2
check(abs(root(2)-g)<1e-14, "quadratic maximizer")
check(abs(profile(2,g)-(3+sqrt(5))/4)<1e-14, "golden ratio value")
check(profile(2,g)>1.25, "strict high-order increase")

# First-order large-power asymptotic; numerical checks are illustrative only.
for t in (30, 40, 60, 100, 150):
    z = t*(2-profile(t,1.0))
    check(0 < z < 4*log(2), "boundary lower profile")
    check(abs(z-4*log(2)) < 9/t, "coarse asymptotic consistency")

print(f"PASS: {CHECKS} deterministic finite checks (not an infinite proof)")
