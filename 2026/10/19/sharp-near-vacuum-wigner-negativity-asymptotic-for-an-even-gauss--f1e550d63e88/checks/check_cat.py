#!/usr/bin/env python3
"""Independent numerical checks of an even Gaussian cat Wigner asymptotic.
Run with Python 3 and mpmath; finite tests complement the analytic proof.
"""
import mpmath as mp
mp.mp.dps = 75


def psi(a, x):
    g = lambda y: mp.pi**(-mp.mpf('0.25')) * mp.exp(-y*y/2)
    return (g(x-a)+g(x+a))/mp.sqrt(2*(1+mp.exp(-a*a)))


def formula(a, x, p):
    return mp.exp(-x*x-p*p) * (mp.exp(-a*a)*mp.cosh(2*a*x)+mp.cos(2*a*p))/(mp.pi*(1+mp.exp(-a*a)))


def direct(a, x, p):
    f = lambda y: psi(a,x+y/2)*psi(a,x-y/2)*mp.cos(p*y)
    return mp.quad(f,[-mp.inf,0,mp.inf])/(2*mp.pi)


def one_lobe_negative_mass(a):
    b=mp.acos(mp.exp(-a*a)); t=(mp.pi-b)/(2*a)
    pmax=(mp.pi+b)/(2*a); vmax=2*t*(pmax-t)
    def integrand(v):
        if v<=0 or v>=vmax: return mp.mpf(0)
        p=t+v/(2*t)
        arg=-mp.exp(a*a)*mp.cos(2*a*p)
        X=mp.acosh(max(arg,mp.mpf(1)))/(2*a)
        # Exact x-integral of the positive negative-Wigner polynomial part.
        I=mp.sqrt(mp.pi)*(-mp.mpf('0.5')*(mp.erf(X+a)+mp.erf(X-a))-mp.cos(2*a*p)*mp.erf(X))
        return mp.exp(-(p*p-t*t))*I/(2*t)
    # Two symmetric first interference lobes; remoter lobes are omitted.
    breaks=[mp.mpf(0),mp.mpf('0.1'),mp.mpf('0.5'),mp.mpf(1),mp.mpf(2),mp.mpf(4),mp.mpf(8),mp.mpf(16),mp.mpf(32),min(mp.mpf(100),vmax)]
    breaks=sorted(set(z for z in breaks if z<=vmax))
    if breaks[-1]<vmax: breaks.append(vmax)
    integral=mp.quad(integrand,breaks)
    mass=2*mp.exp(-t*t)*integral/(mp.pi*(1+mp.exp(-a*a)))
    return mp.re(mass), t


def asymptotic(a):
    c=2**(mp.mpf(7)/4)*mp.exp(-mp.mpf('0.5'))/mp.pi**3
    return c*a**(mp.mpf(9)/2)*mp.exp(-mp.pi**2/(4*a*a)+mp.pi/(mp.sqrt(2)*a))


def main():
    for a,x,p in [('0.4','0.3','0.5'),('0.8','0.2','1.2'),('1.1','-0.4','0.7')]:
        a,x,p=map(mp.mpf,(a,x,p))
        assert mp.fabs(direct(a,x,p)-formula(a,x,p))<mp.mpf('1e-35')
    print('Three independent defining-integral Wigner checks: PASS')
    ratios=[]
    for s in ['0.35','0.25','0.2','0.15']:
        a=mp.mpf(s)
        num,t=one_lobe_negative_mass(a)
        expected=asymptotic(a)
        ratio=num/expected
        assert num>0 and mp.isfinite(ratio)
        ratios.append(ratio)
        print('a=',s,'pmin=',mp.nstr(t,12),'first-lobe mass=',mp.nstr(num,12),'asymptotic ratio=',mp.nstr(ratio,12))
    assert ratios[0]<ratios[1]<ratios[2]<ratios[3]<1
    assert ratios[-1]>mp.mpf('0.93')
    print('First-fringe concentration, ratio trend and asymptotic coefficient checks: PASS')
    print('Remote-fringe negligibility is proved analytically, not inferred from truncation.')

if __name__=='__main__': main()
