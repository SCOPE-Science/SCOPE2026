"""Reproduce exact two-dimensional matrix-pencil identities and illustrative bounds.

The universal assertion and sharpness are established analytically in RESULT.md;
finite checks here are independent consistency checks, not an infinite proof.
"""
from fractions import Fraction as F
from math import sqrt
from random import Random


def det2(a, b, c):
    return a * c - b * b


def envelope(mu, upper, eps):
    center = (mu + upper) / 2
    radius = (upper - mu) / (2 * sqrt(1 - eps * eps))
    return center - radius, center + radius


def pencil_coefficients(mu, upper, eps):
    # B = sym(M A), M = [[1,-eps],[-eps,1]], A=diag(mu,upper).
    # det(B-z*M)=a*z*z+b*z+c.
    a = 1 - eps * eps
    b = -(mu + upper) * (1 - eps * eps)
    c = mu * upper - eps * eps * (mu + upper) ** 2 / 4
    return a, b, c


def exact_tests():
    n = 0
    for mu in [F(1), F(2, 3), F(7, 2)]:
        for upper in [mu * F(2), mu * F(9), mu * F(100)]:
            for eps in [F(0), F(1, 8), F(3, 5), F(4, 5), F(19, 20)]:
                a, b, c = pencil_coefficients(mu, upper, eps)
                # Recompute the determinant directly from the original matrix
                # entries, instead of relying solely on the coefficient formula.
                for z in [F(-3, 2), F(0), F(1, 7), F(3), F(37, 5)]:
                    direct = (mu-z)*(upper-z) - eps*eps*((mu+upper)/2-z)**2
                    assert direct == a*z*z+b*z+c
                alpha = (mu + upper) / 2
                delta = (upper - mu) / 2
                # Discriminant = (upper-mu)^2*(1-eps^2), exactly.
                assert b*b - 4*a*c == (upper-mu)**2 * (1-eps*eps)
                assert a == 1-eps*eps
                assert b == -2*a*alpha
                assert c == a*alpha*alpha-delta*delta
                lower, higher = envelope(float(mu), float(upper), float(eps))
                assert lower <= higher
                assert abs((lower+higher)/2 - float(alpha)) < 1e-10
                assert abs((lower-higher)**2/4 - float(delta*delta/a)) < 1e-8
                n += 1
    return n


def sampled_tests():
    rng = Random(20261022)
    n = 0
    for _ in range(1200):
        mu = 10 ** rng.uniform(-2, 1)
        upper = mu * 10 ** rng.uniform(0, 3)
        eps = rng.uniform(0, .99)
        a, b, c = pencil_coefficients(mu, upper, eps)
        h0, h1 = envelope(mu, upper, eps)
        for h in [h0, h1]:
            val = a*h*h+b*h+c
            assert abs(val) <= 1e-7 * max(1,abs(c),abs(a*h*h),abs(b*h))
        # A particular b=(x,y), with M off-diagonal -eps.
        x = rng.uniform(-1,1)
        y = rng.uniform(-1,1)
        if x*x+y*y < 1e-6:
            continue
        numerator = mu*x*x+upper*y*y-eps*(mu+upper)*x*y
        denominator = x*x+y*y-2*eps*x*y
        assert denominator > 0
        h = numerator/denominator
        assert h0-1e-7*max(1,abs(h0)) <= h <= h1+1e-7*max(1,abs(h1))
        n += 1
    return n


def witness_checks():
    n=0
    for mu,upper in [(1.,9.),(2.,7.),(.01,100.)]:
        crit = 2*sqrt(mu*upper)/(mu+upper)
        for eps in [0.8*crit,crit,crit+(1-crit)*.5]:
            lo,hi=envelope(mu,upper,eps)
            if eps < crit-1e-9: assert lo>0
            elif eps > crit+1e-9: assert lo<0
            else: assert abs(lo)<1e-7
            # Orthogonal eigenvectors of sym(M A)-h M attain both endpoints.
            for h in (lo,hi):
                a=mu-h
                off=-eps*(mu+upper)/2+eps*h
                c=upper-h
                assert abs(a*c-off*off) <= 1e-7 * max(1,abs(a*c),abs(off*off))
            n+=1
    return n

if __name__ == '__main__':
    count=exact_tests()+sampled_tests()+witness_checks()
    print('VERIFY_OK', count)
