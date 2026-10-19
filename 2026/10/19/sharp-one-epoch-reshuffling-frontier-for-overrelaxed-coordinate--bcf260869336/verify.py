"""Exact rational replay for the two-coordinate shuffled-versus-iid energy law."""
from fractions import Fraction as Q
from itertools import product


def energy(y, c):
    return (y[0] * y[0] + 2 * c * y[0] * y[1] + y[1] * y[1]) / 2


def step(y, c, omega, i):
    y = list(y)
    other = 1 - i
    y[i] -= omega * (y[i] + c * y[other])
    return tuple(y)


def final_energy(y, c, omega, pair):
    for i in pair:
        y = step(y, c, omega, i)
    return energy(y, c)


def difference_direct(y, c, omega):
    shuffled = sum(final_energy(y, c, omega, p) for p in [(0, 1), (1, 0)]) / 2
    iid = sum(final_energy(y, c, omega, p) for p in product(range(2), repeat=2)) / 4
    return iid - shuffled


def difference_formula(y, c, omega):
    r1 = y[0] + c * y[1]
    r2 = c * y[0] + y[1]
    a = 2 - omega + omega * c * c
    return omega * omega * (2 - omega) / 8 * (a * (r1 * r1 + r2 * r2) - 4 * c * r1 * r2)


def invert_gradient(c, r):
    return ((r[0] - c * r[1]) / (1 - c * c), (r[1] - c * r[0]) / (1 - c * c))


def diagonal_renormalization(y, c, omega, pair):
    # H = diag(2,3) [[1,c],[c,1]] diag(2,3). Normalize coordinates back to y.
    x = [y[0] / 2, y[1] / 3]
    h00, h11, h01 = Q(4), Q(9), 6 * c
    for i in pair:
        grad = (h00 * x[0] + h01 * x[1], h01 * x[0] + h11 * x[1])
        x[i] -= omega * grad[i] / (h00 if i == 0 else h11)
    return energy((2 * x[0], 3 * x[1]), c)


def run():
    count = 0
    for c in [Q(-3,4), Q(-1,2), Q(-1,4), Q(0), Q(1,4), Q(1,2), Q(3,4)]:
        for omega in [Q(1,4), Q(1,2), Q(1), Q(4,3), Q(3,2), Q(7,4), Q(15,8)]:
            for r1, r2 in product([Q(-3,2), Q(-1), Q(0), Q(1), Q(5,3)], repeat=2):
                if r1 == r2 == 0:
                    continue
                y = invert_gradient(c, (r1, r2))
                d = difference_direct(y, c, omega)
                assert d == difference_formula(y, c, omega), (c, omega, (r1,r2))
                count += 1
                for pair in [(0, 0), (0,1), (1,0), (1,1)]:
                    assert final_energy(y, c, omega, pair) == diagonal_renormalization(y, c, omega, pair)
                    count += 1
    c, omega = Q(1,2), Q(3,2)
    y = invert_gradient(c, (Q(1), Q(1)))
    assert difference_direct(y, c, omega) == -Q(9,256)
    assert difference_direct(invert_gradient(c, (Q(1), Q(-1))), c, omega) == Q(135,256)
    assert difference_direct(invert_gradient(c, (Q(1), Q(1))), c, Q(4,3)) == 0
    assert difference_direct(invert_gradient(c, (Q(1), Q(1))), c, Q(1)) > 0
    for c in [Q(-3,4), Q(-1,2), Q(-1,4), Q(1,4), Q(1,2), Q(3,4)]:
        threshold = 2 / (1 + abs(c))
        assert 1 < threshold < 2
        assert difference_direct(invert_gradient(c, (Q(1), Q(1) if c > 0 else Q(-1))), c, threshold) == 0
        assert difference_direct(invert_gradient(c, (Q(1), Q(1) if c > 0 else Q(-1))), c, (threshold + 2) / 2) < 0
    print(f'VERIFY_OK: {count} exact rational comparisons, plus sharp threshold and witness checks')


if __name__ == '__main__':
    run()
