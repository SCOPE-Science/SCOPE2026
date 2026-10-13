"""Finite checks and high-precision comparisons for random compositions."""
from fractions import Fraction
from math import comb, log2, exp, isclose


def count_avoiding(n, banned):
    count = [0] * (n + 1)
    size = [0] * (n + 1)
    count[0] = 1
    count_prefix, size_prefix = 1, 1
    for t in range(1, n + 1):
        subtraction_count = count[t - banned] if t >= banned else 0
        subtraction_size = size[t - banned] + count[t - banned] if t >= banned else 0
        count[t] = count_prefix - subtraction_count
        size[t] = size_prefix - subtraction_size
        count_prefix += count[t]
        size_prefix += size[t] + count[t]
    return count[n], size[n]


def covariance_exact(n):
    total = 1 << (n - 1)
    mean_k = Fraction(n + 1, 2)
    result = Fraction(0)
    for banned in range(1, n + 1):
        q, s = count_avoiding(n, banned)
        result += (mean_k * q - s) / total
    return result


def covariance_direct(n):
    records = []
    for mask in range(1 << (n - 1)):
        part_lengths = []
        last = 0
        for i in range(1, n):
            if mask & (1 << (i - 1)):
                part_lengths.append(i - last)
                last = i
        part_lengths.append(n - last)
        records.append((len(part_lengths), len(set(part_lengths))))
    total = len(records)
    ksum = sum(a for a, b in records)
    dsum = sum(b for a, b in records)
    kdsum = sum(a*b for a, b in records)
    return Fraction(kdsum,total) - Fraction(ksum*dsum, total**2)


def asymptotic_profile(n):
    L = log2(n)
    theta = L - int(L)
    a, b = 0.0, 0.0
    for k in range(-26, 60):
        u = 2.0**(theta-k-1)
        if u > 740:
            continue
        v = u*exp(-u)
        a += v
        if v:
            b += (4.0+log2(u))*v/2.0
    return -L*a/2.0 + b, a, b


def main():
    for n in range(1,13):
        lhs, rhs = covariance_direct(n), covariance_exact(n)
        assert lhs == rhs, (n, lhs, rhs)
    assert covariance_exact(4) == Fraction(1,16)
    assert covariance_exact(5) == 0
    for n in range(6, 65):
        assert covariance_exact(n) < 0, n
    for n in [50, 100, 200, 500]:
        actual = float(covariance_exact(n))
        prediction, A, B = asymptotic_profile(n)
        err = abs(actual - prediction)
        assert err < {50:0.01,100:0.002,200:0.001,500:0.001}[n], (n, actual,prediction,err)
        print('n=',n,'exact=',actual,'profile=',prediction,'abs_error=',err,'A=',A,'B=',B)
    print('CHECK_OK: 12 exact exhaustive enumerations, 59 finite sign tests, 4 asymptotic comparisons')


if __name__ == '__main__':
    main()
