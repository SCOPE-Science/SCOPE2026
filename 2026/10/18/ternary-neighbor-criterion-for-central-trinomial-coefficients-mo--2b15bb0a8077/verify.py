#!/usr/bin/env python3
"""Exact reproducible checks for the central-trinomial modulo-nine theorem."""
from collections import defaultdict

def times(a, b):
    out = defaultdict(int)
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] += x * y
    return dict(out)

def power(a, n):
    out = {0: 1}
    for _ in range(n):
        out = times(out, a)
    return out

f = {-1:1,0:1,1:1}
h = {-2:1,-1:2,0:2,1:2,2:1}
f3 = times(power(f,2),f)
assert {k: f3.get(k,0)-({-3:1,0:1,3:1}).get(k,0) for k in range(-3,4)} == {k:3*h.get(k,0) for k in range(-3,4)}
jtab = [[times(times(power(f,a),h),power({-3:1,0:1,3:1},b-1)).get(0,0) for b in (1,2)] for a in range(3)]
assert jtab == [[2,2],[6,8],[16,24]]

def digits3(n):
    a=[]
    while n:
        a.append(n%3)
        n//=3
    return a

def predicted_mod9(n):
    d=digits3(n)
    places=[i for i,v in enumerate(d) if v==2]
    if not places:
        # Use first-order corrected residue computation even in the no-two case.
        # For digits 0,1, every active correction has local J_{0,1}=2 or J_{1,1}=6.
        # Formula below evaluates full residue, without assuming its value is 1.
        ans=1
        for i in range(1,len(d)):
            if d[i]==1: ans+=3*jtab[d[i-1]][0]
        return ans%9
    if len(places)>1:return 0
    j=places[0]
    if j==0:return 6 if len(d)>1 and d[1]==1 else 3
    return 0 if len(d)>j+1 and d[j+1]==1 else 6

# Direct recurrence n*T[n] = (2n-1)*T[n-1] + 3*(n-1)*T[n-2].
T0,T1=1,1
nmax=3**9
exact_one=0
nonzero_mod9=0
for n in range(nmax):
    if n==0: t=1
    elif n==1:t=1
    else:
        numerator=(2*n-1)*T1+3*(n-1)*T0
        assert numerator%n==0
        t=numerator//n
        T0,T1=T1,t
    got=t%9
    want=predicted_mod9(n)
    assert got==want, (n,got,want)
    digit_two_count=digits3(n).count(2)
    if digit_two_count==0:assert got%3==1
    else:assert got%3==0
    exact_one+=got in (3,6)
    nonzero_mod9+=got!=0
    if n+1 in {3**L for L in range(1,10)}:
        L=round(__import__('math').log(n+1,3))
        exp_one=1 if L==1 else (L+2)*2**(L-2)
        exp_nonzero=3 if L==1 else (L+6)*2**(L-2)
        assert exact_one==exp_one,(L,exact_one,exp_one)
        assert nonzero_mod9==exp_nonzero,(L,nonzero_mod9,exp_nonzero)
print('VERIFY_OK: Laurent identity, six local constants, 19,683 exact coefficients, all nine digit-length counts')
