"""Exact supplementary checks for spherical Bernstein cone preservation.

Requires Python 3 and SymPy. Finite checks supplement, not replace,
the all-order analytic proof.
"""
from sympy import (Rational, Symbol, binomial, cancel, factorial,
                   gegenbauer, legendre, Poly, simplify)

x = Symbol('x')
checks = 0


def bernstein_from_samples(n, samples):
    return sum(samples[j]*binomial(n, j)*((1+x)/2)**j*
               ((1-x)/2)**(n-j) for j in range(n+1)).expand()


def zonal_coefficients(poly, n):
    return [cancel(Rational(2*k+1, 2)*
                   __import__('sympy').integrate(poly*legendre(k, x),
                                                  (x, -1, 1)))
            for k in range(n+1)]


# Verify the degree-one, -two and -three positivity cone maps on a
# substantial finite set of even and odd input Legendre degrees.
for n in (1, 2, 3):
    for m in range(50):
        samples = [legendre(m, -1+Rational(2*j, n))
                   for j in range(n+1)]
        p = bernstein_from_samples(n, samples)
        coeff = zonal_coefficients(p, n)
        assert all(t >= 0 for t in coeff), (n, m, coeff)
        checks += n+1

# The general-dimension formula compares a Gegenbauer basis vector with
# its Bernstein image at every integer sphere dimension considered.
for d in range(2, 8):
    lam = Rational(d-1, 2)
    for n in range(1, 10):
        m = n+2
        normal_m = gegenbauer(m, lam, 1)
        values = [gegenbauer(m, lam, -1+Rational(2*j,n))/normal_m
                  for j in range(n+1)]
        p = bernstein_from_samples(n, values)
        normal_n = gegenbauer(n, lam, 1)
        lead_input = Poly(gegenbauer(n,lam,x)/normal_n, x).coeff_monomial(x**n)
        measured = cancel(Poly(p,x).coeff_monomial(x**n)/lead_input)
        predicted = (Rational(factorial(n),n**n)*
                     Rational((n+1)*(n+2),3*n)*
                     (n+lam)*(d+1-n)/((n+d-1)*(n+d)))
        assert simplify(measured-predicted) == 0, (d,n,measured,predicted)
        checks += 1

# Exact finite cases underpinning the global odd-degree bound.
assert legendre(1,Rational(1,3)) == Rational(1,3)
assert legendre(3,Rational(1,3)) == Rational(-11,27)
assert legendre(5,Rational(1,3)) == Rational(1,3)
assert legendre(7,Rational(1,3)) == Rational(-121,729)
I8 = sum(binomial(4,j)*(-Rational(8,9))**j*
         binomial(2*j,j)/4**j for j in range(5))
assert I8 == Rational(1921,6561) and I8 < Rational(1,3)
checks += 5

# The published degree-four example is one member of the exact family.
n = 4
vals = [legendre(6,-1+Rational(2*j,n)) for j in range(n+1)]
coeff = zonal_coefficients(bernstein_from_samples(n,vals),n)
assert coeff == [Rational(239,512),0,Rational(291,512),0,Rational(-9,256)]
checks += 5
print(f'VERIFY_OK {checks} exact Gegenbauer/Legendre cone, coefficient, and boundary checks')
