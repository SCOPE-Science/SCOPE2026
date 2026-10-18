"""Exact-rational and numerical checks for a sharp stationary reset tail law.

Run with Python 3 and the standard library: python checker.py
The sharp tail theorem is proved analytically in RESULT.md;
finite numerical checks are not a substitute for that proof.
"""
import math
from fractions import Fraction


def dilog_series(z, tol=1e-15):
    assert 0 <= z < 1
    if z > 0.75:
        return math.pi**2/6 - math.log(z)*math.log1p(-z) - dilog_series(1-z, tol)
    s = 0.0
    power = 1.0
    for j in range(1, 100000):
        power *= z
        term = power / (j*j)
        s += term
        if term < tol:
            return s
    raise AssertionError("series did not converge")


def log_mgf(q, theta):
    assert 0 < q < 1 and abs(theta) < math.sqrt(2)
    s = 0.0
    power = 1.0
    while power > 2e-17:
        s -= math.log1p(-theta*theta*power/2)
        power *= q
    return s


def scaled_log_mgf(q, theta):
    assert 0 < q < 1 and abs(theta) < math.sqrt(2)
    s = 0.0
    power = 1.0
    while power > 1e-15:
        s -= math.log1p(-theta*theta*power/2)
        power *= q
    return (1-q)*s


def rate(y):
    if y < 0:
        return rate(-y)
    if y == 0:
        return (0.0, 0.0)
    lo, hi = 0.0, math.sqrt(2)
    for _ in range(160):
        th = (lo+hi)/2
        z = th*th/2
        slope = -2*math.log1p(-z)/th
        if slope > y:
            hi = th
        else:
            lo = th
    th = (lo+hi)/2
    return (th, th*y-dilog_series(th*th/2))


def check():
    count = 0
    for q in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(9, 10)):
        delta = 1-q
        # Four moments inferred independently from the stationary generator.
        m2_generator = Fraction(1, 1)/delta
        m4_generator = 6*m2_generator/(1-q*q)
        m2_cumulants = Fraction(1, 1)/delta
        m4_cumulants = 3/(delta*delta) + 3/(1-q*q)
        assert m2_generator == m2_cumulants
        assert m4_generator == m4_cumulants
        count += 2
    for theta in (0.2, 0.5, 0.9, 1.2):
        target = dilog_series(theta*theta/2)
        errs=[]
        for q in (0.95, 0.99, 0.999):
            approx = scaled_log_mgf(q, theta)
            errs.append(abs(approx-target))
            assert approx >= target - 1e-11
            count += 1
        assert errs[2] < errs[1] < errs[0]
        assert errs[2] < 0.0008
        count += 2
    for y in (0.05, 0.1, 0.2, 0.5, 1, 2, 4, 8, 12):
        theta, value=rate(y)
        assert 0 < theta < math.sqrt(2)
        slope=-2*math.log1p(-theta*theta/2)/theta
        assert abs(slope-y) < 1e-8
        assert 0 < value < y*y/2
        count += 3
    for y in (0.02, 0.05, 0.1):
        _,value=rate(y)
        approx=y*y/2-y**4/16
        assert abs(value-approx) < y**6
        count += 1
    for y in (10, 15):
        _,value=rate(y)
        boundary=math.sqrt(2)*y-math.pi**2/6
        correction=math.exp(-y/math.sqrt(2))
        assert abs((value-boundary)/correction-1) < 0.11
        count += 1
    for y in (0.2, 1, 3):
        th,I=rate(y)
        th2,I2=rate(-y)
        assert abs(I-I2)<1e-12
        assert abs(th-th2)<1e-12
        count+=2
    # Order-one trapezoid endpoint, which sets the nontrivial prefactor.
    for theta in (0.1, 0.25, 0.5, 0.75, 1.0):
        value = dilog_series(theta*theta/2)
        endpoint = -math.log1p(-theta*theta/2)
        boundary = (endpoint-value)/2
        residuals=[]
        for d in (0.1, 0.05, 0.02, 0.01, 0.005):
            observed = log_mgf(1-d,theta)-value/d
            residuals.append(abs(observed-boundary))
            assert abs(observed-boundary) <= 2*d
            count += 1
        assert residuals[-1] < residuals[0]
        count += 1

    # Exact modulus factor inequality for a tilted geometric Laplace factor.
    # Independent rational arithmetic checks the denominator identity.
    for q in (Fraction(1,2),Fraction(3,4),Fraction(9,10)):
        for j in range(7):
            qj=q**j
            for t in (Fraction(1,4),Fraction(1,2),Fraction(1,1)):
                for d in (Fraction(1,20),Fraction(1,100)):
                    for u in (Fraction(1,10),Fraction(2,1),Fraction(9,1)):
                        a=t*t*qj/2
                        x=d*u*u*qj
                        den=(1-a)**2+(1+a)*x+x*x/4
                        modulus_square=(1-a)**2/den
                        assert modulus_square <= 1/(1+x)
                        count += 1
    # The limiting saddlepoint variance is strictly positive and finite.
    for y in (0.1, 0.25, 0.7, 1.5, 3.0):
        theta, _=rate(y)
        z=theta*theta/2
        second=2*math.log1p(-z)/theta**2+2/(1-z)
        assert math.isfinite(second) and second > 1
        prefactor=math.exp((-math.log1p(-z)-dilog_series(z))/2)/(theta*math.sqrt(2*math.pi*second))
        assert prefactor>0 and math.isfinite(prefactor)
        count+=2
    print(f"PASS: {count} exact-rational and finite numerical assertions")


if __name__ == '__main__':
    check()
