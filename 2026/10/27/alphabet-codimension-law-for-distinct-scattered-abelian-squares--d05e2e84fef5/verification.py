#!/usr/bin/env python3
"""Independent finite checks for distinct scattered Abelian-square expectations.

Uses direct enumeration of actual subsequence sets and, separately, the
multinomial/greedy-waiting-time generating series over any finite alphabet.
All quantities in these finite checks are exact rational numbers.
"""
from fractions import Fraction
from itertools import product
from math import factorial, comb, sqrt, pi


def mul(a, b, N):
    c = [Fraction(0)] * (N + 1)
    for i, x in enumerate(a):
        if x == 0: continue
        for j, y in enumerate(b[:N + 1 - i]):
            if y: c[i + j] += x * y
    return c


def compositions(total, count):
    if count == 1:
        yield (total,)
    else:
        for v in range(total + 1):
            for rest in compositions(total - v, count - 1):
                yield (v,) + rest


def predicted_means(probs, N):
    q = len(probs)
    assert q >= 2 and all(x > 0 for x in probs) and sum(probs) == 1
    g = [[Fraction(0)] + [p * (1 - p) ** (j - 1) for j in range(1, N + 1)] for p in probs]
    gpowers = []
    for h in g:
        powers = [[Fraction(1)] + [Fraction(0)] * N]
        for j in range(1, N + 1):
            powers.append(mul(powers[-1], h, N))
        gpowers.append(powers)
    f = [Fraction(0)] * (N + 1)
    for m in range(1, N // 2 + 1):
        for k in compositions(m, q):
            # Evaluate multinomial exactly before squaring.
            den = 1
            for x in k: den *= factorial(x)
            weight = (factorial(m) // den) ** 2
            seq = [Fraction(1)] + [Fraction(0)] * N
            for a, v in enumerate(k):
                seq = mul(seq, gpowers[a][2 * v], N)
            for j, val in enumerate(seq):
                f[j] += weight * val
    out = []
    acc = Fraction(0)
    for x in f:
        acc += x
        out.append(acc)
    return out


def exact_abelian_square_count(word):
    subseqs = {()}
    for letter in word:
        subseqs |= {v + (letter,) for v in tuple(subseqs)}
    count = 0
    for v in subseqs:
        if not v or len(v) % 2: continue
        m = len(v) // 2
        if all(v[:m].count(a) == v[m:].count(a) for a in set(v)):
            count += 1
    return count


def observed_means(probs, N):
    q = len(probs)
    answers = [Fraction(0)] * (N + 1)
    cases = 0
    for n in range(N + 1):
        for w in product(range(q), repeat=n):
            p = Fraction(1)
            for a in w: p *= probs[a]
            answers[n] += p * exact_abelian_square_count(w)
            cases += 1
    return answers, cases


def binary_coefficients_from_sqrt(p, N):
    """A second independent route: the differential equation D K' + D'K/2=0."""
    a = p; b = 1 - p
    g0 = [Fraction(0)] + [a * b ** (j-1) for j in range(1, N+1)]
    g1 = [Fraction(0)] + [b * a ** (j-1) for j in range(1, N+1)]
    g0sq = mul(g0, g0, N)
    g1sq = mul(g1, g1, N)
    delta = [u-v for u,v in zip(g0sq,g1sq)]
    dsq = mul(delta,delta,N)
    D = [Fraction(1)] + [Fraction(0)]*N
    for j in range(N+1): D[j] += -2*(g0sq[j]+g1sq[j])+dsq[j]
    K = [Fraction(1)] + [Fraction(0)]*N
    for n in range(1,N+1):
        tot = Fraction(0)
        for i in range(1,n+1):
            tot += (2*(n-i)+i)*D[i]*K[n-i]
        K[n] = -tot/(2*n)
    out=[]; accum=Fraction(-1)
    for x in K:
        accum += x
        out.append(accum)
    return out


def asymptotic_binary(p, n):
    s = sqrt(float(p*(1-p)))
    C = (1+2*s)*sqrt(1+s)/(4*sqrt(pi)*s**1.5)
    return C * (1+s)**n / sqrt(n)


def uniform_large_n_check(q, n=100):
    """A separate exact-coefficient check of the predicted leading constant."""
    f = [1] * (n // 2 + 1)
    for _ in range(2, q + 1):
        f = [sum(comb(j, k) ** 2 * f[j - k] for k in range(j + 1))
             for j in range(len(f))]
    from decimal import Decimal, localcontext
    with localcontext() as ctx:
        ctx.prec = 110
        observed = Decimal(0)
        for j in range(2, n + 1):
            num = sum(f[m] * comb(j - 1, 2*m - 1) * (q - 1) ** (j - 2*m)
                      for m in range(1, j // 2 + 1))
            observed += Decimal(num) / Decimal(q) ** j
        lam = Decimal(2) - Decimal(1) / q
        asympt = (Decimal(q) ** Decimal('1.5') / (2*(q-1))
                  * (Decimal(2*q-1) / (2*Decimal(str(pi)))) ** (Decimal(q-1)/2)
                  * lam ** n / Decimal(n) ** (Decimal(q-1)/2))
        ratio = float(observed / asympt)
        assert 0.98 < ratio < 1.04, (q, ratio)
    print('OK uniform_asymptotic q=',q,'n=',n,'exact_to_asympt=',format(ratio,'.7f'))


def main():
    cases = [
        ([Fraction(1,2),Fraction(1,2)], 11),
        ([Fraction(1,3),Fraction(2,3)], 11),
        ([Fraction(2,5),Fraction(3,5)], 10),
        ([Fraction(1,3)]*3, 8),
        ([Fraction(1,2),Fraction(1,3),Fraction(1,6)], 8),
        ([Fraction(1,4)]*4, 6),
        ([Fraction(1,5)]*5, 5),
    ]
    count=0
    for probs,N in cases:
        predicted = predicted_means(probs,N)
        observed,c = observed_means(probs,N)
        count += c
        assert predicted == observed,(probs,N,[(i,x,y) for i,(x,y) in enumerate(zip(predicted,observed)) if x!=y])
        if len(probs)==2:
            assert predicted == binary_coefficients_from_sqrt(probs[0],N)
        print('OK alphabet=',len(probs),'probs=',','.join(map(str,probs)),'N=',N,'words=',c,'last=',predicted[-1])
    for q in (2, 3, 4): uniform_large_n_check(q)
    print('VERIFY_OK exact_source_words=',count,'source_distributions=',len(cases),'binary_algebraic_recurrences=3','uniform_asymptotic_cases=3')


if __name__=='__main__': main()
