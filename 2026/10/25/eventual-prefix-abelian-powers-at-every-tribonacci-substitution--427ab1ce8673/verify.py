#!/usr/bin/env python3
"""Exact finite test cases for a Tribonacci prefix/Parikh theorem.

The infinite theorem additionally uses the cited finiteness property (F) of
Tribonacci beta. This script checks only its finitely stated test cases.
"""
from decimal import Decimal, localcontext


def times_beta(v):
    a, b, c = v
    return c, a+c, b+c


def divide_beta(v):
    a, b, c = v
    return b-a, c-a, a


def powers(lo, hi):
    d = {0: (1, 0, 0)}
    for r in range(1, hi+1):
        d[r] = times_beta(d[r-1])
    for r in range(-1, lo-1, -1):
        d[r] = divide_beta(d[r+1])
    return d


def triples_sum(terms):
    return tuple(sum(t[j] for t in terms) for j in range(3))


def finite_beta_expansions(limit=200):
    with localcontext() as ctx:
        ctx.prec = 105
        beta = Decimal('1.84')
        for _ in range(30):
            numerator = beta**3-beta**2-beta-1
            beta -= numerator / (3*beta**2-2*beta-1)
        assert abs(beta**3-beta**2-beta-1) < Decimal('1e-90')
        power = powers(-90, 20)
        def value(t):
            return Decimal(t[0])+Decimal(t[1])*beta+Decimal(t[2])*beta**2
        expansions = {}
        for j in range(1, limit+1):
            start = 0
            while value(power[start+1]) <= j:
                start += 1
            remaining = (j, 0, 0)
            terms = []
            for r in range(start, -91, -1):
                if value(remaining) >= value(power[r]) - Decimal('1e-85'):
                    remaining = tuple(remaining[i]-power[r][i] for i in range(3))
                    terms.append(r)
                    if remaining == (0, 0, 0):
                        break
            assert remaining == (0, 0, 0), (j, remaining)
            assert not any(r-1 in terms and r-2 in terms for r in terms)
            assert triples_sum([power[r] for r in terms]) == (j, 0, 0)
            expansions[j] = terms
    return expansions


def substitution_words(count):
    seq = '0'
    out = []
    for _ in range(count):
        out.append(seq)
        seq = ''.join({'0':'01', '1':'02', '2':'0'}[c] for c in seq)
    return out


def run():
    exp = finite_beta_expansions(200)
    words = substitution_words(19)
    lengths = [1, 2, 4]
    parikh = [(1, 0, 0), (1, 1, 0), (2, 1, 1)]
    for r in range(3, 50):
        lengths.append(sum(lengths[r-3:r]))
        parikh.append(tuple(sum(parikh[t][a] for t in range(r-3,r)) for a in range(3)))
    assert all(len(w) == lengths[i] and tuple(w.count(str(a)) for a in range(3)) == parikh[i] for i,w in enumerate(words))
    for k in (3, 4, 10, 20, 50, 100, 200):
        threshold = -min(min(exp[j]) for j in range(1, k+1))
        assert threshold + max(max(exp[j]) for j in range(1,k+1)) < len(lengths)
        for m in range(threshold, min(threshold+3, 22)):
            for j in range(1, k+1):
                rhs_length = sum(lengths[m+r] for r in exp[j])
                rhs_parikh = tuple(sum(parikh[m+r][a] for r in exp[j]) for a in range(3))
                assert rhs_length == j*lengths[m]
                assert rhs_parikh == tuple(j*parikh[m][a] for a in range(3))
        print('algebraic_finite_range',k,threshold)
    # Independently check the symbolic canonical digit-to-prefix identity on
    # each n below 10,000 and direct Parikh blocks for selected large examples.
    word = words[18]
    def greedy(n):
        bits = [0]*len(lengths)
        for r in range(len(lengths)-1,-1,-1):
            if n>=lengths[r]:
                n-=lengths[r]
                bits[r]=1
        assert n==0 and not any(bits[r:r+3]==[1,1,1] for r in range(len(bits)-2))
        return [r for r,v in enumerate(bits) if v]
    for n in range(10000):
        chosen = greedy(n)
        formed = ''.join(words[r] for r in reversed(chosen))
        assert formed == word[:n]
    for k in (3,4,10,20,30):
        m = -min(min(exp[j]) for j in range(1,k+1))
        sample = word[:k*lengths[m]]
        assert len(sample)==k*lengths[m]
        for j in range(k):
            block = sample[j*lengths[m]:(j+1)*lengths[m]]
            assert tuple(block.count(str(a)) for a in range(3)) == parikh[m]
    print('TRIB_PREFIX_ABELIAN_PASS beta_expansions=200 canonical_prefix_tests=10000 parikh_examples=5')

if __name__=='__main__':
    run()
