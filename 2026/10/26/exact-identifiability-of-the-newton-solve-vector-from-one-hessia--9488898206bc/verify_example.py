from fractions import Fraction as F

v = (F(1), F(0), F(0))
g = (F(1), F(0), F(0))
A2 = ((F(2), F(1), F(0)), (F(1), F(2), F(0)), (F(0), F(0), F(1)))
A3 = ((F(2), F(1), F(0)), (F(1), F(3), F(0)), (F(0), F(0), F(1)))

def matvec(A, x):
    return tuple(sum(A[i][j] * x[j] for j in range(3)) for i in range(3))

def solve_newton(b):
    # Exact solution for [[2,1],[1,b]] p = (1,0), with third coordinate zero.
    det = F(2) * b - F(1)
    return (b / det, -F(1) / det, F(0))

# Sylvester's criterion: positive leading principal minors imply SPD here.
assert F(2) > 0 and F(3) > 0 and F(1) > 0
assert F(2) * F(2) - F(1) > 0
assert F(2) * F(3) - F(1) > 0
assert matvec(A2, v) == (F(2), F(1), F(0))
assert matvec(A3, v) == (F(2), F(1), F(0))
p2 = solve_newton(F(2))
p3 = solve_newton(F(3))
assert matvec(A2, p2) == g
assert matvec(A3, p3) == g
assert p2 == (F(2, 3), -F(1, 3), F(0))
assert p3 == (F(3, 5), -F(1, 5), F(0))
assert p2 != p3
print('VERIFY_OK: same Hessian-vector product, distinct exact Newton solve vectors')
