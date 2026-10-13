"""Exact integer checks for theta/partition identities in the enumerative asymptotic theorem.
Run with Python 3, standard library only. Finite checks do not prove the asymptotics.
"""
from math import exp, log, pi, sqrt


def conv(a, b, degree):
    v = [0] * (degree + 1)
    for i, ai in enumerate(a):
        if ai:
            for j in range(min(degree - i, len(b) - 1) + 1):
                v[i + j] += ai * b[j]
    return v


def powseries(a, k, degree):
    out = [1] + [0] * degree
    for _ in range(k):
        out = conv(out, a, degree)
    return out


def verify(degree=240):
    a = [0] * (degree + 1)
    a[0] = 1
    for r in range(1, int(sqrt(degree)) + 1):
        if r * r <= degree:
            a[r * r] += 2
    b = [0] * (degree + 1)
    for r in range(degree):
        j = r * (r + 1)
        if j > degree:
            break
        b[j] += 1
    t2four = [0] + [16 * c for c in powseries(b, 4, degree)[:degree]]
    t3four = powseries(a, 4, degree)
    theta = conv(t2four, t3four, degree)
    sigma1 = [0] * (degree + 1)
    sigma3 = [0] * (degree + 1)
    for d in range(1, degree + 1):
        for j in range(d, degree + 1, d):
            sigma1[j] += d
            sigma3[j] += d ** 3
    for n in range(1, degree + 1):
        expected = 16 * (sigma3[n] - (sigma3[n // 2] if n % 2 == 0 else 0))
        assert theta[n] == expected, (n, theta[n], expected)
    colored = [0] * (degree + 1)
    colored[0] = 1
    for n in range(1, degree + 1):
        num = 12 * sum(sigma1[j] * colored[n - j] for j in range(1, n + 1))
        assert num % n == 0
        colored[n] = num // n
    count = [0] * (degree + 1)
    moment = [0] * (degree + 1)
    for n in range(1, degree + 1):
        for r in range((n - 1) // 2 + 1):
            m = n - 2 * r
            count[n] += theta[m] * colored[r]
            moment[n] += m * theta[m] * colored[r]
        assert moment[n] % 4 == 0
        moment[n] //= 4
    assert count[1:7] == [16, 128, 640, 2560, 8832, 27392]
    assert moment[1:6] == [4, 64, 384, 1792, 6912]
    # A second independent construction of the moment numerator via differentiation.
    differentiated = [n * theta[n] for n in range(degree + 1)]
    for n in range(1, degree + 1):
        assert moment[n] * 4 == sum(differentiated[n - 2 * r] * colored[r]
                                            for r in range((n - 1) // 2 + 1))
    for n in (20, 60, 120, 220):
        la = log(count[n]) - (log(0.5) - 1.75 * log(n) + 2 * pi * sqrt(n))
        lm = log(moment[n]) - (log(0.5 / pi) - 1.25 * log(n) + 2 * pi * sqrt(n))
        print('coefficient N=', n, 'G/asympt=', round(exp(la), 6),
              'M/asympt=', round(exp(lm), 6),
              'moment ratio/asympt=', round((moment[n] / count[n]) * pi / sqrt(n), 6))
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
