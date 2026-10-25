def v2(n):
    if n <= 0:
        raise ValueError("v2 requires a positive integer")
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    return e


def h(t):
    return (t + 2) // 2


def delta(j, n):
    return int(n % 3 == j)


def s(n):
    m = n + 1
    return h(v2(m)) if m % 6 == 0 else 0


def g(n):
    m = n + 1
    return h(v2(m)) if m % 3 == 0 else 0


def main():
    fib = [0, 1]
    for _ in range(2, 10001):
        fib.append(fib[-1] + fib[-2])
    for m in range(1, 10001):
        expected_v2 = v2(m) + 2 if m % 6 == 0 else (1 if m % 6 == 3 else 0)
        assert v2(fib[m]) == expected_v2
        value = fib[m]
        v4 = 0
        while value % 4 == 0:
            value //= 4
            v4 += 1
        assert v4 == s(m - 1)

    for e in range(1, 7):
        B = 4 ** e
        for i in range(B):
            for n in range(150):
                actual = s(B * n + i)
                if i + 1 < B:
                    if (i + 1) % 2:
                        expected = 0
                    else:
                        expected = h(v2(i + 1)) * delta((-(i + 1)) % 3, n)
                else:
                    expected = g(n) + e * delta(2, n)
                assert actual == expected, (e, i, n, actual, expected)

    for n in range(200):
        assert s(16 * n + 1) == delta(1, n)
        assert s(16 * n + 5) == delta(0, n)
        assert s(64 * n + 9) == delta(2, n)
        assert s(4 * n + 3) == g(n) + delta(2, n)

    witnesses = [(s(n), g(n), delta(0, n), delta(1, n), delta(2, n))
                 for n in (0, 1, 2, 5, 11)]
    assert witnesses == [
        (0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0),
        (0, 1, 0, 0, 1),
        (1, 1, 0, 0, 1),
        (2, 2, 0, 0, 1),
    ]
    print("RANK5_FORMULA_OK")


if __name__ == "__main__":
    main()
