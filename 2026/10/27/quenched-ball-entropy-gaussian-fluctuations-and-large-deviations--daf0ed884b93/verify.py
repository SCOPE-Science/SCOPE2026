"""Independent finite checks for random limited-permutation ball theorem.
Uses only the Python standard library; finite tests do not establish limiting laws.
"""
from fractions import Fraction
from itertools import product
from math import comb, exp, log, sqrt


def disjoint_effective_swaps(x):
    n = len(x)
    outputs = set()
    def rec(i, result):
        if i >= n:
            outputs.add(tuple(result))
            return
        rec(i + 1, result + [x[i]])
        if i + 1 < n and x[i] != x[i + 1]:
            rec(i + 2, result + [x[i + 1], x[i]])
    rec(0, [])
    return len(outputs)


def fibonacci(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def independent_set_product(x):
    result, run = 1, 0
    for i in range(len(x) - 1):
        if x[i] != x[i + 1]:
            run += 1
        else:
            result *= fibonacci(run + 2)
            run = 0
    result *= fibonacci(run + 2)
    return result


def edge_moment_recurrence(m, q, power):
    p = Fraction(q - 1, q)
    h = Fraction(1, q)
    seq = [Fraction(1)]
    for k in range(1, m + 1):
        val = p**k * fibonacci(k + 2)**power
        for ell in range(k):
            val += h * p**ell * fibonacci(ell + 2)**power * seq[k - ell - 1]
        seq.append(val)
    return seq


def count_checks(q, n):
    total, total2 = 0, 0
    for x in product(range(q), repeat=n):
        ball = disjoint_effective_swaps(x)
        assert ball == independent_set_product(x), (q, x, ball)
        total += ball
        total2 += ball * ball
    rec1 = edge_moment_recurrence(n - 1, q, 1)[n - 1]
    rec2 = edge_moment_recurrence(n - 1, q, 2)[n - 1]
    assert Fraction(total, q**n) == rec1, (q, n, total, rec1)
    assert Fraction(total2, q**n) == rec2, (q, n, total2, rec2)
    p = Fraction(q-1, q)
    f0, f1 = Fraction(1), Fraction(1)
    for j in range(2, n + 1):
        f0, f1 = f1, f1 + p*f0
    assert rec1 == f1
    return q**n


def constants(q):
    p = 1.0-1.0/q
    h = 1.0/q
    phi = (1 + sqrt(5))/2
    logphi = log(phi)
    def logarithmic_fib(l):
        return (l+2)*logphi-log(5)/2+log1p_safe(-(-phi**-2)**(l+2))
    terms = []
    prob = h
    for l in range(100000):
        terms.append((l+1, logarithmic_fib(l), prob))
        prob *= p
        if prob < 1e-15:
            break
    mu = h*sum(prob*R for T, R, prob in terms)
    sigma2 = h*sum(prob*(R-mu*T)**2 for T,R,prob in terms)
    ln_lambda = log((1+sqrt(1+4*p))/2)
    assert 0 < mu < ln_lambda < logphi
    assert sigma2 > 0
    return mu, sigma2, ln_lambda


def log1p_safe(x):
    from math import log1p
    return log1p(x)


def main():
    tested = 0
    for q, max_n in [(2,10),(3,8),(4,7),(5,6)]:
        for n in range(1, max_n + 1):
            tested += count_checks(q, n)
    print(f'Exact ball-injection and moment recurrence: {tested} exhaustive words passed')
    phi = (1+sqrt(5))/2
    d = log(sqrt(5)/phi)
    slope = d-1/(phi*sqrt(5))
    assert d > 1/(phi*sqrt(5))
    for q in [2,3,4,10,100,1000]:
        mu, variance, annealed = constants(q)
        print(f'q={q}: quenched={mu:.9f}; variance={variance:.9f}; annealed={annealed:.9f}; gap={annealed-mu:.9f}')
        if q >= 1000:
            assert abs(q*(annealed-mu)-slope) < 1e-4
            assert abs(q*variance-d*d) < 1e-3
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
