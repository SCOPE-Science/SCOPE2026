"""Independent finite checks for the Gaussian-trace GCV moment-law theorem.

Requires Python 3 only. Infinite-time and moment conclusions follow from proof.
"""
from fractions import Fraction
from math import comb, exp, factorial, gamma, sqrt
from itertools import product

count=0
# Exact isotropic single-mode inverse chi-square expectation, for N>4.
for n in range(2,7):
    for m in range(1,7):
        N=n*m
        if N>4:
            expected=Fraction(N*N,(N-2)*(N-4))
            # E[(N/X)^2] = N²/(4 Gamma(N/2)/Gamma(N/2-2)).
            numerical=N*N*gamma(N/2-2)/(4*gamma(N/2))
            assert abs(float(expected)-numerical)<1e-9
            count+=1

# Every Rademacher vector has squared norm n, and equal trace complements.
for n in (2,3,4):
    vals=[Fraction(j+1,j+3) for j in range(n)]
    for z in product((-1,1), repeat=n):
        # diagonal SPD positive residual, H=I-R.
        direct=sum(a*zi*zi for a,zi in zip(vals,z))
        sub=n-sum((1-a)*zi*zi for a,zi in zip(vals,z))
        assert direct==sub and direct>0
        count+=1

# Isotropic n=2, m=3, R=(1/2)I, b unit.
C=Fraction(1,4)
N=6
mean_direct=C*Fraction(N*N,(N-2)*(N-4))
assert mean_direct==Fraction(9,8)
count+=1

# Chi-square(6) CDF and its exact density (Gamma shape 3, scale 2).
def chi6_cdf(x):
    import math
    # Stable x small via Taylor survival series: CDF=exp(-x/2) sum_{k>=3}(x/2)^k/k!
    z=x/2
    term=z*z*z/factorial(3)
    acc=term
    for k in range(4,60):
        term*=z/k
        acc+=term
    return exp(-z)*acc

def chi6_pdf(x):
    return (x*x/16)*exp(-x/2)

# At n=2 the complement is 2 - chi6/6; its density at zero is 54 exp(-6).
const_sub=54*exp(-6)
const_dir=Fraction(9,16)
for t in (100., 1000., 10000.):
    radius=sqrt(float(C)/t)
    left=6*(2-radius)
    right=6*(2+radius)
    p_sub=chi6_cdf(right)-chi6_cdf(left)
    p_dir=chi6_cdf(3/sqrt(t))
    # Asymptotics approach their coefficients as t grows.
    assert abs(p_sub*sqrt(t)/const_sub-1)<0.08
    assert abs(p_dir*t**1.5/float(const_dir)-1)<0.16
    count+=2

# Check a random nonscalar spectral family for direct/complement trace difference.
for n in (2,3,4):
    lam=[Fraction(j+2,j+5) for j in range(n)]
    for z in product((-2,-1,0,1,2),repeat=n):
        sr=sum(a*zi*zi for a,zi in zip(lam,z))
        sc=n-sum((1-a)*zi*zi for a,zi in zip(lam,z))
        assert sr-sc==sum(zi*zi for zi in z)-n
        count+=1

print('VERIFY_OK',count,'exact rational and asymptotic spot checks')
