#!/usr/bin/env python3
"""Finite checks of the slope law for one-step binary tortoise images.
Uses high-precision mechanical rotation interval sampling and an independent
single-orbit factor catalogue. These finite checks are not an infinite proof.
"""
from decimal import Decimal, getcontext, ROUND_FLOOR

getcontext().prec = 90
D = Decimal

def dfloor(x):
    return int(x.to_integral_value(rounding=ROUND_FLOOR))

def one_step(w):
    j = w.find('1')
    return w if j == -1 else w[:j] + w[j+1:] + '1'

def factor_at(alpha, phase, length):
    return ''.join(str(dfloor(phase+(i+1)*alpha)-dfloor(phase+i*alpha))
                   for i in range(length))

def check_interval(alpha, n):
    thresholds = [D(0)] + sorted([D(dfloor(j*alpha)+1)-j*alpha
                                  for j in range(1, n+1)]) + [D(1)]
    blocks = [factor_at(alpha, (a+b)/2, n)
              for a, b in zip(thresholds, thresholds[1:])]
    assert len(set(blocks)) == n+1
    assert blocks == sorted(blocks)
    images = [one_step(w) for w in blocks]
    assert images == sorted(images)
    q = dfloor(1/alpha)
    assert len(set(images)) == n+1-min(q,n-1)
    if n > 1:
        # Identify thresholds by exact integer k in {1,...,n}.
        labels = sorted(range(1,n+1), key=lambda k:D(dfloor(k*alpha)+1)-k*alpha)
        equal_edges = [labels[i] for i in range(n) if images[i]==images[i+1]]
        assert sorted(equal_edges) == list(range(1,min(q,n-1)+1))
    return len(set(images))

def check_orbit(alpha, n, length):
    s = factor_at(alpha, D(0), length)
    words = {s[i:i+n] for i in range(len(s)-n+1)}
    assert len(words) == n+1, (str(alpha),n,len(words))
    q = dfloor(1/alpha)
    assert len({one_step(w) for w in words}) == n+1-min(q,n-1)

cases = {
    'golden_high': (D(5).sqrt()-1)/2,
    'golden_low': (3-D(5).sqrt())/2,
    'silver_low': D(2).sqrt()-1,
    'sqrt3_over_10': D(3).sqrt()/10,
    'sqrt2_over_100': D(2).sqrt()/100,
}

for name, a in cases.items():
    q = dfloor(1/a)
    for n in range(1, 101):
        check_interval(a, n)
    for n in range(1, 61):
        check_orbit(a, n, 25000)
    print(f'{name}: floor(1/alpha)={q}; n=1..100 checked by intervals; '
          f'n=1..60 checked by 25000-symbol orbit; PASS')
