"""Reproducible exact-arithmetic and numerical checks for relaxed midpoint modal drift.

Requires only Python 3.9+ from the standard library. Checks illustrate finite
instances; the all-step and asymptotic assertions require the analytic proof.
"""
import math
from fractions import Fraction as Q


def energy_step(e, squared_frequency, h):
    t = [h * h * w for w in squared_frequency]
    numerator = sum(tj * ej for tj, ej in zip(t, e))
    denominator = sum(tj * (1 + tj / 4) * ej for tj, ej in zip(t, e))
    gamma = numerator / denominator
    factors = [1 - gamma * tj + gamma * gamma * tj * (1 + tj / 4) for tj in t]
    return [ej * gj for ej, gj in zip(e, factors)], gamma, factors


def test_exact():
    for h in (Q(1, 3), Q(2, 3), Q(3, 2), Q(4, 1)):
        for e in ((Q(1), Q(1)), (Q(2), Q(7)), (Q(1), Q(2), Q(3))):
            squared_frequency = (Q(1), Q(9)) if len(e) == 2 else (Q(1), Q(4), Q(16))
            new, gam, factors = energy_step(e, squared_frequency, h)
            assert sum(new) == sum(e)
            assert gam > 0
            assert new[-1] > e[-1]
            assert all(x > 0 for x in new)
            t = [h * h * f for f in squared_frequency]
            q = sum(tj * tj * ej for tj, ej in zip(t, e)) / sum(tj * ej for tj, ej in zip(t, e))
            c = 1 + q / 4
            assert gam == 1 / c
            for j in range(len(e)):
                assert factors[j] == 1 + t[j] * (t[j] - q) / (4 * c * c)
                assert factors[-1] - factors[j] == ((t[-1] - t[j]) * (t[-1] + t[j] - q)) / (4 * c * c)
    print('exact rational conservation and pairwise identities: PASS')


def test_long_time():
    h = 0.4
    freqsq = (1.0, 4.0, 9.0)
    e = [0.4, 0.3, 0.3]
    total = sum(e)
    prevmax = e[-1]
    for step in range(3000):
        e, gamma, _ = energy_step(e, freqsq, h)
        assert abs(sum(e) - total) < 2e-12
        assert e[-1] >= prevmax - 1e-13
        prevmax = e[-1]
    assert e[-1] > total * (1 - 1e-10), e
    print('long-time high-frequency condensation: PASS')


def slow_field(x, a, b):
    k = a * b * (b - a) / 4
    return k * x * (1 - x) / (a * (1 - x) + b * x)


def slow_solution(x0, a, b, horizon):
    def primitive(x):
        return a * math.log(x) - b * math.log1p(-x)
    target = primitive(x0) + a*b*(b-a)*horizon/4
    lo, hi = x0, 1 - 1e-14
    for _ in range(80):
        mid = (lo+hi)/2
        if primitive(mid) > target:
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2


def test_slow_time():
    x0 = 0.25
    a, b = 1.0, 4.0
    horizon = 1.0
    exact = slow_solution(x0, a, b, horizon)
    errs=[]
    for h in (0.5, 0.25, 0.125):
        n=round(horizon/h**4)
        e=[1-x0, x0]
        for _ in range(n):
            e,_,_=energy_step(e,(a,b),h)
        err=abs(e[1]-exact)
        errs.append(err)
        assert err<0.45*h*h,(h,err,e[1],exact)
    assert errs[1] < errs[0]*0.31
    assert errs[2] < errs[1]*0.30
    print('critical h^-4 step / h^-3 physical-time scaling: PASS',
          'slow-energy=',round(exact,10), 'errors=', [round(t,9) for t in errs])


def test_asymptotic_rate():
    a,b=1.0,4.0
    h=0.65
    t1,t2=h*h*a,h*h*b
    rho=1-t1*(t2-t1)/(4*(1+t2/4)**2)
    e=[0.5,0.5]
    values=[]
    for n in range(700):
        en,_,_=energy_step(e,(a,b),h)
        if n in (350,500,600):
            values.append((n,e[0],en[0]/e[0]))
        e=en
    assert all(abs(r-rho)<1e-7 for n,v,r in values)
    print('sharp lower-mode geometric rate: PASS', 'rho=',round(rho,12))

if __name__=='__main__':
    test_exact()
    test_long_time()
    test_slow_time()
    test_asymptotic_rate()
    print('VERIFY_OK')
