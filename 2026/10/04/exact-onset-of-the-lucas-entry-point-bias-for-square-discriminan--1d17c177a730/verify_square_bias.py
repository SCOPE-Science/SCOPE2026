#!/usr/bin/env python3
import math

def factors(n):
    n=abs(n); out=[]; d=2
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0: n//=d
        d=3 if d==2 else d+2
    if n>1: out.append(n)
    return out

def predicted(P,Q):
    if any(p%2 for p in factors(P)):
        return 2
    if abs(P)==1 and Q==-2:
        return 4
    return 3

def actual(P,Q,s):
    u0,u1=0,1
    vals={1:u1}
    a,b=u0,u1
    for n in range(2,5):
        a,b=b,P*b-Q*a
        vals[n]=b
        for p in factors(b):
            if s%p!=0:
                return n
    return None

count=0
for P in range(-80,81):
    if P==0: continue
    for Q in range(-500,501):
        if Q==0 or math.gcd(P,Q)!=1: continue
        D=P*P-4*Q
        if D<=0: continue
        s=math.isqrt(D)
        if s*s!=D: continue
        got=actual(P,Q,s)
        want=predicted(P,Q)
        if got!=want:
            raise SystemExit(f'FAIL P={P} Q={Q} D={D} got={got} want={want}')
        count+=1
print(f'VERIFY_OK cases={count}')
