#!/usr/bin/env python3
import sympy as s

t, R, a, b, lam, x, y = s.symbols(
    "t R a b lam x y", real=True
)

p = R + a*s.cos(2*t) + b*s.sin(5*t)
rho = s.trigsimp(p + s.diff(p,t,2))
assert s.simplify(
    rho - (R - 3*a*s.cos(2*t) - 24*b*s.sin(5*t))
) == 0

popp = R + a*s.cos(2*t) - b*s.sin(5*t)
assert s.simplify(s.trigsimp(p.subs(t,t+s.pi)-popp)) == 0
w_support = s.simplify((p-popp)/2)
assert s.simplify(w_support - b*s.sin(5*t)) == 0
w_rho = s.trigsimp(w_support+s.diff(w_support,t,2))
assert s.simplify(w_rho + 24*b*s.sin(5*t)) == 0

rho_opp = R - 3*a*s.cos(2*t) + 24*b*s.sin(5*t)
assert s.simplify(s.trigsimp(rho.subs(t,t+s.pi)-rho_opp)) == 0
num = s.trigsimp(s.diff(rho,t)*rho_opp-rho*s.diff(rho_opp,t))
target = -24*b*(
    10*R*s.cos(5*t)
    - a*(9*s.cos(7*t)+21*s.cos(3*t))
)
assert s.simplify(s.expand_trig(num-target)) == 0

F = s.expand(
    10*s.chebyshevt(5,x)
    + lam*(3*s.chebyshevt(7,x)+7*s.chebyshevt(3,x))
)
Q = (
    96*lam*y**3
    +(80-168*lam)*y**2
    +(-100+98*lam)*y
    +25-21*lam
)
assert s.factor(F-2*x*Q.subs(y,x**2)) == 0

disc = s.factor(s.discriminant(Q,y))
expected_disc = -6400*(lam**2+2*lam-4)*(147*lam**2+630*lam+500)
assert s.factor(disc-expected_disc) == 0
assert s.factor(Q.subs(y,0)-(25-21*lam)) == 0
assert s.factor(Q.subs(y,1)-5*(1+lam)) == 0

for L, middle in [
    (s.Rational(1,2), -6),
    (s.Rational(-1,2), -4),
]:
    q = s.expand(Q.subs(lam,L))
    assert q.subs(y,0) > 0
    assert s.simplify(q.subs(y,s.Rational(1,2))-middle) == 0
    assert q.subs(y,1) > 0

q0 = s.factor(Q.subs(lam,0))
r1 = (5-s.sqrt(5))/8
r2 = (5+s.sqrt(5))/8
assert s.simplify(q0.subs(y,r1)) == 0
assert s.simplify(q0.subs(y,r2)) == 0
assert 0 < float(r1) < 1
assert 0 < float(r2) < 1

for L in (-s.Rational(99,100), -s.Rational(1,2), -s.Rational(1,10),
          s.Rational(1,10), s.Rational(1,2), s.Rational(99,100)):
    roots = s.nroots(Q.subs(lam,L), n=40, maxsteps=100)
    inside = [
        complex(z) for z in roots
        if abs(complex(z).imag) < 1e-25
        and 0 < complex(z).real < 1
    ]
    assert len(inside) == 2

assert 31 > 3*abs(2) + 24*abs(1)

print("VERIFY_OK")
print("discriminant =", disc)
print("Q(0) =", s.factor(Q.subs(y,0)))
print("Q(1) =", s.factor(Q.subs(y,1)))
print("lambda_zero_roots =", r1, r2)
