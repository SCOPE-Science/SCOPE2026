import math
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq

# Symbolic small-u expansions for tanh activation.
x, u, r, eps = sp.symbols('x u r eps', positive=True)

# Gaussian expectation of an even Taylor polynomial in x=sqrt(u)Z.
def gaussian_expectation(series_expr, max_order):
    p = sp.series(series_expr, x, 0, max_order + 1).removeO().expand()
    out = 0
    for term in sp.Add.make_args(p):
        k = int(term.as_powers_dict().get(x, 0))
        if k % 2:
            continue
        coeff = sp.simplify(term / x**k) if k else term
        moment = 1 if k == 0 else sp.factorial2(k - 1)
        out += coeff * moment * u**(k // 2)
    return sp.expand(out)

F = gaussian_expectation(sp.sech(x)**4, 12)
G = gaussian_expectation(sp.tanh(x)**2, 12)

# Solve F(u)=1/(1+r), where r=g^2-1.
a = sp.symbols('a1:7')
u_series = sum(a[k-1]*r**k for k in range(1, 7))
resid = sp.series(F.subs(u, u_series) - 1/(1+r), r, 0, 7).removeO().expand()
sol = sp.solve([sp.Eq(resid.coeff(r,k), 0) for k in range(1,7)], a, dict=True)[0]
u_series = sp.expand(u_series.subs(sol))
y2_series = sp.series(u_series - (1+r)*G.subs(u,u_series), r, 0, 7).removeO().expand()
y2_eps = sp.series(y2_series.subs(r,(1+eps)**2-1), eps, 0, 7).removeO().expand()

assert sp.expand(u_series).coeff(r,1) == sp.Rational(1,2)
assert sp.expand(u_series).coeff(r,2) == sp.Rational(3,8)
assert sp.expand(u_series).coeff(r,3) == -sp.Rational(7,48)
assert y2_series.coeff(r,3) == sp.Rational(1,6)
assert y2_series.coeff(r,4) == -sp.Rational(1,8)
assert y2_series.coeff(r,5) == sp.Rational(31,160)
assert y2_eps.coeff(eps,3) == sp.Rational(4,3)
assert y2_eps.coeff(eps,4) == 0
assert y2_eps.coeff(eps,5) == sp.Rational(16,5)

# Literal printed Eq. (4.6) omits the Gaussian variable z.  At g=1.3,
# combine it with Eq. (4.5) and verify that it gives y_c^2<0, whereas
# the self-consistency inherited from Eqs. (4.2)-(4.3) gives y_c about 0.2.
def normal_expect(fun):
    val, err = quad(lambda z: math.exp(-z*z/2)/math.sqrt(2*math.pi)*fun(z),
                    -10.0, 10.0, epsabs=2e-13, epsrel=2e-13, limit=300)
    return val

def F_num(u0):
    return normal_expect(lambda z: 1.0/math.cosh(math.sqrt(u0)*z)**4)

def G_num(u0):
    return normal_expect(lambda z: math.tanh(math.sqrt(u0)*z)**2)

def critical(g):
    uc = brentq(lambda q: g*g*F_num(q)-1.0, 1e-14, 100.0, xtol=1e-13, rtol=1e-13)
    y2 = uc - g*g*G_num(uc)
    return uc, math.sqrt(y2)

g = 1.3
uc, yc = critical(g)
y2_printed = uc - g*g*math.tanh(math.sqrt(uc))**2
assert abs(uc - 0.5019011090908091) < 2e-11
assert abs(yc - 0.1958228668732753) < 2e-11
assert y2_printed < 0

# The paper uses A=sqrt(N), so the normalized target is q=1.
# This is a numerical consequence of the corrected critical equations only.
g_target1 = brentq(lambda gg: critical(gg)[1]-1.0, 1.5, 2.0, xtol=2e-12, rtol=2e-12)
assert abs(g_target1 - 1.8555891011388923) < 2e-10

print('F(u) =', sp.series(F,u,0,6))
print('G(u) =', sp.series(G,u,0,6))
print('u_c(r) =', sp.series(u_series,r,0,6))
print('y_c^2(r) =', sp.series(y2_series,r,0,6))
print('y_c^2(eps) =', sp.series(y2_eps,eps,0,6))
print('leading y_c(eps) coefficient =', 2/sp.sqrt(3))
print(f'g=1.3: u_c={uc:.15f}, corrected y_c={yc:.15f}')
print(f'g=1.3: literal-printed-Eq4.6 y_c^2={y2_printed:.15f}')
print(f'normalized target q=1 crossing (numerical) g={g_target1:.15f}')
print('all_checks_passed=True')
