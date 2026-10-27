#!/usr/bin/env python3
"""Exact rational-function certificate and independent finite parity DP for fan strong-odd colorings."""
from collections import defaultdict
from itertools import permutations
from math import comb


def trim(p):
    p = list(p)
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def neg(a):
    return [-x for x in a]


def sub(a, b):
    return add(a, neg(b))


def scale(a, c):
    return trim([x*c for x in a])


def mul(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def prod(ls):
    p = [1]
    for q in ls:
        p = mul(p, q)
    return p


def powp(a, n):
    return prod([a]*n)


def det4(A):
    ans = [0]
    for perm in permutations(range(4)):
        inversions = sum(perm[i] > perm[j] for i in range(4) for j in range(i+1, 4))
        term = prod([A[i][perm[i]] for i in range(4)])
        ans = add(ans, scale(term, -1 if inversions % 2 else 1))
    return ans


ROLES = [(0,0), (0,1), (1,0), (1,1)]


def signed_word_rational(a, b):
    size = [a, b]
    sign = [1, -1]
    v = [sign[g]*sign[h]*size[g]*(size[h]-(g == h)) for g,h in ROLES]
    M = [[0]*4 for _ in range(4)]
    for i, (g, h) in enumerate(ROLES):
        for u in (0,1):
            j = ROLES.index((h,u))
            M[i][j] += sign[u]*(size[u]-(g == u)-(h == u))
    A = [[[int(i==j), -M[i][j]] for j in range(4)] for i in range(4)]
    B = [[add(A[i][j], [v[j]]) for j in range(4)] for i in range(4)]
    d = det4(A)
    nn = mul([0,0,1], sub(det4(B),d))
    return nn, d


def expected_rational(k):
    if k==3:
        return [0,0,0,6], [1,0,0,0,0,0,-1]
    if k==4:
        numerator = mul([0,0,0,0,24], powp([1,0,-2],2))
        den = prod([[1,0,-4], sub([1], powp([0,-1,0,4],2)), [1,0,1,0,-4]])
        return numerator, den
    numerator = mul([0,0,0,0,0,120],powp([1,0,-3],3))
    den = prod([[1,0,-9], sub([1],powp([0,-2,0,9],2)),
                sub(powp([1,0,2,0,-9],2),powp([0,1,0,-3],2))])
    return numerator, den


def verify_exact_identity(k):
    fractions = [signed_word_rational(k-b,b) for b in range(k+1)]
    full_den = prod([d for _,d in fractions])
    full_num = [0]
    for b, (num, den) in enumerate(fractions):
        numerator = mul(num,prod([d for j,(_,d) in enumerate(fractions) if j!=b]))
        full_num = add(full_num,scale(numerator,(-1)**b*comb(k,b)))
    expected_num, expected_den = expected_rational(k)
    assert mul(full_num,expected_den) == mul(scale(full_den,2**k),expected_num),k


def rational_coeff(num, den, maxn):
    assert den[0] == 1
    cf=[]
    for n in range(maxn+1):
        rhs = num[n] if n<len(num) else 0
        rhs -= sum(den[j]*cf[n-j] for j in range(1,min(len(den),n+1)))
        cf.append(rhs)
    return cf


def dp_coeff(n,k):
    dp={(-1,-1,0):1}
    for _ in range(n):
        new=defaultdict(int)
        for (p,pp,mask), count in dp.items():
            for c in range(k):
                if c!=p and c!=pp:
                    new[c,p,mask^(1<<c)] += count
        dp=new
    return sum(count for (p,pp,mask),count in dp.items() if mask==(1<<k)-1)


def check_word(w):
    return (all(w[i]!=w[j] for i in range(len(w)) for j in range(i+1,min(len(w),i+3)))
            and all(w.count(c)%2 for c in set(w)))


def main():
    for k in (3,4,5):
        verify_exact_identity(k)
        num, den=expected_rational(k)
        cf=rational_coeff(num,den,25)
        for n in range(2,26):
            assert cf[n]==dp_coeff(n,k),(k,n,cf[n],dp_coeff(n,k))
        print('Exact 4-state rational identity and independent DP agree: k=',k)
    words={7:'0120340',8:'01201301',9:'012012012',
           10:'0120120123',11:'01201201234',12:'012013023123'}
    for n in range(7,43):
        b=7+(n-7)%6
        word='012012'*((n-b)//6)+words[b]
        assert len(word)==n and check_word(word)
        expected = 3 if n%6==3 else (4 if n%2==0 else 5)
        assert len(set(word))==expected
    print('All six construction templates and six-step extension: PASS')
    print('VERIFICATION_OK')


if __name__=='__main__':
    main()
