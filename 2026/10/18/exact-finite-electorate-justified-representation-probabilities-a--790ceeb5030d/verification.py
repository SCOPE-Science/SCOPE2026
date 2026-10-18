"""Exact small-instance and asymptotic checks for probabilistic JR.

Run using the Python standard library: python verification.py
Finite checks corroborate, and do not replace, the analytic proofs.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, ceil, exp, lgamma, log


def jr_definition(profile, winners):
    """Independently implement JR by enumerating cohesive voter groups."""
    n = len(profile)
    k = len(winners)
    for group in range(1, 1 << n):
        members = [v for v in range(n) if group & (1 << v)]
        if len(members) * k < n:
            continue
        common = set(profile[members[0]])
        for v in members[1:]:
            common.intersection_update(profile[v])
        if common and all(not (profile[v] & set(winners)) for v in members):
            return False
    return True


def jr_exact(n, probabilities, winners):
    """Conditional-binomial formula with exact rational arithmetic."""
    k = len(winners)
    r = (n + k - 1) // k
    q = Fraction(1)
    for c in winners:
        q *= 1 - probabilities[c]
    result = Fraction(0)
    for u in range(n + 1):
        term = comb(n, u) * q**u * (1-q)**(n-u)
        for c, p in enumerate(probabilities):
            if c in winners:
                continue
            tail = sum((comb(u, h)*p**h*(1-p)**(u-h)
                        for h in range(min(u, r-1)+1)), Fraction(0))
            term *= tail
        result += term
    return result


def independent_enumeration(n, probabilities, k):
    """Directly sum probabilities of all ballot profiles."""
    m = len(probabilities)
    committees = list(combinations(range(m), k))
    answers = {w: Fraction(0) for w in committees}
    for bits in range(1 << (n*m)):
        ballots = [{j for j in range(m) if (bits >> (v*m+j)) & 1}
                   for v in range(n)]
        probability = Fraction(1)
        for v in range(n):
            for j in range(m):
                p = probabilities[j]
                probability *= p if j in ballots[v] else 1-p
        if probability == 0:
            continue
        for w in committees:
            if jr_definition(ballots, w):
                answers[w] += probability
    return answers


def kl(x, q):
    return (x*log(x/q) if x else 0.0) + ((1-x)*log((1-x)/(1-q)) if x<1 else 0.0)


def binomial_log_tail(n, p, threshold):
    terms = [(lgamma(n+1)-lgamma(j+1)-lgamma(n-j+1)
              +j*log(p)+(n-j)*log(1-p)) for j in range(threshold, n+1)]
    top = max(terms)
    return top + log(sum(exp(x-top) for x in terms))


def run():
    checks = 0
    cases = [
        (3, [Fraction(1,5), Fraction(2,5), Fraction(3,5), Fraction(4,5)], 2),
        (3, [Fraction(1,4), Fraction(1,4), Fraction(3,4), Fraction(3,4)], 2),
        (3, [Fraction(0), Fraction(1,2), Fraction(1)], 2),
        (3, [Fraction(1,5), Fraction(2,5), Fraction(3,5), Fraction(4,5)], 3),
        (4, [Fraction(1,4), Fraction(1,2), Fraction(3,4)], 2),
        (2, [Fraction(1,3), Fraction(2,3), Fraction(3,4)], 3),
    ]
    for n, p, k in cases:
        results = independent_enumeration(n, p, k)
        top = tuple(sorted(sorted(range(len(p)), key=lambda c: (-p[c], c))[:k]))
        for w, actual in results.items():
            assert actual == jr_exact(n, p, w), (n, p, k, w, actual)
            assert results[top] >= actual, (n, p, k, w, actual)
            checks += 2
        print('exact instance:', n, len(p), k, 'top:', top, 'JR:', results[top])
    example = jr_exact(4,[Fraction(3,4),Fraction(1,2),Fraction(1,4)],(0,1))
    assert example == Fraction(1042685,1048576)
    checks += 1
    print('four-voter example:', example)
    for k in (1, 2, 3, 5, 10):
        a = k**k / (k+1)**(k+1)
        assert 0 < a < 1/k
        for p in [0.01,1/(k+1),0.21,0.5,0.9,0.99]:
            assert p*(1-p)**k <= a + 1e-13
            checks += 1
        if k>=2:
            n = 600
            observed = -binomial_log_tail(n, a, ceil(n/k))/n
            assert 0 < observed - kl(1/k,a) < 0.05, (k,observed,kl(1/k,a))
            checks += 1
    print('verification assertions:', checks)

if __name__ == '__main__':
    run()
