"""Graph-level independent verification of the LTD polynomial of K_n square K_2.
No use of the proof's column-status classification in the validity oracle.
"""
from collections import Counter
from math import comb
from itertools import combinations


def neighbors(n):
    return tuple(sum((1 << v) for v in range(2*n)
                     if (u%n == v%n and u//n != v//n)
                     or (u//n == v//n and u%n != v%n))
                 for u in range(2*n))


def valid(S, N):
    seen = set()
    for v, adj in enumerate(N):
        c = adj & S
        if c == 0:
            return False
        if S & (1<<v) == 0:
            if c in seen:
                return False
            seen.add(c)
    return True


def coeffs(n):
    if n == 2:
        return Counter({2:4,3:4,4:1})
    # [t^k] t^n(2+t)^n+n t^(n-1)(2+t)^(n-1)-2n t^n-2n^2 t^(n-1)
    c=Counter()
    for j in range(n+1):
        c[n+j] += comb(n,j)*2**(n-j)
    for j in range(n):
        c[n-1+j] += n*comb(n-1,j)*2**(n-1-j)
    c[n] -= 2*n
    c[n-1] -= 2*n*n
    if n==3:
        c[2] += 6
    return Counter({k:v for k,v in c.items() if v})


def test():
    for n in range(2,11):
        N=neighbors(n)
        cnt=Counter()
        for mask in range(1<<(2*n)):
            if valid(mask,N):
                cnt[mask.bit_count()]+=1
        want=coeffs(n)
        assert cnt==want,(n,cnt,want)
        print('n',n,'total',sum(cnt.values()),'min',min(cnt),cnt[min(cnt)],flush=True)
    print('VERIFY_OK: 2^2n full graph-level subsets for n=2..10 match all coefficients')

if __name__=='__main__': test()
