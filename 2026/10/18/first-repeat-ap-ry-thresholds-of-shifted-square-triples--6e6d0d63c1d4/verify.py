#!/usr/bin/env python3
"""Independent capped coin-change check of first-repeat thresholds."""

def predicted(a):
    out=[]
    for r in range(a):
        q,s=divmod(r,4)
        delta=a+1-3*(((r+a)//4)-(r//4))
        threshold=q+s+(delta if q==0 else min(3,delta))
        out.append(r+a*threshold)
    return out

def check(a):
    expected=predicted(a)
    limit=max(expected)
    cnt=[0]*(limit+1)
    cnt[0]=1
    for coin in (a,a+1,a+4):
        for n in range(coin,limit+1):
            cnt[n]=min(2,cnt[n]+cnt[n-coin])
    got=[None]*a
    for n in range(limit+1):
        if cnt[n]==2 and got[n%a] is None:
            got[n%a]=n
    assert got==expected, (a, [(r,got[r],expected[r]) for r in range(a) if got[r]!=expected[r]])
    return a,limit, len(expected)

if __name__=='__main__':
    total=0
    for a in range(2,401):
        a,m,r=check(a);total+=r
    print(f'PASS: independently checked {total} residue thresholds over all a=2..400, each by full capped coin-change DP through its candidate bound')

SMALL = [(7,7),(9,9),(19,14),(22,19),(29,25),(34,30),(55,40),
         (51,44),(59,51),(76,61),(95,70),(89,75),(109,85),
         (119,94),(143,104)]

def polynomial_invariants(a):
    k,d = divmod(a,4)
    g = 4*k*k + (20+d)*k + (-1,3,7,14)[d]
    n = 2*k*k + (20+d)*k + (d*(d+7))//2 -8
    return g,n

def test_invariants():
    for a in range(2,1101):
        threshold=predicted(a)
        actual=(max(threshold)-a, sum((v-r)//a for r,v in enumerate(threshold)))
        expected=SMALL[a-2] if a<=13 else polynomial_invariants(a)
        assert actual==expected, (a,actual,expected)
    print('PASS: all smaller-base entries and quasi-polynomials cross-checked algebraically through a=1100')

test_invariants()
