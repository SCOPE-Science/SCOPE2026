import cmath
import math


def S_formula(L):
    x = math.pi / (2 * L)
    return 1 / math.sin(x) if L % 2 else 1 / math.tan(x)


def gamma_formula(N, a):
    best = -1.0
    for L in range(2, N + 1):
        if N % L:
            continue
        h = math.gcd(a, L)
        c = abs(math.cos(math.pi * h / L))
        val = (2 * L / (N * S_formula(L))) * c
        best = max(best, val)
    return best


def main():
    max_err = 0.0
    sum_cases = 0
    target_cases = 0
    diff_cases = 0
    for N in range(2, 81):
        direct_s = sum(abs(math.cos(math.pi * j / N)) for j in range(N))
        max_err = max(max_err, abs(direct_s - S_formula(N)))
        sum_cases += 1
        den = {}
        for d in range(1, N):
            den[d] = sum(
                abs(1 + cmath.exp(2j * math.pi * d * x / N))
                for x in range(N)
            )
        for a in range(N):
            brute = -1.0
            for d in range(1, N):
                num = 2 * abs(1 + cmath.exp(2j * math.pi * d * a / N))
                brute = max(brute, num / den[d])
                diff_cases += 1
            formula = gamma_formula(N, a)
            err = abs(brute - formula)
            max_err = max(max_err, err)
            if err > 2e-12:
                raise AssertionError((N, a, brute, formula, err))
            target_cases += 1
    prime_cases = 0
    for p in range(3, 500):
        if all(p % d for d in range(2, int(p ** 0.5) + 1)):
            formula = gamma_formula(p, 1)
            closed = 2 * math.sin(math.pi / (2 * p)) * math.cos(math.pi / p)
            if abs(formula - closed) > 2e-12:
                raise AssertionError((p, formula, closed))
            prime_cases += 1
    print(f"sum_cases={sum_cases}")
    print(f"target_cases={target_cases}")
    print(f"frequency_difference_tests={diff_cases}")
    print(f"prime_corollary_cases={prime_cases}")
    print(f"max_error={max_err:.3e}")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
