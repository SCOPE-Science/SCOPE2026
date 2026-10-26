"""Independent exact count tests for minimum one-failure source sets on cycles."""
from itertools import combinations
from math import ceil,comb


def trace_count(n,k,B):
    # Transfer states are gap lengths 1,...,B-1. Enumerate the
    # coefficient of x^n in tr(M_B(x)^k) via a closed-walk DP.
    states=list(range(1,B))
    total=0
    for root in states:
        poly={(root,0):1} # (last,sum of selected gap weights)
        for _ in range(k):
            nxt={}
            for (cur,weight),v in poly.items():
                for b in states:
                    if cur+b<=B and weight+b<=n:
                        key=(b,weight+b)
                        nxt[key]=nxt.get(key,0)+v
            poly=nxt
        total+=poly.get((root,n),0)
    assert (n*total)%k==0
    return n*total//k


def gap_count(n,k,B):
    ans=0
    for S in combinations(range(n),k):
        a=[(S[(i+1)%k]-S[i])%n or n for i in range(k)]
        ans+=all(a[i-1]+a[i]<=B for i in range(k))
    return ans


def run():
    instances=0
    for n in range(3,14):
        for B in range(2,n+1):
            k=ceil(2*n/B)
            exact=gap_count(n,k,B)
            transfer=trace_count(n,k,B)
            assert exact==transfer,(n,B,k,exact,transfer)
            if B==4:
                expected=(6 if n%4==0 else 2) if n%2==0 else n*((n+3)//4)
                assert exact==expected,(n,exact,expected)
            if B==3:
                expected=3 if n%3==0 else n if n%3==1 else n*(n+1)//6
                assert exact==expected,(n,exact,expected)
            instances+=1
    print('VERIFY_OK independent trace and subset census:',instances)

if __name__=='__main__':run()
