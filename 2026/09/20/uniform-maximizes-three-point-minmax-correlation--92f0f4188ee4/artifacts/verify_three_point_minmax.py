import sympy as sp

q, t, r = sp.symbols('q t r', real=True)
x, z = sp.symbols('x z', nonnegative=True)
y = 1 - x - z
vals = (-1, 0, 1)
ps = (x, y, z)
EM = EL = EM2 = EL2 = EML = sp.Integer(0)
for i, a in enumerate(vals):
    for j, b in enumerate(vals):
        w = ps[i] * ps[j]
        m, ell = min(a, b), max(a, b)
        EM += w*m; EL += w*ell
        EM2 += w*m*m; EL2 += w*ell*ell; EML += w*m*ell
cov = sp.factor(EML - EM*EL)
var_m = sp.factor(EM2 - EM**2)
var_l = sp.factor(EL2 - EL**2)
assert sp.factor(cov - (x**2-x+z**2-z)**2) == 0

sub_xz = {x:(q-r)/2, z:(q+r)/2}
G = 2*q-q**2-t
T = 2*(q-t)-G**2/2
Delta2 = 4*t*(1-3*q+q**2+t)**2
R = sp.cancel(G**4/(4*(T**2-Delta2)))

cov_qr = sp.factor(cov.subs(sub_xz))
sum_qr = sp.factor((var_m+var_l).subs(sub_xz))
diff_qr = sp.factor((var_l-var_m).subs(sub_xz))
assert sp.factor(cov_qr - (q**2-2*q+r**2)**2/4) == 0
assert sp.factor(sum_qr - T.subs(t,r**2)) == 0
assert sp.factor(diff_qr**2 - Delta2.subs(t,r**2)) == 0
direct_R_qr = sp.cancel((cov**2/(var_m*var_l)).subs(sub_xz))
assert sp.factor(direct_R_qr - R.subs(t,r**2)) == 0

dRq = sp.factor(sp.together(sp.diff(R,q)).as_numer_denom()[0])
dRt = sp.factor(sp.together(sp.diff(R,t)).as_numer_denom()[0])
common = q**2-2*q+t
P = sp.factor(dRt/(8*common**3))
Q = sp.factor(-dRq/(8*common**3))
resultant = sp.factor(sp.resultant(P,Q,t))
expected = -2304*q*(q-1)**9*(2*q-1)*(4*q**2-2*q+1)
assert sp.factor(resultant-expected) == 0
P_half = sp.factor(P.subs(q,sp.Rational(1,2)))
Q_half = sp.factor(Q.subs(q,sp.Rational(1,2)))
gcd_half = sp.factor(sp.gcd(sp.Poly(P_half,t),sp.Poly(Q_half,t)).as_expr())
assert sp.factor(gcd_half-(4*t-1)/4) == 0

R0 = sp.factor(R.subs(t,0)); dR0 = sp.factor(sp.diff(R0,q))
assert sp.factor(R0.subs(q,sp.Rational(2,3))-sp.Rational(64,361)) == 0
expected_dR0 = -8*q*(q-2)**3*(3*q-2)/(q**3-4*q**2+4*q-4)**3
assert sp.factor(dR0-expected_dR0) == 0

Redge = sp.factor(R.subs(t,q**2)); dRedge=sp.factor(sp.diff(Redge,q))
assert sp.factor(Redge-q*(q-1)/((q-2)*(q+1))) == 0
assert sp.factor(Redge.subs(q,sp.Rational(1,2))-sp.Rational(1,9)) == 0
assert sp.factor(dRedge+2*(2*q-1)/((q-2)**2*(q+1)**2)) == 0

Rmid=sp.factor(R.subs(q,1)); dRmid=sp.factor(sp.diff(Rmid,t))
assert sp.factor(Rmid-(t-1)/(t-9)) == 0
assert sp.factor(Rmid.subs(t,0)-sp.Rational(1,9)) == 0
assert sp.factor(dRmid+8/(t-9)**2) == 0

corr2 = sp.cancel(cov**2/(var_m*var_l))
assert sp.factor(corr2.subs({x:sp.Rational(1,3),z:sp.Rational(1,3)})-sp.Rational(64,361)) == 0
assert sp.factor(corr2.subs({x:sp.Rational(1,4),z:sp.Rational(1,4)})-sp.Rational(81,529)) == 0

print('direct moment identities: PASS')
print('interior resultant:', resultant)
print('q=1/2 common factor:', gcd_half)
print('uniform squared correlation: 64/361')
print('uniform correlation: 8/19')
print('boundary squared-correlation maximum: 1/9')
print('benchmark p=(1/4,1/2,1/4): correlation = 9/23')
print('all exact symbolic checks: PASS')
