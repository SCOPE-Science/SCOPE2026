"""Standalone arithmetic checks for sharp two-moment SIR pressure envelopes.

Requires only the Python standard library. It tests examples, not the
unrestricted Hermite-interpolation and ODE-comparison arguments.
"""
from fractions import Fraction as F
from math import exp, isclose


def extremals(mean, cap, variance):
    b = mean + variance / mean
    c = mean - variance / (cap - mean)
    lower_pressure = [(F(0), variance / (mean * mean + variance)),
                      (b, mean * mean / (mean * mean + variance))]
    upper_pressure = [(c, (cap - mean)**2 / ((cap - mean)**2 + variance)),
                      (cap, variance / ((cap - mean)**2 + variance))]
    return lower_pressure, upper_pressure


def moment(dist, order):
    return sum(weight * atom**order for atom, weight in dist)


def transform(dist, a):
    return sum(float(w) * exp(-float(atom) * a) for atom, w in dist)


def rhs(dist, a, tau, gamma, s0, i0):
    return tau * (i0 + s0 * (1 - transform(dist, a))) - gamma * a


def rk4(dist, t, tau=3.0, gamma=1.0, s0=0.9, i0=0.1, steps=5000):
    h = t / steps
    a = 0.0
    for _ in range(steps):
        k1 = rhs(dist, a, tau, gamma, s0, i0)
        k2 = rhs(dist, a + h*k1/2, tau, gamma, s0, i0)
        k3 = rhs(dist, a + h*k2/2, tau, gamma, s0, i0)
        k4 = rhs(dist, a + h*k3, tau, gamma, s0, i0)
        a += h * (k1 + 2*k2 + 2*k3 + k4) / 6
    return a


def positive_root(dist, tau=3.0, gamma=1.0, s0=0.9, i0=0.1):
    lo, hi = 0.0, tau * (s0+i0) / gamma
    assert rhs(dist,lo,tau,gamma,s0,i0) > 0
    assert rhs(dist,hi,tau,gamma,s0,i0) <= 0
    for _ in range(100):
        mid = (lo+hi)/2
        if rhs(dist,mid,tau,gamma,s0,i0) > 0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def run():
    grids=0
    for mean in [F(1),F(2),F(3)]:
        for gap in [F(2),F(3),F(4)]:
            cap=mean+gap
            for q in [F(1,4),F(1,2),F(3,4)]:
                v=q*mean*(cap-mean)
                low, high=extremals(mean,cap,v)
                for dist in [low,high]:
                    assert sum(p for _,p in dist)==1
                    assert moment(dist,1)==mean
                    assert moment(dist,2)==mean*mean+v
                    assert all(0<=x<=cap and p>0 for x,p in dist)
                gap3=v*cap*(1-v/(mean*(cap-mean)))
                assert moment(high,3)-moment(low,3)==gap3 and gap3>0
                for a in [0.1,0.25,1.0,2.5]:
                    v0=transform(low,a)
                    v1=transform(high,a)
                    assert v1<v0-1.e-14
                    for w in [F(1,4),F(1,2),F(3,4)]:
                        mix=[(x,p*(1-w)) for x,p in low]+[(x,p*w) for x,p in high]
                        assert v1 < transform(mix,a) < v0
                grids+=1
    lo, hi=extremals(F(1),F(3),F(1))
    mid=[(x,p*F(1,2)) for x,p in lo+hi]
    for t in [0.1, 0.5, 1., 2., 5.]:
        a0=rk4(lo,t)
        am=rk4(mid,t)
        a1=rk4(hi,t)
        assert a0<am<a1
    rlow=positive_root(lo)/3
    rmid=positive_root(mid)/3
    rhigh=positive_root(hi)/3
    assert rlow<rmid<rhigh
    assert abs(rlow-0.5314483761174622)<1.e-9
    assert abs(rhigh-0.7745235332146387)<1.e-9
    thirdgap=moment(hi,3)-moment(lo,3)
    coeff=F(3)**4 * F(9,10) * F(1,10)**3 * thirdgap/F(24)
    assert coeff==F(729,160000)  # 0.00455625
    print('VERIFY_OK:',grids,'exact-rational moment/extremality identities;',
          '5 strict trajectory order checks; critical fourth-order coefficient',float(coeff))
    print('EXAMPLE_FINAL_REMOVED:',f'{rlow:.12f}',f'{rhigh:.12f}')


if __name__ == '__main__':
    run()
