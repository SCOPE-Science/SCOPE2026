"""Exact rational sample checks for the local escape Lyapunov estimate.

The analytic proof (not this finite test) establishes the theorem for all
quadratically small perturbations.
"""
from fractions import Fraction as Q
from itertools import product

# A particular smooth perturbation in each branch.  The norm-1 coefficient
# sum is less than C=4, so both remainders obey |E_i| <= C s^2.
C = Q(4)
alpha = Q(1, 3)
delta_pairs = [(Q(2, 3), Q(-5, 4)), (Q(-2, 3), Q(5, 4)),
               (Q(2, 3), Q(5, 4)), (Q(-2, 3), Q(-5, 4))]
D = max(abs(d) for ds in delta_pairs for d in ds)
lam = 12 * C + 2
B = 6 * C + 2 * lam * D * D + 1
A = 6 * C + 1
eta = min(Q(1, 10000), alpha / (2 * B), Q(1, 2 * A))
# eta<1/10000 also gives 54*lambda*C*C*eta**2 <= 1.
assert 54 * lam * C * C * eta * eta <= 1


def V(x, y):
    return x + y - lam * y * y


def F(x, y, mu, delta_l, delta_r):
    d = delta_l if x <= 0 else delta_r
    c = -alpha if x <= 0 else alpha
    e1 = x*x/Q(3) - y*y/Q(5) + x*y/Q(7) + mu*mu/Q(11)
    e2 = -x*y/Q(4) + y*y/Q(6) + mu*x/Q(8)
    return ((1 + d + c)*x + y + mu + e1,
            -d*x + e2)


count = 0
for dl, dr in delta_pairs:
    for mu_fraction in [Q(1, 5), Q(1, 2), Q(3, 4), Q(1)]:
        mu = mu_fraction * eta
        for ix, iy in product(range(-10, 11), repeat=2):
            x = eta * Q(ix, 11)
            y = eta * Q(iy, 11)
            if x*x + y*y > eta*eta:
                continue
            xn, yn = F(x, y, mu, dl, dr)
            drift = V(xn, yn) - V(x, y)
            assert drift >= mu/Q(2), (x, y, mu, dl, dr, drift)
            count += 1
print(f"PASS {count} exact-fraction local drift tests; lambda={lam}, eta={eta}")
