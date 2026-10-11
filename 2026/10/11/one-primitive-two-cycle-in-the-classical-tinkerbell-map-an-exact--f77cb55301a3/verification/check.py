"""Exact rational-arithmetic certificate for the standard Tinkerbell two-cycle."""
import sympy as S

I = S.I
u = S.symbols('u', real=True)
t = S.symbols('t')
A = S.Rational(7, 10) + I*S.Rational(26013, 20000)
B = S.Rational(1, 5) + I*S.Rational(13987, 20000)
Bc, Ac = S.conjugate(B), S.conjugate(A)
P = S.expand(-B**2*t**3/4 - B*t**2 +
             (A**2/4-A/2+Ac*B/2+B/2-S.Rational(3,4))*t+B*Bc/2)
s_mid = -(1+A+B*t)/2
s_mid_conjugate = -(1+Ac+Bc/t)/2
assert S.expand(P - t*(s_mid-s_mid**2-A*s_mid-B*s_mid_conjugate)) == 0
Pc = S.expand(S.conjugate(P).subs(S.conjugate(t), 1/t))
H = S.cancel(t**3*(P-Pc))
t_u = (1+I*u)/(1-I*u)
Q = 44935000*u**6+3880000*u**5-108922000*u**4+267396169*u**3-240753000*u**2+83880000*u+25000000
# P(t)=conjugate(P(t)) iff Q(u)=0, for t=(1+iu)/(1-iu).
assert S.cancel(H.subs(t,t_u)*(1-I*u)**6 + I*Q/25000000) == 0
assert S.im(P.subs(t, -1)) != 0
poly = S.Poly(Q,u)
intervals = [(S.Rational(-123,50), S.Rational(-49,20)),
             (S.Rational(-183,1000), S.Rational(-181,1000))]
assert poly.count_roots(-S.oo,S.oo) == 2
assert [poly.count_roots(l,r) for l,r in intervals] == [1,1]
Pu = S.cancel(P.subs(t,t_u))
rho = S.factor(S.re(S.expand_complex(Pu)))
rho_expected = (291156169*u**6-1166544000*u**5+1701337014*u**4-990336000*u**3-266428507*u**2+1071376000*u-239520000)/(400000000*(1+u**2)**3)
assert S.cancel(rho-rho_expected) == 0
for (left,right), expected_sign in zip(intervals,[1,-1]):
    num, den = map(lambda z:S.Poly(z,u),S.fraction(S.cancel(rho)))
    assert num.count_roots(left,right)==0
    assert den.count_roots(left,right)==0
    assert S.sign(rho.subs(u,(left+right)/2))==expected_sign

# Real trace/determinant of the two-step Jacobian, evaluated on the physical branch.
t_inverse = 1/t_u
W = -1-B*t_u
Wc = -1-Bc*t_inverse
m = B*Bc
trace = S.factor(S.re(S.expand_complex(2*(W**2-4*rho/t_u+m))))
det = S.factor(S.re(S.expand_complex((W*Wc+4*rho-m)**2-
                  4*rho*(W**2*t_u+2*W*Wc+Wc**2*t_inverse))))
discriminant = S.factor(trace**2-4*det)
left,right=intervals[0]
for value,desired_sign in [(det-1,1),(discriminant,-1)]:
    num,den=S.fraction(S.cancel(value))
    assert S.Poly(num,u).count_roots(left,right)==0
    assert S.Poly(den,u).count_roots(left,right)==0
    assert S.sign(value.subs(u,(left+right)/2))==desired_sign
print('PASS: sextic identity, exact two-real-root count, unique positive branch, conjugate repelling multipliers.')
