from sympy import Matrix, diag

U = Matrix([[0, 1], [1, 0]])
# Positive-definite E8 Cartan matrix.
E8 = Matrix([
    [2,-1, 0, 0, 0, 0, 0, 0],
    [-1,2,-1, 0, 0, 0, 0, 0],
    [0,-1, 2,-1, 0, 0, 0,-1],
    [0, 0,-1, 2,-1, 0, 0, 0],
    [0, 0, 0,-1, 2,-1, 0, 0],
    [0, 0, 0, 0,-1, 2,-1, 0],
    [0, 0, 0, 0, 0,-1, 2, 0],
    [0, 0,-1, 0, 0, 0, 0, 2],
])
G = diag(U, Matrix([[1]]), U, E8)
assert G.rows == G.cols == 13
assert G.det() == 1
# Sylvester inertia from exact LDL is awkward at isotropic pivots; exact eigenvalue signs
# are enough here because the characteristic polynomials factor over radicals.
eigs = G.eigenvals()
pos = neg = zero = 0
for ev, mult in eigs.items():
    val = ev.evalf(50)
    if val > 0:
        pos += mult
    elif val < 0:
        neg += mult
    else:
        zero += mult
assert (pos, neg, zero) == (11, 2, 0)
assert any(G[i,i] % 2 for i in range(13))
print(f"rank={G.rows}")
print(f"determinant={G.det()}")
print(f"signature=({pos},{neg})")
print("odd=yes")
print("VERIFY_OK")
