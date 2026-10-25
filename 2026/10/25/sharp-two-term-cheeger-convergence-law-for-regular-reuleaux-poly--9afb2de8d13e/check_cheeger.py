"""Reproduce the regular-Reuleaux Cheeger asymptotics.

Requires sympy and mpmath. Symbolic coefficients are exact; numerical
checks corroborate the formula but are not used to establish the limit.
"""
import sympy as s
import mpmath as mp

z, u, a, b = s.symbols('z u a b', real=True)
R = s.sec(z / 2) / 2
rho = s.Rational(3, 4) - a * z**2 - b * z**4
r = -R * s.cos(z * u) + s.sqrt(rho**2 - R**2 * s.sin(z * u)**2)
jet = s.series(r, z, 0, 6).removeO().expand()
area_over_pi = s.integrate(s.series(jet**2, z, 0, 6).removeO(), (u, -1, 1)) / 2
residual = s.series(area_over_pi - (1-rho)**2, z, 0, 6).removeO().expand()
c2 = s.simplify(residual.coeff(z, 2))
c4 = s.simplify(residual.coeff(z, 4))
assert c2 == -a - s.Rational(5, 288), c2
assert c4 == s.Rational(7, 216)*a - b - s.Rational(107, 69120), c4
aa = s.solve(c2, a)[0]
bb = s.solve(c4.subs(a, aa), b)[0]
assert aa == -s.Rational(5,288)
assert bb == -s.Rational(1313,622080)
h_jet = s.series(1/(s.Rational(1,4)+aa*z**2+bb*z**4),z,0,6).removeO().expand()
assert s.simplify(h_jet.coeff(z,2) - s.Rational(5,18)) == 0
assert s.simplify(h_jet.coeff(z,4) - s.Rational(2063,38880)) == 0
# Area deficit of K_n at zero erosion.
rzero = -R*s.cos(z*u)+s.sqrt(1-R**2*s.sin(z*u)**2)
rzerojet = s.series(rzero,z,0,4).removeO()
area0 = s.series(s.integrate(rzerojet**2,(u,-1,1))/2,z,0,4).removeO().expand()
assert area0 == s.Rational(1,4)-z**2/s.Integer(48)

mp.mp.dps = 60
for n in (3, 5, 7, 9, 15, 31, 101, 401):
    zz = mp.pi/n
    RR = 1/(2*mp.cos(zz/2))
    def area(t):
        rr=1-t
        return n*(rr**2*(zz-mp.asin(RR*mp.sin(zz)/rr)) + RR**2*mp.sin(2*zz)/2
                  - RR*mp.sin(zz)*mp.sqrt(rr**2-RR**2*mp.sin(zz)**2))
    t = mp.findroot(lambda tt: area(tt)-mp.pi*tt**2, (mp.mpf('.2'),mp.mpf('.3')))
    assert 0 < t < 1-RR
    assert abs(area(t)-mp.pi*t**2) < mp.mpf('1e-49')
    approx = 4+5*zz**2/18+mp.mpf(2063)*zz**4/38880
    if n >= 31:
        assert abs(1/t-approx) < mp.mpf('1.2')*zz**6
    print('n=',n,'h=',mp.nstr(1/t,18),'h_minus_two_term=',mp.nstr(1/t-approx,8))
print('EXACT_SYMBOLIC_CHECKS_PASSED')
