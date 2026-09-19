import math
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

# Exact parameter mapping from the normal variational equation to s=1 Whittaker-Hill.
a, b = sp.symbols('a b', nonzero=True, real=True)
alpha = a/(2*b)
lam = 4/b**2 - 2*alpha**2
checks = {
    'cos2_coefficient': sp.simplify(4*alpha - 2*a/b),
    'cos4_coefficient': sp.simplify(2*alpha**2 - a**2/(2*b**2)),
    'spectral_shift': sp.simplify(lam + 2*alpha**2 - 4/b**2),
}

# Principal anti-periodic gap: lambda = 1 + s*r - r^2/8 + O(r^3), r=a/b.
eps, s = sp.symbols('eps s', real=True)
c1, c2 = sp.symbols('c1 c2')
beta = 2 + c1*eps + c2*eps**2
r = eps/beta
A = (4 - eps**2/2)/beta**2
edge = 1 + s*r - r**2/8
series = sp.series(A-edge, eps, 0, 3).removeO().expand()
sol = sp.solve([
    sp.Eq(series.coeff(eps,1),0),
    sp.Eq(series.coeff(eps,2),0)
], [c1,c2], dict=True)[0]


def monodromy(a0, b0):
    T = 2*math.pi/abs(b0)
    def rhs(t, y):
        M = y.reshape(2,2)
        theta = -b0*t
        J = np.array([[0.0, 1.0], [-1.0, -a0*math.sin(theta)]])
        return (J @ M).ravel()
    soln = solve_ivp(rhs, (0.0,T), np.eye(2).ravel(), method='DOP853',
                     rtol=2e-11, atol=2e-13)
    M = soln.y[:,-1].reshape(2,2)
    return M

b0 = 0.5
root = brentq(lambda x: np.trace(monodromy(x,b0)) + 2.0,
              1.5, 1.6, xtol=2e-12, rtol=2e-12)
Mroot = monodromy(root,b0)
Mlo = monodromy(1.5,b0)
Mhi = monodromy(1.6,b0)

Mprimary = monodromy(0.1,2.0)
eigs_primary = np.linalg.eigvals(Mprimary)
chi_num = math.log(max(abs(eigs_primary)))/(math.pi)
chi_lead = 0.1/4

print('symbolic_checks')
for k,v in checks.items():
    print(f'{k}={v}')
print(f'principal_edge_c1={sp.simplify(sol[c1])}')
print(f'principal_edge_c2={sp.simplify(sol[c2].subs(s**2,1))}')
print('numerical_checks')
print(f'b=0.5 critical_a={root:.12f}')
print(f'trace_at_root={np.trace(Mroot):.12f}')
print(f'det_at_root={np.linalg.det(Mroot):.12f}')
print(f'trace_a_1.5={np.trace(Mlo):.12f}')
print(f'trace_a_1.6={np.trace(Mhi):.12f}')
print(f'b=2,a=0.1 growth_rate={chi_num:.12f}')
print(f'b=2,a=0.1 leading_prediction={chi_lead:.12f}')
print('all_symbolic_checks_passed=' + str(all(v == 0 for v in checks.values())))
