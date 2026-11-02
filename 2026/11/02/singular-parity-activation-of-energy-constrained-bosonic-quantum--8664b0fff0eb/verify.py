"""Independent finite and high-precision checks of the parity-channel formulas.

Run with Python 3 and mpmath 1.3 or later. All logarithms inside F
are natural, so multiply by 1/log(2) to express capacity in bits.
"""
import math
import random
import mpmath as mp

mp.mp.dps = 110
checks = 0

def check(cond, message):
    global checks
    if not bool(cond):
        raise AssertionError(message)
    checks += 1

def H(x):
    if x <= 0 or x >= 1:
        return mp.mpf(0)
    return -x*mp.log(x) -(1-x)*mp.log1p(-x)

def G(x):
    if x <= 0:
        return mp.mpf(0)
    return (x+1)*mp.log1p(x) - x*mp.log(x)

def eta(q,r):
    c = 1-r
    z = 1-4*c*q*(1-q)
    return 2*c*q*(1-q)/(1+mp.sqrt(z))

def F(q,E,r):
    return G((E-q)/2)+H(q)-H(eta(q,r))

def dF(q,E,r):
    c = 1-r
    z=1-4*c*q*(1-q)
    e=eta(q,r)
    ep=c*(1-2*q)/mp.sqrt(z)
    m=(E-q)/2
    return -mp.log1p(1/m)/2 +mp.log((1-q)/q) -ep*mp.log((1-e)/e)

def optimal_q(E,r):
    E=mp.mpf(E); r=mp.mpf(r)
    if r == 0: return mp.mpf(0)
    hi=min(E,mp.mpf(1))
    lo=mp.mpf('1e-1200')
    if dF(lo,E,r) <= 0:
        raise AssertionError('Bracketing low endpoint failed')
    for _ in range(1500):
        mid=mp.sqrt(lo*hi) if hi/lo>100 else (lo+hi)/2
        if mid==lo or mid==hi: break
        if dF(mid,E,r)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

# Direct complementary qubit spectrum against closed expression, including asymmetric q.
for a in (mp.mpf('0.01'),mp.mpf('0.1'),mp.mpf('0.36'),mp.mpf('0.5')):
    r=(1-2*a)**2
    for q in (mp.mpf('0.007'),mp.mpf('0.16'),mp.mpf('0.3'),mp.mpf('0.67'),mp.mpf('0.93')):
        d11=1-a
        d22=a
        off=mp.sqrt(a*(1-a))*(1-2*q)
        det=d11*d22-off**2
        e=(1-mp.sqrt(1-4*det))/2
        check(mp.almosteq(e,eta(q,r),rel_eps=mp.mpf('1e-90')), 'environment spectrum mismatch')

# At identity and complete parity dephasing, the known limiting optimizers are recovered.
for Es in ('0.01','0.1','0.7','2','7'):
    E=mp.mpf(Es)
    q_id=E/(1+2*E)
    check(mp.almosteq(F(q_id,E,1),G(E),rel_eps=mp.mpf('1e-90')), 'identity thermal law')
    check(mp.almosteq(F(0,E,0),G(E/2),rel_eps=mp.mpf('1e-90')), 'even code limiting value')

# Positive mismatched phase weights: strict interior stationary maxima.
for Es in ('0.2','0.75','2','9'):
    E=mp.mpf(Es)
    for rs in ('0.05','0.2','0.5','0.95'):
        r=mp.mpf(rs)
        q=optimal_q(E,r)
        check(0<q<min(E,1), 'not interior')
        check(abs(dF(q,E,r))<mp.mpf('1e-85'), 'bad derivative')
        check(F(q,E,r)>F(0,E,r), 'no improvement over even encoding')
        for scale in ('0.5','0.9','1.1','1.4'):
            alt=q*mp.mpf(scale)
            if alt<min(E,1):
                check(F(q,E,r)>F(alt,E,r), 'optimizer not locally strict')
        # Conditional geometric distributions have common K mean.
        m=(E-q)/2
        t=m/(m+1)
        check(mp.almosteq(q+2*m,E,rel_eps=mp.mpf('1e-90')), 'energy')
        check(0<t<1, 'geometric probability')

# Compare entropy of finite-support even/odd alternatives against thermal variational cap.
rng=random.Random(1729)
for _ in range(200):
    vec=[rng.random() for _ in range(8)]
    S=sum(vec); probs=[mp.mpf(str(v/S)) for v in vec]
    En=sum(i*probs[i] for i in range(8)); q=sum(probs[i] for i in (1,3,5,7))
    p=mp.mpf('0.23'); r=(1-2*p)**2
    raw=sum(-v*mp.log(v) for v in probs)-H(eta(q,r))
    check(raw<=F(q,En,r)+mp.mpf('1e-90'), 'finite distribution violates variational envelope')

# Exponentially small odd sector and capacity gain; very-high-precision roots.
E=mp.mpf('2'); L=mp.log(1+2/E)
for rs in ('0.1','0.05','0.025','0.01'):
    r=mp.mpf(rs)
    q=optimal_q(E,r)
    asym=mp.exp(-1-L/(2*r))
    ratio=q/asym
    check(mp.mpf('0.99')<ratio<mp.mpf('1.15'), 'essential singularity magnitude')
    gain=F(q,E,r)-G(E/2)
    check(mp.mpf('0.97')<gain/(r*q)<mp.mpf('1.01'), 'essential singularity capacity gain')

print(f'PASS: {checks} independent finite and high-precision assertions')
