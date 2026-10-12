import sympy as sp

# Matrices use columns for images of e1,e2.
a,b,c,d = sp.symbols("a b c d")
vars_ = [a,b,c,d]
M = sp.Matrix([[a,c],[b,d]])

algebras = {
    "A0": {},
    "Ae": {(0,0):(1,0)},
    "An": {(0,0):(0,1)},
    "AL": {(0,0):(1,0),(0,1):(0,1)},
    "AR": {(0,0):(1,0),(1,0):(0,1)},
    "AD": {(0,0):(1,0),(0,1):(0,1),(1,0):(0,1)},
    "AS": {(0,0):(1,0),(1,1):(0,1)},
}

expected = {
    "A0": [
        (1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)
    ],
    "Ae": [(1,0,0,0),(0,1,0,0),(0,0,0,1)],
    "An": [(1,0,0,0),(0,1,0,0),(0,0,0,1)],
    "AL": [(1,0,0,1)],
    "AR": [(1,0,0,1)],
    "AD": [(1,0,0,1),(0,1,0,0)],
    "AS": [(1,0,0,0),(0,0,0,1)],
}

def product(name, i, j):
    return sp.Matrix(algebras[name].get((i,j),(0,0)))

def qc_matrix(name):
    equations = []
    for i in range(2):
        for j in range(2):
            left = sp.zeros(2,1)
            right = sp.zeros(2,1)
            for k in range(2):
                left += M[k,i] * product(name,k,j)
                right += M[k,j] * product(name,i,k)
            equations.extend(list(left-right))
    A, _ = sp.linear_eq_to_matrix(equations, vars_)
    return A

dims = {}
for name in algebras:
    A = qc_matrix(name)
    null = A.nullspace()
    dims[name] = len(null)
    E = sp.Matrix.hstack(*[sp.Matrix(v) for v in expected[name]])
    assert E.rank() == len(expected[name])
    assert all(A * E[:,j] == sp.zeros(A.rows,1) for j in range(E.cols))
    N = sp.Matrix.hstack(*null) if null else sp.zeros(4,0)
    assert N.rank() == E.rank()
    assert sp.Matrix.hstack(N,E).rank() == N.rank()

assert [dims[n] for n in ["A0","Ae","An","AL","AR","AD","AS"]] == [4,3,3,1,1,2,2]
print(dims)
print("VERIFY_OK")
