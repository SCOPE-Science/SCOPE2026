"""Exact finite tests of contiguous alternating streaks in two-point moving averages."""
from itertools import permutations
from fractions import Fraction
from math import factorial

def q(r):
    return Fraction(1, factorial(r//2+1)*factorial((r+1)//2+1))

def signs(vals):
    # The ordered time-series means are (vals[i]+vals[i+1])/2.
    # The difference sign is exactly the sign of vals[i+2]-vals[i].
    return [1 if vals[i+2]>vals[i] else -1 for i in range(len(vals)-2)]

def longest_alt(sig):
    if not sig:return 0
    out=cur=1
    for i in range(1,len(sig)):
        cur=cur+1 if sig[i]!=sig[i-1] else 1
        out=max(out,cur)
    return out

total=0
for r in range(1,8):
    yes=0
    for p in permutations(range(r+2)):
        s=signs(p)
        yes+=int(all(s[i]!=s[i-1] for i in range(1,len(s))))
    assert Fraction(yes,factorial(r+2))==2*q(r), (r,yes,2*q(r))
    print('block',r,'yes',yes,'total',factorial(r+2),'P',str(2*q(r)))
    total+=factorial(r+2)
for n in range(2,9):
    cnt=[0]*n
    for p in permutations(range(n+1)):
        h=longest_alt(signs(p))
        cnt[h]+=1
    assert sum(cnt)==factorial(n+1)
    for r in range(1,n):
        prob=Fraction(sum(cnt[r:]),factorial(n+1))
        block_count=(n+1)//(r+2)
        lower=1-(1-2*q(r))**block_count
        upper=min(1,2*(n-r)*q(r))
        assert lower<=prob<=upper, (n,r,prob,lower,upper)
    print('length',n,'hist',cnt)
    total+=factorial(n+1)
# Independently inspect the joint events that enter the Chen--Stein bound.
for r in range(2,5):
    for d in range(1,r+2):
        length = r+d+2
        # Two windows, each of length r comparisons, begin d positions apart.
        # For tractability enumerate all rank permutations only up to 9 innovations.
        if length > 9:
            continue
        joint=0
        for p in permutations(range(length)):
            s=signs(p)
            left=all(s[j]!=s[j-1] for j in range(1,r))
            right=all(s[d+j]!=s[d+j-1] for j in range(1,r))
            joint+=int(left and right)
        prob=Fraction(joint,factorial(length))
        if d<r:
            assert prob==2*q(r+d), (r,d,prob)
        else:
            assert prob <= (r+2)**2*(2*q(r))**2,(r,d,prob)
        total+=factorial(length)
        print('overlap',r,d,'joint',prob)
print('VERIFY_OK enumerated',total,'permutations')
