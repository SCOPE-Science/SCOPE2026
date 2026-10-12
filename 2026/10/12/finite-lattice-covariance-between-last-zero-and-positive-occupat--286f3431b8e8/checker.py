from fractions import Fraction
from math import comb

def u(k):
    """Return P(S_{2k}=0) exactly."""
    return Fraction(comb(2*k, k), 4**k)

def check(max_n=9):
    exact_checks = 0
    for n in range(1, max_n + 1):
        N = 2*n
        total = 1 << N
        counts = [0] * (n + 1)
        sums_A = [0] * (n + 1)
        sum_L = 0
        sum_A = 0
        sum_LA = 0

        for mask in range(total):
            s = 0
            last_zero = 0
            A = 0
            for j in range(1, N + 1):
                s += 1 if ((mask >> (j - 1)) & 1) else -1
                if s == 0:
                    last_zero = j
                if s > 0:
                    A += 1
            k = last_zero // 2
            counts[k] += 1
            sums_A[k] += A
            sum_L += last_zero
            sum_A += A
            sum_LA += last_zero * A

        T = sum((u(r) for r in range(n + 1)), Fraction(0))
        assert T == (2*n + 1) * u(n)
        exact_checks += 1
        assert sum(Fraction(r) * u(r) for r in range(n + 1)) == Fraction(n, 3) * T
        exact_checks += 1

        for k in range(n + 1):
            assert Fraction(counts[k], total) == u(k) * u(n-k)
            exact_checks += 1
            expected_cond = Fraction(2*n + 1, 2) - Fraction(1, 2*u(k))
            assert Fraction(sums_A[k], counts[k]) == expected_cond
            exact_checks += 1

        EL = Fraction(sum_L, total)
        EA = Fraction(sum_A, total)
        ELA = Fraction(sum_LA, total)
        covariance = ELA - EL * EA

        assert EL == n
        exact_checks += 1
        assert EA == Fraction(2*n + 1, 2) - T/2
        exact_checks += 1
        assert covariance == -Fraction(n, 6) * T
        exact_checks += 1

    print("VERIFY_OK")
    print(f"max_n={max_n}")
    print(f"exact_checks={exact_checks}")
    print(f"largest_path_count={1 << (2*max_n)}")

if __name__ == "__main__":
    check()
