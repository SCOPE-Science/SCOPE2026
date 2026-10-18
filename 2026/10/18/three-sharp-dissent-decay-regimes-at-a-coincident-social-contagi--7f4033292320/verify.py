"""Reproduce exact identities and numerical asymptotic diagnostics for a three-state contact model.

This program is corroborating evidence. The infinite-time assertions follow from the
proof and are not inferred from the finite integrations below.
"""
import math

import sympy as sp
from scipy.integrate import solve_ivp


def verify_symbolic():
    a, m, k, i, d, r = sp.symbols('a m k i d r', positive=True)
    s = 1 - i - d
    I = m*s*i - k*i*d - m*i
    D = k*i*d + m*s*d + a*s*i - m*d
    I_expected = -m*i*i - (m+k)*i*d
    D_expected = a*i - m*d*d - (a+m-k)*i*d - a*i*i
    assert sp.simplify(I-I_expected) == 0
    assert sp.simplify(D-D_expected) == 0
    # The stretched-time differentiation operator is (1/d) d/dt.
    R_tau = sp.factor(((I*d - 2*i*D)/d**3)/d).subs(i, r*d*d)
    D_log_tau = sp.factor(D/d**2).subs(i, r*d*d)
    R_expected = r*((m-k)-2*a*r+(2*a+m-2*k)*r*d+2*a*r*r*d*d)
    D_expected_tau = -m+a*r-(a+m-k)*r*d-a*r*r*d*d
    assert sp.simplify(R_tau-R_expected) == 0
    assert sp.simplify(D_log_tau-D_expected_tau) == 0
    print('Exact ODE, ratio, and stretched-time identities: PASS')


def compute_case(m, a, k, i0, d0, tau_end=170):
    assert 0<i0 and 0<d0 and i0+d0<1
    def deriv(tau, y):
        logr, logd, log1pt = y
        r, d = math.exp(logr), math.exp(logd)
        i = r*d*d
        lr = (m-k)-2*a*r+(2*a+m-2*k)*r*d+2*a*r*i
        ld = -m+a*r-(a+m-k)*r*d-a*r*i
        log_clock = math.exp(-logd-log1pt)
        return [lr, ld, log_clock]
    initial = [math.log(i0/d0**2), math.log(d0), 0.0]
    sol = solve_ivp(deriv, (0,tau_end), initial, method='DOP853',
                    atol=2e-12, rtol=2e-11, dense_output=False)
    assert sol.success, sol.message
    logr, logd, log1pt = sol.y[:, -1]
    t = math.expm1(log1pt)
    r, d = math.exp(logr), math.exp(logd)
    i = r*d*d
    dlimit = t*d
    if k<m:
        val = t*t*i
        expected = 2*(m-k)/(a*(m+k)**2)
        expected_d = 2/(m+k)
        assert abs(val/expected-1)<0.06, (k, val, expected)
        assert abs(dlimit/expected_d-1)<0.04, (k,dlimit,expected_d)
        desc = ('quadratic',val,expected)
    elif k==m:
        val = t*t*math.log(t)*i
        expected = 1/(2*a*m)
        expected_d = 1/m
        assert abs(val/expected-1)<0.1, (k,val,expected)
        assert abs(dlimit/expected_d-1)<0.07, (k,dlimit,expected_d)
        desc=('logarithmic',val,expected)
    else:
        exponent = 1+k/m
        val = math.exp(exponent*math.log(t)+math.log(i))
        assert val>0 and math.isfinite(val)
        expected_d = 1/m
        assert abs(dlimit/expected_d-1)<0.04, (k,dlimit,expected_d)
        desc=('continuous-exponent',val,'positive finite amplitude')
        # Repeating at a later time must stabilize the predicted amplitude.
        sol2 = solve_ivp(deriv,(tau_end,tau_end+20),sol.y[:,-1],
                         method='DOP853',atol=2e-12,rtol=2e-11)
        assert sol2.success
        r2,d2,L2 = sol2.y[:,-1]
        val2=math.exp(exponent*math.log(math.expm1(L2))+r2+2*d2)
        assert abs(val2/val-1)<0.02,(val,val2)
    print(f'k={k:.3f}; t*d={dlimit:.9g}, expected={expected_d:.9g}; '
          f'{desc[0]} infected scale={desc[1]:.9g}, expected={desc[2]}')


def main():
    verify_symbolic()
    for k in (.2,.4,.7):
        compute_case(.4,.25,k,.15,.25)
    for k in (.08,.2,.6):
        compute_case(.2,.35,k,.3,.35)
    print('Six positive-trajectory diagnostics: PASS')


if __name__=='__main__':
    main()
