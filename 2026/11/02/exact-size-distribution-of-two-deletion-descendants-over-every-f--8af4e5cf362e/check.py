#!/usr/bin/env python3
"""Independent finite checks for the two-deletion descendant-size distribution."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb


def deletion_size(word):
    n = len(word)
    return len({tuple(word[k] for k in range(n) if k != i and k != j)
                for i, j in combinations(range(n), 2)})


def local_size(word):
    n = len(word)
    x = [int(word[i] != word[i+1]) for i in range(n-1)]
    s = sum(x)
    zero_runs = sum(x[i] == 0 and (i == 0 or x[i-1] == 1)
                    for i in range(n-1))
    reversals = sum(word[i] == word[i+2] and word[i] != word[i+1]
                    for i in range(n-2))
    return comb(s+1, 2) + zero_runs - reversals


def formula_hist(q, n):
    m = n - 1
    out = Counter()
    # All increments zero.
    out[1] += q
    # All increments nonzero: one positive block.
    for e in range(m):
        out[comb(m+1,2)-e] += q*(q-1)*comb(m-1,e)*(q-2)**(m-1-e)
    # Mixed zero and nonzero increments, alternating runs.
    for s in range(1, m):
        t = m-s
        for b in range(1, s+1):
            for z in range(1, t+1):
                if abs(b-z)>1:
                    continue
                starts = 2 if b==z else 1
                patterns = starts*comb(s-1,b-1)*comb(t-1,z-1)
                for e in range(s-b+1):
                    out[comb(s+1,2)+z-e] += (q*patterns*(q-1)**b
                        *comb(s-b,e)*(q-2)**(s-b-e))
    return +out


def variance(hist):
    total = sum(hist.values())
    first = sum(k*v for k,v in hist.items())
    second = sum(k*k*v for k,v in hist.items())
    return Fraction(second,total)-Fraction(first,total)**2


def predicted_variance(q,n):
    if n == 2:
        return Fraction(0)
    m=n-1
    p=Fraction(q-1,q)
    return (p*(1-p)*(m-1)*
            (2*m*m*p*p-3*m*p*p+m*p+4*p-2)/2)


def predicted_mean(q,n):
    m=n-1
    p=Fraction(q-1,q)
    return m*p+Fraction(m*(m-1),2)*p*p+Fraction(1,q)


def main():
    cases = [(2,n) for n in range(2,13)]
    cases += [(3,n) for n in range(2,11)]
    cases += [(4,n) for n in range(2,9)]
    cases += [(5,n) for n in range(2,8)]
    words_tested=0
    for q,n in cases:
        direct=Counter()
        for word in product(range(q),repeat=n):
            x=deletion_size(word)
            assert x==local_size(word), (q,n,word,x,local_size(word))
            direct[x]+=1
            words_tested+=1
        closed=formula_hist(q,n)
        assert direct==closed, (q,n,direct,closed)
        assert sum(closed.values())==q**n
        assert variance(closed)==predicted_variance(q,n)
        assert Fraction(sum(k*v for k,v in closed.items()),q**n)==predicted_mean(q,n)
    for q in range(2,13):
        for n in range(2,41):
            c=formula_hist(q,n)
            assert sum(c.values())==q**n
            assert variance(c)==predicted_variance(q,n), (q,n)
            assert Fraction(sum(k*v for k,v in c.items()),q**n)==predicted_mean(q,n)
    print('PASS exhaustive parameter cases:',len(cases))
    print('PASS exhaustively enumerated source words:',words_tested)
    print('PASS symbolic-law test pairs:',11*39)
    print('Example q=3,n=5 histogram:',dict(sorted(formula_hist(3,5).items())))
    print('Example q=4,n=6 histogram:',dict(sorted(formula_hist(4,6).items())))
    print('All identities and moments matched.')

if __name__=='__main__': main()
