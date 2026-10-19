#!/usr/bin/env python3
"""Reproduce exact algebra and numerical illustrations for the fast habitat-pulse theorem.

This verifier is supplementary: finite samples do not prove the general theorem.
Requires sympy and mpmath. Optional scipy checks an ODE illustration.
"""
import sympy as sp
import mpmath as mp

def main():
    a = sp.Rational(1, 2)
    p0 = sp.Rational(4, 5)
    p1 = sp.Rational(9, 10)
    v0 = (1-p0)*(1-a)
    w = a+1/p0-1
    u = sp.symbols('u', positive=True)
    q0 = (1-p0*u)*(u-a)
    assert sp.expand(q0-v0) == sp.expand(-p0*(u-1)*(u-w))
    assert v0 == sp.Rational(1,10) and w == sp.Rational(3,4)
    pc = sp.simplify(1/(sp.sqrt(a+v0)+sp.sqrt(v0))**2)
    assert sp.simplify(pc-(14-4*sp.sqrt(6))/5) == 0
    assert sp.N(pc,18) < p1
    F = lambda p: (1-a*p)**2/(4*p)
    assert sp.simplify(F(pc)-v0) == 0
    q1 = (1-p1*u)*(u-a)
    denominator = sp.factor(v0-q1)
    assert sp.simplify(denominator -(18*u**2-29*u+12)/20) == 0
    mp.mp.dps = 65
    a_mp = mp.mpf('0.5'); p0_mp=mp.mpf('0.8')
    pc_mp = mp.mpf(str(sp.N(pc,70)))
    v_mp = mp.mpf('0.1')
    w_mp = mp.mpf('0.75')
    def s_critical(p):
        return mp.quad(lambda z: 1/(z*(p*z*z-(1+a_mp*p)*z+(a_mp+v_mp))),[w_mp,1])
    sc = s_critical(mp.mpf('0.9'))
    analytic = mp.mpf(5)/6*mp.log(mp.mpf(2)/3) +mp.mpf(145)*mp.sqrt(23)/69*mp.atan(mp.sqrt(23))
    assert abs(sc-analytic)<mp.mpf('1e-57')
    assert 12<sc<15
    C= 4*mp.pi*pc_mp**mp.mpf('1.5')/((1+a_mp*pc_mp)*mp.sqrt(1-a_mp*a_mp*pc_mp*pc_mp))
    assert abs(C-mp.mpf('7.5124496971878742781'))<mp.mpf('1e-18')
    # Confirm convergence of square-root asymptotic at shrinking offsets.
    errors=[]
    for d in [mp.mpf('0.002'),mp.mpf('0.0002'),mp.mpf('0.00002')]:
        scaled=mp.sqrt(d)*s_critical(pc_mp+d)
        errors.append(abs(scaled/C-1))
    assert errors[2]<errors[1]<errors[0]
    assert errors[-1]<mp.mpf('0.015')
    print('Exact polynomial, shock fold, quadrature formula: PASS')
    print('Shock amplitude fold:',mp.nstr(pc_mp,22))
    print('Critical scaled duration:',mp.nstr(sc,25))
    print('Bottleneck coefficient:',mp.nstr(C,25))
    print('Asymptotic relative deviations:',[mp.nstr(e,9) for e in errors])
    try:
        import scipy.integrate
    except ImportError:
        print('Optional SciPy illustration: skipped (not installed)')
        return
    eps=1e-4
    for duration, prediction in [(12,'recovery'),(15,'extinction')]:
        def f(t,Y,phi):
            u,v=Y
            return [u*((1-phi*u)*(u-0.5)-v)/eps,v*(u-1)]
        shocked=scipy.integrate.solve_ivp(lambda t,y:f(t,y,0.9),(0,eps*duration),[1,0.1],rtol=1e-10,atol=1e-13)
        assert shocked.success
        uc=shocked.y[0,-1]
        assert (uc>0.75 if prediction=='recovery' else uc<0.75)
        restored=scipy.integrate.solve_ivp(lambda t,y:f(t,y,0.8),(eps*duration,12),shocked.y[:,-1],rtol=5e-9,atol=1e-11,method='BDF')
        assert restored.success
        ufin,vfin=restored.y[:,-1]
        if prediction=='recovery':
            assert abs(ufin-1)<1e-4 and abs(vfin-0.1)<1e-4
        else:
            assert ufin<1e-5 and vfin<1e-5
        print('Optional ODE illustration',duration,prediction,'postshock prey',round(float(uc),9),'late state',float(ufin),float(vfin))
if __name__ == '__main__':
    main()
