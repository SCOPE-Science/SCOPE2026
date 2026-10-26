"""Deterministic numerical checks for a partial-reset tail-index comparison.

No finite test is used as a proof of stationary Pareto asymptotics.
"""
import math

COUNT = 0

def check(cond, desc):
    global COUNT
    if not cond:
        raise AssertionError(desc)
    COUNT += 1

def psi(p, b, s):
    # lambda is normalized to one and gamma=b.
    return b*p + math.expm1(p*math.log1p(-s))/s

def root_index(b, s):
    # psi is strictly convex, negative at p=1, positive at large p.
    lo, hi = 1., max(3., 10./s)
    while psi(hi, b, s) <= 0:
        hi *= 2
    for _ in range(130):
        mid = (lo+hi)/2
        if psi(mid,b,s) < 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2

def root_c(b):
    lo, hi = 1.e-9, 2./b+10
    for _ in range(110):
        c=(lo+hi)/2
        f=b*c+math.expm1(-c)
        if f<0: lo=c
        else: hi=c
    return (lo+hi)/2

bs = (0.1, 0.25, 0.49, 0.5, 0.6, 0.75, 0.9, 0.98)
ss = (0.01, 0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.5, 0.7, 0.9, 0.98)
for b in bs:
    for s in ss:
        p=root_index(b,s)
        q=1+2*(1-b)/s
        check(p>1 and abs(psi(p,b,s)) < 1.e-10, f'root: b={b}, s={s}')
        check(psi(p-0.05,b,s) < 0 < psi(p+0.05,b,s), f'root bracket: {b}, {s}')
        sign = 1 if s<2*(1-b)-1e-12 else (-1 if s>2*(1-b)+1e-12 else 0)
        check((p-q)*sign>1e-9 if sign else abs(p-q)<1e-9, f'index order: {b}, {s}')
        exact2=2*b-2+s
        approx2=2*(b-1)+s
        check(abs(exact2-approx2)<1e-12, f'second-order generator: {b}, {s}')
        check((p>2)==(s<2*(1-b)), f'variance threshold: {b}, {s}')
        if p>2 and 1/s>2*b:
            D=0.37
            r=1/s
            A2=(1-s)**2*r/(r-2*b)
            B2=D/b*(r/(r-2*b)-1)
            V=B2/(1-A2)
            expected=2*D/(2*(1-b)-s)
            check(abs(V-expected) <= 2e-9*max(1,V), f'perpetuity variance: {b}, {s}')
for s in (0.05, 0.15, 0.25, 0.5, 0.75, 0.95):
    b=1-s/2
    p=root_index(b,s)
    check(abs(p-2)<2e-10, f'crossing b={b} s={s}')
for b in (0.2, 0.5, 0.8):
    c=root_c(b)
    d=c*math.exp(-c)/(2*(b-math.exp(-c)))
    check(c>2*(1-b), f'singular coefficient strict: {b}')
    for s in (0.001,0.002,0.005):
        p=root_index(b,s)
        check(abs(p-c/s-d) < 0.065, f'singular expansion: {b}, {s}')
        q=1+2*(1-b)/s
        check(abs(p/q-c/(2*(1-b)))<0.013, f'singular ratio: {b}, {s}')
print(f'PASS {COUNT} deterministic checks')
for s in (0.02,0.05,0.1,0.2,0.35,0.5,0.6):
    b_d = 1-1.5*s
    b_t = (1-(1-s)**4)/(4*s)
    check(0<b_d<b_t<1, f'fourth-moment wedge exists: {s}')
    for frac in (0.1, 0.5, 0.9):
        b = b_d+frac*(b_t-b_d)
        p=root_index(b,s)
        q=1+2*(1-b)/s
        check(p>4 and q<4, f'exact finite but approximation infinite: {b}, {s}')
        check(p>2 and q>2, f'both variances finite: {b}, {s}')
for s in (0.05,0.1,0.2,0.3):
    for b in (0.1,0.2,0.35):
        if b>=1-1.5*s: continue
        D=.61
        M2 = 2*D/(2*(1-b)-s)
        d_true = 4*(1-b)-6*s+4*s*s-s**3
        d_approx = 4*(1-b)-6*s
        M4_true=12*D*M2/d_true
        M4_approx=12*D*M2/d_approx
        check(0<M4_true<M4_approx, f'fourth moment ordering: {b}, {s}')
        check(abs((1/M4_true)-(1/M4_approx)-(4*s*s-s**3)/(12*D*M2)) < 1e-10,
              f'fourth moment exact gap identity: {b}, {s}')
print(f'PASS {COUNT} deterministic checks (including fourth moment phase wedge)')
