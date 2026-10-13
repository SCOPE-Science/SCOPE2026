"""Exact rational replay of the Markov-Lanczos phase-boundary witness.

All arithmetic is from Python's standard library. The general proof is analytical.
"""
from fractions import Fraction as F


def transpose(A):
    return [list(row) for row in zip(*A)]


def mm(A, B):
    return [
        [sum((A[i][k] * B[k][j] for k in range(len(B))), F(0))
         for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def det2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def generator(R):
    return [[-F(1), F(1), F(0), F(0)],
            [F(1), -F(1), F(0), F(0)],
            [F(0), F(0), -R, R],
            [F(0), F(0), R, -R]]


def compression(R, epsilon):
    G = generator(R)
    z = [[F(1)], [F(0)], [epsilon], [F(0)]]
    Gz = mm(G, z)
    Z = [[z[i][0], Gz[i][0]] for i in range(4)]
    M = mm(transpose(Z), Z)
    H = mm(mm(transpose(Z), G), Z)
    return G, z, M, H


def poly(R, u):
    return R**3*u*u + 2*R*(R**2 - 2*R + 2)*u + 2-R


for R, e in [(F(4), F(1,8)), (F(3), F(1,10)),
             (F(5,2), F(2,5)), (F(2), F(1,4)),
             (F(9,7), F(1,3)), (F(7), F(1,100))]:
    G, z, M, H = compression(R, e)
    u = e*e
    K = [[H[i][j] + R*M[i][j] for j in range(2)]
         for i in range(2)]
    assert K[0][0] == R-1
    assert det2(K) == -R*poly(R, u)
    assert det2(M) > 0
    assert all(sum(row) == 0 for row in G)
    assert G == transpose(G)

R = F(4)
e = F(1,8)
G, z, M, H = compression(R, e)
assert M == [[F(65,64), F(-17,16)],
             [F(-17,16), F(5,2)]]
assert H == [[F(-17,16), F(5,2)],
             [F(5,2), F(-8)]]
assert det2(M) == F(361,256)
assert det2(H) == F(576,256)
assert M[0][0]*H[1][1] + H[0][0]*M[1][1] - 2*M[0][1]*H[0][1] == F(-1400,256)
assert poly(R,e*e) == -F(47,64)
assert det2([[H[i][j] + 4*M[i][j] for j in range(2)] for i in range(2)]) == F(47,16)

# The exact Ritz eigenvalues are (-700 +/- 68*sqrt(61))/361.
# Strict rational root bounds certify negativity of p_1(-4) without
# evaluating an exponential numerically.
assert F(39,5)**2 < 61 < 8**2
assert -F(700+68*8,361) > -F(7,2)  # lambda_minus > -7/2
assert -700 + 68*8 < 0             # lambda_plus < 0
assert F(136*39,5*361) > F(29,10)  # Ritz gap > 29/10
assert 1 + F(29,10) + F(29,10)**2/F(2) > 8
# Therefore exp(gap) > 8 > (4+lambda_plus)/(4+lambda_minus),
# whence p_1(-4)<0 by the explicit two-node interpolation formula.

# For R=4, the positive threshold root solves 64 u^2+80u-2=0
# and equals (3*sqrt(3)-5)/8.
assert 64*F(1,64)**2 + 80*F(1,64) - 2 == -F(47,64)
assert F(3)**2 * F(3) > (F(5)+F(1,8))**2  # 3*sqrt(3)>5+1/8

print('VERIFY_OK')
print('witness_R', R, 'witness_epsilon', e, 'det_H_plus_RM', F(47,16))
