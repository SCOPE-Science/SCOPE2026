"""Standalone finite verification of circular 2-universality necklace formulas.

Run: python checker.py
Pure Python 3, no dependencies.
"""
from collections import Counter
from math import factorial
from itertools import product


def multiset_words(q):
    cnt = [2] * q
    w = [0] * (2*q)
    def walk(i):
        if i == 2*q:
            yield tuple(w)
        else:
            for a in range(q):
                if cnt[a]:
                    cnt[a] -= 1
                    w[i] = a
                    yield from walk(i+1)
                    cnt[a] += 1
    yield from walk(0)


def index_by_arches(w, q):
    seen = set()
    count = 0
    for a in w:
        seen.add(a)
        if len(seen) == q:
            count += 1
            seen.clear()
    return count


def universal_by_subsequences(w, q):
    # direct check of the q^2 length-two patterns
    pairs = set()
    for i, a in enumerate(w):
        for b in w[i+1:]:
            pairs.add((a,b))
    return len(pairs) == q*q


def phases(w,q):
    n=2*q
    return [s for s in range(n) if index_by_arches(w[s:]+w[:s],q) >= 2]


def necklace(w):
    return min(w[i:]+w[:i] for i in range(len(w)))


def decompositions(q):
    # c_n indecomposable permutations; a_{n,b} b direct-sum components.
    c=[0]*(q+1)
    a=[[0]*(q+1) for _ in range(q+1)]
    a[0][0]=1
    for n in range(1,q+1):
        c[n] = factorial(n)-sum(c[j]*factorial(n-j) for j in range(1,n))
        for b in range(1,n+1):
            a[n][b] = sum(c[j]*a[n-j][b-1] for j in range(1,n+1))
    return a[q]


def predicted(q):
    a=decompositions(q)
    labeled={b:factorial(q)*q*a[b]//b for b in range(1,q+1)}
    necklaces={b:(factorial(q)*a[b]//(2*b) if b<q else factorial(q-1))
               for b in range(1,q+1)}
    assert all((factorial(q)*q*a[b]) % b == 0 for b in range(1,q+1))
    assert all((factorial(q)*a[b]) % (2*b) == 0 for b in range(1,q))
    return labeled,necklaces


def main():
    words_tested=0
    for q in range(2,6):
        labeled=Counter()
        necklaces={}
        for w in multiset_words(q):
            words_tested += 1
            starts=phases(w,q)
            if q<=4:
                assert (len(starts)>0)==any(universal_by_subsequences(w[s:]+w[:s],q)
                                                  for s in range(2*q))
            if starts:
                assert len(starts) % 2 == 0
                b=len(starts)//2
                labeled[b]+=1
                key=necklace(w)
                assert key not in necklaces or necklaces[key] == b
                necklaces[key]=b
        orb=Counter(necklaces.values())
        pred_l,pred_n=predicted(q)
        assert dict(labeled)==pred_l,(q,labeled,pred_l)
        assert dict(orb)==pred_n,(q,orb,pred_n)
        print('q=',q,'labeled=',sum(labeled.values()),'necklaces=',len(necklaces),
              'by_cut_pairs=',dict(sorted(orb.items())))
    print('CIRCULAR_PERMUTATION_ARCH_PASS words=',words_tested)


if __name__=='__main__':
    main()
