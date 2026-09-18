import sympy as sp

# Standalone exact/symbolic checks for the conditioning-dependent affine
# reflected-gradient stability threshold.
t, c, q = sp.symbols('t c q', positive=True, real=True)
A = (1-c)*(1-2*c)/(5-4*c)
B = 2*(1-c)/(5-4*c)

# Unit-circle contact: t^2 = B(c) and q = A(c)/t.
c_of_t = sp.factor(sp.solve(sp.Eq(t**2, B), c)[0])
phi = sp.factor((A.subs(c, c_of_t))/t)
poly_identity = sp.factor(2*(1-2*t**2)*(phi-q))
dphi = sp.factor(sp.diff(phi, t))

print('c(t) =', c_of_t)
print('phi(t) =', phi)
print('2(1-2t^2)(phi-q) =', poly_identity)
print('phi prime =', dphi)
print('phi(1/sqrt(3)) =', sp.simplify(phi.subs(t, 1/sp.sqrt(3))))
print('phi(2/3) =', sp.simplify(phi.subs(t, sp.Rational(2,3))))

# Representative q=1/2.
q0 = sp.Rational(1, 2)
poly = 3*t**3 + 4*q0*t**2 - t - 2*q0
roots = sp.nroots(poly, n=50)
t0 = [sp.re(r) for r in roots
      if abs(sp.im(r)) < sp.Float('1e-40')
      and sp.re(r) > 1/sp.sqrt(3)
      and sp.re(r) < sp.Rational(2,3)][0]
c0 = sp.N(c_of_t.subs(t, t0), 40)
theta = sp.acos(c0)
r = sp.exp(-sp.I*theta)
z_target = q0 + sp.I*sp.sqrt(1-q0**2)
z_map = sp.simplify(-(r**2-r)/(t0*(2*r-1)))
residual = sp.N(r**2-r+t0*(2*r-1)*z_target, 20)
print('q=1/2 tau* =', sp.N(t0, 30))
print('q=1/2 contact cos(theta) =', c0)
print('q=1/2 mapped eigenvalue =', sp.N(z_map, 25))
print('q=1/2 boundary residual =', residual)

# Source-paper validation example B=(2I+J): sigma=2, L=sqrt(5).
q_ex = 2/sp.sqrt(5)
poly_ex = 3*t**3 + 4*q_ex*t**2 - t - 2*q_ex
roots_ex = sp.nroots(poly_ex, n=50)
t_ex = [sp.re(r) for r in roots_ex
        if abs(sp.im(r)) < sp.Float('1e-40')
        and sp.re(r) > 1/sp.sqrt(3)
        and sp.re(r) <= sp.Rational(2,3)][0]
lambda_ex = t_ex/sp.sqrt(5)
print('sigma=2,L=sqrt(5): tau* =', sp.N(t_ex, 30))
print('sigma=2,L=sqrt(5): lambda* =', sp.N(lambda_ex, 30))
print('lambda*/(1/64) =', sp.N(64*lambda_ex, 30))

# Endpoint q=1 gives t=2/3 and boundary root r=-1.
endpoint_poly = sp.factor((3*t**3 + 4*t**2 - t - 2).subs(t, sp.Rational(2,3)))
endpoint_residual = sp.simplify(((-1)**2-(-1)) + sp.Rational(2,3)*(2*(-1)-1))
print('q=1 cubic at t=2/3 =', endpoint_poly)
print('q=1 scalar boundary residual at r=-1 =', endpoint_residual)
