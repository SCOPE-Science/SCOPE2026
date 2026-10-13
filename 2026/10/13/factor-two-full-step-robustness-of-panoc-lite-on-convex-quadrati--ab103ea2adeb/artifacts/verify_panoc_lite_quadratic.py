import sympy as sp

# Noncommuting two-dimensional quadratic composite.
A = sp.Matrix([[2, 0], [0, 1]])
B = sp.Matrix([[1, sp.Rational(1, 2)],
               [sp.Rational(1, 2), 1]])
assert A*B != B*A

gamma = sp.Rational(3, 4)
Lf = sp.Integer(2)
assert gamma > 1/Lf
assert gamma < 2/Lf

P = (sp.eye(2) + gamma*B).inv()
H = A + B
assert all(v > 0 for v in H.eigenvals())

a = sp.Matrix([1, -1])
b = sp.Matrix([sp.Rational(-1, 2), sp.Rational(1, 3)])
xstar = -H.inv()*(a+b)
barstar = (sp.eye(2) + gamma*B)*xstar + gamma*b

# PANOC-lite initialization and one generic iteration state.
x0 = sp.Matrix([3, -2])
hat = P*(x0 - gamma*b)
grad = A*hat + a
bar = hat - gamma*grad
y = P*(bar - gamma*b)

Rnat = (hat-y)/gamma
Rnor = A*y + a + (bar-y)/gamma
J = H*P
dN = -J.inv()*Rnor

assert sp.simplify(dN - (barstar-bar)) == sp.zeros(2, 1)
assert sp.simplify(P*(barstar-gamma*b) - xstar) == sp.zeros(2, 1)

def phi(x):
    return (sp.Rational(1,2)*(x.T*A*x)[0] + (a.T*x)[0]
            + sp.Rational(1,2)*(x.T*B*x)[0] + (b.T*x)[0])

c_gamma = gamma*(2-gamma*Lf)/2
sigma = sp.Rational(1, 8)
assert 0 < sigma < c_gamma

for theta in [sp.Rational(0), sp.Rational(1,2), sp.Rational(1),
              sp.Rational(3,2), sp.Rational(2)]:
    zplus = bar + theta*dN
    hplus = P*(zplus-gamma*b)

    identity = sp.simplify(
        hplus - (xstar + (1-theta)*(y-xstar))
    )
    assert identity == sp.zeros(2, 1)

    energy_identity = sp.simplify(
        phi(hplus)-phi(xstar)
        - (1-theta)**2*(phi(y)-phi(xstar))
    )
    assert energy_identity == 0

    lhs = sp.simplify(phi(hplus)-phi(hat))
    rhs = sp.simplify(-sigma*(Rnat.T*Rnat)[0])
    assert sp.simplify(lhs-rhs) <= 0

# The exact Newton scaling theta=1 lands at the minimizer.
h_exact = P*((bar+dN)-gamma*b)
assert sp.simplify(h_exact-xstar) == sp.zeros(2, 1)

# Sharp scalar rejection outside [0,2].
# f(x)=x^2/2, g=0, gamma=1/2, c_gamma=3/8, sigma=37/100.
L = sp.Integer(1)
gamma_s = sp.Rational(1,2)
r = gamma_s*L
c_s = gamma_s*(2-r)/2
sigma_s = sp.Rational(37,100)
assert 0 < sigma_s < c_s
x = sp.Integer(1)

for theta in [sp.Rational(-1,2), sp.Rational(5,2)]:
    candidate = (1-theta)*(1-r)*x
    lhs = sp.Rational(1,2)*L*(candidate**2-x**2)
    rhs = -sigma_s*(L*x)**2
    assert lhs > rhs

print("VERIFY_OK")
