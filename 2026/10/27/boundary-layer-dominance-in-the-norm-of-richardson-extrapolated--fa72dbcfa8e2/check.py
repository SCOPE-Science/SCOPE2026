"""Reproducible finite checks for the extrapolated Bernstein stability theorem.

This program verifies numerical identities and independent finite examples.
It does not replace the local-limit arguments in the proof.
"""
from fractions import Fraction
from itertools import product
from math import comb, exp, erf, sqrt, log, pi


def b(m, j, x):
    return comb(m, j)*x**j*(1-x)**(m-j)


def exact_formula(n, x):
    return 1+2*sum(max(b(n,k,x)-2*b(2*n,2*k,x),0)
                   for k in range(n+1))


def direct_sup(n, x):
    # All sign patterns can be interpolated by a continuous unit-ball function.
    best = Fraction(-1)
    for signs in product((-1,1), repeat=2*n+1):
        total = 2*sum(b(2*n,j,x)*signs[j] for j in range(2*n+1))
        total -= sum(b(n,k,x)*signs[2*k] for k in range(n+1))
        best = max(best, abs(total))
    return best

for n in range(1,5):
    for x in (Fraction(0),Fraction(1,4),Fraction(2,5),Fraction(1,2),Fraction(3,4),Fraction(1)):
        assert exact_formula(n,x) == direct_sup(n,x), (n,x)


def exp_bounds(z, degree=42):
    """Proved rational interval for exp(-z), z nonnegative rational."""
    z=Fraction(z)
    assert z < degree+2
    term=Fraction(1)
    s=term
    for j in range(1,degree+1):
        term=term*z/j
        s+=term
    first=term*z/(degree+1)
    rem_upper=first/(1-z/Fraction(degree+2))
    # exp(z) in [s,s+rem_upper]
    return 1/(s+rem_upper),1/s

q=Fraction(7,5)
low_e,high_e=exp_bounds(q)
ratio=lambda k,e: 2*e*(4*q)**k*Fraction(1,comb(2*k,k)) / Fraction(1) # 2e(4q)^k k!/(2k)! = 2e(4q)^k /[(2k)!/k!]
from math import factorial
ratio=lambda k,e: 2*e*(4*q)**k*Fraction(factorial(k),factorial(2*k))
assert ratio(0,high_e)<1
assert ratio(1,low_e)>1
assert ratio(2,low_e)>1
assert ratio(3,high_e)<1
# R_{k+1}/R_k = 2q/(2k+1) < 1 for k>=2.
assert 2*q/Fraction(7) < 1
lo4,hi4=exp_bounds(4*q)
lo2,hi2=exp_bounds(2*q)
g_lower=1-2*hi4+Fraction(48608,1875)*lo2-Fraction(119,25)*high_e
g_upper=1-2*lo4+Fraction(48608,1875)*hi2-Fraction(119,25)*low_e
assert g_lower>Fraction(1395,1000)
assert g_upper<Fraction(1396,1000)

r=sqrt(log(2))
Phi=lambda z:(1+erf(z/sqrt(2)))/2
bulk=1+4*(Phi(-r)-Phi(-sqrt(2)*r))
assert bulk<1.391
assert 2*(1.415-1)*sqrt(.694/3.14)<.391

def poisson_profile(q, cutoff=250):
    # Poisson probabilities by stable recursion, for moderate q.
    p=exp(-q); r2=exp(-2*q)
    negative=0.0
    for k in range(cutoff):
        negative+=max(0.,p-2*r2)
        p=p*q/(k+1)
        r2=r2*(2*q)*(2*q)/((2*k+1)*(2*k+2))
    return 1+2*negative

g_explicit=1-2*exp(-4*float(q))+(48608/1875)*exp(-2*float(q))-(119/25)*exp(-float(q))
assert abs(g_explicit-poisson_profile(float(q)))<1e-12
assert g_explicit>bulk+0.06

for n in (20,50,100,250,500):
    # Only diagnostic convergence: no finite sample proves the asymptotic theorem.
    edge=exact_formula(n,float(q)/n)
    inside=exact_formula(n,0.5)
    assert abs(edge-g_explicit)<0.06
    assert abs(inside-bulk)<0.08
    print('n=',n,'edge=',round(edge,8),'interior=',round(inside,8))
print('G(7/5) certified in (1.395,1.396); numerical:',g_explicit)
print('interior Gaussian constant:',bulk)
print('all tests passed')
