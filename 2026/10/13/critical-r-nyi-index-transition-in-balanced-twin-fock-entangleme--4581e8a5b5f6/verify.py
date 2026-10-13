"""Reproduce finite-number identities and numerical asymptotic checks for balanced twin-Fock states.
Requires only Python 3 standard library. This is numerical corroboration, not an infinite proof.
"""
from fractions import Fraction
from math import comb, factorial, gamma, lgamma, log, pi, sqrt


def a_exact(m):
    return Fraction(comb(2*m, m), 4**m)


def p_exact(n, k):
    return a_exact(k)*a_exact(n-k)


def p_direct(n, k):
    return Fraction(comb(n,k)**2*factorial(2*k)*factorial(2*n-2*k),
                    4**n*factorial(n)**2)

for n in range(1, 18):
    p = [p_exact(n,k) for k in range(n+1)]
    assert sum(p) == 1
    assert all(p[k] == p_direct(n,k) for k in range(n+1))
    assert max(p) == a_exact(n)
assert [p_exact(2,k) for k in range(3)] == [Fraction(3,8),Fraction(1,4),Fraction(3,8)]


def distribution(n):
    # Forward recurrence is more accurate than taking differences of huge log-gammas.
    a = [1.0]
    for k in range(n):
        a.append(a[-1]*(2*k+1)/(2*k+2))
    return [a[k]*a[n-k] for k in range(n+1)]


def moment(n,q):
    return sum(x**q for x in distribution(n))

n = 20000
p = distribution(n)
assert abs(sum(p)-1) < 1e-10
half_sum = sum(sqrt(x) for x in p)
neg_slope = half_sum**2/n
limit_neg = 4*gamma(0.75)**4/pi**2
assert abs(neg_slope-limit_neg) < 0.004
entropy_shift = -sum(x*log(x) for x in p) - log(n)
assert abs(entropy_shift-log(pi/4)) < 0.01
bulk_half = n**(-0.5) * moment(n,0.5)
expected_half = pi**(-0.5)*gamma(0.75)**2/gamma(1.5)
assert abs(bulk_half-expected_half) < 0.01
critical_n500 = 500*moment(500,2)/log(500)
critical_n20000 = n*moment(n,2)/log(n)
assert abs(critical_n20000-2/pi**2) < abs(critical_n500-2/pi**2)
# For q>2 the edge series is convergent, and its truncations approach from below.
a=1.0
sum3 = 0.0
for k in range(150001):
    sum3 += a**3
    a *= (2*k+1)/(2*k+2)
edge3_approx = 2*pi**(-1.5)*sum3
scaled3 = n**1.5*moment(n,3)
assert abs(scaled3-edge3_approx)/edge3_approx < 0.035
print('VERIFY_OK exact_distribution_n=1..17 mass_normalization=passed endpoint_max=passed')
print('VERIFY_OK negativity_linear_coefficient=%.9f target=%.9f' % (neg_slope,limit_neg))
print('VERIFY_OK entropy_constant=%.9f target=%.9f' % (entropy_shift,log(pi/4)))
print('VERIFY_OK q2_logarithmic_trend=passed q3_edge_scaling=passed')
