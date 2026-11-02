"""Reproduce selected numerical consequences of the geometric Matérn increment theorem.

Requires Python 3 and mpmath >=1.2. These tests are illustrative finite
checks; the infinite-series and minimax statements rest on the written proof.
"""
import mpmath as mp

mp.mp.dps = 60
sigma = mp.mpf(2) / 3


def base_increment(d, t):
    t = mp.mpf(t)
    if t < mp.mpf("1e-8"):
        return 2*(d-1)*mp.fsum([(-1)**k/mp.factorial(k)
            *((d+2)*t**(k+2)/(k+2)-t**(k+3)/(k+3)) for k in range(32)])
    return 2 * (d - 1) * (d - (d + d*t - t*t) * mp.exp(-t))


def mellin_transform(d, s):
    return 2 * (d - 1) * (d + s) * mp.gamma(2 - s) / s


def harmonic(d, q, k):
    L = mp.log(q)
    value = mellin_transform(d, sigma + 2j*mp.pi*k/L) / L
    return mp.re(value) if k == 0 else value


def trace_sum(d, q, r, left=-240, right=240):
    r = mp.mpf(r)
    return mp.fsum([mp.power(q, sigma*j)*base_increment(d, r*mp.power(q, -j))
                    for j in range(left, right+1)])


def finite_error_bound(d, q, r, left, right):
    md = 2*(d-1)*(d + (d+4)*mp.exp(-d-2))
    cd = (d-1)*(d+2)
    return (md*mp.power(q, sigma*(left-1))/(1-mp.power(q,-sigma))
           + cd*r*r*mp.power(q, -mp.mpf(4)*(right+1)/3)
             /(1-mp.power(q, -mp.mpf(4)/3)))


checks = 0
for d in (2, 3):
    s0 = sigma
    integral = mp.quad(lambda t: t**(-1-s0) * base_increment(d, t),
                       [0, mp.mpf('.1'), 1, 10, mp.inf])
    assert mp.almosteq(integral, mellin_transform(d, s0), rel_eps=mp.mpf('1e-19'))
    checks += 1
    for qstr in ('1.5','2','4.795077','8'):
        q = mp.mpf(qstr)
        c0 = harmonic(d, q, 0)
        assert c0 > 0 and abs(harmonic(d,q,1)) > 0
        checks += 1
        for phase in ('0.07','0.24','0.51','0.81'):
            r = mp.power(q, mp.mpf(phase))
            direct = trace_sum(d,q,r)/mp.power(r,sigma)
            fourier = c0 + 2*mp.re(mp.fsum(
                [harmonic(d,q,k)*mp.exp(2j*mp.pi*k*mp.mpf(phase))
                 for k in range(1,18)]))
            assert abs(direct-fourier) < mp.mpf('1e-20')*c0
            assert abs(trace_sum(d,q,q*r)/mp.power(q,sigma)-trace_sum(d,q,r)) < mp.mpf('1e-20')
            checks += 2
        for r in (mp.mpf('.08'), mp.mpf('.7'),mp.mpf('2.6')):
            left,right=-15,15
            finite=trace_sum(d,q,r,left,right)
            infinite=trace_sum(d,q,r)
            bound=finite_error_bound(d,q,r,left,right)
            assert finite >= 0 and infinite >= finite and infinite-finite <= bound*(1+mp.mpf('1e-25'))
            checks += 1

for d in (2,3):
    q=mp.mpf('1.45')
    c0=harmonic(d,q,0)
    c1=abs(harmonic(d,q,1))
    pred=(2*mp.sqrt(2*mp.pi)/((3*d+2)*mp.gamma(mp.mpf(4)/3))
           * (2*mp.pi/mp.log(q))**(mp.mpf(5)/6)*mp.exp(-mp.pi**2/mp.log(q)))
    assert abs(c1/c0/pred-1) < mp.mpf('.05')
    checks += 1

print('Numerical checks passed:',checks)
for d in (2,3):
    q=mp.mpf('4.795077')
    print('Dimension',d,'q',q,'mean',mp.nstr(harmonic(d,q,0),16),
          'first harmonic / mean',mp.nstr(abs(harmonic(d,q,1))/harmonic(d,q,0),14))
