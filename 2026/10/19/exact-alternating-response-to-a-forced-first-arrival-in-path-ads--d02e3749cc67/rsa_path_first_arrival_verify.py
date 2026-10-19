"""Independent finite checks for first-arrival random sequential adsorption on paths.

The general sign theorem is proved analytically in RESULT.md; these finite checks
independently test the recurrence, direct arrival permutations, and the sign law.
No external packages are required.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial


def exact_means(cap):
    values = [Fraction(0)] * (cap + 1)
    for n in range(1, cap + 1):
        values[n] = 1 + Fraction(2, n) * sum(values[:n-1])
    return values


def forced_mean(j, n, i):
    def val(k):
        return j[k] if k >= 0 else Fraction(0)
    return 1 + val(i-2) + val(n-i-1)


def accepted_count(order):
    used = set()
    for v in order:
        if v-1 not in used and v+1 not in used:
            used.add(v)
    return len(used)


def direct_test():
    checks = 0
    for n in range(1, 9):
        j = exact_means(n)
        total = 0
        by_first = [0] * n
        count = 0
        for p in permutations(range(1, n+1)):
            c = accepted_count(p)
            total += c
            by_first[p[0]-1] += c
            count += 1
        assert Fraction(total, count) == j[n], n
        checks += 1
        for i in range(1, n+1):
            actual = Fraction(by_first[i-1], factorial(n-1))
            assert actual == forced_mean(j, n, i), (n, i)
            checks += 1
    return checks


def sign_test():
    j = exact_means(100)
    checks = 0
    for n in range(1, 101):
        for i in range(1, n+1):
            delta = forced_mean(j,n,i)-j[n]
            if n in (1,2,4):
                assert delta == 0, (n,i,delta)
            else:
                assert delta * ((-1)**min(i-1,n-i)) > 0, (n,i,delta)
            d = min(i-1,n-i)
            if d >= 1:
                assert abs(delta) < Fraction(3*(2**d),factorial(d+1)), (n,i)
            checks += 1
    return checks


if __name__ == '__main__':
    a = direct_test()
    b = sign_test()
    print(f'PASS: {a} direct-arrival rational checks; {b} sign and bound checks; n<=100.')
