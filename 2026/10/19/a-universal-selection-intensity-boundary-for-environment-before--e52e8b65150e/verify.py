#!/usr/bin/env python3
"""Reproduce numerical and symbolic checks for random-payoff Fermi selection."""
import math
import sympy as sp
import mpmath as mp

mp.mp.dps = 55
t, p, s = sp.symbols('t p s', real=True)
a = 2*t+t*t
b = 2*t-t*t
# The averaged-payoff comparator is algebraically distinct from averaging Fermi drifts.
assert sp.simplify(p*a-(1-p)*b-(2*t*(2*p-1)+t*t)) == 0
assert sp.factor(a-b) == 2*t*t
assert sp.factor(a+b) == 4*t
z = mp.findroot(lambda x: mp.tanh(2*x)-x, (mp.mpf('0.8'), mp.mpf('1')))
C = z*z/(2*mp.sinh(2*z))
assert abs(z-mp.mpf('0.9575040240772687406765015305')) < mp.mpf('1e-25')
assert abs(C-mp.mpf('0.1380816117194143794921098069')) < mp.mpf('1e-25')

def pc(strength, frequency):
    aa = 2*frequency+frequency*frequency
    bb = 2*frequency-frequency*frequency
    F = mp.tanh(strength*aa/2)
    G = mp.tanh(strength*bb/2)
    return G/(F+G)

def drift(strength, prob, freq):
    aa=2*freq+freq*freq
    bb=2*freq-freq*freq
    return prob*mp.tanh(strength*aa/2)-(1-prob)*mp.tanh(strength*bb/2)

# Rigorous pointwise derivative sign is proved analytically in RESULT.md.
for freq in [mp.mpf('0.001'),mp.mpf('.1'),mp.mpf('.35'),mp.mpf('.8')]:
    vals=[pc(strength,freq) for strength in [mp.mpf('.01'),mp.mpf('.5'),mp.mpf('2'),mp.mpf('10'),mp.mpf('100')]]
    assert all(v1<v2 for v1,v2 in zip(vals,vals[1:]))
    assert all(mp.mpf('0')<v<mp.mpf('.5') for v in vals)

prob=mp.mpf('0.4')
freq=mp.mpf(2)/3
root=mp.mpf(9)/4*mp.atanh(1/mp.sqrt(3))
assert abs(drift(root,prob,freq))<mp.mpf('1e-50')
assert drift(mp.mpf('1'),prob,freq)>0
assert drift(mp.mpf('2'),prob,freq)<0
assert abs(prob*(2*freq+freq**2)-(1-prob)*(2*freq-freq**2)-mp.mpf(8)/45)<mp.mpf('1e-50')

# Leading-order universal crossover verified at its predicted scaling t=z/s.
errs=[]
for strength in [mp.mpf(100), mp.mpf(1000), mp.mpf(10000)]:
    estimate=strength*(mp.mpf('.5')-pc(strength,z/strength))
    errs.append(abs(estimate-C))
assert errs[2]<errs[1]<errs[0]
assert errs[2]<mp.mpf('3e-7')

# Numeric bound for all sampled frequencies:  s(1/2-pc)<=z^2/(2sinh z), z=s*t.
checks=0
for strength in [mp.mpf('.1'),mp.mpf(1),mp.mpf(3),mp.mpf(25),mp.mpf(100)]:
    for j in range(1,200):
        freq=mp.mpf(j)*mp.mpf('.8')/200
        scaled=strength*freq
        actual=strength*(mp.mpf('.5')-pc(strength,freq))
        bound=scaled**2/(2*mp.sinh(scaled))
        assert actual <= bound+mp.mpf('1e-45')
        checks+=1

print('PASS: symbolic payoff identities, intensity monotonicity, witness transition,')
print('      universal crossover and uniform-tail bound,',checks,'bound cases')
print('critical_s',mp.nstr(root,30))
print('z_star',mp.nstr(z,30))
print('C',mp.nstr(C,30))
