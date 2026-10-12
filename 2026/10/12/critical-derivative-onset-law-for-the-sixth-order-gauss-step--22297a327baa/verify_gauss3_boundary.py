"""Exact algebraic checks and illustrative numerical witnesses for a Padé derivative-onset law."""
import sympy as S
import mpmath as M

x, a, t, q = S.symbols('x a t q')
P = lambda z: 120 + 60*z + 12*z**2 + z**3
Q = lambda z: 120 - 60*z + 12*z**2 - z**3
pole_poly = a**3 - 12*a**2 + 60*a - 120
radius_poly = q**3 + 6*q**2 - 40
R = P(x)/Q(x)
assert S.simplify(R.subs(x, 0) - 1) == 0
assert S.simplify(pole_poly.subs(a, 4*(q+5)/(q+4)) + 8*radius_poly/(q+4)**3) == 0

# Residue domination at the common-distance center.
alpha = (12-a)/2
m = a*a-12*a+60
D = S.expand(m**2-16*m*alpha+80*alpha**2+24*m-320*alpha+400)
N = S.expand(m**2-20*m+40*alpha**2+100)
d = a*a-8*a+20
assert S.expand(D-d*(a*a-8*a+32)) == 0
residue_margin = S.expand((a*a+10)**2*D - 4*d*d*N)
assert S.rem(residue_margin, pole_poly, a) == 480*(27*a*a-125*a+20)
assert 27*S.Rational(9,2)**2-125*S.Rational(9,2)+20 == S.Rational(17,4)

# The pole angle is irrational in units of pi: double-angle cosine is not integral.
r = 4*(5-a)/(a-4)
beta_squared = S.factor(m-alpha**2)
assert S.simplify(beta_squared-3*(a*a-8*a+32)/4) == 0
u = S.factor(2-4*beta_squared/(a+r)**2)
num, den = S.fraction(u)
res = S.factor(S.resultant(pole_poly,S.expand(t*den-num),a))
assert S.simplify(res-4096*(25*t**3-195*t**2+534*t-353)) == 0
f = S.Poly(25*t**3-195*t**2+534*t-353,t)
assert f.is_irreducible
assert S.Poly(f.as_expr(),t,modulus=2).is_irreducible
assert f.LC() == 25

# A finite absorbing pure-birth witness strictly past the classical radius.
y = S.symbols('y')
shifted = S.cancel(R.subs(x,y-3))
coef = S.series(shifted,y,0,14).removeO().coeff(y,13)
assert coef == -S.Rational(89074180199761943704,147108257121214334362554931640625)
assert coef < 0

# Approximations are evidence for scale, not proof of the limit.
M.mp.dps = 60
a0 = M.findroot(lambda v:v**3-12*v**2+60*v-120,(M.mpf('4.6'),M.mpf('4.7')))
rho = 4*(5-a0)/(a0-4)
al = (12-a0)/2
bet = M.sqrt(a0*a0-12*a0+60-al*al)
b = M.mpc(al,bet)
A = lambda z: -8*(z*z+10)/(z*z-8*z+20)
U = abs(A(a0)); W = 2*abs(A(b))
C = (a0+rho)**2/(a0-al)*M.log(U/W)
assert U > W and M.mpf('2.207606805') < rho < M.mpf('2.207606806')
assert M.mpf('3.80980') < C < M.mpf('3.80982')
for ds in ('0.2','0.1','0.05','0.02','0.01','0.005'):
    delta = M.mpf(ds); s = rho+delta
    den_a, den_b = a0+s,b+s
    def scaled(k):
        return M.re(-A(a0)-2*A(b)*(den_a/den_b)**(k+1))
    k = next(k for k in range(1,10000) if scaled(k)<0)
    assert scaled(k-1)>=0
    print('delta',ds,'first_negative_order',k,'scaled_product',M.nstr(delta*k,12))
print('rho',M.nstr(rho,19),'onset_constant',M.nstr(C,19))
print('VERIFY_OK')
