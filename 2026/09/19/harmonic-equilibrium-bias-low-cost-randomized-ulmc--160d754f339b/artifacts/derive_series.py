import sympy as sp

h, t, y = sp.symbols("h t y")
gamma, alpha, kappa = sp.symbols("gamma alpha kappa", positive=True)
delta, beta = sp.symbols("delta beta")


def trunc(expr, n=5):
    return sp.series(expr, h, 0, n).removeO().expand()


E = trunc(sp.exp(-gamma*h), 5)
H = trunc((1-sp.exp(-gamma*h))/gamma, 5)
s = (1-t)*h
cx = trunc(alpha*h*(1-sp.exp(-gamma*s))/gamma, 5)
ds = trunc(alpha*h*sp.exp(-gamma*s), 5)
at = trunc((1-sp.exp(-gamma*t*h))/gamma, 5)
I = trunc(t*h/gamma - (1-sp.exp(-gamma*t*h))/gamma**2, 5)
q = delta*alpha*kappa*I
A = sp.Matrix([
    [trunc(1-kappa*cx*(1-q), 5), trunc(H-kappa*cx*at, 5)],
    [trunc(-kappa*ds*(1-q), 5), trunc(E-kappa*ds*at, 5)],
])

kxf = trunc((1-sp.exp(-gamma*h*(1-y)))/gamma, 4)
kvf = trunc(sp.exp(-gamma*h*(1-y)), 4)
kxp = trunc((1-sp.exp(-gamma*h*(t-y)))/gamma, 4)
Kx = trunc(kxf-beta*kappa*cx*kxp, 4)
Kv = trunc(kvf-beta*kappa*ds*kxp, 4)
scale = 2*gamma*alpha*h
Qxx = trunc(scale*(sp.integrate(trunc(Kx*Kx, 4), (y, 0, t)) + sp.integrate(trunc(kxf*kxf, 4), (y, t, 1))), 5)
Qxv = trunc(scale*(sp.integrate(trunc(Kx*Kv, 4), (y, 0, t)) + sp.integrate(trunc(kxf*kvf, 4), (y, t, 1))), 5)
Qvv = trunc(scale*(sp.integrate(trunc(Kv*Kv, 4), (y, 0, t)) + sp.integrate(trunc(kvf*kvf, 4), (y, t, 1))), 5)
Q = sp.Matrix([[Qxx, Qxv], [Qxv, Qvv]])

x1, x2, x3, c1, c2, c3, v1, v2, v3 = sp.symbols("x1 x2 x3 c1 c2 c3 v1 v2 v3")
S = sp.Matrix([
    [1/kappa+x1*h+x2*h**2+x3*h**3, c1*h+c2*h**2+c3*h**3],
    [c1*h+c2*h**2+c3*h**3, alpha+v1*h+v2*h**2+v3*h**3],
])
R = S - (A*S*A.T + Q)
Rbar = sp.Matrix(2, 2, lambda i, j: sp.integrate(trunc(R[i, j], 5), (t, 0, 1)))
eqs = []
for order in range(1, 5):
    for i, j in [(0, 0), (0, 1), (1, 1)]:
        coeff = sp.expand(Rbar[i, j]).coeff(h, order)
        if coeff != 0:
            eqs.append(coeff)
unknowns = [x1, c1, v1, x2, c2, v2, x3, c3, v3]
sol = list(sp.linsolve(eqs, unknowns))[0]
print("Uniform-time predictor family coefficients")
for name, value in zip(unknowns, sol):
    print(name, "=", sp.factor(value))

# Independent arbitrary-time one-gradient predictor family through order h^2.
m1, m2 = sp.symbols("m1 m2")

def expectation_t(poly):
    p = sp.Poly(sp.expand(poly), t)
    moments = {0: 1, 1: m1, 2: m2, 3: sp.symbols("m3"), 4: sp.symbols("m4")}
    return sp.expand(sum(coef*moments[j] for (j,), coef in p.terms()))

A0 = A.subs({delta: 0})
Q0 = Q.subs({delta: 0})
x1b, x2b, c1b, c2b, v1b, v2b = sp.symbols("x1b x2b c1b c2b v1b v2b")
S0 = sp.Matrix([
    [1/kappa+x1b*h+x2b*h**2, c1b*h+c2b*h**2],
    [c1b*h+c2b*h**2, alpha+v1b*h+v2b*h**2],
])
R0 = S0-(A0*S0*A0.T+Q0)
R0bar = sp.Matrix(2, 2, lambda i, j: expectation_t(trunc(R0[i, j], 4)))
eqs0 = []
for order in range(1, 4):
    for i, j in [(0, 0), (0, 1), (1, 1)]:
        coeff = sp.expand(R0bar[i, j]).coeff(h, order)
        if coeff != 0:
            eqs0.append(coeff)
sol0 = sp.solve(eqs0, [x1b, c1b, v1b, x2b, c2b, v2b], dict=True)[0]
print("\nArbitrary-time one-gradient coefficients")
for z in [x1b, c1b, v1b, x2b, c2b, v2b]:
    print(z, "=", sp.factor(sol0[z]))
