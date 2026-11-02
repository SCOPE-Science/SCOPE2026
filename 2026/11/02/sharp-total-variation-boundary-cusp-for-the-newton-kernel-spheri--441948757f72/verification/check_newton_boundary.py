"""Reproduction checks for a sharp Newton-kernel spherical boundary law.
Requires Python 3 standard library only. Numerical quadrature is supporting evidence;
all-dimension asymptotics and signed weak convergence are proved analytically.
"""
import math
from fractions import Fraction

COUNT = 0

def assert_close(actual, expected, tolerance, description):
    global COUNT
    if not math.isfinite(actual) or abs(actual-expected) > tolerance:
        raise AssertionError(f'{description}: actual={actual!r}, expected={expected!r}, atol={tolerance!r}')
    COUNT += 1

def check(condition, description):
    global COUNT
    if not condition:
        raise AssertionError(description)
    COUNT += 1

def simpson(f, lo, hi, panels=16000):
    if panels % 2:
        raise ValueError('even number of panels required')
    step = (hi-lo)/panels
    total = f(lo) + f(hi)
    for j in range(1, panels):
        total += (4 if j % 2 else 2) * f(lo+j*step)
    return total*step/3

def coeff(d):
    return math.exp(math.lgamma(d/2)-math.lgamma((d-1)/2)-0.5*math.log(math.pi))

def jacobian(d,y):
    return math.sqrt(2)*coeff(d)*max(0,1-y*y/2)**((d-3)/2)

def likelihood_ratio(d,eps,y):
    if y == 0:
        return 0.0
    return (1-eps+eps*eps/(2*y*y))**(-(d-2)/2)

def mass_check(d,eps,panels=12000):
    ycap=math.sqrt(eps/2)
    f=lambda y: jacobian(d,y)*likelihood_ratio(d,eps,y)
    f0=lambda y: jacobian(d,y)
    plus=simpson(lambda y: f(y)-f0(y),ycap,math.sqrt(2),panels)
    minus=simpson(lambda y: f0(y)-f(y),0,ycap,panels)
    return plus,minus,simpson(f,0,math.sqrt(2),panels),simpson(f0,0,math.sqrt(2),panels)

# Beta-normalized cusp latitude law and all densities normalized by shell theorem.
for d in [3,4,5,6,7,8,10]:
    c=coeff(d)
    check(0<c<5, f'positive normalizer in dimension {d}')
    for eps in [.95,.75,.5,.25,.1,.01]:
        positive, negative, normrho, normone=mass_check(d,eps)
        assert_close(normrho,1.,2.0e-6,f'normalized interior law d={d}, eps={eps}')
        assert_close(normone,1.,2.0e-6,f'normalized limiting law d={d}, eps={eps}')
        assert_close(positive,negative,2.0e-6,f'positive and negative TV parts d={d}, eps={eps}')
        check(positive>0,f'strictly positive TV d={d}, eps={eps}')

# At epsilon=q^{-2}, dimension three has the exact rational TV 1/(2q(q+1)).
for q in range(2,61):
    eps=Fraction(1,q*q)
    rho=1-eps
    root=Fraction(1,q)
    # Evaluate both antiderivatives exactly at the density crossing.
    positive=Fraction(1,2)*((1+rho-root)/rho-(2-root))
    expected=Fraction(1,2*q*(q+1))
    check(positive==expected,f'exact d=3 antiderivative q={q}')
    numerical=mass_check(3,float(eps),panels=9000)[0]
    assert_close(numerical,float(expected),5e-10,f'exact-vs-quadrature q={q}')

# Sharp fractional correction: residual bounded on the epsilon-squared scale.
for d in [3,4,5,6,8]:
    a=(d-2)/2
    c=coeff(d)
    for eps in [.03,.01,.005,.002]:
        positive=mass_check(d,eps,panels=20000)[0]
        two_term=a*eps-2*a*c*eps**1.5
        check(abs(positive-two_term) < 30*eps*eps,
              f'epsilon^2 remainder d={d}, eps={eps}: {positive=}, {two_term=}')
        check(0<positive<a*eps,
              f'correct strict sign and first-order upper bound d={d}, eps={eps}')

print(f'PASS: {COUNT} exact-rational or independently integrated numerical assertions.')
