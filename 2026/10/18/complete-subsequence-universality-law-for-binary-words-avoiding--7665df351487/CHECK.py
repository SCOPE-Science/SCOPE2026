"""Independent small-size checks for binary 2-run-limited subsequence universality.

Uses only the Python standard library. The general proof is mathematical;
finite enumerations below are corroboration, not a substitute for it.
"""
from collections import Counter
from itertools import product
from math import comb, sqrt


def is_subsequence(pattern, word):
    it = iter(word)
    return all(any(bit == wanted for bit in it) for wanted in pattern)


def index_direct(word):
    k = 0
    while all(is_subsequence(p, word) for p in product((0, 1), repeat=k + 1)):
        k += 1
    return k


def legal(word):
    return all(not (word[j] == word[j + 1] == word[j + 2])
               for j in range(len(word) - 2))


def coefficient_polynomial(n, k):
    def term(m, j):
        return comb(m, j) * (1 << (m - j)) if 0 <= j <= m else 0
    a = term(k, n - 2*k) + 2*term(k, n-2*k-1) + 2*term(k, n-2*k-2)
    if k >= 1:
        a += term(k - 1, n - 2*k - 1)
    return a


def direct_histogram(n):
    c = Counter()
    for w in product((0, 1), repeat=n):
        if legal(w):
            c[index_direct(w)] += 1
    return c


def recurrence_histograms(nmax):
    hist = [{0:1}, {0:2}, {0:2, 1:2}, {1:6}]
    for n in range(4, nmax+1):
        d = Counter()
        for gap, mult in ((2,2), (3,1)):
            for k, v in hist[n-gap].items():
                d[k+1] += mult * v
        hist.append(dict(d))
    return hist[:nmax+1]


def automaton_histograms(nmax):
    # States are (length of terminal equal-letter run, arch-rest occupancy).
    trans = {
        (1,0): [((2,1),0), ((1,1),0)],
        (1,1): [((2,1),0), ((1,0),1)],
        (2,0): [((1,1),0)],
        (2,1): [((1,0),1)],
    }
    out=[{0:1}]
    states={(1,1,0):2}
    out.append({0:2})
    for n in range(2, nmax + 1):
        d=Counter()
        for (r,rest,k),multiplicity in states.items():
            for ((rr,bb),inc) in trans[(r,rest)]:
                d[(rr,bb,k+inc)] += multiplicity
        states=dict(d)
        hist=Counter()
        for (_,_,k),v in states.items():hist[k]+=v
        out.append(dict(hist))
    return out


def main():
    h1=recurrence_histograms(120)
    h2=automaton_histograms(120)
    assert h1==h2, 'four-state automaton disagrees with bivariate recurrence'
    for n in range(0,121):
        expected={k:coefficient_polynomial(n,k) for k in range(n+1)}
        expected={k:v for k,v in expected.items() if v}
        assert h1[n]==expected, ('coefficient identity',n,h1[n],expected)
    for n in range(0,15):
        d=direct_histogram(n)
        assert d==h1[n], ('subsequence brute-force',n,d,h1[n])
        assert min(d)==n//3 and max(d)==n//2, ('extremal indices',n)
    for n in (25,50,100,120):
        h=h1[n];N=sum(h.values());mean=sum(k*v for k,v in h.items())/N
        var=sum((k-mean)**2*v for k,v in h.items())/N
        print('n=%d total=%d mean=%.8f variance=%.8f'% (n,N,mean,var))
    print('asymptotic mean slope =',1/sqrt(5))
    print('asymptotic variance slope =',1-11*sqrt(5)/25)
    print('DIRECT_ENUMERATION n=0..14: PASS')
    print('AUTOMATON_RECURRENCE_COEFFICIENT n=0..120: PASS')
    print('EXTREMAL_INDEX n=0..14: PASS')
    print('ALL CHECKS PASSED')

if __name__=='__main__':main()
