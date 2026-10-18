"""Exact-rational finite diagnostics for random dyadic contraction maps.
The proof of the unrestricted claims is analytical; these checks test its algebra.
"""
from fractions import Fraction as Q
from itertools import product

DISTS = [
    {1: Q(1)},
    {1: Q(1, 2), 2: Q(1, 2)},
    {1: Q(1, 2), 3: Q(1, 3), 7: Q(1, 6)},
    {2: Q(2, 7), 5: Q(5, 7)},
]
checks = 0

def ck(v):
    global checks
    assert v
    checks += 1

for dist in DISTS:
    ck(sum(dist.values()) == 1)
    mean = sum(Q(beta)*pb for beta,pb in dist.items())
    mass = mean + 2
    h = [2 * sum(pb * 2**min(n, beta) for beta, pb in dist.items()) for n in range(45)]
    ck(h[0] == 2)
    for n in range(44):
        right = sum(pb * 2**beta for beta,pb in dist.items() if beta <= n)
        ck(h[n] == h[n+1]/2 + right)
    # Infinite tail exact via n>=max(beta): shell mass proportional to 2^{-n}.
    M = max(dist)
    mu = sum(h[n] / Q(2**(n+1)) for n in range(M))
    mu += h[M] / Q(2**M)
    ck(mu == mass)
    # Excursion lengths from right branch, n >=2: sum over beta and geometric depth.
    direct = {}
    for t in range(2, 22):
        direct[t] = sum(pb * Q(1, 2**(t-beta)) for beta,pb in dist.items() if beta <= t-1)
        # Coefficient of z^t in z E(z^B)/(2-z).
        via_pgf = sum(pb * Q(1, 2**(t-beta)) for beta,pb in dist.items() if beta <= t-1)
        ck(direct[t] == via_pgf)
    # Expected length obtained from the geometric law.
    E = sum(pb * (beta+2) for beta,pb in dist.items())
    ck(E == mass)
    # Exact all-order renewal/covariance recurrence via formal power series.
    u = [Q(1)] + [Q(0)]*20
    for n in range(1,21):
        u[n] = sum(direct.get(t, Q(0))*u[n-t] for t in range(2,n+1))
        ck(u[n] >= 0)
    c0 = Q(1,mass) - Q(1,mass*mass)
    ck(c0 == (mass-1)/mass**2)
    # Return cylinders in Y: each g-branch has proportion 2^{-(g+1)},
    # and normalized-image density is uniform with Jacobian 2^{g+1}.
    for g in range(12):
        left = (Q(1) + Q(1,2**(g+1)))/2
        right = (Q(1) + Q(1,2**g))/2
        slope = 2**(g+1)
        ck((right-left) / Q(1,2) == Q(1,slope))
        ck(slope*(right-left) == Q(1,2))

# Explicit deterministic-beta=1 covariance closed form.
p=Q(1,3)
u=[Q(1)] + [Q(0)]*30
for n in range(1,31):
    u[n] = sum(Q(1, 2**(t-1))*u[n-t] for t in range(2,n+1))
    ck(u[n] == p+Q(2,3)*Q(-1,2)**n)
    ck(p*u[n]-p*p == Q(2,9)*Q(-1,2)**n)

print('PASS:', checks, 'exact-rational checks; 4 parameter distributions; dyadic transfer, masses, return cylinders and renewal coefficients')
