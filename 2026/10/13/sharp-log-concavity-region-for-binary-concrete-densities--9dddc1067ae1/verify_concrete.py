"""Reproduce exact algebra for a binary Concrete density shape theorem.

Requires Python 3 and SymPy.  The infinite-parameter inequality is proved
analytically in RESULT.md; finite checks here are diagnostics, not a proof.
"""

from fractions import Fraction
import sympy as sp


def check_curvature_identity():
    x, w, t = sp.symbols('x w t')
    # h^2 (log f)'', where h=x(1-x) and w=F(x).
    C = (-(t - 1) * (x*x + (1-x)**2)
         + 2*t*(w*(1-x)**2 + (1-w)*x*x)
         - 2*t*t*w*(1-w))
    H = t*(2*w-1) - (2*x-1)
    assert sp.expand(2*C - (H*H - (t*t-1))) == 0


def check_cdf_and_curvature_examples():
    x = sp.symbols('x', positive=True)
    instances = [
        (sp.Integer(1), sp.Integer(1)),
        (sp.Integer(1), sp.Integer(5)),
        (sp.Integer(2), sp.Integer(1)),
        (sp.Integer(2), sp.Integer(100)),
        (sp.Integer(3), sp.Integer(9)),
        (sp.Integer(4), sp.Rational(1, 81)),
    ]
    for t, alpha in instances:
        F = x**t/(x**t+alpha*(1-x)**t)
        f = t*alpha*x**(t-1)*(1-x)**(t-1)/(x**t+alpha*(1-x)**t)**2
        assert sp.factor(sp.diff(F, x) - f) == 0
        curv = sp.diff(sp.log(f), x, 2)
        at_half = sp.factor(curv.subs(x, sp.Rational(1, 2)))
        formula = 8*(t*t*((alpha-1)/(alpha+1))**2-(t*t-1))
        assert sp.simplify(at_half-formula) == 0
    assert sp.factor(sp.diff(sp.log(
        2*100*x*(1-x)/(x*x+100*(1-x)**2)**2), x, 2
    ).subs(x, sp.Rational(1, 2))) == sp.Rational(68808, 10201)


def check_threshold_and_alternative_parameterization():
    t = sp.symbols('t', positive=True)
    a = t + sp.sqrt(t*t - 1)
    assert sp.simplify((a*a+1/(a*a))-(4*t*t-2)) == 0
    alpha = sp.symbols('alpha', positive=True)
    p = alpha/(1+alpha)
    assert sp.simplify((sp.sqrt(alpha)+1/sp.sqrt(alpha))/2
                       - 1/(2*sp.sqrt(p*(1-p)))) == 0
    x, mu = sp.symbols('x mu', positive=True)
    for beta in (1, 2, 3):
        aa = (mu/(1-mu))**beta
        bc = sp.Integer(beta)
        f1 = bc*aa*x**(beta-1)*(1-x)**(beta-1)/(x**beta+aa*(1-x)**beta)**2
        f2 = bc*mu**beta*(1-mu)**beta*x**(beta-1)*(1-x)**(beta-1)/(
            (1-mu)**beta*x**beta+mu**beta*(1-x)**beta)**2
        assert sp.factor(f1-f2) == 0


def check_rational_sign_diagnostics():
    x = sp.symbols('x', positive=True)
    points = [sp.Rational(k, 16) for k in range(1,16)]
    for t, alpha in [(2,1),(2,9),(3,1),(3,25),(4,sp.Rational(1,49))]:
        f = sp.Integer(t)*alpha*x**(t-1)*(1-x)**(t-1)/(
            x**t+alpha*(1-x)**t)**2
        curv = sp.diff(sp.log(f),x,2)
        assert all(sp.factor(curv.subs(x,y)) <= 0 for y in points)
    t, alpha = 2, 100
    f = t*alpha*x**(t-1)*(1-x)**(t-1)/(x**t+alpha*(1-x)**t)**2
    assert sp.factor(sp.diff(sp.log(f),x,2).subs(x,sp.Rational(1,2))) > 0


if __name__ == '__main__':
    check_curvature_identity()
    check_cdf_and_curvature_examples()
    check_threshold_and_alternative_parameterization()
    check_rational_sign_diagnostics()
    print('PASS: exact polynomial identity, density/CDF derivatives,')
    print('parameter transforms, and 76 finite rational curvature tests.')
    print('Infinite-domain sufficiency rests on the analytic proof.')
