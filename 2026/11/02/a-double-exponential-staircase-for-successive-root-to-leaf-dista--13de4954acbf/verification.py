"""Exact small-depth checks of the finite polynomial identity and staircase bounds.
Scientific proof uses elementary-symmetric domination; checks are not proof.
"""
from fractions import Fraction
from itertools import combinations
from math import comb

checks=0

def conv(a,b,m):
    out=[Fraction(0)]*(m+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=m:
                out[i+j]+=x*y
    return out

def support_prob(r,m):
    g=[Fraction(1,2),Fraction(1,2)]+[Fraction(0)]*(m-1)
    ans=[Fraction(1)]+[Fraction(0)]*m
    for h in range(r):
        ans=conv(ans,g,m)
        gg=conv(g,g,m)
        g=[z/Fraction(2) for z in gg]
        if m>=1:g[1]+=Fraction(1,2)
    return sum(ans),ans

def staircase(r,m):
    return Fraction(1,2**(2**(r-m+1)-r+2*m-2))

for r in range(1,9):
    for m in range(min(5,r+1)):
        pr,co=support_prob(r,m)
        assert sum(co)==pr
        checks+=1
        if m==0:
            assert pr==staircase(r,m)
            checks+=1
        if r>=m+1:
            low=staircase(r,m)
            assert low<=pr
            checks+=1
            err=pr/low-1
            eps=Fraction(1,2**(2**(r-m)))
            upper=((5**m-1)+2**m*(m+1)*r**m)*eps
            assert err<=upper,(r,m,err,upper)
            checks+=1
for r in range(2,15):
    for m in range(1,min(r,6)):
        w=[2**(h+1)-1 for h in range(r)]
        star=set(range(r-m,r))
        opt=sum(w[h] for h in star)
        for j in range(m+1):
            for s in combinations(range(r),j):
                if set(s)!=star:
                    assert opt-sum(w[h] for h in s)>=2**(r-m)
                    checks+=1
print(f'PASS: {checks} exact-rational/coefficient/subset-weight assertions')
