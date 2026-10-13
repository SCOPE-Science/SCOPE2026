def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def is_zero(A):
    return all(x == 0 for row in A for x in row)

weight_checks = coordinate_checks = matrix_checks = 0

for n in range(2, 31):
    Q = 3
    c = [Q**(i+1) for i in range(n)]
    L = 3 * (Q**(n+1))

    Aoff = {}
    Boff = {}
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            wa = c[i] - c[j]
            wb = L + wa
            assert wa not in Aoff
            assert wb not in Boff
            Aoff[wa] = (i,j)
            Boff[wb] = (i,j)
            weight_checks += 2

    assert set(Aoff).isdisjoint(Boff)
    assert 0 not in Aoff and L not in Aoff
    assert 0 not in Boff and L not in Boff

    predicted = 2*n*(n-1)
    assert len(Aoff) + len(Boff) == predicted
    coordinate_checks += predicted

    if n <= 12:
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                E = [[0]*n for _ in range(n)]
                E[i][j] = 1
                assert is_zero(matmul(E,E))
                Z = [[0]*n for _ in range(n)]
                assert matmul(E,Z) == matmul(Z,E)
                matrix_checks += 2

print("VERIFY_OK", weight_checks, coordinate_checks, matrix_checks)
