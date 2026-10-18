"""Exact-rational checks for the finite Lorentz centering identities.

This verifies finite instances only. The complete proof is given separately.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def lorentz_norm(x, w):
    return sum((a*b for a, b in zip(sorted(map(abs, x), reverse=True), w)), F(0))


def formula(n, w):
    W = [F(0)]
    for a in w:
        W.append(W[-1] + a)
    best = F(0)
    witness = None
    for k in range(1, n+1):
        for s in range(k//2+1):
            r = k-s
            d = F(r-s, n)
            if 2*d <= 1:
                numerator = ((1+d)*W[s]+(1-d)*(W[k]-W[s])+d*(W[n]-W[k]))
            else:
                numerator = ((1+d)*W[s]+d*(W[s+n-k]-W[s])+(1-d)*(W[n]-W[s+n-k]))
            ratio = numerator/W[k]
            if ratio > best:
                best, witness = ratio, (k,s)
    return best, witness


def direct(n, w):
    best = F(0)
    for x in product((-1,0,1), repeat=n):
        if all(a==0 for a in x):
            continue
        mean = F(sum(x), n)
        q = [F(a)-mean for a in x]
        best = max(best, lorentz_norm(q,w)/lorentz_norm(x,w))
    return best


def assert_main():
    rng = Random(203174)
    tests = 0
    for n in range(2, 8):
        for _ in range(12):
            w = sorted([F(rng.randrange(1,14),rng.randrange(1,9)) for i in range(n)], reverse=True)
            value, _ = formula(n,w)
            assert value == direct(n,w), (n,w,value,direct(n,w))
            if n==2:
                assert value==1
            if n==3:
                W=sum(w)
                expected=max((W+w[0])/(3*w[0]), 2*(W+w[0])/(3*W))
                assert value == expected
                assert (value == 1) == (W==2*w[0])
            if n>=4:
                assert value>1
            tests+=1
    for w in ([F(1),F(3,4),F(1,4)], [F(1),F(1,2),F(1,2)], [F(1),F(9,10),F(1,10)]):
        assert formula(3,w)[0]==1
    for n in (4,5,6,7,8,9,10):
        w = [F(1)] + [F(1,n-1)]*(n-1)
        assert formula(n,w)[0] > 1
    print(f'PASS: {tests} random rational-weight operator norms independently enumerated;')
    print('PASS: n=2 and n=3 exact closed forms; n>=4 strict gap in samples;')
    print('PASS: explicit n=3 contractive weights and critical total-weight families.')


if __name__ == '__main__':
    assert_main()
