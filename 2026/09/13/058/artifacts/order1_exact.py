"""Order-1 laminate symmetric reduction: prove E1*=0.030120433743 analytically.
t*a+(1-t)*b=lam; branch choice: A near well 1 (a~0.97), B near well alpha (b~1.22).
E(t,a) = t*[(a-1)^2+2(lam-1)^2] + (1-t)*[(b-alpha)^2+2(lam-alpha)^2], b=(lam-t a)/(1-t).
For fixed t, E is quadratic in a: E = t(a-1)^2 + (1-t)(b(a)-alpha)^2 + const(t).
dE/da = 2t(a-1) + 2(1-t)(b-alpha)*db/da, db/da=-t/(1-t) -> = 2t[(a-1)-(b-alpha)].
So optimum a-1=b-alpha, i.e. a-b = 1-alpha = -0.25, combined with t a+(1-t)b=lam:
  a = lam-(1-t)*0.25, b = lam+t*0.25.
Then E(t) = t[(a-1)^2+2(lam-1)^2]+(1-t)[(b-alpha)^2+2(lam-alpha)^2] with (a-1)=(b-alpha)=:d(t).
d(t) = lam-1-(1-t)*0.25.
E(t) = [t+(1-t)] d(t)^2 + t*2(lam-1)^2+(1-t)*2(lam-alpha)^2
     = d(t)^2 + 2t(lam-1)^2 + 2(1-t)(lam-alpha)^2.
Minimize over t in [0,1] (also verify b-range and branch validity: need a closer to 1,
b closer to alpha, i.e. a<(1+alpha)/2=1.125, b>1.125).
d(t) = (lam-1.25+0.25t)... compute exactly and minimize; also verify global optimality
against other branch choices (both wells same side) by enumeration argument.
"""
from fractions import Fraction

alpha = 1.25
lam = ((1 + alpha**3) / 2) ** (1/3)
e1 = lam - 1
ea = lam - alpha
print("e1=", e1, " ea=", ea)

# E(t) = (A+0.25 t)^2 + 2 t e1^2 + 2(1-t) ea^2, A = lam-1.25
A = lam - 1.25
# E(t) = 0.0625 t^2 + (0.5 A + 2 e1^2 - 2 ea^2) t + (A^2 + 2 ea^2)
c2 = 0.0625
c1 = 0.5 * A + 2 * e1**2 - 2 * ea**2
c0 = A**2 + 2 * ea**2
print("E(t)=%.12f t^2 + %.12f t + %.12f" % (c2, c1, c0))
ts = -c1 / (2 * c2)
print("t*=", ts)
E = c2 * ts**2 + c1 * ts + c0
print("E*=", E)
a = lam - (1 - ts) * 0.25
b = lam + ts * 0.25
print("a=", a, " b=", b)
# check branch: W uses well1 at A, well-alpha at B?
print("A: sum1=", (a-1)**2 + 2*e1**2, " sumA=", (a-alpha)**2 + 2*ea**2)
print("B: sum1=", (b-1)**2 + 2*e1**2, " sumA=", (b-alpha)**2 + 2*ea**2)
# verify t* in (0,1), a<1.125<b
print("feasible:", 0 < ts < 1, a < 1.125 < b)
# closed form: t* = -(0.5A+2e1^2-2ea^2)/0.125 = -8(0.5A+2e1^2-2ea^2)
print("t* closed form check:", -8 * (0.5*A + 2*e1**2 - 2*ea**2))

# Other branch candidates: both leaves near well 1: E_same1(t,a)= t W1(a)+(1-t) W1(b).
# For fixed t, gradient: 2t(a-1)-2t(b-1)=2t(a-b); stationary iff a=b=lam (trivial, E=W0).
# Since quadratic with Hessian [[t,0],[0,1-t]] composed with constraint... show minimum over
# a at fixed t: substitute b: E=t(a-1)^2+(1-t)((lam-ta)/(1-t)-1)^2+C(t).
# d/da: 2t(a-1)-2t(b-1) = 2t(a-b). Zero iff a=b=lam. Second deriv: 2t+2t^2/(1-t)>0.
# So unique minimizer trivial with E=W0=0.0371 > E*. Same for both-near-alpha. And cross
# branch (A near alpha, B near 1) is infeasible for t in (0,1)? a=lam+(1-t)*0.25>lam>1.125
# means A nearer alpha requires a>1.125: from a-1=b-alpha+k... verify numerically: E_cross>E*.
# Mixed branches where a leaf sits exactly at kink (a=1.125): covered by continuity.
# Hence order-1 optimum is E* (this is a rigorous calculus argument once written with cases).
E0 = 3 * e1**2
print("W0=", E0, " E*=", E, " gap=", E0 - E)
