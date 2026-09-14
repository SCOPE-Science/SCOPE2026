"""Discover bilinear (y,z) forms vanishing on all H_K (chart s,t), lane-1875."""
import sympy as sp

s, t = sp.symbols('s t')
m = sp.Matrix([1, t, -s])  # Y direction (a,b,c)
Z1 = sp.Matrix([1, t, 0, -s, 0, 2*s, s*t, -s**2])
Z2 = sp.Matrix([0, 0, 1, t, -s, t, t**2, -s*t])

C = sp.symbols('c0:24')  # c[j*8+l]
def P(Z):
    expr = 0
    for j in range(3):
        for l in range(8):
            expr += C[j*8+l]*m[j]*Z[l]
    return sp.expand(expr)

eqs = []
for Z in (Z1, Z2):
    p = sp.Poly(P(Z), s, t)
    eqs.extend(p.as_dict()[mon] for mon in p.monoms())
A, _ = sp.linear_eq_to_matrix(eqs, list(C))
print("equations:", A.shape, "rank:", A.rank())
ns = A.nullspace()
print("nullspace dim:", len(ns))
names_y = ['a', 'b', 'c']
for i, v in enumerate(ns):
    terms = []
    for j in range(3):
        for l in range(8):
            if v[j*8+l] != 0:
                terms.append(f"{v[j*8+l]}*{names_y[j]}*z{l+1}")
    print(f"E{i+1} =", " + ".join(terms))
