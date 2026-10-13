"""Exact integer checks for the nearest-integer transport obstruction."""
from math import comb


def rounded_weights(n):
    out = [0] * (2 * n + 1)
    for k in range(3 * n + 1):
        j = (4 * k + 3) // 6  # nearest integer to 2k/3
        assert 0 <= j <= 2 * n
        assert abs(2 * k - 3 * j) <= 1
        out[j] += comb(3 * n, k)
    return out


def verify_finite_integer_identities(limit=350):
    for n in range(2, limit + 1):
        a = rounded_weights(n)
        N = 3 * n
        assert sum(a) == 2 ** N
        assert a[1] == N + comb(N, 2)
        assert a[2] == comb(N, 3)
        assert a[3] == comb(N, 4) + comb(N, 5)
        m = n - 2
        rhs = n*n*(3*n-2)*(3*n-1)*(81*m**3+279*m*m+279*m+41)
        assert 80 * (a[1]*a[3] - a[2]*a[2]) == rhs
        assert a[1]*a[3] > a[2]*a[2]
    return limit - 1


def verify_sharp_coupling():
    # Monotone mass transport: X~Bin(6,1/2), Y~Bin(4,1/2).
    x = [comb(6, k) for k in range(7)]
    y = [4*comb(4, j) for j in range(5)]
    assert sum(x) == sum(y) == 64
    i = j = 0
    maximum_numerator = 0
    while i < len(x) and j < len(y):
        mass = min(x[i], y[j])
        if mass:
            maximum_numerator = max(maximum_numerator, abs(2*i - 3*j))
            assert abs(2*i - 3*j) <= 2
        x[i] -= mass
        y[j] -= mass
        if x[i] == 0:
            i += 1
        if j < len(y) and y[j] == 0:
            j += 1
    assert i == len(x) and j == len(y)
    assert maximum_numerator == 2
    return maximum_numerator


def verify_first_size():
    assert rounded_weights(1) == [1, 6, 1]
    # 1 + 6z + z^2 has negative real roots: discriminant=32.
    assert 6 * 6 - 4 * 1 * 1 == 32


if __name__ == '__main__':
    verify_first_size()
    cases = verify_finite_integer_identities()
    transport = verify_sharp_coupling()
    print(f'VERIFY_OK parameter_cases={cases} coupling_maximum_thirds={transport}')
