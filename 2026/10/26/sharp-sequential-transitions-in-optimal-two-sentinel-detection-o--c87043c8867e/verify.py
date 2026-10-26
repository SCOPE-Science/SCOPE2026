"""Standalone exact checks for two-sentinel eventual detection on path contact networks."""
from fractions import Fraction
from itertools import combinations
from hashlib import sha256
import json

def reach(n,a,b,p):
    # a,b are zero-based positions.
    out=Fraction(0)
    for i in range(n):
        if i<a: out+=p**(a-i)
        elif i>b: out+=p**(i-b)
        elif i==a or i==b: out+=1
        else: out+=p**(i-a)+p**(b-i)-p**(b-a)
    return out

def formula(n,d,p):
    s=n-d-1
    l=s//2;r=s-l
    return 2+2*sum((p**j for j in range(1,d+1)),Fraction(0))+sum((p**j for j in range(1,l+1)),Fraction(0))+sum((p**j for j in range(1,r+1)),Fraction(0))-(d+1)*p**d

def brute(n,a,b,p):
    total=Fraction(0)
    for bits in range(1<<(n-1)):
        z=bits.bit_count();w=p**z*(1-p)**(n-1-z)
        for seed in range(n):
            # exactly open edges on path connecting seed to a or b
            for goal in (a,b):
                lo=min(seed,goal);hi=max(seed,goal)
                if all(bits&(1<<j) for j in range(lo,hi)):
                    total+=w
                    break
    return total

def expected_opt(n,p):
    m=n//3+1
    for d in range(m,n-1):
        q=(n-d)//2 # ceil((n-d-1)/2)=floor((n-d)/2)
        if p**(d-q)*(d+1-d*p)>1: m+=1
        elif p**(d-q)*(d+1-d*p)==1:
            return (m,m+1)
        else: break
    return (m,)

cases=0;brutes=0;threshold_order=0
for n in range(4,31):
  for p in (Fraction(1,20),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(19,20),Fraction(99,100)):
    optval=None;arg=[]
    for a,b in combinations(range(n),2):
        v=reach(n,a,b,p)
        d=b-a
        assert v<=formula(n,d,p)
        if optval is None or v>optval: optval=v;arg=[d]
        elif v==optval:arg.append(d)
        cases+=1
    assert set(arg)==set(expected_opt(n,p)),(n,p,arg,expected_opt(n,p))
    for d in range(1,n):
        assert formula(n,d,p)==max(reach(n,a,a+d,p) for a in range(n-d))
        if d<n-1:
            q=(n-d)//2
            delta=formula(n,d+1,p)-formula(n,d,p)
            assert delta==p**d*((d+1)-d*p)-p**q
            threshold_order+=1
for n in range(4,11):
 for p in (Fraction(1,4),Fraction(1,2),Fraction(3,4)):
  for a,b in combinations(range(n),2):
    assert reach(n,a,b,p)==brute(n,a,b,p),(n,p,a,b)
    brutes+=1
# exact one-crossing and strict ascending comparisons of polynomial threshold roots
# Interval bisection uses integer rational fractions: each f_d has unique proper root.
for n in range(4,100):
    last=Fraction(0)
    for d in range(n//3+1,n-1):
        q=(n-d)//2; k=d-q
        f=lambda x: x**k*(d+1-d*x)-1
        lo=Fraction(0);hi=Fraction(1)
        for j in range(40):
            mid=(lo+hi)/2
            if f(mid)>0: hi=mid
            else:lo=mid
        assert lo>last,(n,d,lo,last)
        last=hi
report={'verification':'passed','pair_placement_fraction_cases':cases,'edge_subset_exact_cases':brutes,'adjacent_distance_difference_cases':threshold_order,'critical_threshold_order_checked_n':list(range(4,100)),'method':'Exact Fraction arithmetic for finite verification; universal proof is analytical.'}
print(json.dumps(report,sort_keys=True,separators=(',',':')))
