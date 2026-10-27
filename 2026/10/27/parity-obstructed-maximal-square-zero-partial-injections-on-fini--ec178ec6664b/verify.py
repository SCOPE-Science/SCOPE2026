#!/usr/bin/env python3
"""Finite verification of square-zero partial injections preserving a fence and parity.

This uses the defining relations on the zig-zag poset directly, not the
successive-gap criterion used in the mathematical proof.
"""
from itertools import combinations
from collections import Counter

def below(x, y):
    """Strict order relation on the up-fence 1<2>3<4>... ."""
    return (x % 2 == 1 and abs(x-y) == 1)

def allowed(D, E):
    if len(D) != len(E) or any(x % 2 != y % 2 for x,y in zip(D,E)):
        return False
    p = dict(zip(D,E))
    inv = dict(zip(E,D))
    for a in D:
        for b in D:
            if below(a,b) and not below(p[a],p[b]):
                return False
    for a in E:
        for b in E:
            if below(a,b) and not below(inv[a],inv[b]):
                return False
    return True

def all_count(n):
    count = Counter()
    top_words=[]
    for k in range(1,n//2+1):
        for D in combinations(range(1,n+1), k):
            Dset=set(D)
            rem=[x for x in range(1,n+1) if x not in Dset]
            for E in combinations(rem,k):
                if allowed(D,E):
                    count[k]+=1
                    if 2*k == n:
                        top_words.append(''.join('0' if i in Dset else '1' for i in range(1,n+1)))
    return count, top_words

# Independent combinatorial prediction of the sharp range.
def top_rank(n):
    return n//2 - (n % 4 == 2)

def paired_run_words(k):
    res=set()
    for mask in range(1 << (k-1)):
        breaks=[i+1 for i in range(k-1) if mask >> i & 1]
        sizes=[b-a for a,b in zip([0]+breaks,breaks+[k])]
        for a,b in [("0","1"),("1","0")]:
            res.add(''.join(a*(2*i)+b*(2*i) for i in sizes))
    return res

if __name__ == '__main__':
    known={
      2:[1,0],3:[1,2],4:[1,4,2],5:[1,8,4],
      6:[1,12,10,0],7:[1,18,22,6],8:[1,24,46,24,4],
      9:[1,32,88,62,12],10:[1,40,156,152,42,0],
      11:[1,50,260,324,138,16],12:[1,60,410,672,394,88,8]
    }
    total=0
    for n in range(2,13):
        counts,words=all_count(n)
        row=[int(k==0)+counts[k] for k in range(n//2+1)]
        assert row==known[n], (n,row,known[n])
        assert max(j for j,v in enumerate(row) if v) == top_rank(n), n
        assert all(row[j]>0 for j in range(top_rank(n)+1)), n
        if n%4==0:
            assert set(words)==paired_run_words(n//4), (n,words,paired_run_words(n//4))
        total+=sum(row)
        print('n=%d histogram=%s' % (n,','.join(map(str,row))))
    # This is an additional independent full-size extremizer check.
    n=16
    extremal=[]
    for D in combinations(range(1,n+1),n//2):
        E=tuple(i for i in range(1,n+1) if i not in D)
        if allowed(D,E):
            ds=set(D)
            extremal.append(''.join('0' if i in ds else '1' for i in range(1,n+1)))
    assert set(extremal)==paired_run_words(4), (len(extremal),extremal)
    print('n=16 complementary extremizers=%d' % len(extremal))
    print('ALL_FENCE_SQUARE_ZERO_RANK_AND_EXTREMIZER_CHECKS_PASSED cases=11 total_square_zero=%d n16_top=16' % total)
