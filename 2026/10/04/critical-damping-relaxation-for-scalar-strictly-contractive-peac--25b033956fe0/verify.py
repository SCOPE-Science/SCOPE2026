from fractions import Fraction
import math


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def direct_matrix(a, b, beta, alpha):
    # Affine-free scalar recurrence on state (y, lambda).
    # Represent x = cx_y*y + cx_l*lambda, then propagate coefficients.
    cx_y = beta / (a + beta)
    cx_l = Fraction(1, 1) / (a + beta)

    lh_y = -alpha * beta * (cx_y - 1)
    lh_l = 1 - alpha * beta * cx_l

    yn_y = (beta * cx_y - lh_y) / (b + beta)
    yn_l = (beta * cx_l - lh_l) / (b + beta)

    ln_y = lh_y - alpha * beta * (cx_y - yn_y)
    ln_l = lh_l - alpha * beta * (cx_l - yn_l)
    return [[yn_y, yn_l], [ln_y, ln_l]]


def trace_det(M):
    tr = M[0][0] + M[1][1]
    det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    return tr, det


def closed_trace_det(a, b, beta, alpha):
    Q = (a + beta) * (b + beta)
    tr = (beta * beta * alpha * alpha
          - 2 * beta * (a + b + beta) * alpha
          + a * b + a * beta + b * beta + 2 * beta * beta) / Q
    det = beta * beta * (1 - alpha) * (1 - alpha) / Q
    return tr, det


def check_rational_identities():
    cases = [
        (Fraction(1), Fraction(4), Fraction(2), Fraction(3, 4)),
        (Fraction(2), Fraction(9), Fraction(3), Fraction(4, 5)),
        (Fraction(7), Fraction(2), Fraction(5), Fraction(2, 3)),
        (Fraction(3), Fraction(11), Fraction(7), Fraction(9, 10)),
    ]
    for a, b, beta, alpha in cases:
        M = direct_matrix(a, b, beta, alpha)
        got = trace_det(M)
        want = closed_trace_det(a, b, beta, alpha)
        assert got == want, (a, b, beta, alpha, got, want)


def critical_data(a, b, beta):
    Q = (a + beta) * (b + beta)
    u = beta / math.sqrt(Q)
    w = beta * (a + b + beta) / Q
    rad = (w + u) ** 2 - u * u * (1 + u) ** 2
    assert rad > 0
    astar = (w + u - math.sqrt(rad)) / (u * u)
    rho = u * (1 - astar)
    return u, w, astar, rho


def spectral_radius_from_trace_det(T, D):
    disc = T * T - 4 * D
    if abs(disc) < 1e-14:
        disc = 0.0
    if disc >= 0:
        s = math.sqrt(disc)
        return max(abs((T + s) / 2), abs((T - s) / 2))
    return math.sqrt(D)


def check_examples():
    examples = [(1.0, 4.0, 2.0), (2.0, 9.0, 3.0), (7.0, 2.0, 5.0)]
    for a, b, beta in examples:
        assert min(a, b) < beta < max(a, b)
        Q = (a + beta) * (b + beta)
        u, w, astar, rho = critical_data(a, b, beta)
        assert 0 < astar < 1
        T = u*u*astar*astar - 2*w*astar + (1 + u*u)
        D = u*u*(1-astar)*(1-astar)
        assert abs(T + 2*rho) < 2e-12
        assert abs(T*T - 4*D) < 2e-12
        assert abs(spectral_radius_from_trace_det(T, D) - rho) < 2e-12
        # Check representative points on both sides are strictly slower.
        for alpha in [astar/2, (astar+1)/2, 1.0]:
            T2 = u*u*alpha*alpha - 2*w*alpha + (1 + u*u)
            D2 = u*u*(1-alpha)*(1-alpha)
            assert spectral_radius_from_trace_det(T2, D2) > rho + 1e-10

    u, w, astar, rho = critical_data(1.0, 4.0, 2.0)
    assert abs(astar - 0.9462158829301036) < 2e-15
    assert abs(rho - 0.025354075933503258) < 2e-15
    endpoint = abs((2.0-1.0)*(2.0-4.0)/((1.0+2.0)*(4.0+2.0)))
    assert abs(endpoint - 1/9) < 1e-15
    assert endpoint / rho > 4.38


if __name__ == '__main__':
    check_rational_identities()
    check_examples()
    print('VERIFY_OK')
