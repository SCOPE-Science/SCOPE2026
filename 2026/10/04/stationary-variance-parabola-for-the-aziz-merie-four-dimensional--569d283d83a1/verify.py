import sympy as s
x,y,z,w=s.symbols("x y z w")
rho,a,delta,phi,k=s.symbols("rho a delta phi k", nonzero=True)
f=s.Matrix([rho*(y-x), a*x-delta*x*z+w, phi*x*y-z, -k*x])
vars=(x,y,z,w)
def L(g):
    return s.expand(sum(s.diff(g,v)*fv for v,fv in zip(vars,f)))
assert s.expand(L(x**2/s.Integer(2)) - rho*x*(y-x)) == 0
assert s.expand(L(z) - (phi*x*y-z)) == 0
assert s.expand(L(w**2/s.Integer(2)) + k*x*w) == 0
assert s.expand(L(x*w) - (rho*y*w-rho*x*w-k*x**2)) == 0
assert s.expand(L(y**2/s.Integer(2)) - (a*x*y-delta*x*y*z+y*w)) == 0
assert s.expand(L(z**2/s.Integer(2)) - (phi*x*y*z-z**2)) == 0
B=s.simplify((a+k/rho)/delta)
# Stationary moment elimination: q=E[x^2], E[xy]=q, E[xw]=0,
# E[yw]=k*q/rho, E[xyz]=B*q, zbar=phi*q, E[z^2]=phi*B*q=B*zbar.
q=s.symbols("q")
yw=k*q/rho
xyz=s.simplify((a*q+yw)/delta)
assert s.simplify(xyz-B*q)==0
zbar=phi*q
z2=s.simplify(phi*xyz)
assert s.simplify(z2-B*zbar)==0
Bp=s.simplify(B.subs({rho:s.Integer(10),a:s.Rational(593,2),delta:s.Integer(40),k:s.Integer(8)}))
assert Bp==s.Rational(2973,400)
assert s.simplify(Bp/s.Integer(10))==s.Rational(2973,4000)
print("VERIFY_OK")
