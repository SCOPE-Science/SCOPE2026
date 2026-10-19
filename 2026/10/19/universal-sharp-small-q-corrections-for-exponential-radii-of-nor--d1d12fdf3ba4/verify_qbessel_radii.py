"""Reproducible finite checks for scaled q-Bessel exponential radii.

Requires mpmath >= 1.3.0; run: python verify_qbessel_radii.py.
Finite evaluations supplement, but do not replace, the analytic proof.
"""
import mpmath as mp

mp.mp.dps = 65
DELTA = 1 - mp.exp(-1)


def constants(m, a):
    u, v = m*a, 1 + m*a
    xs = DELTA/(DELTA + u)
    x1s = xs*xs*(DELTA + 2*u)/(DELTA + u)
    aa = v*(DELTA + u)
    bb = DELTA*(v + 1) + u*(1 + m)
    xc = 2*DELTA/(bb + mp.sqrt(bb*bb - 4*aa*DELTA))
    num = ((a - 1)*(2*xc - xc*xc)/(1 - xc)**2
           + (1 + 2*u)*(2*xc - v*xc*xc)/(1 - v*xc)**2)
    den = (a - 1)/(1 - xc)**2 + v/(1 - v*xc)**2
    return (xs, xs*xs*(2-xs), xc, xc*num/den)


def coefficients(q, nu, kind, cutoff=22):
    power = 2 if kind == 2 else 1
    cs = [mp.mpf(1)]
    for n in range(1, cutoff+1):
        ratio = q**(power*(n-1)) * (1-q)*(1-q**(nu+1)) / (
            (1-q**n)*(1-q**(nu+n)))
        cs.append(cs[-1]*ratio)
    eps = q**power/(1+q) * (1-q**(nu+1))/(1-q**(nu+2))
    assert mp.almosteq(cs[1], 1)
    assert mp.almosteq(cs[2], eps)
    return cs, eps


def polynomial(cs, x, derivative=0):
    return sum((-1)**n*cs[n]*mp.fac(n)/mp.fac(n-derivative)*x**(n-derivative)
               for n in range(derivative, len(cs)))


def roots(cs, m, a, xs, xc):
    u = m*a
    def star(x):
        return 1 + u*x*polynomial(cs,x,1)/polynomial(cs,x) - mp.exp(-1)
    def convex(x):
        b=polynomial(cs,x); bp=polynomial(cs,x,1); bpp=polynomial(cs,x,2)
        d=b+u*x*bp; dp=(1+u)*bp+u*x*bpp
        return 1 + m*x*((a-1)*bp/b+dp/d) - mp.exp(-1)
    def bisect(func, lo, hi):
        assert func(lo)>0 and func(hi)<0
        for _ in range(180):
            mid=(lo+hi)/2
            if func(mid)>0:lo=mid
            else:hi=mid
        return (lo+hi)/2
    return (bisect(star, mp.mpf(0), min(xs*mp.mpf('1.6'),mp.mpf('0.9'))),
            bisect(convex, mp.mpf(0), min(xc*mp.mpf('1.6'),mp.mpf('0.86')/(1+u))))


def main():
    checked=0
    max_scaled_remainder=mp.mpf(0)
    for nu in map(mp.mpf, ['0.25', '0.5', '1.0']):
        for q in map(mp.mpf, ['0.02', '0.06', '0.12']):
            e2=coefficients(q,nu,2)[1];e3=coefficients(q,nu,3)[1]
            assert mp.almosteq(e2/q, e3)
            for s in (2,3):
                cs,eps=coefficients(q,nu,s)
                for m,a in ((2,1/nu),(2,mp.mpf(1)),(1,mp.mpf(1))):
                    xs,x1s,xc,x1c=constants(m,a)
                    assert 0<xc<1/(1+m*a) and 0<xs<1
                    assert x1s>0 and x1c>0
                    rs,rc=roots(cs,m,a,xs,xc)
                    for actual,leading,first in ((rs,xs,x1s),(rc,xc,x1c)):
                        error=abs(actual-leading-first*eps)/eps**2
                        max_scaled_remainder=max(max_scaled_remainder,error)
                        assert error < 2, (nu,q,s,m,a,error)
                        checked+=1
    print('PASS',checked,'radius checks; maximum |residual|/eps^2 =',mp.nstr(max_scaled_remainder,10))


if __name__=='__main__':
    main()
