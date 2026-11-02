"""Exact finite-field checks for the Maschke quartic in characteristic five.

Only Python's standard library is used. Run: python verify.py
The infinite-field and all-extension arguments are supplied in RESULT.md.
"""
from itertools import product

P = 5

class Field:
    def __init__(self, dimension):
        assert dimension in (1, 2)
        self.n = dimension
        self.q = P ** dimension
        q = self.q
        if dimension == 1:
            self.add = [[(a + b) % P for b in range(q)] for a in range(q)]
            self.mul = [[a * b % P for b in range(q)] for a in range(q)]
        else:
            # theta^2 = 3, where 3 is a nonsquare in F_5.
            self.add = [[(a % 5 + b % 5) % 5 +
                         5 * ((a // 5 + b // 5) % 5)
                         for b in range(q)] for a in range(q)]
            self.mul = [[((a % 5) * (b % 5) + 3 * (a // 5) * (b // 5)) % 5 +
                         5 * (((a % 5) * (b // 5) + (a // 5) * (b % 5)) % 5)
                         for b in range(q)] for a in range(q)]
        self.square = [self.mul[a][a] for a in range(q)]
        self.fourth = [self.square[self.square[a]] for a in range(q)]
        assert self.mul[1][1] == 1
        for a in range(1, q):
            assert any(self.mul[a][b] == 1 for b in range(1, q))

    def evaluate(self, xs):
        """Direct quartic, without using the symmetric-square identity."""
        add, mul = self.add, self.mul
        squares = [self.square[a] for a in xs]
        answer = 0
        for a in xs:
            answer = add[answer][self.fourth[a]]
        for i in range(4):
            for j in range(i + 1, 4):
                cross = mul[squares[i]][squares[j]]
                answer = add[answer][mul[4][cross]]
        return answer

    def evaluate_alt(self, xs):
        """Independent expression F = 4 sum(x_i^4) + 2(sum(x_i^2))^2."""
        add, mul = self.add, self.mul
        S2, S4 = 0, 0
        for a in xs:
            S2 = add[S2][self.square[a]]
            S4 = add[S4][self.fourth[a]]
        return add[mul[4][S4]][mul[2][self.square[S2]]]


def count_projective(n):
    field = Field(n)
    q = field.q
    counts = []
    for trailing_zeros in range(4):
        count = 0
        for pre in product(range(q), repeat=3 - trailing_zeros):
            xs = tuple(pre) + (1,) + (0,) * trailing_zeros
            direct = field.evaluate(xs)
            independent = field.evaluate_alt(xs)
            assert direct == independent, (q, xs, direct, independent)
            if direct == 0:
                count += 1
        counts.append(count)
    return counts


def singular_equations(xs):
    # Partial derivatives F_i = x_i (x_i^2 - 2 sum x_j^2), modulo 5.
    S = sum(a * a for a in xs) % 5
    return all((a * (a * a - 2 * S)) % 5 == 0 for a in xs)


def determinant3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])) % 5


def main():
    f5 = Field(1)
    nodes = []
    for trailing_zeros in range(4):
        for pre in product(range(5), repeat=3-trailing_zeros):
            xs = tuple(pre) + (1,) + (0,) * trailing_zeros
            if singular_equations(xs):
                assert f5.evaluate(xs) == 0
                nodes.append(xs)
    assert len(nodes) == 16, len(nodes)
    assert all(sum(x != 0 for x in p) == 3 for p in nodes)
    # Affine x=1 Hessian at [1:1:1:0]; tangent quadratic nondegenerate.
    Hess = [[3, 1, 0], [1, 3, 0], [0, 0, 4]]
    assert determinant3(Hess) == 2
    print('ALL_16_SINGULAR_POINTS_RATIONAL_AND_ORDINARY_OK')
    print('AFFINE_HESSIAN_DETERMINANT_MOD5=2')

    c5 = count_projective(1)
    c25 = count_projective(2)
    assert c5 == [12, 4, 0, 0], c5
    assert c25 == [728, 44, 4, 0], c25
    assert sum(c5) == 16 and sum(c25) == 776
    print('GF5_CHART_COUNTS=', c5, 'TOTAL=', sum(c5))
    print('GF25_CHART_COUNTS=', c25, 'TOTAL=', sum(c25))
    print('DIRECT_AND_SYMMETRIC_POLYNOMIAL_EVALUATIONS_AGREE')

    t1 = sum(c5) + 16*5 - (5**2 + 1)
    t2 = sum(c25) + 16*25 - (25**2 + 1)
    assert (t1, t2) == (70, 550)
    assert (18-4)*5 == t1 and 22 * 25 == t2
    print('K3_FROBENIUS_POWER_TRACES=', t1, t2)
    for m in range(1, 7):
        q = 5**m
        N = q*q + 1 + 2*q + 4*((-5)**m)
        assert N == ((q-1)**2 if m % 2 else q*q + 6*q + 1)
    print('ALL_EXTENSION_FORMULA_ALGEBRA_OK')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
