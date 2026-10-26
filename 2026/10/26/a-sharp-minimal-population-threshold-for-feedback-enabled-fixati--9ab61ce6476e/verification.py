from fractions import Fraction as F

def solve(A, b):
    A = [[F(v) for v in row] for row in A]
    b = [F(v) for v in b]
    n = len(b)
    for k in range(n):
        pivot = next((r for r in range(k, n) if A[r][k] != 0), None)
        if pivot is None:
            raise ArithmeticError("singular backward system")
        A[k], A[pivot] = A[pivot], A[k]
        b[k], b[pivot] = b[pivot], b[k]
        q = A[k][k]
        A[k] = [v / q for v in A[k]]
        b[k] /= q
        for r in range(n):
            if r == k:
                continue
            q = A[r][k]
            if q:
                A[r] = [A[r][j] - q * A[k][j] for j in range(n)]
                b[r] -= q * b[k]
    return b

# N=3 feedback model: states (1,+), (2,+), (1,-), (2,-).
x, y, e, M = F(2), F(3), F(1, 10), F(10)
A = [
    [1+x+e, -1, -e, 0],
    [-y, 1+y+M, 0, -M],
    [-M, 0, 1+y+M, -1],
    [0, -e, -x, 1+x+e],
]
phi = solve(A, [0, 1, 0, 1])
u, v, w, z = phi
assert u == F(181, 1373), u
assert v == F(54954, 138673), v
assert w == F(17171, 138673), w
assert z == F(57584, 138673), z
static_plus = F(1, 1+x+x*y)
static_minus = F(1, 1+y+x*y)
Fthreshold = x*M*M + (x*y-e)*M - e*(e+1)*(y+1)
assert static_plus == F(1, 9)
assert static_minus == F(1, 10)
assert u > static_plus > static_minus
assert Fthreshold == F(6464, 25) and Fthreshold > 0

# N=2 comparison: one transient count, switching rates alpha and beta.
alpha, beta = F(1, 10), F(10)
D2 = alpha*y + alpha + beta*x + beta + x*y + x + y + 1
phi_plus_2 = (alpha + beta + y + 1) / D2
phi_minus_2 = (alpha + beta + x + 1) / D2
assert phi_plus_2 == F(141, 424)
assert phi_minus_2 == F(131, 424)
assert phi_plus_2 < F(1, 3) and phi_minus_2 < F(1, 3)
print("EXACT_CHECK_OK N=3 phi=181/1373 static=(1/9,1/10) F=6464/25 N=2=(141/424,131/424) < 1/3")
