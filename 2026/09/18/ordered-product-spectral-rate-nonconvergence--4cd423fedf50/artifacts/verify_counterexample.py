import cmath
import math


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def rotation(theta):
    c, s = math.cos(theta), math.sin(theta)
    return [[c, -s], [s, c]]


def spectral_radius(A):
    tr = A[0][0] + A[1][1]
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    disc = cmath.sqrt(tr * tr - 4.0 * det)
    return max(abs((tr + disc) / 2.0), abs((tr - disc) / 2.0))


def transpose(A):
    return [[A[j][i] for j in range(2)] for i in range(2)]


def largest_singular_value(A):
    ATA = matmul(transpose(A), A)
    tr = ATA[0][0] + ATA[1][1]
    det = ATA[0][0] * ATA[1][1] - ATA[0][1] * ATA[1][0]
    lam = (tr + math.sqrt(max(0.0, tr * tr - 4.0 * det))) / 2.0
    return math.sqrt(lam)


def main():
    a, b = 2.0, 1.0
    q = math.pi / 2.0
    D = [[math.exp(a), 0.0], [0.0, math.exp(b)]]
    J = [matmul(matmul(rotation((n + 1) * q), D), rotation(-n * q)) for n in range(4)]

    max_rate_error = 0.0
    max_singular_error = 0.0
    rows = []
    for L in range(1, 13):
        expected_h = a if L % 2 == 0 else (a + b) / 2.0
        rates = []
        singular_rates = []
        for n in range(4):
            P = [[1.0, 0.0], [0.0, 1.0]]
            for j in range(L):
                P = matmul(J[(n + j) % 4], P)
            h = math.log(spectral_radius(P)) / L
            s = math.log(largest_singular_value(P)) / L
            rates.append(h)
            singular_rates.append(s)
            max_rate_error = max(max_rate_error, abs(h - expected_h))
            max_singular_error = max(max_singular_error, abs(s - a))
        rows.append((L, min(rates), max(rates), min(singular_rates), max(singular_rates)))

    assert max_rate_error < 1e-12
    assert max_singular_error < 1e-12
    print("L  min_h       max_h       min_sigma_rate  max_sigma_rate")
    for row in rows:
        print(f"{row[0]:2d} {row[1]:.10f} {row[2]:.10f} {row[3]:.10f}      {row[4]:.10f}")
    print(f"max spectral-rate identity error: {max_rate_error:.3e}")
    print(f"max singular-rate identity error: {max_singular_error:.3e}")


if __name__ == "__main__":
    main()
