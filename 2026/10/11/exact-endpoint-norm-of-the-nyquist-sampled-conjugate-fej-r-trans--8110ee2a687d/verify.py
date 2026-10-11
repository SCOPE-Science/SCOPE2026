import math

EULER_GAMMA = 0.577215664901532860606512090082402431

def direct_kernel(n, r):
    t = math.pi * r / n
    return 2.0 * sum((1.0 - k / n) * math.sin(k * t) for k in range(1, n))

def closed_kernel(n, r):
    r %= 2 * n
    if r == 0 or r == n:
        return 0.0
    return 1.0 / math.tan(math.pi * r / (2.0 * n))

def direct_norm(n):
    return sum(abs(direct_kernel(n, r)) for r in range(2 * n)) / (2.0 * n)

def closed_norm(n):
    return sum(1.0 / math.tan(math.pi * r / (2.0 * n)) for r in range(1, n)) / n

def odd_cot_sum(n):
    return sum(1.0 / math.tan((2 * j + 1) * math.pi / (4.0 * n)) for j in range(n)) / n

def asymptotic(n):
    return ((2.0 / math.pi) * math.log(n)
            + (2.0 / math.pi) * (EULER_GAMMA + math.log(2.0 / math.pi))
            - math.pi / (36.0 * n * n))

max_kernel_err = 0.0
max_norm_err = 0.0
kernel_cases = 0
for n in range(2, 241):
    for r in range(2 * n):
        err = abs(direct_kernel(n, r) - closed_kernel(n, r))
        max_kernel_err = max(max_kernel_err, err)
        kernel_cases += 1
    max_norm_err = max(max_norm_err, abs(direct_norm(n) - closed_norm(n)))

max_dyadic_err = 0.0
for n in range(2, 501):
    err = abs((2.0 * closed_norm(2 * n) - closed_norm(n)) - odd_cot_sum(n))
    max_dyadic_err = max(max_dyadic_err, err)

max_scaled_asymptotic_residual = 0.0
for n in (40, 80, 160, 320, 640):
    scaled = abs(closed_norm(n) - asymptotic(n)) * n**4
    max_scaled_asymptotic_residual = max(max_scaled_asymptotic_residual, scaled)

assert max_kernel_err < 2e-10
assert max_norm_err < 2e-12
assert max_dyadic_err < 5e-13
assert max_scaled_asymptotic_residual < 0.02

print(
    "VERIFY_OK "
    f"kernel_cases={kernel_cases} "
    f"norm_cases={239} "
    f"dyadic_cases={499} "
    f"asymptotic_cases=5 "
    f"max_kernel_err={max_kernel_err:.3e} "
    f"max_norm_err={max_norm_err:.3e} "
    f"max_dyadic_err={max_dyadic_err:.3e} "
    f"max_scaled_asymptotic_residual={max_scaled_asymptotic_residual:.3e}"
)
