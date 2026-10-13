"""Independent finite corroboration of the arithmetic-derivative/aliquot theorem."""
from argparse import ArgumentParser

def check(limit: int = 500000):
    least = [0] * (limit + 1)
    omega = [0] * (limit + 1)
    derivative = [0] * (limit + 1)
    sigma = [0] * (limit + 1)
    for p in range(2, limit + 1):
        if not least[p]:
            for j in range(p, limit + 1, p):
                if not least[j]:
                    least[j] = p
    for n in range(2, limit + 1):
        p = least[n]
        m = n // p
        omega[n] = omega[m] + 1
        derivative[n] = m + p * derivative[m]
    for d in range(1, limit + 1):
        for k in range(d, limit + 1, d):
            sigma[k] += d
    zeros = []
    with_omega = 0
    for n in range(2, limit + 1):
        if omega[n] <= 4:
            with_omega += 1
            actual = derivative[n] == sigma[n] - n
            expected = least[n] == n or n in (12, 18, 220)
            if actual != expected:
                raise AssertionError((n, actual, expected))
            if actual and n not in (12, 18, 220):
                if least[n] != n:
                    raise AssertionError(('composite', n))
            if actual and least[n] != n:
                zeros.append(n)
    assert sigma[396] - 396 == derivative[396] == 696
    assert omega[396] == 5
    print(f'VERIFY_OK limit={limit} omega_le4_checked={with_omega} composite_zeros={zeros} boundary_omega5=396')

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--limit', type=int, default=500000)
    args = parser.parse_args()
    check(args.limit)
