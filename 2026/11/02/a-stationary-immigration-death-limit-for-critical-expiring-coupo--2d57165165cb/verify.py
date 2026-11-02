"""Reproducibility checks for finite sliding-window missing-type identities.

Only finite identities and numerical consistency are checked; process-level convergence
and the hitting-time limit follow from the mathematical proof.
"""
from fractions import Fraction
from itertools import product
from math import exp, log, log1p, factorial

checks = 0

def check(cond, explanation):
    global checks
    assert cond, explanation
    checks += 1


def falling(n, r):
    out = 1
    for k in range(r):
        out *= n-k
    return out

# For a word of length m+k, enumerate missing types in the two windows.
for n in (2, 3, 4):
    for m in (2, 3, 4):
        for lag in (0, 1, 2):
            total = n**(m+lag)
            sum_d0 = sum_d1 = sum_product = sum_f2 = 0
            for word in product(range(n), repeat=m+lag):
                d0 = n-len(set(word[:m]))
                d1 = n-len(set(word[lag:lag+m]))
                sum_d0 += d0
                sum_d1 += d1
                sum_product += d0*d1
                sum_f2 += d0*(d0-1)
            p = Fraction(n-1,n)**m
            check(Fraction(sum_d0,total) == n*p, f'first moment n={n} m={m}')
            check(Fraction(sum_d1,total) == n*p, f'first moment second n={n} m={m}')
            check(Fraction(sum_f2,total) == falling(n,2)*Fraction(n-2,n)**m, 'factorial second moment')
            same = Fraction(n-1,n)**(m+min(lag,m))
            if lag <= m:
                cross = Fraction(n-2,n)**(m-lag)*Fraction(n-1,n)**(2*lag)
            else:
                cross = p*p
            predicted = n*same+n*(n-1)*cross
            check(Fraction(sum_product,total) == predicted, f'two-time product n={n} m={m} lag={lag}')

# Stationary immigration-death generator detailed balance at sample rates.
for numerator, denominator in ((1, 2), (1, 1), (3, 2), (3, 1)):
    lam = Fraction(numerator, denominator)
    for j in range(12):
        pi_j = lam**j/Fraction(factorial(j))
        pi_jp1 = lam**(j+1)/Fraction(factorial(j+1))
        check(pi_j*lam == (j+1)*pi_jp1, 'detailed balance')

# Critical stationary mean, variance and covariance converge at the stated values.
for c in (-0.5, 0.0, 0.7):
    lam = exp(-c)
    for n in (10000, 100000, 1000000):
        m = int(n*(log(n)+c))
        k = n
        p = exp(m*log1p(-1/n))
        same = exp((m+k)*log1p(-1/n))
        cross = exp((m-k)*log1p(-2/n)+2*k*log1p(-1/n))
        cov = n*same+n*(n-1)*cross-n*n*p*p
        check(abs(n*p-lam) < 0.035, 'mean asymptotic')
        check(abs(cov-lam/exp(1)) < 0.04, 'covariance asymptotic')

# Independent quadratures of the Laplace-resolvent identity.
def simpson(f, a, b, intervals=40000):
    assert intervals % 2 == 0
    h = (b-a)/intervals
    return h/3*(f(a)+f(b)+4*sum(f(a+h*j) for j in range(1,intervals,2))+2*sum(f(a+h*j) for j in range(2,intervals,2)))

for lam in (0.5, 1.0, 2.0):
    for s in (1.0, 2.0, 3.0):
        kernel = simpson(lambda t: exp(-s*t-lam*(1-exp(-t))),0,40,10000)
        candidate = 1/(s*simpson(lambda u: u**(s-1)*exp(lam*u),0,1,10000))
        check(abs(candidate-exp(-lam)/(s*kernel)) < 1.e-8, 'Laplace resolvent')
    mean1 = simpson(lambda u: (exp(lam*u)-1)/u if u>0 else lam,0,1,20000)
    mean2 = sum(lam**j/(j*factorial(j)) for j in range(1,50))
    check(abs(mean1-mean2)<1.e-10, 'mean series')
print(f'{checks} deterministic finite-identity and consistency assertions passed')
