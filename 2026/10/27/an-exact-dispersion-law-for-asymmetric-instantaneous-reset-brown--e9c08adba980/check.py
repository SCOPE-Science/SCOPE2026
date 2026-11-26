"""Bounded numerical diagnostics for the physical drift optimizer."""
from math import exp, expm1


def scaled_slope(x, c):
    """x times the log speed derivative; positive iff speed increases."""
    def E(y):
        return exp(-2*y)/(-expm1(-2*y))
    return 2-(1-c)*x+2*x*(c*E(c*x)-E(x))


def root(c):
    lo, hi = 0.125, 4/(1-c)
    assert scaled_slope(lo,c)>0 and scaled_slope(hi,c)<0
    for _ in range(100):
        mid=(lo+hi)/2
        if scaled_slope(mid,c)>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def main():
    last=0
    for c in (0.01,0.1,0.3,0.5,0.8,0.95,0.99,0.99999):
        x=root(c)
        assert x>last
        assert abs(scaled_slope(x,c))<2e-12
        assert scaled_slope(0.8*x,c)>0>scaled_slope(1.2*x,c)
        print(f'c={c:.5f}, x_*={x:.10g}, r_* L^2/D={4*x*x:.10g}, (1-c)x_*={(1-c)*x:.10g}')
        last=x
    for c in (0.95,0.99,0.99999):
        assert abs((1-c)*root(c)-2)<1e-10
    print('PASS: eight sampled drift roots and three scaled near-endpoint roots')


if __name__=='__main__':
    main()
