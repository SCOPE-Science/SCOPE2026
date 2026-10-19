"""Independent numerical and exact-arithmetic spot checks for the stated orbit theorem.

This is a finite consistency checker, not a substitute for the analytic proof.
Run: python verify.py
"""
import math
from fractions import Fraction

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def R(p, s):
    if s == 0.0:
        return 1.0
    t = math.sinh(s)
    return (t * math.cosh(s) / s) * (1.0 - t*t/p)


def pc(s):
    t, c = math.sinh(s), math.cosh(s)
    A = t*c
    Ap = t*t + c*c
    B = A*t*t
    Bp = Ap*t*t + 2*A*A
    D = s*Ap-A
    N = s*Bp-B
    return N/D


def bisection(f, lo, hi, it=110):
    flo, fhi = f(lo), f(hi)
    check(flo*fhi < 0, 'bracket must change sign')
    for _ in range(it):
        mid = (lo+hi)/2
        fm = f(mid)
        if fm == 0: return mid
        if (flo>0)==(fm>0):
            lo,flo=mid,fm
        else:
            hi,fhi=mid,fm
    return (lo+hi)/2


def critical(p):
    end = math.asinh(math.sqrt(p))
    return bisection(lambda s: pc(s)-p, 0.01, end)


def potential(p, t, u):
    beta = math.asinh(math.sqrt(p))
    S = math.sinh(beta*u)
    return t*p/(4*(1+p)*beta*beta)*(S*S/p-1)**2


def grad(p,t,u):
    beta=math.asinh(math.sqrt(p)); S=math.sinh(beta*u)
    return t/((1+p)*beta)*S*math.cosh(beta*u)*(S*S/p-1)


def F(p,t,u,v):
    return (2*u-v+grad(p,t,u),u)


def roots(p,t):
    end=math.asinh(math.sqrt(p))
    target=4*(1+p)/t
    if p<=1.5:
        return [] if t<=4*(1+p) else [bisection(lambda s: R(p,s)-target, 1e-10,end)]
    sstar=critical(p)
    peak=R(p,sstar)
    t_sn=4*(1+p)/peak
    if t<t_sn-1e-10:
        return []
    if abs(t-t_sn)<1e-10:
        return [sstar]
    out=[]
    if t<4*(1+p):
        out.append(bisection(lambda s:R(p,s)-target,1e-10,sstar))
    out.append(bisection(lambda s:R(p,s)-target,sstar,end))
    return out

# An exact Taylor-sign certificate, including the degenerate fourth-order coefficient.
p=Fraction(3,2)
check(Fraction(2,3)-1/p==0,'quadratic cancellation')
check(Fraction(2,15)-1/p==Fraction(-8,15),'quartic coefficient')
check(Fraction(4,315)-Fraction(2,5)/p==Fraction(-16,63), 'sixth-order coefficient')
for p0 in [Fraction(1,2),Fraction(3,2),Fraction(2),Fraction(4),Fraction(9)]:
    c2=Fraction(2,3)-1/p0
    check((c2>0)==(p0>Fraction(3,2)), 'quadratic sign')

# Strictly increasing critical curve, matching its endpoint limit.
sgrid=[.03+.002*j for j in range(450)]
values=[pc(s) for s in sgrid]
for j in range(1,len(values)):
    check(values[j]>values[j-1], 'critical parameter strictly increasing on grid')
check(abs(pc(.003)-1.5)<.0001, 'critical ratio tends to 3/2')

# Exact derivative reconstruction from the original potential and direct map.
for p0 in (.25,1,1.5,2,4,9):
    for t in (2,5,11,23):
        for u in (-.8,-.1,.15,.7):
            h=1e-5
            num=(potential(p0,t,u+h)-potential(p0,t,u-h))/(2*h)
            check(abs(grad(p0,t,u)-num)<1e-8, 'potential gradient numerical check')

# Complete orbit count checked across threshold regimes (not a proof of completeness).
for p0 in (.5,1.5):
    ac=4*(1+p0)
    for t,n_expected in ((.8*ac,0),(ac,0),(1.05*ac,1),(2*ac,1)):
        arr=roots(p0,t)
        check(len(arr)==n_expected, 'monotone branch count')
        for s in arr:
            y=s/math.asinh(math.sqrt(p0))
            u,v=F(p0,t,y,-y)
            check(abs(u+y)<1e-10 and abs(v-y)<1e-10, 'first orbit step')
            uu,vv=F(p0,t,u,v)
            check(abs(uu-y)<1e-10 and abs(vv+y)<1e-10,'second orbit step')
for p0 in (1.51,2,4,9):
    ac=4*(1+p0)
    ss=critical(p0); peak=R(p0,ss); sn=ac/peak
    check(peak>1 and sn<ac,'peak precedes criticality')
    for t,n_expected in ((sn-(ac-sn)/3,0),(sn,1),((sn+ac)/2,2),(ac,1),(ac+.1*(ac-sn),1)):
        arr=roots(p0,t)
        check(len(arr)==n_expected, 'fold branch count')
        for s in arr:
            y=s/math.asinh(math.sqrt(p0))
            u,v=F(p0,t,y,-y)
            check(abs(u+y)<2e-9 and abs(v-y)<2e-9,'first orbit step')
            uu,vv=F(p0,t,u,v)
            check(abs(uu-y)<2e-9 and abs(vv+y)<2e-9,'second orbit step')

# Independent asymptotic limit probes.  The exact asymptotic follows from Taylor algebra.
for d in (.01,.005,.002):
    p0=1.5+d
    sstar=critical(p0)
    width=4*(1+p0)-4*(1+p0)/R(p0,sstar)
    ratio=width/(d*d)
    check(abs(ratio-25/27)<.03, 'quadratic fold-width asymptotic')
    check(abs(sstar*sstar/d-5/12)<.04,'fold location asymptotic')
print(f'PASS: {checks} deterministic finite checks (analytic proof required for all global claims)')
