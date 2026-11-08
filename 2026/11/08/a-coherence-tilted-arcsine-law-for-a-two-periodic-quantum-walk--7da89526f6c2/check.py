#!/usr/bin/env python3
"""Independent numerical diagnostics for the dimerized quantum-walk limit law.

This program checks finite Fourier quadratures and finite-time wave evolution.
It does not prove weak convergence or establish publication priority.
Requires NumPy.
"""
import math
import numpy as np


def bloch(a, b, c, d, N=32768):
    k = 2*np.pi*(np.arange(N)+0.5)/N - np.pi
    E = np.abs(a+b*np.exp(1j*k))
    v = -2*a*b*np.sin(k)/E
    z = np.conj(c)*d
    s = 2*(z.real*(a+b*np.cos(k)) + z.imag*b*np.sin(k))/E
    return k, E, v, s


def moments_formula(a, b, c, d, j):
    m = min(a, b)
    w = (np.conj(c)*d).imag
    if j % 2 == 0:
        return math.comb(j, j//2)*m**j
    return -(w/a)*math.comb(j+1, (j+1)//2)*m**(j+1)


def finite_time_distribution(a, b, c, d, T, N=16384):
    k = 2*np.pi*np.arange(N)/N
    E = np.abs(a+b*np.exp(1j*k))
    q = a+b*np.exp(-1j*k)
    e = np.cos(T*E)
    f = -1j*np.sin(T*E)/E
    F0 = e*c + f*q*d
    F1 = e*d + f*np.conj(q)*c
    u0 = np.fft.ifft(F0)
    u1 = np.fft.ifft(F1)
    n = np.arange(N)
    n[n>=N//2] -= N
    x0 = 2*n/T
    x1 = (2*n+1)/T
    p0 = np.abs(u0)**2
    p1 = np.abs(u1)**2
    return x0, x1, p0, p1


def assert_close(actual, expected, atol, explanation):
    assert abs(actual-expected) <= atol, (explanation, actual, expected, atol)


def run():
    cases = [
        (1., 2., 2**-.5+0j, 1j*2**-.5),
        (2., 1., 2**-.5+0j, 1j*2**-.5),
        (.5, 3., 2**-.5+0j, 1j*2**-.5),
        (1., 1., 2**-.5+0j, 1j*2**-.5),
        (1.7, .9, np.sqrt(.3)+0j, np.exp(0.7j)*np.sqrt(.7)),
        (1.7, .9, np.sqrt(.3)+0j, np.exp(-0.7j)*np.sqrt(.7)),
        (2.1, 1.3, 1+0j, 0j),
        (2.1, 1.3, 0j, 1+0j),
        (2.1, 1.3, 2**-.5+0j, 2**-.5+0j),
    ]
    assertions = 0
    for a,b,c,d in cases:
        assert_close(abs(c)**2+abs(d)**2, 1., 1e-13, 'initial state normalization'); assertions += 1
        k,E,v,s = bloch(a,b,c,d)
        assert np.max(np.abs(s)) <= 1+3e-13; assertions += 1
        assert np.max(np.abs(v)) <= 2*min(a,b)+2e-12; assertions += 1
        for j in range(9):
            num = np.mean(((1+s)*v**j +(1-s)*(-v)**j)/2)
            pred = moments_formula(a,b,c,d,j)
            assert_close(num, pred, 2e-6 + abs(pred)*2e-5, f'Bloch moment j={j} a={a} b={b}'); assertions += 1
        for T in (40., 80.):
            x0,x1,p0,p1=finite_time_distribution(a,b,c,d,T)
            assert_close(np.sum(p0+p1), 1, 2e-12, 'finite-time total norm'); assertions += 1
            mean=np.sum(p0*x0+p1*x1)
            assert_close(mean, moments_formula(a,b,c,d,1), 0.095, 'finite-time mean'); assertions += 1
            for tau in (.4, .9, 1.7):
                actual=np.sum(p0*np.exp(1j*tau*x0)+p1*np.exp(1j*tau*x1))
                kk,EE,vv,ss=bloch(a,b,c,d)
                predicted=np.mean((1+ss)/2*np.exp(1j*tau*vv)+(1-ss)/2*np.exp(-1j*tau*vv))
                assert_close(actual,predicted,.095,'finite-time characteristic function'); assertions += 1
    print(f'PASS: {assertions} finite diagnostic assertions; no assertion asserts an infinite-time proof')


if __name__=='__main__':
    run()
