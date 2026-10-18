"""Independent finite checks for the two-term spherical-depth asymptotic.

Requires mpmath and numpy; run `python check_depth_asymptotic.py`.
The theorem's all-n assertion is established in RESULT.md, not by this script.
"""
import math
import mpmath as mp
import numpy as np

mp.mp.dps = 42


def coefficient(n, j):
    a = mp.pi / n
    return mp.quad(lambda t: mp.cos(j*n*t)/mp.cos(t)**2, [0, a])/mp.tan(a)


def depth_fourier(n, max_odd=61):
    if n % 2 == 0:
        return mp.mpf('0.5')
    signed = mp.fsum(((-1)**((n*j-1)//2))*coefficient(n,j)**2/(n*j)
                     for j in range(1,max_odd+1,2))
    return mp.mpf('0.5')-2*signed/mp.pi


def depth_fft(n, grid=262144):
    alpha=math.pi/n
    t=2*math.pi*np.arange(grid)/grid
    a=((t+alpha)%(2*alpha))-alpha
    density=1/(2*n*math.tan(alpha)*np.cos(a)**2)
    weights=density/density.sum()
    autocorr=np.fft.ifft(np.abs(np.fft.fft(weights))**2).real
    return float(autocorr[np.cos(t)<=0].sum())


def two_term(n):
    return mp.mpf('0.5')+(-1)**((n+1)//2)*(5*mp.pi**4/(192*n**5)+7*mp.pi**6/(720*n**7))


def main():
    triangle=mp.mpf(1)/3+mp.log(3)/6
    v3=depth_fourier(3, max_odd=121)
    assert abs(v3-triangle)<mp.mpf('1e-11'), (v3, triangle)
    print('TRIANGLE_BASELINE_OK', mp.nstr(v3, 18))
    for n in [3,4,5,6,7,8,9,11,15,21]:
        val=depth_fourier(n, max_odd=91)
        independent=depth_fft(n)
        assert abs(float(val)-independent)<0.000011, (n,val,independent)
        if n%2:
            sign=(-1)**((n+1)//2)
            assert sign*(val-mp.mpf('.5'))>0, n
            if n>=5:
                err=abs(val-two_term(n))
                assert err< 55/mp.mpf(n)**9, (n,err)
                print('ODD',n,mp.nstr(val,18),'second_order_residual',mp.nstr(err,6))
            else:
                print('ODD',n,mp.nstr(val,18))
        else:
            assert val==mp.mpf('.5')
            print('EVEN',n,'0.5')
    for n in [11,21,41]:
        for j in [1,3,5]:
            exact=coefficient(n,j)
            approx=(-1)**j*(mp.mpf(2)/(j*j*n*n)+(2*mp.pi**2/(j*j)-mp.mpf(16)/(j**4))/n**4)
            assert abs(exact-approx)<mp.mpf('240')/(j*j*n**6),(n,j)
    print('VERIFY_OK independent_FFT_checks=10 coefficients=9 triangle_baseline=1')


if __name__=='__main__':
    main()
