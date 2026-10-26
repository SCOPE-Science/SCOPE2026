#!/usr/bin/env python3
"""Independent numerical and algebraic checks for the finite-site arrival-direction theorem.

Requires Python 3, mpmath, sympy. Run: python verify.py
Finite checks supplement the analytic proof and cannot certify every parameter.
"""
import itertools
import math
import mpmath as mp
import sympy as sp

mp.mp.dps = 65
checks = 0

def insist(test, message):
    global checks
    if not test:
        raise AssertionError(message)
    checks += 1

u = sp.symbols('u', real=True, positive=True)
z = sp.symbols('z', real=True)
# sinh(3u)=sinh(u)(4cosh(u)^2-1); sinh(2u)=2sinh(u)cosh(u).
polynomial = 25 - 20*z + 4*z*z - 1
insist(sp.simplify(polynomial-4*(z-2)*(z-3)) == 0, 'exact factorization')

weights = [mp.mpf(25)/36, mp.mpf(10)/36, mp.mpf(1)/36]
positions = [mp.mpf(3),mp.mpf(6),mp.mpf(1)]


def physical_split(k, length=mp.mpf(8)):
    left = sum(w*mp.sinh(k*(length-x))/mp.sinh(k*length)
               for w,x in zip(weights,positions))
    right = sum(w*mp.sinh(k*x)/mp.sinh(k*length)
                for w,x in zip(weights,positions))
    return left/(left+right), right/(left+right)

for k in [mp.mpf(1)/8, mp.mpf(1)/2, mp.mpf(1), mp.acosh(2),
          mp.mpf(17)/10, mp.acosh(3), mp.mpf(12)/5]:
    l,r = physical_split(k)
    direct = (25*mp.sinh(k)-10*mp.sinh(2*k)+mp.sinh(3*k))/36
    factored = 4*mp.sinh(k)*(mp.cosh(k)-2)*(mp.cosh(k)-3)/36
    insist(abs(direct-factored) < mp.mpf('1e-57'), 'three-site sinh factor')
    insist(abs(l+r-1) < mp.mpf('1e-57'), 'normalization')
    insist(abs((l-r)*(sum(w*mp.sinh(k*(8-x)) for w,x in zip(weights,positions))+
                       sum(w*mp.sinh(k*x) for w,x in zip(weights,positions)))
               -(sum(w*mp.sinh(k*(8-x)) for w,x in zip(weights,positions))-
                 sum(w*mp.sinh(k*x) for w,x in zip(weights,positions)))) < mp.mpf('1e-50'),
           'conditional flux algebra')
for k, sign in [(mp.mpf('0.5'), 1),(mp.mpf('1.7'),-1),(mp.mpf('2.4'),1)]:
    l,r=physical_split(k)
    insist(sign*(l-r)>0, 'three alternating direction regimes')
for k in (mp.acosh(2), mp.acosh(3)):
    l,r = physical_split(k)
    insist(abs(l-r)<mp.mpf('1e-55'), 'exact critical rate')

# Strict positivity of hyperbolic-sine minors and forced interpolation signs.
for m in range(2,7):
    a = [mp.mpf(j)/10 for j in range(1,m+1)]
    sample = [mp.mpf(j)/2 for j in range(1,m+1)]
    for size in range(1,m+1):
        for indices in itertools.combinations(range(m),size):
            mat = mp.matrix([[mp.sinh(sample[i]*a[j]) for j in indices]
                            for i in indices])
            insist(mp.det(mat)>0, 'positive principal minor')
    ks = sample[:-1]
    c = []
    for j in range(m):
        remainder = [i for i in range(m) if i!=j]
        mat = mp.matrix([[mp.sinh(k*a[i]) for i in remainder] for k in ks])
        c.append(((-1)**(m+j+1))*mp.det(mat))
    for k in ks:
        residual = sum(c[j]*mp.sinh(k*a[j]) for j in range(m))
        scale = sum(abs(c[j]*mp.sinh(k*a[j])) for j in range(m))
        insist(abs(residual) < mp.mpf('1e-48')*max(scale,mp.mpf('1e-80')),
               'cofactor interpolation')
    samples_between = [ks[0]/2]+[(ks[j]+ks[j+1])/2 for j in range(len(ks)-1)]+[ks[-1]+1]
    signals = [sum(c[j]*mp.sinh(k*a[j]) for j in range(m)) for k in samples_between]
    for left,right in zip(signals,signals[1:]):
        insist(left*right<0, 'forced root sign reversal')
print('PASS:',checks,'symbolic and high-precision deterministic checks')
