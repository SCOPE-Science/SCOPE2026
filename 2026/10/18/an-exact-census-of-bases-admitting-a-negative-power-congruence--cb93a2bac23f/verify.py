#!/usr/bin/env python3
"""Check an exact residue census against independent direct power-orbit enumeration."""
from math import gcd, prod

def factor(n):
    d=2;out={}
    while d*d<=n:
        while n%d==0:
            out[d]=out.get(d,0)+1;n//=d
        d+=1
    if n>1:out[n]=out.get(n,0)+1
    return out

def predicted(m):
    z=factor(m);e=z.pop(2,0);v=[]
    for p,k in z.items():
        h=(p-1)*p**(k-1);s=0
        while h%2==0:s+=1;h//=2
        v.append((s,h))
    u=prod(h for s,h in v)
    if e>=2:return u
    if not v:return 1
    r=len(v)
    return u*sum(2**(r*j) for j in range(min(s for s,h in v)))

def brute(m):
    total=0
    for a in range(1,m):
        if gcd(a,m)!=1:continue
        seen=set();x=a%m
        while x not in seen:
            if x==m-1:
                total+=1;break
            seen.add(x);x=(x*a)%m
    return total

def main():
    for m in range(3,401):
        p,b=predicted(m),brute(m)
        assert p==b,(m,p,b)
    print('VERIFY_OK: 398 moduli 3..400')

if __name__=='__main__':main()
