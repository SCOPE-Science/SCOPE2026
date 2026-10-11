import sympy as sp
q,r,nu,eps,c,ybar=sp.symbols('q r nu eps c ybar', positive=True)
mu=(1-q)/r
# Stationarity: ybar=q*(ybar+eps*c)
y_sol=sp.solve(sp.Eq(ybar,q*(ybar+eps*c)),ybar)[0]
rho=nu*(1+mu*y_sol)+eps*nu*mu*c
assert sp.simplify(rho-(nu+nu*eps*c/r))==0
kappa=nu*(1-q)/(r*q)
yprime=q*(sp.Symbol('y')+eps*sp.Symbol('C'))
delta=nu*(1+mu*sp.Symbol('y'))+eps*nu*mu*sp.Symbol('C')
assert sp.simplify(delta-(nu+kappa*yprime))==0
yplus=q*eps/(1-q)
yminus=-yplus
assert sp.simplify(nu+kappa*yplus-(nu+nu*eps/r))==0
assert sp.simplify(nu+kappa*yminus-(nu-nu*eps/r))==0
print('ALGEBRA_OK')
