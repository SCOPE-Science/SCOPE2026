"""Independent checks for idempotents of dihedral quandle algebras.

Usage: python3 check_idempotents.py [--extended]
Requires only the Python 3 standard library.
"""
import itertools
import math
import sys


def divisors(n):
    return [t for t in range(1, n + 1) if n % t == 0]


def phi(t):
    return sum(math.gcd(i, t) == 1 for i in range(1, t + 1))


def prediction(n, q):
    assert n >= 3 and n % 2 and q >= 2 and math.gcd(n, q) == 1
    result = 2
    for t in divisors(n):
        if t == 1:
            continue
        d = 1
        while pow(2, d, t) != 1:
            d += 1
        powers = {pow(2, j, t) for j in range(d)}
        contained_minus_one = t - 1 in powers
        H = set(powers)
        if not contained_minus_one:
            H.update((-u) % t for u in powers)
        N = (1 << (d // 2)) + 1 if contained_minus_one else (1 << d) - 1
        rho = {pow(2, j, t): pow(2, j, N) for j in range(d)}
        if not contained_minus_one:
            rho.update({(-pow(2, j, t)) % t: (-pow(2, j, N)) % N
                        for j in range(d)})
        assert len(rho) == len(H) and set(rho) == H and N % t == 0
        e = 1
        while pow(q, e, t) not in H:
            e += 1
        h = pow(q, e, t)
        g = math.gcd(N, q**e - rho[h])
        assert phi(t) % (len(H) * e) == 0
        result *= (1 + g)**(phi(t) // (len(H) * e))
    return result


def brute(n, q, add, mul):
    """Check x*x=x from the multiplication table, not by Fourier theory."""
    answer = 0
    for a in itertools.product(range(q), repeat=n):
        out = [0] * n
        support = [i for i, v in enumerate(a) if v]
        for i in support:
            for j in support:
                k = (2*j - i) % n
                out[k] = add(out[k], mul(a[i], a[j]))
        answer += (out == list(a))
    return answer


def modulo_ops(p):
    return lambda a, b: (a + b) % p, lambda a, b: a*b % p


def gf4_mul(a, b):
    """GF(4) = GF(2)[u]/(u*u+u+1), 2 denotes u."""
    result = 0
    for i in range(2):
        for j in range(2):
            if (a >> i) & 1 and (b >> j) & 1:
                result ^= (3 if i + j == 2 else (1 << (i + j)))
    return result


def main():
    tests = [(3, 2), (3, 5), (5, 2), (5, 3), (7, 2),
             (9, 2), (11, 2), (15, 2)]
    if '--extended' in sys.argv:
        tests += [(7, 3), (9, 5), (11, 3)]
    for n, p in tests:
        add, mul = modulo_ops(p)
        a = brute(n, p, add, mul)
        b = prediction(n, p)
        print(f'GF({p}) n={n}: direct={a} formula={b}', flush=True)
        assert a == b
    for n in (3, 5, 9):
        a = brute(n, 4, lambda x, y: x ^ y, gf4_mul)
        b = prediction(n, 4)
        print(f'GF(4) n={n}: direct={a} formula={b}', flush=True)
        assert a == b
    print('All selected independent coefficient-space checks passed.')


if __name__ == '__main__':
    main()
