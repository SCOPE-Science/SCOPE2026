from fractions import Fraction
from decimal import Decimal, getcontext
from math import exp, factorial

# Conditional identities under Dirichlet(1,...,1).
for n in range(0, 1001):
    eq = Fraction(2, n + 2)
    ecv = Fraction(n, n + 2)
    assert Fraction(n + 1, 1) * eq - 1 == ecv
    assert Fraction(2, n + 3) - eq == -Fraction(2, (n + 2) * (n + 3))
    assert Fraction(n + 1, n + 3) - ecv == Fraction(2, (n + 2) * (n + 3))

# Direct Poisson summation versus the closed form.
def direct(mu, cutoff=400):
    p = exp(-mu)
    enq = eqm = ecv = encv = en = 0.0
    for n in range(cutoff + 1):
        if n:
            p *= mu / n
        q = 2.0 / (n + 2.0)
        cv = n / (n + 2.0)
        en += p * n
        eqm += p * q
        enq += p * n * q
        ecv += p * cv
        encv += p * n * cv
    return enq - en * eqm, encv - en * ecv

def closed(mu):
    return 2.0 * ((mu - 2.0) + (mu + 2.0) * exp(-mu)) / (mu * mu)

for mu in [0.01, 0.03, 0.1, 0.3, 1.0, 2.0, 5.0, 10.0, 25.0, 50.0]:
    cq, cc = direct(mu)
    a = closed(mu)
    assert abs(cq + a) < 2e-11 * max(1.0, abs(a))
    assert abs(cc - a) < 2e-11 * max(1.0, abs(a))
    assert a > 0.0

# High-precision small-intensity check, avoiding cancellation in the closed form.
getcontext().prec = 60
for s in ['0.0001', '0.001', '0.01']:
    mu = Decimal(s)
    # A = 2 mu * sum P(N=n)/((n+2)(n+3)).
    p = (-mu).exp()
    total = Decimal(0)
    for n in range(80):
        if n:
            p *= mu / Decimal(n)
        total += p / (Decimal(n + 2) * Decimal(n + 3))
    a = Decimal(2) * mu * total
    approx = mu / Decimal(3) - mu * mu / Decimal(6) + mu**3 / Decimal(20)
    assert abs(a - approx) < Decimal('1e-15') + Decimal('0.1') * mu**4

print('VERIFY_OK conditional=1001 poisson=10 small_mu=3')
