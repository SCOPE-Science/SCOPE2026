from sympy import Matrix, symbols, Poly, expand

x = symbols("x")

def eval_poly_matrix(poly, X):
    p = Poly(poly, x)
    n = X.rows
    out = Matrix.zeros(n)
    I = Matrix.eye(n)
    for (deg,), coeff in p.terms():
        out += coeff * (X ** deg if deg else I)
    return out

# Sharpness: ranks are (1,...,1) versus ell.
for ell in range(1, 8):
    lambdas = list(range(ell))
    fs = []
    for i in range(ell):
        f = 1
        for j in range(ell):
            if i != j:
                f *= x - lambdas[j]
        fs.append(expand(f))
    X = Matrix.diag(*lambdas)
    ranks = [eval_poly_matrix(f, X).rank() for f in fs]
    target = Matrix.eye(ell).rank()
    assert ranks == [1] * ell
    assert target == ell

# Nonmembership witnesses: all generators vanish on J_a(lambda), target does not.
def jordan(a, lam):
    J = lam * Matrix.eye(a)
    for i in range(a - 1):
        J[i, i + 1] = 1
    return J

examples = [
    (3, 2, 2, [(x-2)**3, (x-2)**4*(x+1)], (x-2)**2*(x+3)),
    (4, -1, 1, [(x+1)**4*(x-3), (x+1)**5], (x+1)*(x**2+1)),
    (2, 5, 0, [(x-5)**2, (x-5)**3*(x+2)], x+1),
]
for a, lam, b, fs, g in examples:
    X = jordan(a, lam)
    assert all(eval_poly_matrix(f, X) == Matrix.zeros(a) for f in fs)
    assert eval_poly_matrix(g, X) != Matrix.zeros(a)
    assert eval_poly_matrix(g, X).rank() > 0

print("VERIFY_OK")
print("sharpness_cases=7")
print("obstruction_cases=3")
