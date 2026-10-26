"""Supplementary exact finite checks for the squarefree reduced Ramanujan-sum matrix."""
from itertools import combinations
from math import gcd, prod
from sympy import Matrix, ZZ, divisors, mobius, totient
from sympy.matrices.normalforms import smith_normal_form


def ramanujan(q, t):
    # Gcd-divisor definition of the integer Ramanujan sum.
    return sum(int(h) * int(mobius(q // h)) for h in divisors(gcd(q, t)))


def check(primes):
    n = prod(primes)
    divs = [int(d) for d in divisors(n) if d != 1]
    c = Matrix([[ramanujan(d, e) for e in divs] for d in divs])
    d = Matrix.diag(*divs)
    mu = Matrix([[int(mobius(e)) for e in divs]])
    b = d + Matrix.ones(len(divs), 1) * mu
    # Check the full integer incidence factorization and its inverse.
    h = Matrix([[int(mobius(x // y)) if x % y == 0 else 0 for y in divs] for x in divs])
    z = Matrix([[int(e % x == 0) for e in divs] for x in divs])
    u = Matrix([int(mobius(x)) for x in divs])
    assert c == h * d * z + u * Matrix.ones(1, len(divs))
    assert h.det() in (-1, 1) and z.det() in (-1, 1)
    assert h.inv() * c * z.inv() == b
    observed = [abs(int(s)) for s in smith_normal_form(c, domain=ZZ).diagonal()]
    k = len(primes)
    expected = ([int(primes[0] - 1)] if k == 1 else
                [1] * (2 ** (k-1)) + [n] * (2 ** (k-1) - 2) + [n * int(totient(n))])
    assert observed == expected, (n, observed, expected)
    assert abs(int(c.det())) == (int(primes[0]-1) if k == 1 else n ** (2 ** (k-1)-1) * int(totient(n)))
    return n, len(divs), observed


def main():
    primes = [2, 3, 5, 7, 11, 13]
    cases = []
    for k in (1, 2, 3):
        for ps in combinations(primes, k):
            cases.append(check(ps))
    for ps in [(2, 3, 5, 7), (2, 3, 5, 11), (2, 3, 7, 11), (2, 5, 7, 11), (3, 5, 7, 11)]:
        cases.append(check(ps))
    print('VERIFY_OK: %d squarefree integers; %d largest matrix dimension; exact C=H D Z+u1^T and Smith forms' %
          (len(cases), max(x[1] for x in cases)))
    print('SAMPLE:', [x for x in cases if x[0] in (6, 30, 210)])


if __name__ == '__main__':
    main()
