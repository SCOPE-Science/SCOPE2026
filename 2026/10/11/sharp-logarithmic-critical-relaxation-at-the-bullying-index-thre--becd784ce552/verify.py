import sympy as sp

x, y, b, beta, c, alpha = sp.symbols("x y b beta c alpha", positive=True)
xstar = c / alpha
xdot = c*beta/alpha - beta*x - b*x*y
ydot = -c*y + alpha*x*y

V = x - xstar - xstar*sp.log(x/xstar) + (b/alpha)*y
Vdot = sp.simplify(sp.diff(V, x)*xdot + sp.diff(V, y)*ydot)
target_Vdot = -beta*(x-xstar)**2/x
assert sp.simplify(Vdot - target_Vdot) == 0

q, Y = sp.symbols("q Y")
qdot = -beta*q - b*(1+q)*Y
Ydot = c*q*Y

r = q + (b/beta)*Y
rdot = sp.expand(qdot + (b/beta)*Ydot)
target_rdot = -beta*r + b*(c-beta)*q*Y/beta
assert sp.simplify(rdot - target_rdot) == 0

a2 = b**2*(beta-c)/beta**3
s = q + (b/beta)*Y - a2*Y**2
sdot = sp.expand(qdot + (b/beta)*Ydot - 2*a2*Y*Ydot)
coef = -beta + b*(c-beta)*Y/beta + 2*b**2*c*(c-beta)*Y**2/beta**3
target_sdot = (
    coef*s
    - b**3*(beta-c)*(beta-3*c)*Y**3/beta**4
    - 2*b**4*c*(beta-c)**2*Y**4/beta**6
)
assert sp.simplify(sdot - target_sdot) == 0

lam = b*c/beta
log_coeff = sp.simplify(-c*a2/lam)
assert sp.simplify(log_coeff - b*(c-beta)/beta**2) == 0

print("VERIFY_OK")
