"""Finite corroborative checks of weighted analytic-quadratic moment identities.

Python 3 standard library only. Tests corroborate algebra; see RESULT.md for proofs.
"""
from fractions import Fraction
from math import sqrt
from random import Random


def moments(beta):
    value = Fraction(1)
    result = [value]
    for k in range(1, 5):
        value *= Fraction(k, 1) / (beta + k - 1)
        result.append(value)
    return result


def coeffs(beta):
    C = 2 * beta / (beta + 1)
    E = 12 * beta / (beta + 2)
    F = 6 * beta * (beta + 1) / ((beta + 2) * (beta + 3))
    return float(C), 4 * sqrt(float(C)), float(E), float(F)


def normalized(x, y, z, beta):
    C, D, E, F = coeffs(beta)
    return (x ** 4 + 4 * x*x * y*y + 4 * x*x*z*z +
            C*y**4 + D*x*y*y*z + E*y*y*z*z + F*z**4)


def original(x, y, z, beta):
    m = list(map(float, moments(beta)))
    a, b, c = x, y/sqrt(m[1]), z/sqrt(m[2])
    return (a**4+4*m[1]*(a*b)**2+
            m[2]*(b*b+2*a*c)**2+4*m[3]*(b*c)**2+m[4]*c**4)


def q(u, v):
    return -8*u*u+4*sqrt(2)*u*v-4*v*v+24*v


def run():
    rng = Random(20261023)
    assertions = 0
    for b in [Fraction(1001,1000), Fraction(3,2), Fraction(2),
              Fraction(4), Fraction(10), Fraction(100), Fraction(1000)]:
        c, d, e, f = coeffs(b)
        m = moments(b)
        assert m[1] == 1/b; assertions += 1
        assert m[2] == 2/(b*(b+1)); assertions += 1
        assert m[3] == 6/(b*(b+1)*(b+2)); assertions += 1
        assert m[4] == 24/(b*(b+1)*(b+2)*(b+3)); assertions += 1
        assert 12*b/(b+2)-4 == 8*(b-1)/(b+2); assertions += 1
        assert 12*b/(b+2)-2*6*b*(b+1)/((b+2)*(b+3)) == 24*b/((b+2)*(b+3)); assertions += 1
        assert (12*b/(b+2)-2*b/(b+1)-6*b*(b+1)/((b+2)*(b+3))) == 2*b*(2*b*b+13*b+9)/((b+1)*(b+2)*(b+3)); assertions += 1
        for j in range(150):
            x, y, z = (rng.random() for _ in range(3))
            scale = sqrt(x*x+y*y+z*z)
            x, y, z = x/scale, y/scale, z/scale
            lhs, rhs = normalized(x,y,z,b), original(x,y,z,b)
            assert abs(lhs-rhs) < 1e-10 * max(1.0,abs(rhs)); assertions += 1
            q_face = 2*x**4 + (e-4)*x*x*z*z + (e-2*f)*z**4
            assert q_face > -1e-12; assertions += 1
    assert abs(q(sqrt(2),4)-48) < 1e-12; assertions += 1
    for _ in range(1000):
        u, v = rng.random()*20, rng.random()*30
        sos = 48 - 8*(u-sqrt(2)*v/4)**2 - 3*(v-4)**2
        assert abs(q(u,v)-sos)<1e-10; assertions += 1
    for beta in (50.0,100.0,500.0,1000.0):
        C,D,E,F = coeffs(Fraction(int(beta)))
        x,t=sqrt(2)/beta,4/beta
        z=sqrt(1-x*x-t)
        candidate=normalized(x,sqrt(t),z,Fraction(int(beta)))
        two=F+(E-2*F)**2/(4*(E-C-F))
        assert candidate>two; assertions+=1
        assert abs((candidate-F)*beta*beta-48)<8000/beta; assertions+=1
        assert abs((two-F)*beta*beta-36)<8000/beta; assertions+=1
    print(f"PASS: {assertions} exact-rational and finite numerical checks")


if __name__=='__main__':
    run()
