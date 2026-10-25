"""Independent exact-arithmetic checks of GC exact-window constraints.

No external data or third-party packages. Run: python verification_long_window.py
"""
from fractions import Fraction
from collections import defaultdict
from itertools import product
from math import comb

def bin_weight(k, i):
    return (i + 1) * (k - i + 1)

def W(k, m):
    return sum(bin_weight(k, i) for i in range(m + 1))

def exact_success(k, bins, m):
    coeff = [1]
    for i in bins:
        nxt = [0] * (len(coeff) + 1)
        for j, z in enumerate(coeff):
            nxt[j] += z * (k - i)
            nxt[j+1] += z * i
        coeff = nxt
    return Fraction(coeff[m], k ** len(bins))

def count_valid(k, w, target, epsilon, n):
    states = {}
    for b in product(range(k+1), repeat=w-1):
        weight = 1
        for i in b:
            weight *= bin_weight(k, i)
        states[b] = weight
    for _ in range(w-1, n):
        updated = defaultdict(int)
        for b, mass in states.items():
            for j in range(k+1):
                if exact_success(k, b+(j,), target) >= 1-epsilon:
                    updated[b[1:]+(j,)] += mass * bin_weight(k, j)
        states = updated
    return sum(states.values())

def check():
    total = 0
    for k in range(2,6):
        for w in range(3,6):
            for m in range(1,w):
                tolerances = (Fraction(0), Fraction(1,2*k), Fraction(1,k), Fraction(1,3*(w+1)))
                for eps in tolerances:
                    if not 0 <= eps < Fraction(1,w+1):
                        continue
                    a = W(k, k*eps.numerator // (w*eps.denominator))
                    b = W(k, k*eps.numerator // eps.denominator)
                    for n in (w,w+1,w+2):
                        actual = count_valid(k,w,m,eps,n)
                        assert a**n <= actual <= comb(w,m)*b**n, (k,w,m,eps,n,actual)
                        if eps == 0:
                            assert actual == comb(w,m)*(k+1)**n
                        if eps < Fraction(1,k):
                            assert actual == comb(w,m)*(k+1)**n
                        total += 1
    print('all exact finite-length bounds and zero-tolerance counts verified')
    print('checked_cases:',total)
    print('sample:', [(k,w,m,str(eps),count_valid(k,w,m,eps,w+1)) for k,w,m,eps in [(3,3,1,Fraction(0)),(4,4,2,Fraction(1,8)),(5,5,2,Fraction(1,10))]])
    print('VERIFY_OK')

if __name__=='__main__':
    check()

def threshold_count_formula(k, w, m, n):
    total = (k+1)**n
    for j in range(1, (n+w-1)//w+1):
        available = n-(w-1)*(j-1)
        if available >= j:
            total += comb(available,j) * (2*k)**j * (k+1)**(n-j)
    return comb(w,m)*total

def check_onset():
    total=0
    for k in range(3,7):
        for w in range(3,7):
            for m in range(1,w):
                for n in (w,w+1,w+3):
                    observed = count_valid(k,w,m,Fraction(1,k),n)
                    expected = threshold_count_formula(k,w,m,n)
                    assert observed == expected,(k,w,m,n,observed,expected)
                    total += 1
    print('onset_exact_cases:',total)
    print('threshold_example:',threshold_count_formula(4,4,2,6))
    print('ONSET_VERIFY_OK')

if __name__ == '__main__':
    check_onset()
