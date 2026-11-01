"""Independent finite checks for the radial Bergman/Fock transfer identity.

Python standard library only. These finite checks are not a proof of the theorem.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
from math import comb, factorial


def beta_cdf_integer_weight(n, N, t):
    """Exact P(N*Beta(n+1,N+1) <= t) for integer N and rational t."""
    a = t / N
    beta = F(factorial(n) * factorial(N), factorial(n+N+1))
    integral = sum(F((-1)**j * comb(N,j), n+j+1) * a**(n+j+1)
                   for j in range(N+1))
    return integral / beta


def gamma_cdf(n,t,prec=100):
    with localcontext() as ctx:
        ctx.prec=prec
        z=Decimal(t.numerator)/Decimal(t.denominator)
        poisson=Decimal(1)
        term=Decimal(1)
        for j in range(1,n+1):
            term *= z/Decimal(j)
            poisson += term
        return Decimal(1)-(-z).exp()*poisson


def dec(x):
    return Decimal(x.numerator)/Decimal(x.denominator)


checks=0
for N,t in [(2,F(1)), (5,F(2)), (10,F(3)), (25,F(7,2))]:
    assert 0 < t < N
    with localcontext() as ctx:
        ctx.prec=100
        ds=[]
        for n in range(31):
            beta=beta_cdf_integer_weight(n,N,t)
            ga=gamma_cdf(n,t)
            gap=dec(beta)-ga
            assert gap > Decimal('1e-85'), (N,t,n,gap)
            ds.append(gap)
            checks += 1
        # The exact trace identity upper-bounds all finite partial sums, as the gaps are positive.
        exact=dec(t*(1+t)/(N-t))
        assert sum(ds) <= exact + Decimal('1e-80')
        assert exact-sum(ds) < Decimal('0.05'), (N,t,exact-sum(ds))
        checks += 2

# Differential identity for the log-likelihood ratio of scaled Beta and Gamma densities:
# derivative of N*log(1-v/N)+v is -v/(N-v), checked at rational inputs.
for N in [F(2),F(5),F(13,2),F(22)]:
    for v in [N/F(5),N/F(3),N/F(2),N*F(4,5)]:
        left = -N/(N-v)+1
        right = -v/(N-v)
        assert left == right and right < 0
        checks += 1

# Exact disk trace difference identity and leading coefficient for rational N,t.
for N,t in [(F(2),F(1)),(F(10),F(3)),(F(21,2),F(5,2)),(F(120),F(4))]:
    trB = (N+1)*t/(N-t)
    trF = t
    assert trB-trF == t*(1+t)/(N-t)
    assert N*(trB-trF) > t*(t+1)
    checks += 2

# A nonmonotone radial annulus defeats positivity: at N=2 and v>=3/2,
# the n=0 Beta/Gamma density ratio is below 1, since it decreases and
# q(3/2)/p(3/2)=3*e^(3/2)/32 < 1.
with localcontext() as ctx:
    ctx.prec=90
    assert 3*(Decimal(3)/2).exp() < 32
    checks += 1
print(f'TRANSFER_FINITE_CHECKS_OK count={checks} disk_cases=4 modes_per_case=31')
