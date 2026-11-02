#!/usr/bin/env python3
"""Independent finite checks for periodic palindromic-prefix and shortest
palindromic-factorization statements. Checks are not infinite proofs."""
from itertools import product
from collections import Counter


def primitive(period):
    p = len(period)
    return all(period != period[:d] * (p//d) for d in range(1,p) if p % d == 0)


def calculate(period, n):
    p = len(period)
    word = (period * ((n+p-1)//p))[:n]
    # palindromicity for all factors, by the standard interior recurrence
    pal = [bytearray(n) for _ in range(n)]
    for i in range(n):
        pal[i][i] = 1
    for i in range(n-1):
        pal[i][i+1] = (word[i] == word[i+1])
    for length in range(3,n+1):
        for i in range(n-length+1):
            pal[i][i+length-1] = (word[i] == word[i+length-1] and pal[i+1][i+length-2])
    pl = [0]*(n+1)
    for j in range(1,n+1):
        pl[j] = 1 + min(pl[i] for i in range(j) if pal[i][j-1])
    palpref = [j for j in range(1,n+1) if pal[0][j-1]]
    return pl,palpref


def run():
    count=0; p_tests=0; small_profile=[]
    for q,pmax in ((2,9),(3,6)):
        for p in range(2,pmax+1):
            sample=[]; rhos=[]
            for tup in product(range(q), repeat=p):
                period=tuple(tup)
                if not primitive(period):
                    continue
                n=2*p*p+2*p+2
                pl,palp=calculate(period,n)
                if not any(z>=p for z in palp):
                    continue
                r=palp[-1]%p
                assert all((j in palp) == (j%p==r) for j in range(p,n+1)), (period,palp)
                assert all(pl[j]==pl[j+p] for j in range(p*(p-1)+1,n-p+1)), (period,p,pl)
                assert max(pl)<=p, (period,p,pl)
                M=max(pl)
                classes={j%p for j in range(p*(p-1)+1,p*p+1) if pl[j]==M}
                assert 1<=len(classes)<=p-1, (period,p,classes)
                if q==2:
                    rhos.append(len(classes))
                count+=1
            if q==2:
                small_profile.append((p,sorted(set(rhos)),len(rhos)))
            p_tests+=1
    for p in range(2,40):
        for r in range(1,p):
            s=p-r
            # asymmetric alpha/beta runs; direct period pattern at many n
            per=(0,)*r+(1,)*s
            n=3*p+4
            pl,pre=calculate(per,n)
            assert all(pl[j]==(1 if (j<=r or (j>=r and (j-r)%p==0)) else 2) for j in range(1,n+1)), (p,r,pl)
    print('PASS: all periodic-palindrome-prefix examples across primitive binary periods 2..9 and ternary periods 2..6')
    print('Number of primitive palindromic-period test instances:',count)
    print('PASS: effective period cutoff n >= p(p-1)+1, unique palindrome-prefix residue, global prefix bound, and integer ratio range')
    print('Observed ratios and counts by binary primitive period:')
    for x in small_profile: print(' ',x)
    print('PASS: exact two-run-word palindromic-length profile for periods 2..39 and all splits')
if __name__=='__main__':
    run()
