"""Exact finite checks for the finite-chain IS4 endpoint-reconstruction theorem.
Usage: python verify_is4_profiles.py
Only standard-library modules are used.
"""
from collections import Counter
from itertools import product


def is_closure(f):
    n = len(f)
    return (all(f[i] >= i and f[f[i]] == f[i] for i in range(n))
            and all(f[i] <= f[i+1] for i in range(n-1)))


def closure_maps(n):
    return [f for f in product(range(n), repeat=n) if is_closure(f)]


def transitive_closure(rows, n):
    rows = list(rows)
    for k in range(n):
        for i in range(n):
            if rows[i] >> k & 1:
                rows[i] |= rows[k]
    return tuple(rows)


def transitive(rows, n):
    return all((rows[j] & ~rows[i]) == 0
               for i in range(n) for j in range(n) if rows[i] >> j & 1)


def frame_conditions_literal(rows, n):
    # Test the original quantified witnesses without using row/column maxima.
    reflexive = all(rows[i] >> i & 1 for i in range(n))
    trans = transitive(rows, n)
    forth_up = all(any(rows[ip] >> jp & 1 for jp in range(j,n))
                   for i in range(n) for ip in range(i,n)
                   for j in range(n) if rows[i] >> j & 1)
    back_up = all(any(rows[ip] >> jp & 1 for ip in range(i,n))
                  for i in range(n) for j in range(n)
                  if rows[i] >> j & 1 for jp in range(j,n))
    return reflexive and trans and forth_up and back_up


def maxima(rows,n):
    h = tuple(r.bit_length()-1 for r in rows)
    b = tuple(max(i for i in range(n) if rows[i] >> j & 1)
              for j in range(n))
    return h,b


def endpoints(h,b):
    n=len(h)
    gen=[(1<<i)|(1<<h[i]) for i in range(n)]
    for j in range(n):
        gen[b[j]] |= 1 << j
    lo = transitive_closure(gen,n)
    hi = tuple(sum(1<<j for j in range(n)
                   if j<=h[i] and i<=b[j]) for i in range(n))
    return lo,hi


def local_unique(h,b):
    n=len(h)
    H = [h[t] > t for t in range(n-1)]
    B = [b[t] > t for t in range(n-1)]
    return all(not(H[t-1] and H[t] and not B[t])
               and not(B[t-1] and B[t] and not H[t])
               for t in range(1,n-1))


def subrelations(lo,hi,n):
    optional=[(i,j) for i in range(n) for j in range(n)
              if ((hi[i]>>j)&1) and not ((lo[i]>>j)&1)]
    for bits in range(1<<len(optional)):
        r=list(lo)
        for k,(i,j) in enumerate(optional):
            if bits>>k&1:
                r[i]|=1<<j
        yield tuple(r)


def verify():
    # Route A: literal direct enumeration, independent of any endpoint lemma.
    direct=[]
    for n in range(1,5):
        count=0
        rows_choices=[[mask for mask in range(1<<n) if (mask>>i)&1]
                      for i in range(n)]
        for rows in product(*rows_choices):
            if frame_conditions_literal(rows,n):
                count+=1
                h,b=maxima(rows,n)
                assert is_closure(h) and is_closure(b)
                lo,hi=endpoints(h,b)
                assert all((lo[i]&~rows[i])==0 and (rows[i]&~hi[i])==0
                           for i in range(n))
        direct.append(count)
    assert direct==[1,4,20,126],direct

    # Route B: independently enumerate all closure-map pairs; validate the
    # constructions and every local uniqueness criterion through eight worlds.
    for n in range(1,9):
        maps=closure_maps(n)
        assert len(maps)==2**(n-1)
        unique=0
        possible=0
        interval_count=0
        for h in maps:
            for b in maps:
                lo,hi=endpoints(h,b)
                assert transitive(lo,n) and transitive(hi,n)
                assert maxima(lo,n)==(h,b)==maxima(hi,n)
                assert frame_conditions_literal(lo,n)
                assert frame_conditions_literal(hi,n)
                assert all(lo[i]&~hi[i]==0 for i in range(n))
                assert (lo==hi)==local_unique(h,b)
                unique+=lo==hi
                possible+=1
                if n<=6:
                    for rows in subrelations(lo,hi,n):
                        if transitive(rows,n):
                            interval_count+=1
                            assert maxima(rows,n)==(h,b)
                            assert frame_conditions_literal(rows,n)
        predicted=1 if n==1 else 4*(3**(n-2))
        assert unique==predicted,(n,unique,predicted)
        assert possible==4**(n-1)
        if n<=4:
            assert interval_count==direct[n-1]
        print('n',n,'profiles',possible,'uniquely_determined',unique,
              'total_IS4_relations',interval_count if n<=6 else 'not enumerated')
    print('VERIFY_OK')

if __name__=='__main__':
    verify()
