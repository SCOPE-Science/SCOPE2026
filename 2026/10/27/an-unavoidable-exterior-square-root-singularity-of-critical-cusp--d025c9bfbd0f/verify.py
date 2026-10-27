"""Standard-library algebraic checks for the square-root cusp branch-point formula.

These finite checks are not a substitute for the analytic proof.
"""
from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 65
D = Decimal


def close(a, b, tol=D('1e-47')):
    assert abs(a - b) < tol, (a, b, abs(a - b))


def trial_phi(y):
    return D(1) + y + y*y


cases = [(Fraction(5, 4), Fraction(169, 160), Fraction(9, 200)),
         (Fraction(3, 2), Fraction(49, 48), Fraction(1, 72)),
         (Fraction(7, 4), Fraction(225, 224), Fraction(1, 392))]
checks = 0
for rat_theta, rat_star, rat_v in cases:
    theta = D(rat_theta.numerator)/D(rat_theta.denominator)
    K = (D(1)-theta/D(2))/D(2).sqrt()
    star = D(1)+K*K/theta
    v = K*K/(theta*theta)
    close(star, D(rat_star.numerator)/D(rat_star.denominator))
    close(v, D(rat_v.numerator)/D(rat_v.denominator))
    close(K*K+theta*(D(1)-star), D(0))
    bound = D(1)/(D(1)+theta/D(2))
    for j in range(51):
        x = D(j)/D(50)
        s = (K*K+theta*(D(1)-x)).sqrt()
        u = (s-K)/theta
        w = u/s
        assert -D('1e-55') <= u <= D(1)/D(2).sqrt()+D('1e-55')
        assert -D('1e-55') <= w <= bound+D('1e-55')
        for sign in (-1, 1):
            g = D('0.5')+sign*u*u
            t = abs(g-D('0.5'))
            fx = D(1)-theta*t-D(2)*K*t.sqrt()
            close(fx, x)
            checks += 1
    amp = -K/(theta*theta.sqrt()) * (trial_phi(D('0.5')-v)+trial_phi(D('0.5')+v))
    errors = []
    for power in (6, 10, 14, 18):
        delta = D(10)**(-power)
        x = star-delta
        s = (K*K+theta*(D(1)-x)).sqrt()
        u = (s-K)/theta
        continued = (u/s)*(trial_phi(D('0.5')-u*u)+trial_phi(D('0.5')+u*u))
        approximation = delta.sqrt()*continued
        errors.append(abs(approximation-amp))
    assert errors[-1] < errors[0]/D(10000), errors
    checks += 4
print('VERIFY_OK parameters=3 inverse_checks=306 branch_limit_checks=12 total_checks=', checks)
