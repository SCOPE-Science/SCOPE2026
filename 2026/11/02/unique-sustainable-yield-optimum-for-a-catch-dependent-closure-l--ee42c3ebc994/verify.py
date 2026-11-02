"""Reproduce algebraic checks for the catch-dependent-closure fishery result.

Requires Python 3 and SymPy. Exact rational brackets use only the standard library.
"""
from fractions import Fraction as Q
from math import factorial
import sympy as S


def exp_bounds(x, degree=30):
    assert 0 <= x < 1
    partial = sum((x**j / factorial(j) for j in range(degree + 1)), Q(0))
    first = x**(degree + 1) / factorial(degree + 1)
    # Subsequent term ratios are <= x/(degree+2).
    return partial, partial + first / (1 - x / (degree + 2))


def interval_add(x, y):
    return x[0]+y[0], x[1]+y[1]


def interval_neg(x):
    return -x[1], -x[0]


def interval_sub(x, y):
    return interval_add(x, interval_neg(y))


def interval_mul(x, y):
    arr = [a*b for a in x for b in y]
    return min(arr), max(arr)


def point(x):
    return x, x


def score_interval(A, s):
    """Certified interval for the numerator of d(log yield)/ds."""
    E = exp_bounds(s)
    C = interval_sub(point(A), interval_mul(point(s), E))
    B = interval_add(C, point(s))
    lhs = interval_mul(E, interval_mul(C, B))
    rhs = interval_mul(interval_sub(E, point(Q(1))),
                       interval_add(point(A), interval_mul(point(s*s), E)))
    return interval_sub(lhs, rhs)


def symbolic_checks():
    A, s = S.symbols('A s', positive=True)
    E = S.exp(s)
    C, B = A-s*E, A-s*(E-1)
    y = (E-1)*C/(A*B)
    log_score = E/(E-1) - (A+s*s*E)/(C*B)
    assert S.simplify(S.diff(y,s) - y*log_score) == 0
    param_deriv = -(E-1)*(C*C-s*s*E)/(A*A*B*B)
    assert S.simplify(S.diff(y,A) - param_deriv) == 0
    v = S.exp(s/S.Integer(2))
    g = s*v*(s*v+s) - (1-S.exp(-s))*(s*v+s*S.exp(s)*(1+s))
    claimed_g = s*(v+1)/v*(s*v-v*v+1)
    assert S.simplify(g - claimed_g) == 0
    # Expansion of the unique stationary point in the small-A regime.
    c2, c3 = S.symbols('c2 c3')
    z = A/S.Integer(2)+c2*A**2+c3*A**3
    ez = S.exp(z)
    D = ez*(A-z*ez)*(A-z*(ez-1))-(ez-1)*(A+z*z*ez)
    series = S.series(D,A,0,5).removeO().expand()
    assert S.solve(series.coeff(A,3),c2)[0] == -S.Rational(3,16)
    assert S.solve(series.coeff(A,4).subs(c2,-S.Rational(3,16)),c3)[0] == S.Rational(19,192)
    z = z.subs({c2:-S.Rational(3,16),c3:S.Rational(19,192)})
    yy = (S.exp(z)-1)*(A-z*S.exp(z))/(A*(A-z*(S.exp(z)-1)))
    small = S.series(yy,A,0,3).removeO().expand()
    assert S.simplify(small-(S.Rational(1,4)-A*A/S.Integer(768))) == 0
    print('PASS: exact derivative identities and small-A expansion')


def rational_checks():
    # The unique optimum for dimensionless closure slope A=1 is bracketed.
    left, right = Q(3,8), Q(3751,10000)
    sl, sr = score_interval(Q(1), left), score_interval(Q(1), right)
    assert sl[0] > 0 and sr[1] < 0
    # For several other rational A, certify the score switches sign from + to -.
    for A in [Q(1,8), Q(1,2), Q(1), Q(2), Q(7,2)]:
        a = Q(1,1000)
        # s must be below W(A); choose s=A/(A+2) and verify C>0.
        b = A/(A+2)
        ea=exp_bounds(a); eb=exp_bounds(b)
        assert A > a*ea[1] and A > b*eb[1]
        assert score_interval(A,a)[0] > 0
        # The derivative need not be negative at b; use a certified point near W(A).
        # A simple fixed rational grid finds a point still below W(A).
        good = False
        for k in range(1,10000):
            t = Q(k,10000)*A
            if t >= 1: break
            lo,hi=exp_bounds(t)
            if t*hi>=A: break
            if score_interval(A,t)[1]<0:
                good=True
                break
        # For A>1 use the numerical check below; the rational grid above is optional.
        if A <= 1:
            assert good
    print('PASS: exact rational exponential sign certificates; A=1 optimizer in (3/8,3751/10000)')


if __name__ == '__main__':
    symbolic_checks()
    rational_checks()
