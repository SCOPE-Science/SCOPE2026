#!/usr/bin/env python3
import cmath
import math


def multiplier(N, k):
    if k == 0:
        return 0j
    if N % 2 == 0 and k == N // 2:
        return 0j
    if k < (N + 1) // 2:
        return -1j
    return 1j


def direct_kernel(N, r):
    z = 0j
    for k in range(N):
        z += multiplier(N, k) * cmath.exp(2j * math.pi * k * r / N)
    return z.real


def closed_kernel(N, r):
    if r % N == 0:
        return 0.0
    if N % 2:
        x = math.pi * r / (2 * N)
        return 1.0 / math.tan(x) if r % 2 else -math.tan(x)
    if r % 2 == 0:
        return 0.0
    return 2.0 / math.tan(math.pi * r / N)


def exact_formula(N):
    if N % 2:
        return (2.0 / N) * sum(1.0 / math.tan((2*j+1)*math.pi/(2*N)) for j in range((N-1)//2))
    top = (N - 2) // 4
    return (4.0 / N) * sum(1.0 / math.tan((2*j+1)*math.pi/N) for j in range(top + 1))


def direct_norm(N):
    return sum(abs(direct_kernel(N, r)) for r in range(N)) / N


def main():
    max_kernel_err = 0.0
    max_formula_err = 0.0
    kernel_cases = 0
    formula_cases = 0
    for N in range(3, 181):
        for r in range(N):
            e = abs(direct_kernel(N, r) - closed_kernel(N, r))
            max_kernel_err = max(max_kernel_err, e)
            kernel_cases += 1
        e = abs(direct_norm(N) - exact_formula(N))
        max_formula_err = max(max_formula_err, e)
        formula_cases += 1
    assert max_kernel_err < 2e-10, max_kernel_err
    assert max_formula_err < 2e-10, max_formula_err

    dyadic_cases = 0
    max_dyadic_err = 0.0
    for N in range(3, 301, 2):
        e = abs(exact_formula(2*N) - exact_formula(N))
        max_dyadic_err = max(max_dyadic_err, e)
        dyadic_cases += 1
    assert max_dyadic_err < 2e-13, max_dyadic_err

    gamma = 0.5772156649015328606
    c_odd = 2.0 / math.pi * (gamma + math.log(4.0 / math.pi))
    c_even = 2.0 / math.pi * (gamma + math.log(2.0 / math.pi))
    target_odd = -7.0 * math.pi / 36.0
    target_0 = 2.0 * math.pi / 9.0
    target_2 = -7.0 * math.pi / 9.0
    asymptotic_cases = 0
    for N in (401, 801, 1601):
        coeff = N*N*(exact_formula(N) - 2.0/math.pi*math.log(N) - c_odd)
        assert abs(coeff - target_odd) < 2e-5, (N, coeff, target_odd)
        asymptotic_cases += 1
    for N in (400, 800, 1600):
        coeff = N*N*(exact_formula(N) - 2.0/math.pi*math.log(N) - c_even)
        assert abs(coeff - target_0) < 2e-5, (N, coeff, target_0)
        asymptotic_cases += 1
    for N in (402, 802, 1602):
        coeff = N*N*(exact_formula(N) - 2.0/math.pi*math.log(N) - c_even)
        assert abs(coeff - target_2) < 2e-5, (N, coeff, target_2)
        asymptotic_cases += 1

    print('VERIFY_OK '
          f'kernel_cases={kernel_cases} formula_cases={formula_cases} '
          f'dyadic_cases={dyadic_cases} asymptotic_cases={asymptotic_cases} '
          f'max_kernel_err={max_kernel_err:.3e} '
          f'max_formula_err={max_formula_err:.3e} '
          f'max_dyadic_err={max_dyadic_err:.3e}')


if __name__ == '__main__':
    main()
