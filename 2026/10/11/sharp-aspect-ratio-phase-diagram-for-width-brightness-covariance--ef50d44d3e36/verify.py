"""Reproducible finite consistency checks for width--brightness covariance.

Python standard library only. These checks do not replace the analytic proof.
"""
import itertools
import math
import random


def beta(d):
    mu = math.exp(math.lgamma(d / 2) - math.lgamma((d + 1) / 2)) / math.sqrt(math.pi)
    return mu * mu - 2 / (math.pi * d)


def critical_q(d):
    return (1 - 2 / math.pi) / beta(d)


def covariance(a):
    d = len(a)
    volume = math.prod(a)
    q = sum(a) * sum(1 / x for x in a)
    return volume * (1 - 2 / math.pi - beta(d) * q)


def q_range(d, ratio):
    qmin = (d - 2 + math.sqrt(ratio) + 1 / math.sqrt(ratio)) ** 2
    qmax = d * d + (d * d // 4) * (ratio + 1 / ratio - 2)
    return qmin, qmax


def transition(d):
    t = critical_q(d)
    z = 2 + (t - d * d) / (d * d // 4)
    lower = (z + math.sqrt(z*z - 4)) / 2
    s = math.sqrt(t) - (d - 2)
    upper = ((s + math.sqrt(s*s - 4)) / 2) ** 2
    return lower, upper


def spherical_covariance_estimate(a, n=50000, seed=8):
    g = random.Random(seed)
    d = len(a)
    vol = math.prod(a)
    sw = sb = swb = 0.
    for _ in range(n):
        x = [g.gauss(0, 1) for i in range(d)]
        norm = math.sqrt(sum(v*v for v in x))
        u = [abs(v)/norm for v in x]
        w = sum(a[i]*u[i] for i in range(d))
        b = vol*sum(u[i]/a[i] for i in range(d))
        sw += w
        sb += b
        swb += w*b
    return swb/n - (sw/n)*(sb/n)


def check():
    count = 0
    for d in range(2, 13):
        t = critical_q(d)
        assert t > d*d
        lo, hi = transition(d)
        assert 1 < lo and lo <= hi + 1e-12
        assert abs(q_range(d, lo)[1]-t) <= 2e-8*max(1,t)
        assert abs(q_range(d, hi)[0]-t) <= 2e-8*max(1,t)
        if d == 2:
            assert abs(lo-hi) < 1e-10
        else:
            assert lo < hi
        count += 5
        rng = random.Random(331+d)
        for ratio in [1.00001, 1.1, lo, (lo+hi)/2, hi, hi+1, 10]:
            a = [1, ratio] + [math.exp(rng.random()*math.log(ratio)) for _ in range(d-2)]
            q = sum(a)*sum(1/v for v in a)
            mi, ma = q_range(d, ratio)
            assert mi - 1e-9 <= q <= ma + 1e-9
            amin = [1, ratio]+[math.sqrt(ratio)]*(d-2)
            q0 = sum(amin)*sum(1/x for x in amin)
            assert abs(q0-mi) <= 2e-10*max(1,mi)
            k = d//2
            amax = [1]*k+[ratio]*(d-k)
            q1 = sum(amax)*sum(1/x for x in amax)
            assert abs(q1-ma) <= 2e-10*max(1,ma)
            count += 3
        # Local maximality and minimality also checked over all binary patterns.
        for ratio in [1.05, 1.6, 3]:
            for bits in itertools.product((1.0,ratio),repeat=d-2):
                a=(1.0,ratio)+bits
                q=sum(a)*sum(1/x for x in a)
                mi,ma=q_range(d,ratio)
                assert mi-1e-9<=q<=ma+1e-9
                count += 1
    cases = [
        [1,1], [1,2], [1,1,1], [1,1,1.75],
        [1,1.38,1.9], [1,1,1,1], [1,1,2,2],
    ]
    for i,a in enumerate(cases):
        analytic = covariance(a)
        empirical = spherical_covariance_estimate(a, n=65000, seed=1481+i)
        # Sampling tolerance is deliberately conservative; it is not a certificate.
        assert abs(empirical - analytic) <= 0.015*math.prod(a), (a, empirical, analytic)
        count += 1
    d=2000
    l,h=transition(d)
    v=2+4*(math.pi-3)
    llim=(v+math.sqrt(v*v-4))/2
    hcoeff=(math.sqrt(math.pi-2)-1)**2
    assert abs(l-llim)<0.01
    assert abs(h/d**2-hcoeff)<0.0002
    count += 2
    return count


if __name__ == '__main__':
    print('VERIFY_OK', check())
