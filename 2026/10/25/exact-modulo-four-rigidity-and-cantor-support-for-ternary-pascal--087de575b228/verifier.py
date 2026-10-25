#!/usr/bin/env python3
"""Standalone integer checks for the Pascal-row modulo-four theorem."""

def digits3(n):
    result = []
    while n:
        result.append(n % 3)
        n //= 3
    return result


def predicted(n):
    d = digits3(n)
    r = d.count(2)
    signed = 0 if 1 in d else (3 - 3**r) // 2
    return signed, int(1 not in d and r % 2 == 0)


def run():
    row = [1]                  # row of Pascal's triangle reduced modulo 3
    for n in range(2300):
        signed = sum((-1 if j % 2 else 1) * c for j, c in enumerate(row))
        t_mod4 = sum((3 if j % 2 else 1) * c for j, c in enumerate(row)) % 4
        exp_signed, exp_mod4 = predicted(n)
        assert signed == exp_signed, (n, signed, exp_signed)
        assert t_mod4 == exp_mod4, (n, t_mod4, exp_mod4)
        row = [1] + [(row[j-1] + row[j]) % 3 for j in range(1, len(row))] + [1]
    for k in range(1, 9):
        count = sum(predicted(n)[1] for n in range(3**k))
        assert count == 2**(k-1), (k, count)
    print('PASS: 2300 independently generated Pascal rows and exact signed sums;')
    print('PASS: congruence classes and eight triadic interval counts.')

if __name__ == '__main__':
    run()
