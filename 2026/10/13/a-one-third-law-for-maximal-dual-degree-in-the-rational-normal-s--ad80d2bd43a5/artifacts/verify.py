from math import comb, factorial

def dual_degree_closed(d, k):
    return (2 ** k) * comb(d - k, k)

def dual_degree_hilbert(d, k):
    # Partition {1^(d-2k), 2^k} has length d-k.
    length = d - k
    numerator = factorial(length) * (2 ** k)
    denominator = factorial(d - 2*k) * factorial(k)
    assert numerator % denominator == 0
    return numerator // denominator

def F(d, k):
    return 2*d*d - 9*d*k - 3*d + 9*k*k + 5*k

degree_checks = 0
ratio_checks = 0
mode_checks = 0

for d in range(2, 1001):
    ks = list(range(1, d // 2 + 1))
    vals = []
    for k in ks:
        a = dual_degree_closed(d, k)
        b = dual_degree_hilbert(d, k)
        assert a == b
        vals.append(a)
        degree_checks += 1

    m = (d + 1) // 3
    maxv = max(vals)
    modes = [k for k, v in zip(ks, vals) if v == maxv]
    assert modes == [m], (d, modes, m)
    mode_checks += 1

    for k in ks[:-1]:
        lhs = dual_degree_closed(d, k + 1) * (k + 1) * (d - k)
        rhs = dual_degree_closed(d, k) * 2 * (d - 2*k) * (d - 2*k - 1)
        assert lhs == rhs

        sign_ratio = (dual_degree_closed(d, k + 1) > dual_degree_closed(d, k)) - (
            dual_degree_closed(d, k + 1) < dual_degree_closed(d, k)
        )
        sign_F = (F(d, k) > 0) - (F(d, k) < 0)
        assert sign_ratio == sign_F
        ratio_checks += 1

    for i in range(len(vals) - 1):
        if ks[i] < m:
            assert vals[i] < vals[i + 1]
        else:
            assert vals[i] > vals[i + 1]

print("VERIFY_OK", degree_checks, ratio_checks, mode_checks)
