#!/usr/bin/env python3
"""Self-contained independent finite-size verification of local dynamics."""
from collections import defaultdict

def update(x,n):
    y=0
    for i in range(n):
        count=sum((x>>(j%n))&1 for j in (i-1,i,i+1))
        bit=int(count>=2)^(i==0)
        y|=bit<<i
    return y

def counts(n):
    L=n-1
    # Count strings by run-compositions, with bit of first run chosen freely.
    odd=even=0
    def compositions(rem,parts):
        if rem==0:
            return int(parts>0 and parts%2==1),int(parts>0 and parts%2==0)
        a=b=0
        for k in range(2,rem+1):
            x,y=compositions(rem-k,parts+1)
            a+=x;b+=y
        return a,b
    odd,even=compositions(L,0)
    return 2*odd,2*even

for n in range(3,17):
    f=[update(x,n) for x in range(1<<n)]
    seen=set();fixed=0;cycles=0
    for start in range(1<<n):
        if start in seen:
            continue
        pos={};route=[];x=start
        while x not in seen and x not in pos:
            pos[x]=len(route)
            route.append(x)
            x=f[x]
        if x in pos:
            cyc=route[pos[x]:]
            if len(cyc)==1:fixed+=1
            elif len(cyc)==2:
                cycles+=1
                assert (cyc[0]^cyc[1])==1,(n,cyc)
            else:
                raise AssertionError(('unexpected_period',n,len(cyc)))
        seen.update(route)
    a,b=counts(n)
    assert (fixed,cycles)==(a,b),(n,(fixed,cycles),(a,b))
print('CONTRARIAN_VERIFY_OK')
