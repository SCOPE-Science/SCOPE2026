from itertools import product
from math import comb


def occurrences_012(word):
    # dp[j] counts subsequences matching the first j symbols of 012.
    dp = [0, 0, 0, 0]
    dp[0] = 1
    for symbol in word:
        for j, target in ((2, 2), (1, 1), (0, 0)):
            if symbol == target:
                dp[j + 1] += dp[j]
    return dp[3]


def denominator_coefficient(m, degree):
    # [x^degree] 1/((1-(m-3)x)(1-(m-1)x)^2(1-(m-2)x)^3)
    if degree < 0:
        return 0
    total = 0
    for a in range(degree + 1):
        ca = (m - 3) ** a
        for b in range(degree - a + 1):
            c = degree - a - b
            cb = (b + 1) * (m - 1) ** b
            cc = comb(c + 2, 2) * (m - 2) ** c
            total += ca * cb * cc
    return total


def predicted_count(m, n):
    return (3 * denominator_coefficient(m, n - 4)
            - (3 * m - 8) * denominator_coefficient(m, n - 5))


def main():
    for m in (3, 4):
        actual = [0] * 9
        for n in range(9):
            for word in product(range(m), repeat=n):
                if occurrences_012(word) == 2:
                    actual[n] += 1
            expected = predicted_count(m, n)
            assert actual[n] == expected, (m, n, actual[n], expected)
        print(f"m={m}: n=0..8 matched; counts n=4..8: "
              + ", ".join(str(actual[n]) for n in range(4, 9)))
    print("VERIFY_OK")


if __name__ == '__main__':
    main()
