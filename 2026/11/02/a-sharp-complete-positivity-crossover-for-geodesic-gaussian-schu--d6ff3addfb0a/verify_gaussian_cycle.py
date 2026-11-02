#!/usr/bin/env python3
"""Supplementary finite tests for Gaussian Schur symbols on cycle graphs.

Requires mpmath. Finite tests do not prove the stated asymptotic theorem.
"""
import mpmath as mp

mp.mp.dps = 90


def eigenvalue(n, j, c):
    theta = 2 * mp.pi * j / n
    t = c / n
    return mp.fsum(mp.exp(-t * min(k, n - k) ** 2) * mp.cos(theta * k)
                   for k in range(n))


def nearest_even_index(n):
    return 2 * ((n // 2) // 2)


def theta_periodized(t, theta, limit=35):
    return mp.sqrt(mp.pi/t) * mp.fsum(
        mp.exp(-(theta-2*mp.pi*q)**2/(4*t)) for q in range(-limit, limit+1))


def omitted_tail(n, j, c, max_index=500):
    theta = 2*mp.pi*j/n
    t = c/n
    if n % 2 == 0:
        m = n//2
        return mp.exp(-t*m*m)*mp.cos(theta*m) + 2*mp.fsum(
            mp.exp(-t*k*k)*mp.cos(theta*k) for k in range(m+1,max_index+1))
    m = n//2
    return 2*mp.fsum(mp.exp(-t*k*k)*mp.cos(theta*k)
                     for k in range(m+1,max_index+1))


def predicted_negative(n, j, c):
    if n%2==0:
        return -mp.tanh(c/2)*mp.exp(-c*n/4)
    delta = n-2*j
    return -mp.pi*delta/n * mp.exp(-c/2)*(1-mp.exp(-c))/(1+mp.exp(-c))**2 * mp.exp(-c*n/4)


def main():
    checked = 0
    # Exact finite Fourier/periodization identities, high precision.
    for n in (7, 8, 11, 12, 19, 20, 31, 32):
        for c in (mp.mpf('0.8'), mp.mpf('1.7'), mp.mpf('4.5')):
            for j in (0, 1, nearest_even_index(n)):
                a = eigenvalue(n,j,c)
                theta = 2*mp.pi*j/n
                b = theta_periodized(c/n,theta)-omitted_tail(n,j,c)
                assert mp.almosteq(a,b,rel_eps=mp.mpf('1e-48'),abs_eps=mp.mpf('1e-48'))
                checked += 1

    # High-precision complete spectrum at dimensions safely separated from crossover.
    for n in (20, 24, 31, 32, 47, 48, 63, 64):
        for c in (mp.mpf('4'), mp.mpf('5')):
            assert min(eigenvalue(n,j,c) for j in range(n)) > 0
            checked += 1
    for n in (32, 47, 48, 63, 64, 95, 96, 127, 128):
        for c in (mp.mpf('1'), mp.mpf('2')):
            j = nearest_even_index(n)
            assert eigenvalue(n,j,c) < 0
            checked += 1

    # Ratio of measured negative witness to the predicted parity constant tends to one.
    for n in (95, 96, 127, 128, 255, 256):
        for c in (mp.mpf('0.8'), mp.mpf('1.4')):
            j = nearest_even_index(n)
            ratio = eigenvalue(n,j,c)/predicted_negative(n,j,c)
            assert abs(ratio-1) < mp.mpf('0.07'), (n,c,ratio)
            checked += 1
    print('PASS: %d high-precision finite checks (not an infinite proof)'%checked)


if __name__ == '__main__':
    main()
