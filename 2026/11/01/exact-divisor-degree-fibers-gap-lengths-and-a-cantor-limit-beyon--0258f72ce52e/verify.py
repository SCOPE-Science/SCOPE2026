"""Exact coefficient-convolution checker for cyclotomic divisor-degree spectra.

Uses integer convolutions of the separate cyclotomic factor degrees, not
any of the proof's digital or gap formulas to construct the coefficients.
"""
from collections import Counter
from math import comb


def divisor_degree_counts(a, p, b):
    degrees = []
    for j in range(b + 1):
        pj = 1 if j == 0 else (p - 1) * p ** (j - 1)
        for i in range(a + 1):
            pi = 1 if i <= 1 else 2 ** (i - 1)
            degrees.append(pi * pj)
    c = {0: 1}
    for d in degrees:
        nxt = c.copy()
        for degree, count in c.items():
            nxt[degree + d] = nxt.get(degree + d, 0) + count
        c = nxt
    return c


def prediction(a, p, b):
    A = 2**a
    h = lambda u: 1 if u in (0, A) else 2
    predicted = {}
    for digits in __import__('itertools').product(range(A+1), repeat=b+1):
        degree = digits[0] + (p-1) * sum(digits[j] * p**(j-1) for j in range(1, b+1))
        assert degree not in predicted, (a,p,b,degree,digits)
        val = 1
        for digit in digits:
            val *= h(digit)
        predicted[degree] = val
    return predicted


def verify(a, p, b):
    A = 2**a
    assert p > A + 1
    true = divisor_degree_counts(a,p,b)
    pred = prediction(a,p,b)
    assert true == pred, (a,p,b, next(((k, true.get(k), pred.get(k)) for k in true.keys() | pred.keys() if true.get(k)!=pred.get(k)), None))
    assert sum(true.values()) == 2**((a+1)*(b+1))
    assert len(true) == (A+1)**(b+1)
    actual_hist = Counter(true.values())
    predicted_hist = {2**r: comb(b+1,r) * (A-1)**r * 2**(b+1-r) for r in range(b+2)}
    assert actual_hist == predicted_hist, (a,p,b,actual_hist,predicted_hist)
    # Uniform choice among all monic divisor polynomials induces the
    # predicted exact marginal distribution of each cyclotomic-degree digit.
    marginals = [Counter() for _ in range(b+1)]
    for degree, multiplicity in true.items():
        u0 = degree % (p-1)
        t = (degree-u0)//(p-1)
        digits = (u0,) + tuple((t // p**j) % p for j in range(b))
        assert all(0 <= u <= A for u in digits)
        for j,u in enumerate(digits):
            marginals[j][u] += multiplicity
    for j in range(b+1):
        expected = {u:(2*A)**b * (1 if u in (0,A) else 2) for u in range(A+1)}
        assert marginals[j] == expected, (a,p,b,j,marginals[j],expected)
    ordered = sorted(true)
    gaps = Counter(ordered[j+1] - ordered[j] - 1 for j in range(len(ordered)-1) if ordered[j+1] > ordered[j] + 1)
    gap_pred = {(p-1-A)*p**k - 1: A*(A+1)**(b-1-k) for k in range(b)}
    assert gaps == gap_pred, (a,p,b,gaps,gap_pred)
    assert ordered[0] == 0 and ordered[-1] == A * p**b
    return len(ordered), sum(gaps.values())


def main():
    primes = (5,7,11,13,17,19,23,29,31,37)
    cases=0; coeffs=0; gaps=0
    for a in range(1, 5):
        for p in primes:
            if p <= 2**a+1:
                continue
            for b in range(1, 4):
                if (2**a+1)**(b+1) > 150000:
                    continue
                n,g=verify(a,p,b)
                coeffs += n; gaps += g; cases += 1
                print(f"CASE_OK a={a} p={p} b={b} degrees={n} gaps={g}")
    print(f"VERIFY_OK cases={cases} represented_degree_coefficients={coeffs} complement_gaps={gaps}")


if __name__ == '__main__':
    main()
