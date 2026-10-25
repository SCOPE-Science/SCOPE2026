"""Numerical checks for sharp dimension bounds in a Gauss survivor set.

Requires Python 3 and mpmath >= 1.3.0. The analytical theorem does not
rely on numerical root-finding or finite sampling.
"""
import mpmath as mp

mp.mp.dps = 55


def bracketed_root(N, offset=0):
    """Find root of Hurwitz-zeta branch-pressure envelope by bisection."""
    a = mp.mpf('0.500000001')
    b = mp.mpf('0.999999999')
    q = mp.mpf(N) + offset
    assert mp.zeta(2*a, q) > 1 and mp.zeta(2*b, q) < 1
    for _ in range(200):
        mid = (a+b)/2
        if mp.zeta(2*mid, q) > 1:
            a = mid
        else:
            b = mid
    return (a+b)/2


def main():
    print('N lower_root upper_root W_prediction upper_minus_prediction width')
    for N in (20, 50, 100, 300, 1000, 10000):
        L = mp.log(N)
        w = mp.lambertw(L)
        prediction = mp.mpf('0.5') + w/(2*L) + w*w/(4*N*L*L*(w+1))
        lo = bracketed_root(N, mp.mpf(1)/N)
        hi = bracketed_root(N)
        assert mp.mpf('0.5') < lo < hi < 1
        assert abs(hi-prediction) < mp.mpf(1)/(N*N*L)
        assert hi-lo < mp.mpf(2)/(N*N*L)
        print(N, *(mp.nstr(t, 15) for t in (lo,hi,prediction,hi-prediction,hi-lo)))
    print('NUMERICAL_PRESSURE_ENCLOSURES_PASS 6')
    print('COUNTABLE_IFS_DIMENSION_AND_ASYMPTOTICS_REQUIRE_ANALYTIC_PROOF')


if __name__ == '__main__':
    main()
