"""Supplementary finite numerical checks for the homogeneous Hankel power/resolvent theorem.

No numerical test here substitutes for the analytic infinite-dimensional proof.
Run: python3 verify_power_resolvent.py
"""
import math

PI = math.pi
COUNT = 0


def logcosh(t):
    t = abs(t)
    return t - math.log(2.0) + math.log1p(math.exp(-2.0*t))


def log_constant(a):
    a = abs(a)
    c = PI*a
    return (math.log(PI) + math.log(math.sinh(c)) - math.log(a))/2.0


def log_phi(a, s):
    return log_constant(a) - 0.5*(logcosh(PI*s)+logcosh(PI*(s-a)))


def log_power_exact(a, n):
    assert n >= 1 and a != 0
    c = PI*abs(a)
    return (n*log_constant(a) - logcosh(c*n/2)
            - sum(logcosh(c*(n-2*j)/2) for j in range(1,n)))


def log_power_at(a, n, s):
    return sum(log_phi(a, s-k*a) for k in range(n))


def logsumexp(values):
    m = max(values)
    return m + math.log(sum(math.exp(x-m) for x in values))


# Reproduce the power multiplier directly, including negative oscillation.
for a in [-2.0,-0.7,-0.12,0.12,0.7,2.0]:
    for n in range(1,31):
        peak = n*a/2
        exact = log_power_exact(a,n)
        assert abs(log_power_at(a,n,peak)-exact) < 5e-12*(1+abs(exact))
        COUNT += 1
        for step in range(-20,21):
            s = peak + step*0.05
            assert log_power_at(a,n,s) <= exact + 3e-12*(1+abs(exact))
            COUNT += 1

# Verify the claimed quadratic leading term and uniformly bounded remainder.
for a in [-1.1,-0.33,0.33,1.1]:
    c = PI*abs(a)
    for n in range(1,161):
        rem = (log_power_exact(a,n)+c*n*n/4
               -n*math.log(2)-n*log_constant(a))
        assert abs(rem) < 15 + 5/c
        COUNT += 1

# Finite Neumann series saddle upper and localized lower bounds, both uniform
# in the argument of lambda because the powers of a short-support input
# have disjoint supports. These estimates bound, not compute, the resolvent.
for a in [-1.0,-0.6,0.6,1.0]:
    c = PI*abs(a)
    delta = abs(a)/5
    for L in [5,10,20,40,80,160]:
        nmax = max(40, int(5*L/c)+70)
        vals = [(n+1)*L+log_power_exact(a,n) if n else L
                for n in range(nmax+1)]
        upper = logsumexp(vals)
        lower = max(v-PI*n*delta for n,v in enumerate(vals))
        target = L*L/c
        assert lower <= upper+1e-12
        assert (upper-target)/L < 90+15/c
        assert (target-lower)/L < 90+15/c
        COUNT += 3

# Separate optional check of the Gamma-function normalization, when mpmath
# happens to be available. Absence of that package is not a proof failure.
try:
    import mpmath as mp
    for a in [-2.,-0.7,-0.13,0.13,0.7,2.]:
        constant = PI/abs(complex(mp.gamma(1-1j*a)))
        assert abs(math.log(constant)-log_constant(a)) < 1e-11
        COUNT += 1
    print('Gamma-function normalization: checked with optional mpmath')
except ImportError:
    print('Gamma-function normalization: analytic reflection identity only')

print(f'PASS: {COUNT} finite checks; infinite-dimensional conclusions are analytic.')
