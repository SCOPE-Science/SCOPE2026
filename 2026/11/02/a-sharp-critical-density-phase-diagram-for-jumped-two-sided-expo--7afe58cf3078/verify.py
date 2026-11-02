"""Supplementary checks for critical Gabor bounds of jumped exponential windows.

This file uses only the Python standard library. It checks finite Zak sums,
pointwise endpoint identities, threshold classifications, and sharp-bound
approximations. Infinite-dimensional assertions are proved analytically.
"""
import cmath
import math


def zak_closed(rate, amplitude, x, theta):
    r = math.exp(-rate)
    z = cmath.exp(1j * theta)
    return math.exp(-rate*x)/(1-r*z) + amplitude*r*math.exp(rate*x)/(z-r)


def zak_truncated(rate, amplitude, x, theta, count=100):
    out = 0j
    for n in range(-count, count+1):
        t = x+n
        g = math.exp(-rate*t) if t >= 0 else amplitude*math.exp(rate*t)
        out += g * cmath.exp(1j*n*theta)
    return out


def predicted(rate, amplitude):
    r = math.exp(-rate)
    if amplitude < r:
        lower = ((r-amplitude)/(1+r))**2
    elif amplitude > 1/r:
        lower = ((amplitude*r-1)/(1+r))**2
    else:
        lower = 0.0
    upper = ((1+amplitude*r) if amplitude <= 1 else (r+amplitude))**2/(1-r)**2
    return lower, upper


def independent_endpoint(rate, amplitude, x):
    r = math.exp(-rate)
    p = math.exp(-rate*x)
    q = amplitude*r*math.exp(rate*x)
    return ((p-q)/(1+r))**2, ((p+q)/(1-r))**2


def run():
    passed=0
    rates=(0.5,1.0,1.6,2.3)
    for rate in rates:
        r=math.exp(-rate)
        amplitudes=(r/3, r*0.98, r, r*1.02, 0.8, 1.0,
                    1/r*0.98, 1/r, 1/r*1.02, 3/r)
        for c in amplitudes:
            exact_min, exact_max=predicted(rate,c)
            sample_min=math.inf
            sample_max=0.0
            for i in range(251):
                x=(i+0.5)/251
                lo,hi=independent_endpoint(rate,c,x)
                assert abs(abs(zak_closed(rate,c,x,math.pi))**2-lo)<1e-10*max(1,lo)
                assert abs(abs(zak_closed(rate,c,x,0))**2-hi)<1e-10*max(1,hi)
                passed+=2
                for j in (0,2,7,13,19,31):
                    theta=2*math.pi*j/37
                    y=abs(zak_closed(rate,c,x,theta))**2
                    assert lo-1e-9*max(1,lo)<=y<=hi+1e-9*max(1,hi)
                    passed+=1
                sample_min=min(sample_min,lo)
                sample_max=max(sample_max,hi)
            assert sample_min>=exact_min-1e-12
            assert sample_max<=exact_max+1e-12
            # Numerical finite mesh must approach both extremal boundary limits.
            assert sample_min-exact_min<0.04*max(1,exact_max)
            assert exact_max-sample_max<0.04*max(1,exact_max)
            passed+=4
            for x in (0.11,0.37,0.79):
                for theta in (0,0.5,1.2,math.pi,5.1):
                    z0=zak_closed(rate,c,x,theta)
                    zn=zak_truncated(rate,c,x,theta,100)
                    assert abs(zn-z0)<1e-12*max(1,abs(z0))
                    passed+=1
            if c<r or c>1/r:
                cond=exact_max/exact_min
                infimum=((1+r)/(r*(1-r)))**2
                assert cond>=infimum-1e-8
                passed+=1
    # Explicit interior zero at theta=pi, exactly when the jump is in the nonframe interval.
    for rate in rates:
        r=math.exp(-rate)
        for c in (r, math.sqrt(r), 1, 1/math.sqrt(r), 1/r):
            x=(math.log(1/(c*r)))/(2*rate)
            assert -1e-12<=x<=1+1e-12
            assert abs(zak_closed(rate,c,x,math.pi))<1e-10
            passed+=2
    return passed


if __name__ == '__main__':
    print('PASS',run(),'supplementary assertions')
