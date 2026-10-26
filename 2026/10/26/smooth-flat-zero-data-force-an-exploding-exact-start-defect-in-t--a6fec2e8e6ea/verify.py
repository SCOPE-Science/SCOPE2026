"""Reproducible checks of a smooth flat-zero RBF Runge-Kutta defect theorem.
No external datasets; mpmath and sympy are used only for exact identities and diagnostics.
"""
import math
import sympy as sp
import mpmath as mp

z=sp.symbols('z',real=True, nonzero=True)
g=sp.exp(-1/z**2)
assert sp.simplify(sp.diff(g,z,2)/g-(4/z**6-6/z**4))==0
assert sp.simplify(sp.diff(g,z)/g-2/z**3)==0

mp.mp.dps=100
TAU=mp.sqrt(2)/4
assert TAU>0 and TAU<1

count=2
for N in [4,5,6,8,12,16,32,64,128,256,512]:
    h=mp.mpf(1)/N
    n=int(mp.ceil(N*TAU))
    t=mp.mpf(n)/N
    delta=t-TAU
    assert 0<delta<h and t+h<=1
    eps_sq=-(4/delta**6-6/delta**4)/2
    E=-eps_sq*(2*h/3)**2
    log_amplified=-1/delta**2+E
    assert E>0 and log_amplified>=mp.mpf('0.5')*h**(-4)
    logB=mp.log(3*h/4)+log_amplified
    # The formula below is the complete, algebraically exact one-step update,
    # expressed as B+C to avoid allocating an exponentially large numeral.
    d2=delta+2*h/3
    g_t=mp.exp(-1/delta**2)
    gp_t=2*g_t/delta**3
    g_s=mp.exp(-1/d2**2)
    gp_s=2*g_s/d2**3
    C=g_t+h*(gp_t/4+(mp.mpf(3)/4)*((2*h/3)*gp_t+gp_s-g_s))
    g_next=mp.exp(-1/(delta+h)**2)
    assert abs(C)<2, (N, C)
    assert logB>0
    assert logB>=mp.log(3*h/4)+mp.mpf('0.5')*N**4
    # Verify the full formula directly for modest N.
    if N<=8:
        start=g_t
        k1=gp_t
        v_stage=start*mp.exp(E)+(2*h/3)*k1
        k2=v_stage+gp_s-g_s
        actual=start+h*(k1/4+3*k2/4)
        B=mp.exp(logB)
        assert mp.almosteq(actual, B+C, rel_eps=mp.mpf('1e-60'))
        assert actual>g_next
        assert mp.almosteq(mp.log(actual),logB,rel_eps=mp.mpf('1e-20'))
        count+=3
    count+=7
print('VERIFY_OK',count,'exact symbolic identities and mesh/log-domain diagnostics')
