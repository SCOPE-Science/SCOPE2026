"""Exact independent checks of conditional midpoint-height peak formulas.

Run: python3 verify.py
Only standard-library modules are required.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb

checks = 0

def checked(condition, context):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(context)


def expected_peaks(n, h):
    if not (n >= 1 and 0 <= h <= n and (n-h)%2 == 0):
        raise ValueError((n,h))
    return (Fraction((n-h)*(n+h+2), 2*n) +
            Fraction(h*(n+h+2), 2*n*(h+1)) ** 2)


def ballot_dp(n):
    # State (height, last step U or D) -> (count, sum of peaks).
    states = {(0, False):(1,0)}
    for step in range(n):
        future = defaultdict(lambda:(0,0))
        for (height,last_up),(count,peak_total) in states.items():
            c,p=future[(height+1,True)]
            future[(height+1,True)]=(c+count,p+peak_total)
            if height:
                c,p=future[(height-1,False)]
                future[(height-1,False)]=(c+count,p+peak_total+int(last_up)*count)
        states=future
    return states


for n in range(1,121):
    state=ballot_dp(n)
    for h in range(n%2,n+1,2):
        u=(n+h)//2
        d=(n-h)//2
        count=sum(state.get((h,last),(0,0))[0] for last in (False, True))
        peak_total=sum(state.get((h,last),(0,0))[1] for last in (False, True))
        end_up=state.get((h,True),(0,0))[0]
        ballot=(h+1)*comb(n,d)//(u+1)
        checked(count==ballot,('ballot',n,h,count,ballot))
        checked(Fraction(peak_total,count)==Fraction(d*(u+1),n),('peak',n,h))
        checked(Fraction(end_up,count)==Fraction(h*(u+1),n*(h+1)),('end',n,h))
        checked(expected_peaks(n,h)==2*Fraction(peak_total,count)+Fraction(end_up,count)**2,
                ('split',n,h))

# Independent enumeration of full excursions, rather than products of half-paths.
for n in range(1,12):
    counts=defaultdict(lambda:[0,0])
    def build(steps,height,up,down,peaks):
        if len(steps)==2*n:
            checked(height==0,('endpoint',n))
            middle=0
            for s in steps[:n]: middle += (1 if s=='U' else -1)
            counts[middle][0]+=1
            counts[middle][1]+=peaks
            return
        if up<n: build(steps+'U',height+1,up+1,down,peaks)
        if height>0 and down<n:build(steps+'D',height-1,up,down+1,peaks+int(steps.endswith('U')))
    build('',0,0,0,0)
    checked(sum(pair[0] for pair in counts.values())==comb(2*n,n)//(n+1),('Catalan',n))
    for h,(ct,s) in counts.items():
        checked(Fraction(s,ct)==expected_peaks(n,h),('full',n,h))

for n in range(2,501):
    heights=list(range(n%2,n+1,2))
    values=[expected_peaks(n,h) for h in heights]
    for j in range(len(values)-2):
        checked(values[j+2]-2*values[j+1]+values[j]<0,('strict concavity',n,heights[j]))
    first=values[1]-values[0]
    if n%2==0:
        checked((first>0)==(n>=28),('even threshold',n))
    else:
        checked((first>0)==(n>=65),('odd threshold',n))
        checked((first==0)==(n==63),('odd tie',n))

# A large example checks scaling of the optimizing midpoint level.
for n in (1000, 10000, 100000):
    heights=list(range(n%2, min(n, 500)+1,2))
    maximizer=max(heights,key=lambda h:expected_peaks(n,h))
    prediction=(n/2)**(1/3)
    checked(abs(maximizer-prediction)<=5,('scale',n,maximizer,prediction))

print(f'PASS: {checks} exact assertions, full-path enumeration to semilength 11, ballot DP to length 120')
