"""Numerical checks for radial-power boundary measure on nested ellipses.

Run with Python 3 and mpmath 1.3 or later. Finite checks support,
but do not replace, the dominated-convergence proof of the theorem.
"""
import mpmath as mp

mp.mp.dps = 55


def energy(p, a):
    p, a = mp.mpf(p), mp.mpf(a)
    integrand = lambda t: 4 * (a*a*mp.cos(t)**2 + mp.sin(t)**2)**(p/2) * mp.sqrt(a*a*mp.sin(t)**2 + mp.cos(t)**2)
    knots = [mp.mpf('0'), a/4, a, min(4*a, mp.pi/8), mp.pi/4, mp.pi/2]
    knots = sorted(set(knots))
    return mp.fsum(mp.quad(integrand, [lo, hi]) for lo,hi in zip(knots, knots[1:]))


def derivative(p,a):
    p, a = mp.mpf(p), mp.mpf(a)
    def df(t):
        s,c = mp.sin(t),mp.cos(t)
        r2 = a*a*c*c + s*s
        v = mp.sqrt(a*a*s*s + c*c)
        return 4*a*(p*c*c*r2**(p/2-1)*v + s*s*r2**(p/2)/v)
    knots = sorted(set([mp.mpf(0), a/4, a, min(4*a,mp.pi/8), mp.pi/4, mp.pi/2]))
    return mp.fsum(mp.quad(df,[lo,hi]) for lo,hi in zip(knots,knots[1:]))


def cusp_derivative(p):
    p=mp.mpf(p)
    return 2*p*mp.sqrt(mp.pi)*mp.gamma((1-p)/2)/mp.gamma(1-p/2)


def verify():
    for p in ['-0.9', '-0.5','-0.1']:
        P=mp.mpf(p)
        a=mp.mpf('0.0001')
        limit = 4/(P+1)
        C = cusp_derivative(P)/(P+1)
        num = (energy(P,a)-limit)/a**(P+1)
        slope = derivative(P,a)/a**P
        assert C < 0 and slope < 0
        assert abs((num-C)/C)<mp.mpf('0.02'), (p, str(num), str(C))
        assert abs((slope-(P+1)*C)/((P+1)*C))<mp.mpf('0.02'),(p,str(slope))
        assert energy(P,a*2) < energy(P,a)
        assert derivative(P,mp.mpf('1')) > 0
        print('p=',p,'C=',mp.nstr(C,18),'normalized difference=',mp.nstr(num,18), 'slope=',mp.nstr(slope,18))
    for p in ['0','1','2']:
        assert energy(p, mp.mpf('0.8')) > energy(p,mp.mpf('0.2'))
        assert abs(derivative(p,mp.mpf('1'))-mp.pi*(1+mp.mpf(p))) < mp.mpf('1e-48')
    print('NESTED_ELLIPSE_FINITE_CHECKS_OK')

if __name__=='__main__':
    verify()
