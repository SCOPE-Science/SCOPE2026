from fractions import Fraction as F


def check(alpha, delta):
    p0 = alpha
    p1 = F(1, 2) - 2 * alpha + delta
    p2 = F(1, 2) + alpha - 2 * delta
    p3 = delta
    assert min(p0, p1, p2, p3) >= 0
    assert p0 + p1 + p2 + p3 == 1
    assert F(1, 4)*p0 + F(3, 4)*p1 + F(5, 4)*p2 + F(7, 4)*p3 == 1
    q = [
        [0, F(1, 4)-alpha, 0, alpha],
        [F(1, 4)-delta, 0, delta, 0],
        [0, alpha, 0, F(1, 4)-alpha],
        [delta, 0, F(1, 4)-delta, 0],
    ]
    for row in q:
        assert sum(row) == F(1, 4)
        assert min(row) >= 0
    for j in range(4):
        assert sum(q[i][j] for i in range(4)) == F(1, 4)
    diag = {d: sum(q[i][j] for i in range(4) for j in range(4) if i-j == d)
            for d in (-3, -1, 1, 3)}
    assert diag[-3] == p0
    assert diag[-1] == p1
    assert diag[1] == p2
    assert diag[3] == p3

cases = 0
for ia in range(17):
    for idelta in range(17):
        check(F(ia, 64), F(idelta, 64))
        cases += 1
print(f"VERIFY_OK cases={cases}")
