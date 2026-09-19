from math import comb


def nu2(n):
    if n == 0:
        return 10**9
    n = abs(n)
    return (n & -n).bit_length() - 1


def t_coeff(m, n):
    """Return [x^n] T(x)^m using T(x)^m=(1-x)^m T(x^2)^m."""
    t = [0] * (n + 1)
    t[0] = 1
    for q in range(1, n + 1):
        total = 0
        for j in range(q & 1, min(m, q) + 1, 2):
            total += (-1 if j & 1 else 1) * comb(m, j) * t[(q - j) // 2]
        t[q] = total
    return t[n]


def check_A_v(A, v):
    assert A >= 2 and v > 0 and v % 2 == 1
    N = 1 << A
    n = N - 1
    m = 2 + N * v

    t = t_coeff(m, n)
    b = comb(n + m - 1, m - 1)

    assert (t - N * (v - 1)) % (4 * N) == 0
    assert nu2(b) == A + nu2(v + 1)

    if v % 4 == 1:
        assert nu2(t) >= A + 2
        assert nu2(b) == A + 1
    else:
        assert nu2(t) == A + 1
        assert nu2(b) >= A + 2

    return t, b


general_grid_cases = 0
for A in range(2, 9):
    for v in range(1, 32, 2):
        check_A_v(A, v)
        general_grid_cases += 1

odd_u_cases = 0
for u in range(3, 256, 2):
    a = nu2(u - 1)
    A = a + 1
    v = (u - 1) >> a
    t, b = check_A_v(A, v)
    assert nu2(t) != nu2(b)
    odd_u_cases += 1

print(f"general_grid_cases={general_grid_cases}")
print(f"odd_u_cases={odd_u_cases}")
print("all_checks=passed")
