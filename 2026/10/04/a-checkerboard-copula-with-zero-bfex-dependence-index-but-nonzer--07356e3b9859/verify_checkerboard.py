from fractions import Fraction

Q = [
    [-4, 2, 2],
    [3, 2, -5],
    [1, -4, 3],
]
t = Fraction(-4, 121)
P = [[Fraction(1, 9) + t*q for q in row] for row in Q]
expected = [
    [Fraction(265,1089), Fraction(49,1089), Fraction(49,1089)],
    [Fraction(13,1089), Fraction(49,1089), Fraction(301,1089)],
    [Fraction(85,1089), Fraction(265,1089), Fraction(13,1089)],
]
assert P == expected
assert all(sum(row) == Fraction(1,3) for row in P)
assert all(sum(P[i][j] for i in range(3)) == Fraction(1,3) for j in range(3))
assert all(x > 0 for row in P for x in row)
assert any(x != Fraction(1,9) for row in P for x in row)

def integrals(P):
    I1 = Fraction(0)
    I2 = Fraction(0)
    for i in range(3):
        for j in range(3):
            A = sum(P[a][b] for a in range(i) for b in range(j))
            B = sum(P[i][b] for b in range(j))
            C = sum(P[a][j] for a in range(i))
            D = P[i][j]
            e1 = A + B/Fraction(2) + C/Fraction(2) + D/Fraction(4)
            e2 = (A*A + B*B/Fraction(3) + C*C/Fraction(3) + D*D/Fraction(9)
                  + A*B + A*C + A*D/Fraction(2) + B*C/Fraction(2)
                  + B*D/Fraction(3) + C*D/Fraction(3))
            I1 += e1/Fraction(9)
            I2 += e2/Fraction(9)
    return I1, I2

I1, I2 = integrals(P)
assert I2 == Fraction(1,9)
assert Fraction(1,4)*I2 == Fraction(1,36)
rho = 12*I1 - 3
assert I1 == Fraction(1153,4356)
assert rho == Fraction(64,363)

# Along the checkerboard direction P(t)=1/9+tQ, the exact square integral is
# 1/9 + (4/81)t + (121/81)t^2. Verify by interpolation at three rational values.
def matrix(s):
    return [[Fraction(1,9)+s*q for q in row] for row in Q]
for s in [Fraction(0), Fraction(1,100), Fraction(-1,100), t]:
    _, sq = integrals(matrix(s))
    rhs = Fraction(1,9) + Fraction(4,81)*s + Fraction(121,81)*s*s
    assert sq == rhs

print('cell matrix:', P)
print('integral_C:', I1)
print('integral_C2:', I2)
print('BFEx:', I2/Fraction(4))
print('Spearman_rho:', rho)
