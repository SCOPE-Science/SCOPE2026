#!/usr/bin/env python3
"""Finite numerical corroboration for first-level Fock disk concentration.
All-mode and all-radius statements follow from the accompanying analytic proof.
"""
import math
import random
import mpmath as mp
mp.mp.dps = 60
checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def eig(n, t):
    t = mp.mpf(t)
    if n == 0:
        return 1 - (1+t)*mp.exp(-t)
    return mp.gammainc(n, 0, t)/mp.factorial(n-1) + mp.exp(-t)*t**n*(n-1-t)/mp.factorial(n)

def integral(n, t):
    t = mp.mpf(t)
    if n == 0:
        return mp.quad(lambda x: x*mp.exp(-x), [0,t])
    return mp.quad(lambda x: x**(n-1)*(n-x)**2*mp.exp(-x)/mp.factorial(n), [0,t])

radii = [mp.mpf('0.01'), mp.mpf('0.2'), mp.mpf('0.7'),
         mp.mpf('0.99'),mp.mpf('1'),mp.mpf('1.01'),
         mp.mpf('1.5'),mp.mpf('2'),mp.mpf('2.5'),
         mp.mpf('3'),mp.mpf('4.2'),mp.mpf('8.1'),mp.mpf('15')]
rng=random.Random(260825)
for _ in range(20):
    radii.append(mp.mpf(rng.uniform(0.015,12)))

for t in radii:
    for n in range(19):
        analytic=eig(n,t)
        if n<=8:
            check(abs(analytic-integral(n,t)) < mp.mpf('1e-43'),f'integral {n},{t}')
        check(-mp.mpf('1e-50') < analytic < 1+mp.mpf('1e-50'),f'range {n},{t}')
        if n>=1:
            delta=eig(n+1,t)-analytic
            expected=-mp.exp(-t)*t**n*(t-n)*(t-n-1)/mp.factorial(n+1)
            check(abs(delta-expected)<mp.mpf('1e-45'),f'difference {n},{t}')
    check(abs((eig(1,t)-eig(0,t)) -mp.exp(-t)*t*(1-t)) <mp.mpf('1e-47'),f'first gap {t}')
    eigen=[eig(n,t) for n in range(75)]
    expected=1-mp.exp(-t)*(1+(t*t if t<1 else t))
    check(abs(max(eigen)-expected)<mp.mpf('1e-45'),f'operator norm {t}')
    if t<1:
        check(all(eigen[1]>x for i,x in enumerate(eigen) if i!=1),f'one mode {t}')
    if t>1:
        check(all(eigen[0]>x for i,x in enumerate(eigen) if i!=0),f'zero mode {t}')
    if t==1:
        check(abs(eigen[0]-eigen[1])<mp.mpf('1e-50') and abs(eigen[1]-eigen[2])<mp.mpf('1e-50'), 'triple maximal crossing')
        check(eigen[0]>eigen[3], 'other modes lower')
for m in range(1,11):
    check(abs(eig(m-1,m)-eig(m,m))<mp.mpf('1e-47'), f'integer left tie {m}')
    check(abs(eig(m,m)-eig(m+1,m))<mp.mpf('1e-47'), f'integer right tie {m}')
    check(eig(m,m)<mp.mpf('0.5'), f'gamma median {m}')
print(f'PASS: {checks} deterministic checks, 60-decimal-digit working precision')
