"""High-precision independent heat-trajectory and Vandermonde checks.

Requires mpmath. This independently constructs every measurement matrix
from the cycle heat kernel and compares its Gram determinant with the
closed formula, rather than generating the Gram from the formula.
"""
import math
import mpmath as mp


def test():
    mp.mp.dps = 80
    tau = mp.mpf('0.3')
    tests = 0
    zero_cases = 0
    even_parity_cases = 0
    for n in range(3, 13):
        m = n // 2
        r = m + 1
        nodes = [mp.exp(-tau * (2 - 2 * mp.cos(2 * mp.pi * k/n))) for k in range(r)]
        vandermonde = mp.matrix([[x**t for x in nodes] for t in range(r)])
        h = vandermonde.T * vandermonde
        hinv = h**-1
        determinant_h = mp.det(h)
        # Separately assemble the powers of the entire heat kernel by Fourier sum.
        powers = []
        for t in range(r):
            kernel = [sum(mp.exp(-tau * (2-2*mp.cos(2*mp.pi*k/n))*t)
                          * mp.cos(2*mp.pi*k*j/n) for k in range(n))/n
                      for j in range(n)]
            powers.append(kernel)
        for d in range(1, m+1):
            obs = mp.matrix(2*r, n)
            for t, kernel in enumerate(powers):
                for j in range(n):
                    obs[2*t, j] = kernel[j]
                    obs[2*t+1, j] = kernel[(j-d) % n]
            direct = mp.det(obs.T * obs)
            if n % 2:
                predicted = (2*determinant_h**2*hinv[0, 0]/mp.mpf(n)**(n-1)
                             if math.gcd(d, n) == 1 else mp.mpf(0))
            else:
                predicted = (determinant_h**2 / mp.mpf(n)**(n-2)
                             * (hinv[0,0]*hinv[m,m] - (hinv[0,m]**2 if d % 2 == 0 else 0))
                             if math.gcd(d, m) == 1 else mp.mpf(0))
            if predicted == 0:
                assert abs(direct) < mp.mpf('1e-65'), (n,d,'false nonzero')
                zero_cases += 1
            else:
                relative = abs(direct-predicted)/abs(predicted)
                assert relative < mp.mpf('1e-34'), (n,d,mp.nstr(relative,6))
                assert predicted > 0
                if n%2 == 0 and d%2 == 0:
                    assert hinv[0,m] != 0
                    even_parity_cases += 1
            tests += 1
    print('HEAT_VERIFY_OK')
    print('cycle orders: 3 through 12')
    print('time parameter: 0.3')
    print('precision: 80 decimal places')
    print('direct heat Gram determinants checked:',tests)
    print('structural zero determinants checked:', zero_cases)
    print('positive even-separation comparisons checked:',even_parity_cases)


if __name__ == '__main__':
    test()
