import sympy as sp

sigma, k, beta, rho = sp.symbols("sigma k beta rho", positive=True)
x, y, z, v = sp.symbols("x y z v", real=True)
q = sp.symbols("q")

# Weak-rotation parametrization: s = (sigma^2-k^2)/3, 0 <= k < sigma.
srot = (sigma**2-k**2)/3
K = sigma**2+srot
M = sigma**2/K

P11 = (4*sigma-k)/(sigma*(2*sigma+k))
P12 = 2*(sigma-k)/(2*sigma+k)
P22 = (sigma-k)**2*(4*sigma+k)/(3*sigma*(2*sigma+k))
P = sp.Matrix([[P11, P12], [P12, P22]])

u = sp.Matrix([x, v])
A = sp.Matrix([[-sigma, srot], [-1, -sigma]])
B = sp.Matrix([sigma, 0])
udot = A*u+B*y
Sdot = sp.expand((u.T*P*udot)[0])

psi = sp.sqrt(2/K) * (
    sigma*y - (2*sigma-k)*x
    - (2*sigma-k)*(sigma-k)*v/3
)

# Remove the harmless positive square-root product before simplification.
residual = sp.expand(M*y**2-x*y-Sdot-sp.Rational(1,2)*psi**2)
residual = sp.factor(residual)

detP = sp.factor(P.det())

# Characteristic polynomial of the (x,y,v) linear block.
J = sp.Matrix([[-sigma, sigma, srot],
               [rho, -1, 0],
               [-1, 0, -sigma]])
charpoly = sp.expand(J.charpoly(q).as_expr())
expected = sp.expand(
    q**3 + (2*sigma+1)*q**2
    + (sigma**2+2*sigma+srot-sigma*rho)*q
    + (sigma**2+srot-sigma**2*rho)
)
char_residual = sp.factor(charpoly-expected)

print("storage_identity_residual =", residual)
print("det_P =", detP)
print("characteristic_polynomial_residual =", char_residual)
print("K =", sp.factor(K))
