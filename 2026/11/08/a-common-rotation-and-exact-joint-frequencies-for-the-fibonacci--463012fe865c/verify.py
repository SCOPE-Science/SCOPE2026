"""Finite reproducibility tests for joint Fibonacci/Lucas-word letter frequencies.

Only Python's standard library is required. The mathematical proof establishes
unrestricted statements; these finite tests check definitions and derived coding.
"""
from decimal import Decimal, localcontext
from math import isqrt


def quadratic_beatty(k, integer_coefficient):
    """floor(k*(integer_coefficient+sqrt(5))/2), for k>=1."""
    assert k >= 1
    return (integer_coefficient*k + isqrt(5*k*k)) // 2


def fibonacci_word_prefix(n):
    word = "0"
    while len(word) < n:
        word = "".join("01" if ch == "0" else "0" for ch in word)
    return word[:n]


def lucas_word_prefix(n):
    previous, current = "0", "011"
    while len(current) < n:
        previous, current = current, current + previous
    return current[:n]


def main():
    n = 50000
    fib = fibonacci_word_prefix(n)
    luc = lucas_word_prefix(n)
    inflated_fib = "".join("0" if x == "0" else "11"
                           for x in fibonacci_word_prefix(n))[:n]
    assert luc == inflated_fib

    f_b = bytearray(n)
    l_b = bytearray(n)
    k = 1
    while True:
        idx = quadratic_beatty(k, 3)-1
        if idx >= n:
            break
        f_b[idx] = 1
        k += 1
    k = 1
    while True:
        idx = quadratic_beatty(k, 5)-2
        if idx >= n:
            break
        l_b[idx] = 1
        if idx+1 < n:
            l_b[idx+1] = 1
        k += 1
    assert all((fib[i] == str(f_b[i]) and luc[i] == str(l_b[i]))
               for i in range(n))

    with localcontext() as context:
        context.prec = 90
        gamma = (Decimal(5)-Decimal(5).sqrt())/10
        beta = 5*gamma-1
        assert Decimal(0) < gamma < Decimal('0.3')
        theoretical = (Decimal(7)/5-4*gamma, Decimal(3)/5-gamma,
                       2*gamma-Decimal(2)/5, 3*gamma-Decimal(3)/5)
        assert abs(sum(theoretical)-1) < Decimal('1e-80')
        assert all(v > 0 for v in theoretical)
        counts = [0, 0, 0, 0]
        for idx in range(n):
            t = ((idx+1)*gamma) % 1
            f = int((5*t) % 1 > 1-beta)
            l = int(t > 1-2*gamma)
            assert f == f_b[idx] and l == l_b[idx], (idx, f, l)
            counts[2*f+l] += 1
            if (idx+1) in (100, 1000, 10000, n):
                errors = [abs(Decimal(counts[j])-(idx+1)*theoretical[j])
                          for j in range(4)]
                assert max(errors) < 80, (idx+1, counts, errors)
                print("PREFIX", idx+1, "pair_counts", counts,
                      "max_absolute_error", float(max(errors)))
        assert abs(theoretical[0]+theoretical[3]-(Decimal(4)/5-gamma)) < Decimal('1e-80')
        print("VERIFY_OK N=50000 morphism_and_Lucas_recursion=yes exact_Beatty=yes",
              "joint_rotation_coding=yes four_densities=yes")


if __name__ == '__main__':
    main()
