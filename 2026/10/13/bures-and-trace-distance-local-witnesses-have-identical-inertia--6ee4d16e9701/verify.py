from fractions import Fraction as F

def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]

def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def scale(c, A):
    return [[c * z for z in row] for row in A]

def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def tr(A):
    return [list(r) for r in zip(*A)]

def outer(x, y):
    return [[a*b for b in y] for a in x]

def dot(x, y):
    return sum(a*b for a, b in zip(x, y))

def verify_case(x, B):
    s = F(1) - dot(x, x)
    assert s > 0
    X = outer(x, x)
    R = add(eye(3), scale(F(1, 1) / s, X))
    left = mul(mul(R, B), R)
    scalar = dot(x, [sum(B[i][j] * x[j] for j in range(3)) for i in range(3)])
    right = add(B, scale(F(1, 1) / s, add(mul(B, X), mul(X, B))))
    right = add(right, scale(scalar / (s*s), X))
    assert left == right
    Rinv = add(eye(3), scale(F(-1), X))
    assert mul(R, Rinv) == eye(3)
    assert mul(Rinv, R) == eye(3)

def main():
    cases = [
        ([F(1,3), F(-1,4), F(1,5)], [[F(2),F(1),F(-1)],[F(1),F(-3),F(2)],[F(-1),F(2),F(5)]]),
        ([F(1,2), F(1,3), F(0)], [[F(-4),F(2),F(0)],[F(2),F(1),F(3)],[F(0),F(3),F(-2)]]),
        ([F(0), F(0), F(0)], [[F(1),F(2),F(3)],[F(2),F(4),F(5)],[F(3),F(5),F(6)]])
    ]
    for x, B in cases:
        assert B == tr(B)
        verify_case(x, B)
    print("VERIFY_OK")
    print("exact_rational_cases =", len(cases))

if __name__ == "__main__":
    main()
