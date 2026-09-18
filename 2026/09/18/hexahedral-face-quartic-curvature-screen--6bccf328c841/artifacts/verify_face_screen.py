import sympy as sp

s,t = sp.symbols('s t', real=True)
a0,a1,b0,b1,b2,c0,c1,c2 = sp.symbols('a0 a1 b0 b1 b2 c0 c1 c2', real=True)
a = a0+a1*t
b = b0+b1*t+b2*t**2
c = c0+c1*t+c2*t**2
f = a*s**2+b*s+c
sv = -b/(2*a)
h = sp.cancel(f.subs(s,sv))
P = sp.expand(4*a**2*sp.diff(f,t).subs(s,sv))
assert sp.simplify(sp.diff(h,t)-P/(4*a**2)) == 0

# At a stationary root P=0, det(Hess f) = P'/(2a).
H = sp.hessian(f,(s,t))
detH = sp.factor(H.det().subs(s,sv))
identity = sp.factor(2*a*detH - sp.diff(P,t) + 2*a1*P/a)
assert sp.simplify(identity) == 0
# Hence when P=0: detH=P'/(2a).

# Fourth derivative of the reduced vertex value is nonpositive on a>0.
# Constant-a case.
A,B0,B1,B2,C0,C1,C2 = sp.symbols('A B0 B1 B2 C0 C1 C2', real=True, nonzero=True)
bc = B0+B1*t+B2*t**2
cc = C0+C1*t+C2*t**2
hc = sp.expand(cc-bc**2/(4*A))
assert sp.simplify(sp.diff(hc,t,4) + 6*B2**2/A) == 0

# Nonconstant-a case: divide b=a*l+r.  The rational remainder controls h''''.
q,r = sp.div(sp.Poly(b,t), sp.Poly(a,t))
l = q.as_expr()
r0 = r.as_expr()
hdiv = sp.cancel(c - a*l**2/4 - r0*l/2 - r0**2/(4*a))
assert sp.simplify(h-hdiv) == 0
assert sp.simplify(sp.diff(h,t,4) + 6*r0**2*a1**4/a**5) == 0

# Sharp three-stationary-root example within the face-polynomial class.
a_ex = sp.Integer(1)
b_ex = t**2-t-sp.Rational(1,10)
c_ex = sp.Rational(13,100)*t-sp.Rational(13,100)*t**2
f_ex = a_ex*s**2+b_ex*s+c_ex
sv_ex = -b_ex/2
P_ex = sp.factor(4*sp.diff(f_ex,t).subs(s,sv_ex))
expected = -4*(t-sp.Rational(1,5))*(t-sp.Rational(1,2))*(t-sp.Rational(4,5))
assert sp.expand(P_ex-expected)==0
roots=[sp.Rational(1,5),sp.Rational(1,2),sp.Rational(4,5)]
assert all(0 < sv_ex.subs(t,x) < 1 for x in roots)
slopes=[sp.simplify(sp.diff(P_ex,t).subs(t,x)) for x in roots]
assert slopes[0] < 0 and slopes[1] > 0 and slopes[2] < 0

print('symbolic identities: verified')
print('example P(t) =', sp.factor(P_ex))
print('feasible s*(roots) =', [sp.simplify(sv_ex.subs(t,x)) for x in roots])
print("P'(roots) =", slopes)
