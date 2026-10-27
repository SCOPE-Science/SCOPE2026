#!/usr/bin/env python3
"""Direct finite checks of a three-adic Abelian block-composition identity.

Every computation uses exact integer arithmetic. Run with Python 3.
"""

def iterate_h(level):
    s = '0'
    for _ in range(level):
        s = ''.join(('001' if c == '0' else '011') for c in s)
    return s


def value_by_digits(n):
    while n:
        d = n % 3
        if d == 0:
            return 0
        if d == 2:
            return 1
        n //= 3
    return 0


def run_checks():
    z = iterate_h(10)  # 59,049 symbols
    assert len(z) == 3 ** 10
    for n, c in enumerate(z):
        assert int(c) == value_by_digits(n), ('digit recursion', n)
    prefix = [0]
    for c in z:
        prefix.append(prefix[-1] + int(c))
    num_windows = 0
    num_pairs = 0
    num_triples = 0
    for k in range(7):
        m = 3 ** k
        p = (m - 1) // 2
        for i in range(6000):
            assert i + 3 * m <= len(z)
            q = (i + m - 1 - p) // m
            sums = [prefix[i+(j+1)*m] - prefix[i+j*m] for j in range(3)]
            expected = [(m-1)//2 + value_by_digits(q+j) for j in range(3)]
            assert sums == expected, ('three-adic block composition',k,i,sums,expected)
            e = int(sums[0] == sums[1]); e2 = int(value_by_digits(q) == value_by_digits(q+1))
            assert e == e2, ('square classification',k,i)
            assert not (sums[0] == sums[1] == sums[2]), ('cube prohibition',k,i)
            num_windows += 1
            num_pairs += e
            num_triples += 1
        for r in range(110):
            E = [int(value_by_digits(3*r+j)==value_by_digits(3*r+j+1)) for j in range(3)]
            assert E == [1-value_by_digits(r),value_by_digits(r),0], ('coding law',r)
            # At every fixed scale, one of these three adjacent root-symbol pairs agrees.
            assert sum(E) == 1
    print('PASS: digit recursion verified on',len(z),'symbols')
    print('PASS: block sum, adjacent pair, and forbidden triple verified on',num_windows,'windows')
    print('PASS: exact local coding identity for',7*110,'triple-index tests')
    print('finite-square-count',num_pairs,'finite-triple-count',num_triples)
    print('These finite checks are not proofs of the all-scale theorem.')


if __name__ == '__main__':
    run_checks()
