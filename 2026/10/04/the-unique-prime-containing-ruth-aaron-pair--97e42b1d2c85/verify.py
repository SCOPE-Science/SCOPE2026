#!/usr/bin/env python3
LIMIT=2_000_000
spf=list(range(LIMIT+2))
for i in range(2,int((LIMIT+1)**0.5)+1):
    if spf[i]==i:
        for j in range(i*i,LIMIT+2,i):
            if spf[j]==j:
                spf[j]=i

def isprime(n):
    return n>=2 and spf[n]==n

def sopfr(n):
    s=0
    while n>1:
        p=spf[n]
        s+=p
        n//=p
    return s

minus=[]
for m in range(4,LIMIT+1):
    if not isprime(m) and sopfr(m)==m-1:
        minus.append(m)
assert minus==[6], minus

hits=[]
for n in range(1,LIMIT):
    if sopfr(n)==sopfr(n+1) and (isprime(n) or isprime(n+1)):
        hits.append(n)
assert hits==[5], hits
print(f"VERIFY_OK limit={LIMIT} composite_minus_one={minus} prime_member_starts={hits}")
