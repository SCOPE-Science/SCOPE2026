"""Self-contained exact arithmetic checks for circular binary 2-binomial profiles.

Run: python3 checker.py
This is a finite diagnostic; the written proof establishes the universal claims.
"""
from itertools import product, combinations
from math import gcd


def count_01(s):
    zeros = total = 0
    for a in s:
        if a == '0':
            zeros += 1
        else:
            total += zeros
    return total


def count_all_scattered_pairs(s):
    ans = {a+b:0 for a in '01' for b in '01'}
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            ans[s[i]+s[j]] += 1
    return tuple(ans[t] for t in ('00','01','10','11'))


def heights(s):
    p=s.count('0'); q=s.count('1')
    h=0; out=[]
    for a in s:
        out.append(h)
        h+= p if a=='1' else -q
    assert h==0
    return out


def orbit_profiles(s):
    return [count_all_scattered_pairs(s[i:]+s[:i]) for i in range(len(s))]


def brute_all_lengths():
    nwords=0
    for N in range(2,15):
        possible={}
        for v in product('01',repeat=N):
            s=''.join(v)
            p=s.count('0');q=N-p
            if p==0 or q==0:continue
            nwords+=1
            d=gcd(p,q); L=N//d
            hh=heights(s)
            C=len(set(hh))
            # Independent evaluation of every length-two scattered subword.
            direct=len(set(orbit_profiles(s)))
            assert C==direct,(s,C,direct)
            assert L<=C<=N-d+1,(s,C,L,N-d+1)
            # Minimum exact characterization.
            assert (C==L)==(s==s[:L]*d),(s,C,L,d)
            # Equal profiles iff every intervening circular arc is balanced.
            for i in range(N):
                for j in range(i+1,N):
                    length=j-i
                    segment=(s+s)[i:j]
                    equivalent=(hh[i]==hh[j])
                    balanced=(segment.count('1')*N==length*q)
                    assert equivalent==balanced,(s,i,j)
            possible.setdefault((p,q),set()).add(C)
        for (p,q),found in possible.items():
            d=gcd(p,q);N=p+q
            assert found==set(range(N//d,N-d+2)),(p,q,found)
    return nwords


def construction_and_bound_large():
    for p in range(1,100):
        for q in range(1,100):
            d=gcd(p,q); N=p+q;L=N//d
            a=('0'* (p//d)+'1'*(q//d))*d
            b='0'*p+'1'*q
            assert len(set(heights(a)))==L,(p,q)
            assert len(set(heights(b)))==N-d+1,(p,q)
            for w in (a,b):
                xs=[(w+w)[i:i+L].count('1') for i in range(N)]
                assert q//d in xs,(p,q)
    return 99*99


if __name__=='__main__':
    a=brute_all_lengths()
    b=construction_and_bound_large()
    print('PASS: exhaustive mixed binary words lengths 2..14:', a)
    print('PASS: fixed-content extremizers and balanced arcs for count pairs:', b)
    print('Proof, not these finite checks, establishes unbounded lengths.')
