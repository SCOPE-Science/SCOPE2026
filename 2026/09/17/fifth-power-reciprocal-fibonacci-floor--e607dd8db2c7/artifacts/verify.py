from fractions import Fraction

M = 31958


def fib(n: int) -> int:
    if n < 0:
        raise ValueError("negative index")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def lucas(n: int) -> int:
    if n == 0:
        return 2
    return fib(n - 1) + fib(n + 1)


def numerator_A(n: int) -> int:
    return (
        M * (fib(n) ** 5 - fib(n - 1) ** 5)
        + 1102 * ((-1) ** n) * (7 * fib(3 * n) - 2 * lucas(3 * n))
        + 1763 * fib(n)
        - 106 * lucas(n)
    )


def predicted_floor(n: int) -> int:
    A = numerator_A(n)
    r = A % M
    return (A - r) // M


def inverse_tail_interval(n: int, extra: int = 40):
    K = n + extra
    partial = sum(
        (Fraction(1, fib(k) ** 5) for k in range(n, K + 1)),
        Fraction(0, 1),
    )

    # F_{j+2} >= 2 F_j gives an exact geometric majorant for the omitted tail.
    remainder = Fraction(32, 31) * (
        Fraction(1, fib(K + 1) ** 5) + Fraction(1, fib(K + 2) ** 5)
    )
    lower = Fraction(1, 1) / (partial + remainder)
    upper = Fraction(1, 1) / partial
    return lower, upper


def verify_small_cases():
    checked = []
    for n in range(4, 27):
        q = predicted_floor(n)
        lo, hi = inverse_tail_interval(n)
        assert lo >= q
        assert hi < q + 1
        checked.append(n)
    return checked


def verify_nonintegrality_mod_19():
    # Since 19 divides both 31958 and 1102,
    # A_n == 4 F_n - 3 F_{n-1} (mod 19).
    residues = [
        (4 * fib(n) - 3 * fib(n - 1)) % 19
        for n in range(1, 10)
    ]
    assert residues == [4, 1, 5, 6, 11, 17, 9, 7, 16]

    # The state (F_n,F_{n-1}) repeats after 18 modulo 19,
    # and the displayed linear combination already repeats after 9.
    for n in range(1, 200):
        assert (4 * fib(n + 9) - 3 * fib(n + 8)) % 19 == (
            4 * fib(n) - 3 * fib(n - 1)
        ) % 19
        assert numerator_A(n) % 19 != 0
    return residues


def verify_period_3654():
    N = 3 * (2 * 3654 + 1) + 1
    f = [0] * (N + 1)
    f[1] = 1
    for k in range(2, N + 1):
        f[k] = (f[k - 1] + f[k - 2]) % M

    def L(k):
        if k == 0:
            return 2
        return (f[k - 1] + f[k + 1]) % M

    assert f[3654] == 0 and f[3655] == 1

    residues = []
    for n in range(1, 2 * 3654 + 1):
        A = (
            M * (pow(f[n], 5, M) - pow(f[n - 1], 5, M))
            + 1102 * ((-1) ** n) * (7 * f[3 * n] - 2 * L(3 * n))
            + 1763 * f[n] - 106 * L(n)
        ) % M
        residues.append(A)
    assert residues[:3654] == residues[3654:]
    return len(set(residues[:3654]))


if __name__ == "__main__":
    small = verify_small_cases()
    mod19 = verify_nonintegrality_mod_19()
    distinct = verify_period_3654()
    assert fib(27) == 196418 and fib(26) == 121393
    # alpha > 3/2 and alpha^27 = F_27 alpha + F_26.
    assert 3 * fib(27) + 2 * fib(26) > 2 * 319580

    print(f"exact interval checks: n={small[0]}..{small[-1]} passed")
    print("A_n mod 19 cycle:", mod19)
    print("all A_n are nonzero mod 19")
    print(f"A_n mod {M} repeats with period 3654; distinct residues in one period: {distinct}")
    print("alpha^27 > 319580 certified from alpha > 3/2")
