"""Exact-rational checks of the sharp sketched Galerkin positivity boundary.

Run: python3 verify.py (Python standard library only).
Finite checks corroborate the algebra; the universal result has a written proof.
"""
from fractions import Fraction as Q

checks = 0

def ck(b):
    global checks
    assert b
    checks += 1

# Exact contraction/angle inequality for two extreme eigenvalues, many
# integer vectors, and a wide range of condition numbers.
for low in range(1, 8):
    for high in range(low, 16):
        for a in range(-9, 10):
            for b in range(-7, 8):
                if not (a or b):
                    continue
                n2 = a*a+b*b
                ax = low*a*a+high*b*b
                a2x = low*low*a*a+high*high*b*b
                ck(ax*ax*(low+high)**2 >= 4*low*high*n2*a2x)

# Sharpness for the genuine Krylov subspace span(b,Ab), with b=(q,1,0).
# The following use only rational arithmetic, no floating-point claims.
for q in range(2, 37):
    low, high = Q(1), Q(q*q)
    critical = Q(2*q,q*q+1)
    ck(0 < critical < 1)
    for eps in [Q(0), critical/2, critical, (critical+1)/2, Q(9,10) if Q(9,10)>critical else (critical+1)/2]:
        numerator = 2*q*q - eps*q*(q*q+1)
        denominator = q*q+1-2*eps*q
        ck(denominator > 0)
        if eps < critical:
            ck(numerator > 0)
        elif eps == critical:
            ck(numerator == 0)
        else:
            ck(numerator < 0)
        # generalized Rayleigh quotient identity for W=[[1,-eps],[-eps,1]]
        ck(numerator == q*(q-eps*q*q) + (q*q-eps*q))
        ck(denominator == q*(q-eps) + (1-eps*q))

# One fixed, all-rational compressive 2-by-3 sketch of a 3-by-3 SPD system.
for eps, expected in [(Q(59,100), Q(15,323)), (Q(3,5), Q(0)),(Q(4,5), Q(-15,13))]:
    val = (18 - 30*eps)/(10 - 6*eps)
    ck(val == expected)
    ck(eps < 1)

# Sharp angle equality at |b1|:|b2|=sqrt(L):sqrt(mu), with L=q^2.
for q in range(2,37):
    mu,L=Q(1),Q(q*q)
    x2=Q(q*q+1)
    a=Q(2*q*q)
    ax2=Q(q*q*(q*q+1))
    ck(a*a*(mu+L)**2==4*mu*L*x2*ax2)

# Epsilon-distortion of W=[[1,-eps],[-eps,1]] exactly epsilon.
for eps in [Q(1,10),Q(3,5),Q(4,5),Q(19,20)]:
    for a in range(-6,7):
        for b in range(-6,7):
            val=(a*a+b*b-2*eps*a*b)
            norm=a*a+b*b
            ck((1-eps)*norm<=val<=(1+eps)*norm)

print('EXACT_CHECKS_PASS', checks)
