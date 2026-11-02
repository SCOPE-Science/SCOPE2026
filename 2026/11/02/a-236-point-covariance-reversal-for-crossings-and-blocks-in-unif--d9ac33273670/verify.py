"""Exact, stand-alone verification of the block-count/crossing covariance sign theorem.

Run with Python 3.9 or later: python verify.py
Only standard-library integer arithmetic is used. The infinite tail is
handled analytically in RESULT.md, not by extrapolating finite checks.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb


def bells(max_n):
    # Bell numbers from their binomial recurrence, with B_0=1.
    B = [1]
    for n in range(max_n):
        B.append(sum(comb(n, j) * B[j] for j in range(n+1)))
    return B


def stirling_row(n):
    S = [1]
    for m in range(1, n+1):
        S = [(k*S[k] if k<len(S) else 0) +
             (S[k-1] if k else 0) for k in range(m+1)]
    return S


def numerator(n, B):
    a,b,c,d = B[n:n+4]
    return ((2*n+9)*(a*c-b*b) + 5*b*c + 4*a*b
            - 5*a*d + (4*n+2)*a*a)


def arcs_and_crossings(rgf):
    groups = defaultdict(list)
    for i, label in enumerate(rgf):
        groups[label].append(i)
    arcs = [(b[j], b[j+1]) for b in groups.values()
            for j in range(len(b)-1)]
    return sum((a<c<b<d) or (c<a<d<b)
               for i, (a,b) in enumerate(arcs)
               for c,d in arcs[i+1:])


def restricted_growth_words(n):
    a = [0]*n
    def step(i, largest):
        if i==n:
            yield tuple(a)
            return
        for label in range(largest+2):
            a[i] = label
            yield from step(i+1, max(largest,label))
    yield from step(1,0)


def check():
    assertions = 0
    B = bells(803)
    assert B[:8] == [1,1,2,5,15,52,203,877]; assertions+=1
    # Independent Stirling recurrence reproduces Bell numbers and first-crossing moments.
    for n in range(1,16):
        S = stirling_row(n)
        assert sum(S)==B[n]; assertions+=1
        if n<4: continue
        K = sum(k*S[k] for k in range(1,n+1))
        C2 = sum((n*(k-1)-5*comb(k,2))*S[k]
             + 3*(n+1-k)*S[k-1] for k in range(1,n+1))
        KC2 = sum(k*((n*(k-1)-5*comb(k,2))*S[k]
             + 3*(n+1-k)*S[k-1]) for k in range(1,n+1))
        D = numerator(n,B)
        assert 2*(KC2*B[n]-K*C2)==D; assertions+=1
        assert C2 >= 0; assertions+=1
    # Independent enumeration tests the actual crossing definition.
    for n in range(4,9):
        total=0; sumK=0; sumC=0; sumKC=0
        for rgf in restricted_growth_words(n):
            k=max(rgf)+1
            x=arcs_and_crossings(rgf)
            total+=1;sumK+=k;sumC+=x;sumKC+=k*x
        assert total==B[n];assertions+=1
        assert 4*(sumKC*total-sumK*sumC)==numerator(n,B);assertions+=1
    # Exhaustive exact-integer sign certification on the finite range.
    neg = [n for n in range(4,236) if not numerator(n,B)<0]
    pos = [n for n in range(236,800) if not numerator(n,B)>0]
    assert not neg and not pos,(neg,pos); assertions+=796
    # A single integer inequality gives the rigorous infinite-range result.
    assert 5*B[801] < 801*B[800]; assertions+=1
    # Certified rational bounds, with no floating-point comparisons.
    assert Fraction(-278,1000) < Fraction(numerator(235,B),4*B[235]**2) < Fraction(-277,1000);assertions+=1
    assert Fraction(189,1000) < Fraction(numerator(236,B),4*B[236]**2) < Fraction(190,1000);assertions+=1
    print('PASS: exact Stirling cross-check, direct enumeration n=4..8,')
    print('      D_n<0 for 4<=n<=235; D_n>0 for 236<=n<=799;')
    print('      5 B_801 < 801 B_800; all rational checks exact.')
    print('total assertion groups/instances:',assertions)
    print('cov(235) ≈',float(Fraction(numerator(235,B),4*B[235]**2)))
    print('cov(236) ≈',float(Fraction(numerator(236,B),4*B[236]**2)))
    print('Bell-800 decimal digits:',len(str(B[800])))

if __name__=='__main__': check()
