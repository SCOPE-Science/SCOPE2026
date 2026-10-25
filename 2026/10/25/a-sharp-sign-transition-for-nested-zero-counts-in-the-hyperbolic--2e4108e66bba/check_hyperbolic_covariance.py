"""Reproduce boundary-covariance computations for hyperbolic Gaussian zero counts.

Dependencies: Python 3.10+, scipy, sympy. Run: python check_hyperbolic_covariance.py.
All displayed statistics are numerical checks; the proof is in RESULT.md.
"""
import math
from scipy.integrate import quad
from scipy.special import gammaln
import sympy as sp


def covariance_integral(r, s, L):
    """Exact finite-radius covariance integral from Gaussian log covariance."""
    assert 0 < r < 1 and 0 < s < 1 and r != s and L > 0

    def integrand(theta):
        z = r * s
        c = math.cos(theta)
        D = (1-z)**2 + 2*z*(1-c)
        Q = (1-r*r)*(1-s*s)/D
        A = Q**L
        B = 2*z*(z-c)/D
        Ur = L*(-2*r*r/(1-r*r)-B)
        Us = L*(-2*s*s/(1-s*s)-B)
        Urs = -L*(B+2*z*z/D-B*B)
        return A/(1-A)*Ur*Us-math.log1p(-A)*Urs

    value, error = quad(integrand, 0, math.pi, epsabs=2e-10,
                        epsrel=2e-10, limit=400, points=[0])
    assert error < 2e-7
    return value/(4*math.pi)


def boundary_kernel_two(alpha, beta):
    p = alpha + beta
    v = abs(alpha-beta)/p
    return 2/(p*(1-v*v))*(1+v*v-v-1/math.sqrt(2-v*v))


def boundary_kernel_series(L, alpha, beta):
    p = alpha + beta
    v = abs(alpha-beta)/p
    q = 1-v*v
    acc = 0.0
    for k in range(1, 30000):
        nu = L*k
        term = (L/k)*math.exp(gammaln(nu-0.5)-gammaln(nu)) * \
               q**(nu-1)*(1-(2*nu-1)*v*v)
        acc += term
        if k > 100 and abs(term) < 2e-14:
            break
    return acc/(4*math.sqrt(math.pi)*p)


def main():
    assertions = 0
    v = sp.symbols('v')
    factor = sp.factor((1+v*v-v)**2*(2-v*v)-1)
    assert factor == -(v-1)**2*(v**4+2*v-1)
    assertions += 1
    root = sp.nsolve(v**4+2*v-1, sp.Rational(47,100), prec=45)
    assert sp.Rational(474626,1000000)<root<sp.Rational(474627,1000000)
    assertions += 1
    assert sp.diff(v**4+2*v-1, v) == 4*v**3+2
    assertions += 1

    for vvalue in [0.1,0.25,0.3,0.46,0.5,0.6,0.8,0.95]:
        alpha, beta = 1+vvalue, 1-vvalue
        a = boundary_kernel_series(2,alpha,beta)
        b = boundary_kernel_two(alpha,beta)
        assert abs(a-b) < 1.5e-9, (vvalue,a,b)
        assertions += 1

    for alpha,beta in [(1.0,1.1),(1.5,0.5),(1.3,0.7),
                       (1.0,0.2),(1.0,2.0),(1.0,3.0)]:
        h = boundary_kernel_two(alpha,beta)
        previous = None
        for eps in [.04,.015,.005]:
            current=eps*covariance_integral(1-alpha*eps,1-beta*eps,2)
            if previous is not None:
                assert abs(current-h)<abs(previous-h)+2e-8
                assertions += 1
            previous=current
            if eps == .005:
                assert abs(current-h)<.0012,(alpha,beta,current,h)
                assertions += 1

    for L in [1.2,1.5,2.0,3.0,5.0]:
        assert boundary_kernel_series(L,1.03,.97)>0
        assertions += 1
        vlarge=math.sqrt(1/(2*L-1)) + .03
        assert vlarge<1
        assert boundary_kernel_series(L,1+vlarge,1-vlarge)<0
        assertions += 1

    r,s = .72,.89
    known = r*r/(1-r*r) - r*r*s*s/(1-r*r*s*s)
    assert abs(covariance_integral(r,s,1)-known)<1e-8
    assertions += 1

    for epsilon in [.02,.005,.001]:
        radius = 1-epsilon
        exact_var = (4*radius*radius/(1-radius*radius) *
                     (1/(1+radius*radius)-1/(2*math.sqrt(1+radius**4))))
        assert abs(epsilon*exact_var-(1-1/math.sqrt(2)))<.012
        assertions += 1

    print('PASS',assertions,'independent symbolic, series and finite-radius tests')
    print('critical v =',root)
    print('critical inner/outer boundary-gap ratio =', (1-root)/(1+root))

if __name__=='__main__':
    main()
