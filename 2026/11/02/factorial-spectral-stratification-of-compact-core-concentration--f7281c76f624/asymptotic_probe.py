"""High-precision supplementary checks of the large-frequency branch constants.

Requires mpmath. Run: python asymptotic_probe.py.
These finite comparisons are not a substitute for the asymptotic proof.
"""
import mpmath as mp

mp.mp.dps = 180


def eigenvalues(q, m, s):
    s = mp.mpf(s)
    full = mp.matrix([[1 / mp.mpf(m+i+j+1) for j in range(q)]
                      for i in range(q)])
    small = mp.matrix([[s**(m+i+j+1)/mp.mpf(m+i+j+1)
                        for j in range(q)] for i in range(q)])
    lower = mp.cholesky(full)
    inv = lower**-1
    matrix = inv * small * inv.T
    vals, _ = mp.eigsy(matrix)
    return list(vals)[::-1]


def predicted(q, m, s):
    s = mp.mpf(s)
    return [s**(m+2*j-1) *
            (mp.factorial(j-1)/mp.factorial(q-j))**2 *
            (m*(1-s))**(2*(q+1-2*j))
            for j in range(1, q+1)]


def run():
    n = 0
    for q in (3, 4, 5):
        for s in ('0.5', '0.8'):
            for m in (200, 1000):
                exact = eigenvalues(q, m, s)
                approx = predicted(q, m, s)
                ratio = [float(e/a) for e, a in zip(exact, approx)]
                product = mp.fprod(exact)
                expected = mp.mpf(s)**(q*(m+q))
                assert abs(product/expected-1) < mp.mpf('1e-80')
                assert all(0.01 < v < 20 for v in ratio)
                if m == 1000:
                    assert max(abs(v-1) for v in ratio) < 0.15
                print(f'q={q}, s={s}, m={m}, eigenvalue/asymptotic={ratio}')
                n += 2
    print(f'PASS: {n} high-precision determinant and asymptotic-ratio checks')


if __name__ == '__main__':
    run()
