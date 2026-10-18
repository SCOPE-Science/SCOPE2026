"""Reproduce the exact finite portion of the square-prime-counting root inequality.

Uses only Python's standard library and integer arithmetic. Run beside
FINITE_CASES.csv: python VERIFY.py
"""
from csv import reader
from pathlib import Path
from math import isqrt

LIMIT = 10000


def prime_table_sieve(limit):
    mark = bytearray(b'\x01') * (limit + 1)
    mark[0:2] = b'\x00\x00'
    for d in range(2, isqrt(limit) + 1):
        if mark[d]:
            mark[d * d:limit + 1:d] = b'\x00' * (((limit - d * d) // d) + 1)
    return mark


def trial_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def prefix_counts(indicator):
    count = 0
    output = []
    for v in indicator:
        count += int(v)
        output.append(count)
    return output


def main():
    a = prime_table_sieve(LIMIT)
    b = bytearray(trial_prime(x) for x in range(LIMIT + 1))
    assert a == b, 'Sieve and trial division disagree'
    counts = prefix_counts(a)
    records = []
    for n in range(3, 100):
        c = counts[n * n]
        d = counts[(n + 1) ** 2]
        assert c ** (n + 1) > d ** n, ('root inequality fails', n, c, d)
        records.append([str(n), str(c), str(d)])
    csv_path = Path(__file__).with_name('FINITE_CASES.csv')
    with csv_path.open(newline='', encoding='utf-8') as f:
        actual = list(reader(f))
    assert actual == [['n', 'pi_n_squared', 'pi_next_squared']] + records
    assert counts[4] ** 3 < counts[9] ** 2, 'Sharpness at n=2 failed'
    print('PASS: two independent prime indicators agree for every integer 0..10000')
    print('PASS: all 97 integer-power inequalities for n=3..99')
    print('PASS: all 97 certificate rows match computed exact prime counts')
    print('PASS: n=2 violates the proposed decreasing direction')


if __name__ == '__main__':
    main()
