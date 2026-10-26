"""Independent finite checks for Bernoulli convolution on finite-chain contractions.
No third-party libraries. Run: python verify_random_contractions.py
"""
from fractions import Fraction
from itertools import product
from collections import Counter
from math import comb


def maps(n):
    return [(1,) + tuple(1 + sum(bits[:i]) for i in range(1,n))
            for bits in product((0, 1), repeat=n-1)]


def from_bits(bits):
    v=[1]
    for x in bits: v.append(v[-1]+x)
    return tuple(v)


def all_maps(n):
    return [from_bits(b) for b in product((0,1),repeat=n-1)]


def compose(f,g):
    # First apply g, then f; both are tuples of images.
    return tuple(f[x-1] for x in g)


def rank(f):
    return f[-1]


def increments(f):
    return [f[i+1]-f[i] for i in range(len(f)-1)]


def mu(f,p):
    m=sum(increments(f))
    return p**m*(1-p)**(len(f)-1-m)


def check_pair(n,p,q):
    fam=all_maps(n)
    observed={f:Fraction(0) for f in fam}
    for f in fam:
        wf=mu(f,p)
        if not wf: continue
        for g in fam:
            wg=mu(g,q)
            if wg: observed[compose(f,g)]+=wf*wg
    for h in fam:
        assert observed[h]==mu(h,p*q), (n,p,q,h,observed[h],mu(h,p*q))
    assert sum(observed.values())==1


def check_words(n,k):
    fam=all_maps(n)
    cnt=Counter()
    cnt[tuple(range(1,n+1))]=1
    for _ in range(k):
        nxt=Counter()
        for h,count in cnt.items():
            for f in fam:nxt[compose(f,h)]+=count
        cnt=nxt
    assert sum(cnt.values()) == len(fam)**k
    for h in fam:
        r=rank(h)
        assert cnt[h] == (2**k-1)**(n-r), (n,k,h,cnt[h])
        # The probability is ((1/2^k)^(r-1))*((1-1/2^k)^(n-r)).
    for r in range(1,n+1):
        assert sum(c for h,c in cnt.items() if rank(h)==r)==comb(n-1,r-1)*(2**k-1)**(n-r)


def main():
    for n in range(1,8):
        fam=all_maps(n)
        assert len(fam)==2**(n-1)
        for f in fam:
            assert all(1<=f[i]<=i+1 for i in range(n))
            assert all(0<=d<=1 for d in increments(f))
    for n in range(1,7):
        for p,q in [(Fraction(1,3),Fraction(2,5)),(Fraction(1,2),Fraction(1,2)),
                    (Fraction(0),Fraction(3,4)),(Fraction(1),Fraction(4,5))]:
            check_pair(n,p,q)
    for n in range(2,7):
        for k in range(1,4):check_words(n,k)
    for n in range(2,6):check_words(n,4)
    for n in (10,50,100):
        for k in (1,2,5,11):
            p=Fraction(1,2**k)
            total=sum(comb(n-1,r-1)*p**(r-1)*(1-p)**(n-r) for r in range(1,n+1))
            assert total==1
            assert (1-p)**(n-1)==(1-Fraction(1,2**k))**(n-1)
    print('VERIFY_OK_BERNOULLI_CONVOLUTION_CONTRACTIONS')

if __name__=='__main__':main()
