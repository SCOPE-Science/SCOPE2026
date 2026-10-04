#!/usr/bin/env python3
import sympy as sp

Ra,Rb,Rc,gb,gc,gd,l,hc = sp.symbols('Ra Rb Rc gb gc gd l hc', positive=True)
lam = sp.symbols('lam')
d1 = (Rc-1)/l
c1 = gd*Rc*d1/hc

la = Ra/Rc - 1
lb = gb*(Rb/Rc - 1)
Jcd = sp.Matrix([
    [0, -l*gc*c1/Rc],
    [hc/Rc, -gd-l*hc*c1/Rc**2]
])
phi1 = gd*(2-1/Rc)
phi2 = gc*gd*(1-1/Rc)
assert sp.simplify(sp.trace(Jcd) + phi1) == 0
assert sp.simplify(Jcd.det() - phi2) == 0
quad = sp.expand((lam*sp.eye(2)-Jcd).det())
assert sp.simplify(quad - (lam**2 + phi1*lam + phi2)) == 0

# Full lower-triangular lineage Jacobian has these factors.
char = sp.expand((lam-la)*(lam-lb)*quad)
assert sp.factor(char) == sp.factor((lam-la)*(lam-lb)*(lam**2+phi1*lam+phi2))

# Exact witness from admissible underlying parameters.
ua=sp.Rational(3,4); sa=sp.Rational(3,1)
ub=sp.Rational(4,5); sb=sp.Rational(2,1)
uc=sp.Rational(3,4); sc=sp.Rational(4,1)
gbv=sp.Rational(1,1); gcv=sp.Rational(1,1); gdv=sp.Rational(1,10); lv=sp.Rational(1,1)
Rav=(2*ua-1)*sa
Rbv=(2*ub-1)*sb/gbv
Rcv=(2*uc-1)*sc/gcv
assert Rav == sp.Rational(3,2)
assert Rbv == sp.Rational(6,5)
assert Rcv == sp.Rational(2,1)

lav=sp.simplify(Rav/Rcv-1)
lbv=sp.simplify(gbv*(Rbv/Rcv-1))
assert lav == -sp.Rational(1,4)
assert lbv == -sp.Rational(2,5)

phi1v=sp.simplify(gdv*(2-1/Rcv))
phi2v=sp.simplify(gcv*gdv*(1-1/Rcv))
assert phi1v == sp.Rational(3,20)
assert phi2v == sp.Rational(1,20)
assert -phi1v/2 == -sp.Rational(3,40)

source_l1=sp.simplify(Rav/Rbv-1)
source_l2=sp.simplify(gbv*Rbv/Rcv-gdv)
assert source_l1 == sp.Rational(1,4)
assert source_l2 == sp.Rational(1,2)

d1v=sp.simplify((Rcv-1)/lv)
hcv=2*(1-uc)*sc
c1v=sp.simplify(gdv*Rcv*d1v/hcv)
assert d1v == 1
assert c1v == sp.Rational(1,10)

print('VERIFY_OK')
print('Ra_Rb_Rc', Rav, Rbv, Rcv)
print('correct_upstream', lav, lbv)
print('source_upstream', source_l1, source_l2)
print('cd_real_part', -phi1v/2)
print('E1_c_d', c1v, d1v)
