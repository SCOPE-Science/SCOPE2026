#!/usr/bin/env python3
"""Two finite checks for closed-neighborhood balanced binary colorings.
Run with Python 3.9+; no nonstandard dependencies.
"""
from itertools import product
from math import comb


def expected(m, n):
    assert m >= 2 and m % 2 == 0 and n >= 3
    if m == 2:
        return 2 + (4 if n % 4 == 0 else 0) if n % 2 == 0 else 0
    return comb(m, m // 2)**2 if n % 4 == 0 else 0


def valid(m, n, bits):
    """Test every actual closed neighborhood without using the recurrence."""
    for j in range(n):
        for a in range(m):
            pos = j*m+a
            total = sum((bits >> (j*m+b)) & 1 for b in range(m))
            total += (bits >> (((j-1) % n)*m+a)) & 1
            total += (bits >> (((j+1) % n)*m+a)) & 1
            if total * 2 != m + 2:
                return False
    return True


def brute_count(m, n):
    return sum(valid(m,n,b) for b in range(1 << (m*n)))


def seed_count(m,n):
    """Construct all cyclic solutions from the first two columns.
    This uses local constraints but not the structural classification.
    """
    ans = 0
    for u in range(1 << m):
        for v in range(1 << m):
            cols = [u,v]
            for j in range(1,n+1):
                prev,mid = cols[j-1:j+1]
                colsum = mid.bit_count()
                nextmask = 0
                okay = True
                for a in range(m):
                    prevbit = (prev >> a)&1
                    # closed neighborhood has m column vertices and two lateral vertices
                    nextbit = (m + 2)//2-colsum-prevbit
                    if nextbit not in (0,1):
                        okay=False
                        break
                    nextmask |= nextbit << a
                if not okay:break
                cols.append(nextmask)
            if okay and cols[n]==cols[0] and cols[n+1]==cols[1]:
                ans +=1
    return ans


def main():
    bcases=[(2,n) for n in range(3,9)] + [(4,n) for n in range(3,6)] + [(6,3)]
    for m,n in bcases:
        cnt=brute_count(m,n)
        assert cnt==expected(m,n),(m,n,cnt,expected(m,n))
        print('BRUTE',m,n,cnt)
    scases=[(m,n) for m in (2,4,6,8) for n in range(3,13)]
    for m,n in scases:
        cnt=seed_count(m,n)
        assert cnt==expected(m,n),(m,n,cnt,expected(m,n))
        print('SEEDS',m,n,cnt)
    print('VERIFY_OK',len(bcases),'direct brute-force graphs;',len(scases),'cyclic seed cases')

if __name__=='__main__':
    main()
