"""Exact algebraic checks for centered and raw dispersion coefficients."""
import sympy as sp

D, L, a, b = sp.symbols('D L a b', positive=True)
y = sp.symbols('y', real=True)
S, delta = a + b, a - b
H = 2*D + L*S
Q, v = 2*D*L/H, 2*D*delta/H


def same(lhs, rhs):
    assert sp.factor(lhs - rhs) == 0


# y=u/L; densities in u and y differ by L.
rho_y = 1 + (L*delta/H)*(1-2*y)
rho_0, rho_L = rho_y.subs(y, 0)/L, rho_y.subs(y, 1)/L
same(sp.integrate(rho_y, (y, 0, 1)), 1)
same(-D*sp.diff(rho_y, y)/L**2, v/L)
same(a*rho_L - b*rho_0, v/L)

# Derive psi from the endpoint jump size, without imposing the displacement.
q = sp.symbols('q')
psi_q = sp.integrate(q*(b+delta*y)*L/D, (y, 0, y))
q_root, = sp.solve(q-L+psi_q.subs(y, 1)-psi_q.subs(y, 0), q)
same(q_root, Q)
psi = psi_q.subs(q, q_root)
dpsi = sp.diff(psi, y)/L
same(D*dpsi.subs(y, 0), b*Q)
same(D*dpsi.subs(y, 1), a*Q)
same(D*sp.diff(dpsi, y)/L, v)

chi = psi-L*y
alpha, eta = 2*D/H, L*delta/H
same(chi, -L*(alpha*y+eta*y*(1-y)))
chi_bar = sp.integrate(chi*rho_y, (y, 0, 1))
same(chi_bar, L*(-alpha/2+alpha*eta/6-eta/6))
c_mid = chi.subs(y, sp.Rational(1, 2)) - chi_bar
same(c_mid, -L**2*delta*(6*D+L*S)/(12*H**2))

diffusion = D*sp.integrate(dpsi**2*rho_y, (y, 0, 1))
variance = sp.factor(diffusion + Q**2*(a*rho_L+b*rho_0)/2)
same(variance, D*L*S/H - D*L**2*(4*D+L*S)*delta**2/(3*H**3))
raw_mid = sp.factor(variance + v*c_mid)
same(raw_mid, D*L*S/H - D*L**2*(14*D+3*L*S)*delta**2/(6*H**3))
printed = D*L*(24*D**2*S + 2*D*L*(7*a*a+34*a*b+7*b*b)
               + L**2*S*(5*a*a+14*a*b+5*b*b))/(6*H**3)
same(variance-printed, D*L**2*(2*D-L*S)*delta**2/(6*H**3))
same(raw_mid-printed, -D*L**2*delta**2/(3*H**2))

one_way = {D: 1, L: 1, a: 1, b: 0}
same(variance.subs(one_way), sp.Rational(22, 81))
same(raw_mid.subs(one_way), sp.Rational(37, 162))
same(printed.subs(one_way), sp.Rational(43, 162))
s = sp.symbols('s', positive=True)
laplace = 1/(sp.cosh(sp.sqrt(s)) + sp.sqrt(s)*sp.sinh(sp.sqrt(s)))
poly = sp.series(laplace, s, 0, 3).removeO()
mean, second = -poly.coeff(s), 2*poly.coeff(s, 2)
same(mean, sp.Rational(3, 2))
same(second-mean**2, sp.Rational(11, 6))
same((second-mean**2)/(2*mean**3), variance.subs(one_way))
print('PASS: mean offset, centered and raw dispersion, printed comparisons, renewal limit')
