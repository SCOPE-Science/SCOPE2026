"""Independent finite checks for the four-run complementary-factor theorem.

Run with Python 3 (standard library only). These are finite checks, not
substitutes for the case-analysis and extremal inequality proofs.
"""
from itertools import product


def factor_spectrum(word):
    fac = {word[i:j] for i in range(len(word)) for j in range(i+1, len(word)+1)}
    return {r: sum((s.translate(str.maketrans('01', '10')) in fac)
                   for s in fac if len(s) == r)
            for r in range(1, len(word)+1)}


def formula(a,b,c,d):
    m = min(max(a,c),max(b,d))
    alpha = min(a,b)
    beta = min(b,c)
    gamma = min(c,d)
    overlap = min(a,b,c) * min(b,c,d)
    triple = min(a,b)*min(c,d) if b == c else 0
    return 2*(m + alpha*beta + beta*gamma - overlap + triple)


def spectrum_formula(a,b,c,d):
    n = a+b+c+d
    v = [0]*(n+1)
    m = min(max(a,c),max(b,d))
    for h in range(1,m+1):
        v[h] += 2
    # A two-run factor 0^i1^j and its complement 1^i0^j.
    for i in range(1,b+1):
        for j in range(1,c+1):
            if (i <= a and j <= b) or (i <= c and j <= d):
                v[i+j] += 2
    if b == c:
        for i in range(1,min(a,b)+1):
            for j in range(1,min(c,d)+1):
                v[i+b+j] += 2
    return {r:v[r] for r in range(1,n+1)}


def sharp_max(n):
    if n == 5:
        return 6
    t = (n+3)//4
    return 2*t*(n-2*t+1)


def run():
    count = 0
    for a,b,c,d in product(range(1,8), repeat=4):
        w = '0'*a+'1'*b+'0'*c+'1'*d
        direct = factor_spectrum(w)
        expected = spectrum_formula(a,b,c,d)
        assert direct == expected, (a,b,c,d,direct,expected)
        assert sum(expected.values()) == formula(a,b,c,d)
        count += 1

    max_checked = 0
    for n in range(4,65):
        best = -1
        optimizers = []
        for a in range(1,n-2):
            for b in range(1,n-a-1):
                for c in range(1,n-a-b):
                    d = n-a-b-c
                    k = formula(a,b,c,d)
                    if k > best:
                        best = k
                        optimizers = [(a,b,c,d)]
                    elif k == best:
                        optimizers.append((a,b,c,d))
        assert best == sharp_max(n), (n,best,sharp_max(n))
        if n >= 6:
            t=(n+3)//4
            expected = [(a,t,t,n-2*t-a) for a in range(1,n-2*t)
                        if a <= t and 1 <= n-2*t-a <= t]
            assert sorted(optimizers) == sorted(expected), (n,optimizers,expected)
        if n == 4:
            assert optimizers == [(1,1,1,1)]
        if n == 5:
            assert sorted(optimizers) == [(1,1,1,2),(2,1,1,1)]
        max_checked += 1
    print(f'VERIFY_OK exhaustive_length_spectra={count} extremal_lengths=4..64 ({max_checked})')


if __name__=='__main__':
    run()
