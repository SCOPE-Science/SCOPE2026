#!/usr/bin/env python3
import cmath
import math


def r_multiplier(N, k):
    return 0j if k % N == 0 else 1j * cmath.exp(1j * math.pi * k / N)


def r_kernel_closed(N, r):
    return -1.0 / math.tan(math.pi * (r + 0.5) / N)


def r_kernel_fourier(N, r):
    return sum(r_multiplier(N, k) * cmath.exp(2j * math.pi * k * r / N) for k in range(N))


def h_kernel_closed(N, s):
    if s % 2 == 0:
        return 0.0
    return 2.0 / math.tan(math.pi * s / (2 * N))


def h_kernel_fourier(N, s):
    M = 2 * N
    z = 0j
    for k in range(1, N):
        z += (-1j) * cmath.exp(2j * math.pi * k * s / M)
    for k in range(N + 1, M):
        z += (1j) * cmath.exp(2j * math.pi * k * s / M)
    return z


def c_norm(N):
    return sum(abs(r_kernel_closed(N, r)) for r in range(N)) / N


def c_half(N):
    return (2.0 / N) * sum(
        1.0 / math.tan((2 * r + 1) * math.pi / (2 * N))
        for r in range(N // 2)
    )


def main():
    max_kernel = 0.0
    max_hkernel = 0.0
    max_square = 0.0
    max_block = 0.0
    max_norm = 0.0
    kernel_cases = 0
    block_cases = 0
    square_cases = 0
    norm_cases = 0

    for N in range(3, 121):
        for r in range(N):
            err = abs(r_kernel_fourier(N, r) - r_kernel_closed(N, r))
            max_kernel = max(max_kernel, err)
            kernel_cases += 1

        for k in range(N):
            lhs = r_multiplier(N, k) ** 2
            rhs = 0j if k == 0 else -cmath.exp(2j * math.pi * k / N)
            max_square = max(max_square, abs(lhs - rhs))
            square_cases += 1

        for s in range(2 * N):
            max_hkernel = max(max_hkernel, abs(h_kernel_fourier(N, s) - h_kernel_closed(N, s)))

        # Kernel-level parity blocks. Even input to odd output gives -R.
        for d in range(N):
            odd_from_even = 0.5 * h_kernel_closed(N, 2 * d + 1)
            even_from_odd = 0.5 * h_kernel_closed(N, 2 * d - 1)
            max_block = max(max_block, abs(odd_from_even + r_kernel_closed(N, d)))
            max_block = max(max_block, abs(even_from_odd + r_kernel_closed(N, (d - 1) % N)))
            block_cases += 2

        hnorm = sum(abs(h_kernel_closed(N, s)) for s in range(2 * N)) / (2 * N)
        max_norm = max(max_norm, abs(c_norm(N) - c_half(N)), abs(c_norm(N) - hnorm))
        norm_cases += 1

    const = (2.0 / math.pi) * (math.euler_gamma + math.log(4.0 / math.pi)) if hasattr(math, 'euler_gamma') else None
    if const is None:
        # 50 correct decimal digits; only a regression constant.
        gamma = 0.57721566490153286060651209008240243104215933593992
        const = (2.0 / math.pi) * (gamma + math.log(4.0 / math.pi))

    asymptotic_checks = []
    for N in (800, 1200, 801, 1201):
        base = (2.0 / math.pi) * math.log(N) + const
        scaled = N * N * (c_norm(N) - base)
        target = math.pi / 18.0 if N % 2 == 0 else -7.0 * math.pi / 36.0
        asymptotic_checks.append((N, scaled, target, abs(scaled - target)))

    assert max_kernel < 2e-10, max_kernel
    assert max_hkernel < 3e-10, max_hkernel
    assert max_square < 2e-14, max_square
    assert max_block < 5e-12, max_block
    assert max_norm < 2e-13, max_norm
    assert max(x[3] for x in asymptotic_checks) < 5e-6, asymptotic_checks

    print(
        'VERIFY_OK '
        f'kernel_cases={kernel_cases} square_cases={square_cases} '
        f'block_cases={block_cases} norm_cases={norm_cases} '
        f'max_kernel_err={max_kernel:.3e} max_hkernel_err={max_hkernel:.3e} '
        f'max_square_err={max_square:.3e} max_block_err={max_block:.3e} '
        f'max_norm_err={max_norm:.3e}'
    )
    print('ASYMPTOTIC ' + ' '.join(f'N={N}:scaled={s:.12f}:target={t:.12f}' for N, s, t, _ in asymptotic_checks))


if __name__ == '__main__':
    main()
