#!/usr/bin/env python3
from itertools import combinations
from collections import Counter


def v2_mod(x, m):
    N = 1 << m
    x %= N
    assert x != 0
    r = 0
    while x % 2 == 0:
        r += 1
        x //= 2
    return r


def matchings(A):
    a,b,c,d = A
    return [((a,b),(c,d)), ((a,c),(b,d)), ((a,d),(b,c))]


def B_of(A, m):
    B = set()
    for (a,b),(c,d) in matchings(A):
        r1 = v2_mod(a-b, m)
        r2 = v2_mod(c-d, m)
        if r1 == r2:
            B.add(r1)
    return B


def predicted_zero_set(A, m):
    N = 1 << m
    out = set()
    for r in B_of(A,m):
        j = m - 1 - r
        for k in range(1,N):
            if v2_mod(k,m) == j:
                out.add(k)
    return out


def cyclotomic_zero(A, k, m):
    # Phi_{2^m}(X)=X^(N/2)+1. Reduce sum X^(ka) exactly.
    N = 1 << m
    h = N >> 1
    coeff = [0] * h
    for a in A:
        e = (k*a) % N
        if e >= h:
            coeff[e-h] -= 1
        else:
            coeff[e] += 1
    return all(c == 0 for c in coeff)


def direct_zero_set(A,m):
    N=1<<m
    return {k for k in range(N) if cyclotomic_zero(A,k,m)}


def allowed_B(B,m):
    if not B:
        return True
    s=sorted(B)
    if len(s)==1:
        return 0 <= s[0] <= m-3
    if len(s)==2:
        return 0 <= s[0] < s[1] <= m-1
    return False


def exhaust(m):
    N=1<<m
    bc=Counter(); zc=Counter(); total=0
    for A in combinations(range(N),4):
        A=tuple(A); total += 1
        B=B_of(A,m)
        assert allowed_B(B,m), (m,A,B)
        pred=predicted_zero_set(A,m)
        direct=direct_zero_set(A,m)
        assert pred == direct, (m,A,B,pred,direct)
        bc[tuple(sorted(B))]+=1
        zc[len(direct)]+=1
    allowed=set()
    allowed.add(())
    for r in range(0,m-2): allowed.add((r,))
    for r in range(m):
        for s in range(r+1,m): allowed.add((r,s))
    assert set(bc)==allowed, (m,set(bc),allowed)
    return total, bc, zc


def witnesses(m):
    N=1<<m
    A=(0,1,2,4)
    assert B_of(A,m)==set()
    assert direct_zero_set(A,m)==predicted_zero_set(A,m)
    for r in range(0,m-2):
        A=(0,1<<(r+1),1<<r,(1<<r)+(1<<(r+2)))
        assert len(set(x%N for x in A))==4
        assert B_of(A,m)=={r}, (m,r,A,B_of(A,m))
        assert direct_zero_set(A,m)==predicted_zero_set(A,m)
    for r in range(m):
        for s in range(r+1,m):
            A=(0,1<<s,1<<r,(1<<r)+(1<<s))
            assert len(set(x%N for x in A))==4
            assert B_of(A,m)=={r,s}, (m,r,s,A,B_of(A,m))
            assert direct_zero_set(A,m)==predicted_zero_set(A,m)


def main():
    expected = {
      3: {0:32,1:16,3:16,5:4,6:2},
      4: {0:960,1:448,2:32,3:256,5:64,6:32,9:16,10:8,12:4},
      5: {0:19840,1:8960,2:896,3:4096,4:64,5:1024,6:512,9:256,10:128,12:64,17:64,18:32,20:16,24:8},
    }
    grand=0
    for m in (3,4,5):
        total,bc,zc=exhaust(m); grand += total
        assert dict(sorted(zc.items())) == expected[m]
        print('m=',m,'N=',1<<m,'subsets=',total,'zero_count_distribution=',dict(sorted(zc.items())))
    for m in range(3,10):
        witnesses(m)
    print('exhaustive_subsets=',grand)
    print('witness_levels_checked_through_m=9')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
