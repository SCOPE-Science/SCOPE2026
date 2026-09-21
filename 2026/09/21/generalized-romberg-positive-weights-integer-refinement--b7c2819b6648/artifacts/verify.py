from fractions import Fraction
import platform


def richardson_coefficients(r, depth):
    q = r * r
    P = [1]
    for j in range(1, depth + 1):
        P.append(P[-1] * (q**j - 1))
    return [
        Fraction(((-1) ** (depth - k)) * q ** (k * (k + 1) // 2),
                 P[k] * P[depth - k])
        for k in range(depth + 1)
    ]


def quadrature_weights(r, depth, base=1):
    coeffs = richardson_coefficients(r, depth)
    N = base * r**depth
    weights = [Fraction(0) for _ in range(N + 1)]
    for k, ck in enumerate(coeffs):
        nk = base * r**k
        stride = r ** (depth - k)
        h = Fraction(1, nk)
        for j in range(0, N + 1, stride):
            endpoint = (j == 0 or j == N)
            weights[j] += ck * h * (Fraction(1, 2) if endpoint else 1)
    return coeffs, weights


def monomial_moment(weights, degree):
    N = len(weights) - 1
    return sum(w * Fraction(j, N) ** degree for j, w in enumerate(weights))


def main():
    cases = 0
    min_ratio = None
    for r in range(2, 6):
        for base in range(1, 4):
            for depth in range(1, 6):
                coeffs, weights = quadrature_weights(r, depth, base)
                assert sum(coeffs) == 1
                assert all(w > 0 for w in weights)
                assert sum(weights) == 1
                assert sum(abs(w) for w in weights) == 1
                for p in range(2 * depth + 2):
                    assert monomial_moment(weights, p) == Fraction(1, p + 1)
                a = [abs(c) * Fraction(1, r**k) for k, c in enumerate(coeffs)]
                for k in range(depth):
                    ratio = a[k + 1] / a[k]
                    assert ratio > 1
                    min_ratio = ratio if min_ratio is None else min(min_ratio, ratio)
                cases += 1
    # Representative exact non-dyadic case.
    coeffs, weights = quadrature_weights(3, 4, 1)
    print(f"python={platform.python_version()}")
    print(f"exact_cases={cases}")
    print(f"minimum_checked_tail_ratio={float(min_ratio):.12f}")
    print(f"r3_depth4_nodes={len(weights)}")
    print(f"r3_depth4_min_weight={float(min(weights)):.15e}")
    print(f"r3_depth4_max_weight={float(max(weights)):.15e}")
    print(f"r3_depth4_l1_weight_sum={float(sum(abs(w) for w in weights)):.1f}")
    print("moment_exactness=through_degree_2d_plus_1")
    print("status=PASS")


if __name__ == "__main__":
    main()
