from math import comb


def crown_neighbors(n, v):
    if v < n:
        return [n + j for j in range(n) if j != v]
    j = v - n
    return [i for i in range(n) if i != j]


def is_ktrds(n, k, mask):
    for v in range(2 * n):
        neigh = crown_neighbors(n, v)
        if sum((mask >> u) & 1 for u in neigh) < k:
            return False
        if ((mask >> v) & 1) == 0:
            if sum(1 - ((mask >> u) & 1) for u in neigh) < k:
                return False
    return True


def criterion(n, k, mask):
    I = {i for i in range(n) if (mask >> i) & 1}
    J = {i for i in range(n) if (mask >> (n + i)) & 1}
    if len(I) == n and len(J) == n:
        return k <= n - 1
    if len(I) == n or len(J) == n:
        return False
    if len(I) < k + 1 or len(J) < k + 1:
        return False
    X = set(range(n)) - I
    Y = set(range(n)) - J
    a, b = len(X), len(Y)
    if a < k or b < k:
        return False
    if a == k and not X.isdisjoint(Y):
        return False
    if b == k and not X.isdisjoint(Y):
        return False
    return True


def formula_coefficients(n, k):
    coeff = {2 * n: 1}
    if n >= 2 * k + 1:
        N = n - k - 1
        for a in range(k + 1, N + 1):
            for b in range(k + 1, N + 1):
                d = 2 * n - a - b
                coeff[d] = coeff.get(d, 0) + comb(n, a) * comb(n, b)
        for b in range(k + 1, N + 1):
            d = 2 * n - k - b
            coeff[d] = coeff.get(d, 0) + 2 * comb(n, k) * comb(n - k, b)
        d = 2 * n - 2 * k
        coeff[d] = coeff.get(d, 0) + comb(n, k) * comb(n - k, k)
    return coeff


def expected_gamma(n, k):
    return 2 * k + 2 if n >= 2 * k + 1 else 2 * n


def expected_minimum_count(n, k):
    if n <= 2 * k:
        return 1
    if n == 2 * k + 1:
        return comb(n, k) * comb(n - k, k)
    return comb(n, k + 1) ** 2


def main():
    subset_checks = 0
    criterion_checks = 0
    coefficient_checks = 0
    minimum_checks = 0
    for n in range(3, 9):
        for k in range(1, n):
            actual = {}
            for mask in range(1 << (2 * n)):
                subset_checks += 1
                direct = is_ktrds(n, k, mask)
                structural = criterion(n, k, mask)
                criterion_checks += 1
                assert direct == structural, (n, k, mask, direct, structural)
                if direct:
                    w = mask.bit_count()
                    actual[w] = actual.get(w, 0) + 1
            predicted = formula_coefficients(n, k)
            all_degrees = set(actual) | set(predicted)
            for d in all_degrees:
                coefficient_checks += 1
                assert actual.get(d, 0) == predicted.get(d, 0), (n, k, d, actual, predicted)
            gamma = min(actual)
            minimum_checks += 2
            assert gamma == expected_gamma(n, k), (n, k, gamma, expected_gamma(n, k))
            assert actual[gamma] == expected_minimum_count(n, k), (
                n, k, actual[gamma], expected_minimum_count(n, k)
            )
    print(
        f"VERIFY_OK n_range=3..8 subset_checks={subset_checks} "
        f"criterion_checks={criterion_checks} coefficient_checks={coefficient_checks} "
        f"minimum_checks={minimum_checks} max_order=16"
    )


if __name__ == '__main__':
    main()
