"""Finite checks of the stated Fock-space Taylor and Jordan formulas.

This program uses the Python standard library. Numerical checks are not proofs.
"""
import itertools
import math


def multiindices(d, degree):
    return sorted((a for a in itertools.product(range(degree + 1), repeat=d)
                   if sum(a) <= degree), key=lambda a: (sum(a), a))


def factorial_multi(a):
    return math.prod(math.factorial(k) for k in a)


def compose_columns(u, B, degree):
    d = len(u)
    bases = multiindices(d, degree)
    constant = [u[i] - sum(B[i][j] * u[j] for j in range(d)) for i in range(d)]
    output = []
    for alpha in bases:
        poly = {(0,) * d: 1 + 0j}
        for i in range(d):
            for _ in range(alpha[i]):
                nxt = {}
                for beta, v in poly.items():
                    nxt[beta] = nxt.get(beta, 0) + v * constant[i]
                    for j in range(d):
                        gamma = list(beta)
                        gamma[j] += 1
                        gamma = tuple(gamma)
                        nxt[gamma] = nxt.get(gamma, 0) + v * B[i][j]
                poly = nxt
        col = {beta: v * math.sqrt(factorial_multi(beta) / factorial_multi(alpha))
               for beta, v in poly.items()}
        output.append(col)
    return bases, output


def linear_columns(u, B, bases):
    d = len(u)
    result = []
    for a in bases:
        derivatives = []
        for i in range(d):
            if a[i] == 0:
                derivatives.append(0j)
                continue
            value = a[i] / math.sqrt(factorial_multi(a))
            for j in range(d):
                value *= u[j] ** (a[j] - (1 if i == j else 0))
            derivatives.append(value)
        coeff = [sum(B[i][j] * derivatives[i] for i in range(d)) for j in range(d)]
        col = {(0,) * d: -sum(u[j] * coeff[j] for j in range(d))}
        for j in range(d):
            e = tuple(1 if m == j else 0 for m in range(d))
            col[e] = coeff[j]
        result.append(col)
    return result


def frobenius_discrepancy(u, matrix, N):
    bases, comp = compose_columns(u, matrix, N)
    lin = linear_columns(u, matrix, bases)
    z = (0,) * len(u)
    error2 = 0.
    for k, alpha in enumerate(bases):
        eval_alpha = math.prod(u[j] ** alpha[j] for j in range(len(u))) / math.sqrt(factorial_multi(alpha))
        for beta in bases:
            y = comp[k].get(beta, 0) - lin[k].get(beta, 0)
            if beta == z:
                y -= eval_alpha
            error2 += abs(y) ** 2
    return math.sqrt(error2)


def gram_check(u, N):
    d = len(u)
    bases = multiindices(d, N)
    for i in range(d):
        for j in range(d):
            value = 0j
            for alpha in bases:
                if not alpha[i] or not alpha[j]:
                    continue
                def derivative(k):
                    ans = alpha[k] / math.sqrt(factorial_multi(alpha))
                    for p in range(d):
                        ans *= u[p] ** (alpha[p] - (1 if p == k else 0))
                    return ans
                value += derivative(i) * derivative(j).conjugate()
            target = math.exp(sum(abs(x) ** 2 for x in u)) * ((1 if i == j else 0) + u[j] * u[i].conjugate())
            assert abs(value - target) < 2e-12, (i, j, value, target)


def jordan_check():
    lam = 0.47 + 0.07j
    t = 0.13 - 0.04j
    power = [[1 + 0j, 0j], [0j, 1 + 0j]]
    A = [[lam, t], [0j, lam]]
    for n in range(1, 51):
        power = [[sum(power[i][k] * A[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
        assert abs(power[0][0] - lam ** n) < 1e-10
        assert abs(power[1][1] - lam ** n) < 1e-10
        assert abs(power[0][1] - n * (lam ** (n - 1)) * t) < 1e-10
        assert abs(power[1][0]) < 1e-15


def main():
    u = (0.28 + 0.17j, -0.20 + 0.14j)
    T = ((0.6 + 0.1j, 0.3 - 0.2j), (-0.1 + 0.15j, 0.2 + 0.05j))
    gram_check(u, 9)
    errors = []
    for epsilon in (0.10, 0.05, 0.025):
        B = tuple(tuple(epsilon * x for x in row) for row in T)
        error = frobenius_discrepancy(u, B, 8)
        errors.append(error)
        print('epsilon', epsilon, 'finite Taylor remainder Frobenius', '{:.12g}'.format(error))
    for larger, smaller in zip(errors[:-1], errors[1:]):
        ratio = larger / smaller
        assert 3.4 < ratio < 4.5, ratio
    jordan_check()
    print('PASS: derivative Gram identity, quadratic Taylor scaling, Jordan powers')


if __name__ == '__main__':
    main()
