"""Finite numerical checks for boundary-density return-excess asymptotics.

Run with: python verify.py
The all-time and all-parameter theorems are established by the proof, not these tests.
"""
import math


def inverse_orbit(alpha, steps):
    b = 2.0 ** alpha
    sequence = [0.5]
    for _ in range(steps):
        x = sequence[-1]
        z = x / (1.0 + b * x ** alpha)
        for _ in range(8):
            z -= (z * (1.0 + b * z ** alpha) - x) / (
                1.0 + (1.0 + alpha) * b * z ** alpha
            )
        assert 0 < z < x
        assert abs(z * (1.0 + b * z ** alpha) - x) < 1e-12
        sequence.append(z)
    return sequence


def phi(x, kappa, beta, d=1.0):
    r = kappa + 1.0
    return (x / 2) ** r / r + d * (x / 2) ** (r + beta) / (r + beta)


def limit_constant(alpha, kappa, beta, d=1.0):
    r = kappa + 1.0
    p = r / alpha
    delta = beta / alpha
    C = (alpha * 2**alpha) ** (-1.0 / alpha)
    Q = (1.0 + alpha) / (2 * alpha * alpha)
    if beta < alpha:
        L = d * r / (r + beta) * 2**(-beta) * C**beta
        return abs(L) * delta / (p + delta) * (p / (p + delta)) ** (p / delta)
    return r * Q / (p + 1) * (p / (p + 1)) ** p


def measured(alpha, kappa, beta, n, seq):
    p = (kappa + 1.0) / alpha
    den = phi(seq[n-1], kappa, beta)
    best = 0.0
    for j in range(1000, 5501):
        u = j / 1000.0
        k = int(math.floor(u * n)) - 1
        tail = phi(seq[k], kappa, beta) / den
        best = max(best, abs(tail - u**(-p)))
    if beta < alpha:
        return best * n**(beta/alpha)
    return best * n / math.log(n)


def test_return_cylinders(alpha):
    seq = inverse_orbit(alpha, 40)
    b = 2**alpha
    def T(x):
        return x * (1 + b*x**alpha) if x<=0.5 else 2*x-1
    for n in range(1, 14):
        threshold = (1+seq[n-1])/2
        eps = min(1e-8,seq[n-1]-seq[n]) / 10
        for y, expected in [(threshold-eps,True),(threshold+eps,False)]:
            x=y; first=None
            for j in range(1,n+1):
                x=T(x)
                if x>0.5:
                    first=j
                    break
            assert (first is None)==expected, (alpha,n,y,first)


def main():
    for alpha in (0.25,0.5,1.0,2.0):
        test_return_cylinders(alpha)
    seq = inverse_orbit(0.5, 100001)
    checks=[]
    for kappa,beta in ((0.0,0.25),(0.0,1.0),(0.5,0.25),(0.5,0.5)):
        target=limit_constant(0.5,kappa,beta)
        vals=[measured(0.5,kappa,beta,n,seq) for n in (1500,5000,15000)]
        assert abs(vals[-1]-target)<abs(vals[0]-target),(kappa,beta,vals,target)
        checks.append((kappa,beta,tuple(round(x,6) for x in vals),round(target,6)))
    print('VERIFY_OK return_cylinder_tests=52 weighted_cases=4 normalized_rate_checks=12')
    for x in checks: print('case',x)

if __name__ == '__main__':
    main()
