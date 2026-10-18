"""Independent finite checks of exact rotational 2-binomial statistics.
Run: python3 rotation_checker.py. Python standard library only.
Finite tests support, but do not replace, the all-parameter combinatorial proof.
"""
from math import comb, gcd
from fractions import Fraction
from itertools import combinations
from collections import Counter


def signature_direct(word):
    n = len(word)
    singles = [0, 0]
    pairs = [[0, 0], [0, 0]]
    for i in range(n):
        singles[word[i]] += 1
        for j in range(i+1, n):
            pairs[word[i]][word[j]] += 1
    return tuple(singles)+tuple(v for row in pairs for v in row)


def rotations(word):
    return [word[i:]+word[:i] for i in range(len(word))]


def exact_expectation(n, k):
    g = gcd(n, k)
    L = n // g
    K = k // g
    total = Fraction(0)
    for mask in range(1, 1 << g):
        ts = [i for i in range(g) if (mask >> i) & 1]
        r = len(ts)
        gaps = [ts[(j+1) % r] - ts[j] if j+1 < r else g + ts[0] - ts[-1] for j in range(r)]
        numerator = 1
        for d in gaps:
            numerator *= comb(d*L, d*K)
        total += (-1)**(r+1)*Fraction(numerator, comb(n,k))
    return L*total


def empirical(n,k):
    total=0
    L=n//gcd(n,k)
    saw=0
    expected_multiplicity = Counter()
    for ix in combinations(range(n),k):
        w=[0]*n
        for j in ix:w[j]=1
        rr=rotations(w)
        sigs=[signature_direct(x) for x in rr]
        moments=[sum(j*x for j,x in enumerate(t)) for t in rr]
        assert all((sigs[i]==sigs[j])==(moments[i]==moments[j]) for i in range(n) for j in range(n))
        observed=len(set(sigs))
        assert observed>=L
        assert (observed==L)==all(w[i]==w[(i+L)%n] for i in range(n))
        if gcd(n,k)==1:assert observed==n
        total+=observed
        saw+=1
        if gcd(n,k) in (2,3):
            cnt=Counter(moments)
            for m in cnt.values():expected_multiplicity[m]+=1
    return Fraction(total,saw),expected_multiplicity


def check_all():
    cases=words=0
    for n in range(2,13):
        for k in range(1,n):
            observed,multiplicity=empirical(n,k)
            predicted=exact_expectation(n,k)
            assert observed==predicted,(n,k,observed,predicted)
            g=gcd(n,k);L=n//g;K=k//g
            if g==2:
                p=Fraction(comb(L,K)**2,comb(n,k))
                assert predicted==n-L*p
                assert Fraction(multiplicity[2],comb(n,k))==L*p
            if g==3:
                p=Fraction(comb(L,K)*comb(2*L,2*K),comb(n,k))
                q=Fraction(comb(L,K)**3,comb(n,k))
                assert predicted==n-3*L*p+L*q
                assert Fraction(multiplicity[3],comb(n,k))==L*q
                assert Fraction(multiplicity[2],comb(n,k))==3*L*(p-q)
                assert Fraction(multiplicity[1],comb(n,k))==3*L*(1-2*p+q)
            cases+=1;words+=comb(n,k)
    print('PASS_EXACT_ALL_BOUNDARY', 'pairs_nk',cases,'words',words,'n_range=2..12', 'gcd2_3_multiplicities=verified')


if __name__=='__main__':check_all()
