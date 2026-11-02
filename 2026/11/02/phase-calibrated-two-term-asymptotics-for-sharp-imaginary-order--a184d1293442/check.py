"""Numerical consistency tests for fixed-order imaginary Macdonald Turán minima.
Requires mpmath; run python check.py. Finite tests do not certify an infinite theorem.
"""
from mpmath import mp
mp.dps = 70
count = 0
for vv in [mp.mpf('0.5'), mp.mpf('1'), mp.mpf('2'), mp.mpf('5')]:
    A = 1+vv*vv
    eta = mp.im(mp.loggamma(1+1j*vv))
    for n in [2,3,4,5,6]:
        q = 2*mp.exp((eta-n*mp.pi-mp.atan(vv))/vv)
        if not (mp.mpf('1e-8') < q < mp.mpf('0.30')):
            continue
        def z(x):
            f=mp.besselk(1j*vv,x)
            return mp.re(-x*(mp.besselk(1j*vv-1,x)+mp.besselk(1j*vv+1,x))/(2*f))
        def t(x):
            return (vv**2+z(x)**2)/x**2-1
        def stationary(x):
            return 1+(1+z(x))*t(x)
        alpha=mp.findroot(stationary,(q*mp.mpf('0.999'),q*mp.mpf('1.001')))
        tau=t(alpha)
        c=(A+8)/(4*A*A)
        pred_alpha=q*(1+c*q*q)
        pred_tau=A/q**2-mp.mpf('1.5')-2/A
        err_alpha=abs(alpha/q-1-c*q*q)
        err_tau=abs(tau-pred_tau)
        assert abs(stationary(alpha)) < mp.mpf('1e-40')
        assert err_alpha < 5*q**4
        assert err_tau < 2*q**2
        assert alpha>0 and tau>0
        print('nu',mp.nstr(vv,4),'n',n,
              'position_error_over_q4',mp.nstr(err_alpha/q**4,7),
              'minimum_error_over_q2',mp.nstr(err_tau/q**2,7))
        count+=1
assert count>=7
print('Passed',count,'fixed-order / nodal-index numerical consistency cases.')
