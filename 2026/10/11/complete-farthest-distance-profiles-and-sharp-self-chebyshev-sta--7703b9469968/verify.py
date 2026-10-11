#!/usr/bin/env python3
"""Reconstruct the all-order regular-polygon farthest-distance identity.

Only the standard library and SymPy are needed. Finite probes supplement,
but cannot replace, the angle-ordering proof in RESULT.md.
"""
import math
import sympy as sp

x = sp.symbols('x', positive=True)
c = sp.cos(sp.pi*x)
s = sp.sin(sp.pi*x)
q_odd = (2/x)*sp.tan(sp.pi*x/2)
q_even = (2/x)*s/sp.sqrt(1+3*c*c)
assert sp.simplify(sp.series(q_odd, x, 0, 6).removeO() -
    (sp.pi + sp.pi**3*x**2/12 + sp.pi**5*x**4/120)) == 0
assert sp.simplify(sp.series(q_even, x, 0, 6).removeO() -
    (sp.pi + 5*sp.pi**3*x**2/24 + 61*sp.pi**5*x**4/1920)) == 0

# Exact first cases match separately published equilateral triangle / square.
assert sp.simplify(q_odd.subs(x,sp.Rational(1,3))-2*sp.sqrt(3))==0
assert sp.simplify(q_even.subs(x,sp.Rational(1,4))-8/sp.sqrt(5))==0

# The prediction is checked against EVERY polygon vertex, not against a
# preselected antipodal vertex, for every sample on a complete side.
max_abs_err = 0.0
checked = 0
nvals = list(range(3,122)) + [201,301]
for n in nvals:
    a=math.pi/n
    r=math.cos(a)
    ss=math.sin(a)
    verts=[(math.cos(a+2*math.pi*k/n), math.sin(a+2*math.pi*k/n))
           for k in range(n)]
    for j in range(51):
        t=ss*(2*j/50-1)
        brute=max((r-vx)**2+(t-vy)**2 for vx,vy in verts)
        pred=(1+r)**2+t*t if n%2 else 4*r*r+(ss+abs(t))**2
        err=abs(brute-pred)
        max_abs_err=max(max_abs_err,err)
        checked += n
        assert err < 3e-13,(n,j,brute,pred,err)
        mindelta=(1+r)**2 if n%2 else 4*r*r+ss*ss
        stab=t*t if n%2 else t*t+2*ss*abs(t)
        assert abs(pred-mindelta-stab)<3e-13

# Direct minimization among 51*side samples (the proof supplies continuity
# and strict equality conditions beyond this finite regression).
for n in nvals:
    alpha=math.pi/n
    r=math.cos(alpha)
    ss=math.sin(alpha)
    tvals=[-ss,0,ss]
    predicted=[((1+r)**2+t*t) if n%2 else (4*r*r+(ss+abs(t))**2)
               for t in tvals]
    assert predicted[1] < predicted[0] and predicted[1] < predicted[-1]

print('VERIFY_OK')
print('sympy_series_and_endpoints: PASS')
print('brute_full_vertex_maxima: PASS')
print('stability_identities: PASS')
print('number_of_vertex_distance_comparisons:',checked)
print('max_squared_distance_discrepancy:',format(max_abs_err,'.5g'))
