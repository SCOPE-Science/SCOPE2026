#!/usr/bin/env python3
"""Exact arithmetic replay for a formula about consecutive coin denominations."""

def formula(a,p):
    h=a//2
    if p<=h:
        return a*(h+p)+2*p-1
    if p<=a+1:
        return a*(h+p+1)-1
    j,e=divmod(p-a-2,2)
    return a*(h+a+2+j+e)+2*j+1

def replay():
    cases=0
    for a in range(3,121):
        top=formula(a,2*a)+a
        den=[0]*(top+1)
        den[0]=1
        for coin in (a,a+1,a+2):
            for n in range(coin,top+1):
                den[n]+=den[n-coin]
        for p in range(2*a+1):
            g=formula(a,p)
            assert den[g]==p,(a,p,g,den[g])
            assert all(den[n]>p for n in range(g+1,g+a+1)),(a,p,g)
            # The finite table also independently locates the last level-p gap.
            assert next((n for n in range(top,g,-1) if den[n]<=p),None) is None
            assert next((n for n in range(g+1) if den[n]<=p),None) is not None
            cases+=1
    # Independent exhaustive coefficients, with no coin-change DP.
    instances=0
    for a in range(3,17):
        top=formula(a,2*a)+a
        den=[0]*(top+1)
        den[0]=1
        for coin in (a,a+1,a+2):
            for n in range(coin,top+1): den[n]+=den[n-coin]
        for n in range(top+1):
            brute=0
            for x in range(n//a+1):
                rest=n-a*x
                for y in range(rest//(a+1)+1):
                    if (rest-(a+1)*y)%(a+2)==0: brute+=1
            assert brute==den[n],(a,n,brute,den[n])
            instances+=1
    print('PASS',cases,'exact (a,p) checks',instances,'independent denumerant cases')
if __name__=='__main__':
    replay()
