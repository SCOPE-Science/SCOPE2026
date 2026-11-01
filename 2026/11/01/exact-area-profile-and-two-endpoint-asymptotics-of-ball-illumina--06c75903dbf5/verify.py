"""Recompute the exact small-angle coefficients for the planar R-ball hull
of a disk and one exterior point, and test the two endpoint asymptotics.
Run: python verify.py (requires sympy and mpmath)."""
import sympy as S
import mpmath as mp

k, t = S.symbols('k t', real=True)
beta = S.series(S.asin(k * S.sin(t)), t, 0, 8).removeO()
h = S.series(S.cos(beta) - k * S.cos(t) - (1-k), t, 0, 8).removeO()
d = S.series(t-beta-k*S.sin(t-beta)-(1-k)**2*t, t, 0, 8).removeO()
checks = {
    'h2': (h.coeff(t, 2), k*(1-k)/2),
    'h4': (h.coeff(t, 4), k*(1-k)*(3*k*k+3*k-1)/24),
    'd3': (d.coeff(t, 3), k*(1-k)**2/3),
    'd5': (d.coeff(t, 5), k*(1-k)**2*(3*k*k+6*k-1)/60),
}
for label,(actual, expected) in checks.items():
    assert S.simplify(actual-expected)==0, (label, actual, expected)

# With R=1, leading area expansion is 2*pi*r*w + pi*B*w^2,
# w=(delta/C)^(2/3), C=(2 sqrt(2)/3)*sqrt(r/(1-r)).
h2=checks['h2'][1]
b=checks['h4'][1]/h2
q=checks['d5'][1]/checks['d3'][1]
L=S.factor((q-S.Rational(3,2)*b)/h2)
assert S.simplify(L + 3*(3*k*k+k-1)/(20*k*(1-k)))==0
B=S.factor(1-S.Rational(4,3)*(1-k)*L)
assert S.simplify(B-(8-12*(1-k)+3*(1-k)**2)/(5*k))==0

mp.mp.dps=65
for rho in (mp.mpf('0.2'),mp.mpf('0.5'),mp.mpf('0.9')):
    R=mp.mpf(1); r=rho; a=R-r; kk=a/R
    C=2*mp.sqrt(2)/3*mp.sqrt(r*R/a)
    Bpred=(8*R*R-12*R*r+3*r*r)/(5*R*a)
    for aa in (mp.mpf('0.015'),mp.mpf('0.004')):
        be=mp.asin(kk*mp.sin(aa)); ga=aa-be
        s=R*mp.cos(be)-a*mp.cos(aa)
        increment=R**2*ga-R*a*mp.sin(ga)-r*r*aa
        assert increment>0
        w=(increment/C)**(mp.mpf(2)/3)
        estimate=(mp.pi*(s*s-r*r)-2*mp.pi*r*w)/(mp.pi*w*w)
        assert abs(estimate-Bpred)<mp.mpf('0.002'), (rho,aa,estimate,Bpred)
    # Terminal expansion: delta_max-delta ~ C_terminal sqrt(s_max-s).
    tt=mp.mpf('0.004'); aa=mp.pi-tt
    be=mp.asin(kk*mp.sin(aa)); ga=aa-be
    s=R*mp.cos(be)-a*mp.cos(aa)
    increment=R*R*ga-R*a*mp.sin(ga)-r*r*aa
    terminal=4*R*mp.sqrt(2*R*a/(R+a))
    ratio=(mp.pi*(R*R-r*r)-increment)/(terminal*mp.sqrt(R+a-s))
    assert abs(ratio-1)<mp.mpf('0.002')

print('PASS: four exact Taylor coefficients, inverse-area coefficient,')
print('      three radii in both endpoint regimes (sympy and mpmath).')
print('B(r/R=1/2)=',B.subs(k,S.Rational(1,2)))
print('zero of B at r/R =', 2-2*S.sqrt(3)/3)
