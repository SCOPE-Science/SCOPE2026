#!/usr/bin/env python3
"""Independent exact checks for the circular-prism two-independence theorem.

Uses only the Python standard library; no external papers or data are needed.
"""
from fractions import Fraction

STATES = tuple((a, b) for a in range(4) for b in range(4))
N = 16


def transfer_matrix():
    out = [[0] * N for _ in range(N)]
    for i, (a, b) in enumerate(STATES):
        for c in range(4):
            valid = all(
                not (b & (1 << j)) or
                ((a >> j) & 1) + ((c >> j) & 1) + ((b >> (1-j)) & 1) <= 1
                for j in range(2)
            )
            if valid:
                out[i][STATES.index((b, c))] = (-1) ** b.bit_count()
    return out


def matmul(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def characteristic(a):
    # Faddeev-LeVerrier over exact integers.
    n = len(a)
    b = identity(n)
    coefficients = [1]
    for k in range(1, n+1):
        m = matmul(a, b)
        tr = sum(m[i][i] for i in range(n))
        assert tr % k == 0
        c = -(tr // k)
        coefficients.append(c)
        b = [[m[i][j] + (c if i == j else 0)
              for j in range(n)] for i in range(n)]
    assert all(v == 0 for row in b for v in row)
    return coefficients


def independent_z(n):
    # Exhaustive vertex-mask test, independent of rung-state transfer method.
    adj = [0] * (2*n)
    for layer in range(2):
        for i in range(n):
            v = layer*n+i
            for w in (layer*n+(i-1)%n,
                      layer*n+(i+1)%n,
                      (1-layer)*n+i):
                adj[v] |= 1 << w
    ans = 0
    num_faces = 0
    for mask in range(1 << (2*n)):
        rest = mask
        valid = True
        while rest:
            bit = rest & -rest
            j = bit.bit_length()-1
            rest ^= bit
            if (adj[j] & mask).bit_count() >= 2:
                valid = False
                break
        if valid:
            num_faces += 1
            ans += -1 if mask.bit_count() & 1 else 1
    return ans, num_faces


def q(x):
    return x**4 - x**2 - 2*x + 1


def run():
    t = transfer_matrix()
    # (x^2-x+1)(x^4-x^2-2x+1) times x^10.
    expected = [1, -1, 0, -1, 2, -3, 1] + [0]*10
    coeff = characteristic(t)
    assert coeff == expected, (coeff, expected)
    print('CHARPOLY=x^10*(x^2-x+1)*(x^4-x^2-2*x+1)')
    powers = identity(N)
    traces = {}
    for n in range(1, 21):
        powers = matmul(powers, t)
        traces[n] = sum(powers[i][i] for i in range(N))
    expected_first = [4,-3,11,10,1,29,4,21,67,6,105]
    assert [traces[n] for n in range(3,14)] == expected_first
    for n in range(1,15):
        assert (traces[n+6] - traces[n+5] - traces[n+3]
                + 2*traces[n+2] - 3*traces[n+1] + traces[n]) == 0
    print('Z_3_TO_13=' + ','.join(str(x) for x in expected_first))
    for n in range(3,9):
        sign_sum, face_count = independent_z(n)
        assert sign_sum == traces[n], (n, sign_sum, traces[n])
        print(f'BRUTE_FORCE_n={n} faces_including_empty={face_count} signed_sum={sign_sum}')
    # Monotonicity of q follows from q'(x)=2(x-1)(2x^2+2x+1).
    assert q(Fraction(0)) > 0 and q(Fraction(1)) < 0 and q(Fraction(2)) > 0
    assert q(Fraction(17,40)) > 0 and q(Fraction(69,50)) < 0
    assert Fraction(17,40)*Fraction(69,50) > Fraction(1, 1)/Fraction(131,100)**2
    # Dividing growth inequality by (131/100)^n makes LHS increasing,
    # RHS decreasing in n. One rational check proves every n>=14.
    assert (Fraction(69,50)/Fraction(131,100))**14 > 2 + 2/Fraction(131,100)**14
    print('RATIONAL_ROOT_AND_GROWTH_BOUND=PASS')
    print('ALL_CHECKS_PASS')


if __name__ == '__main__':
    run()
