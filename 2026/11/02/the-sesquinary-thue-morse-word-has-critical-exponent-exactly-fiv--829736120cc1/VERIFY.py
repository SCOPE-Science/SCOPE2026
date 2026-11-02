#!/usr/bin/env python3
"""Finite checks for the rational-base repetition theorem; no infinite proof is claimed."""
N=65536
x=bytearray(N)
for n in range(1,N):
    x[n]=x[2*(n//3)]+(n%3==1)
    x[n]&=1

def digitsum_parity(n):
    parity=0
    while n:
        parity^=(n%3)&1
        n=2*(n//3)
    return parity

for n in range(N):
    assert x[n]==digitsum_parity(n),n
assert ''.join(str(v) for v in x[18:33])=='101101101101101'
for m in range(N//3):
    if 3*m+2>=N or 2*m>=N:break
    assert (x[3*m],x[3*m+1],x[3*m+2])==(x[2*m],1-x[2*m],x[2*m])
u=x[0::2]
for m in range(len(u)//3):
    if 2*m+1>=len(u):break
    assert (u[3*m],u[3*m+1],u[3*m+2])==(u[2*m],u[2*m],1-u[2*m+1])
assert not any(u[i:i+6]==bytearray([u[i]])*6 for i in range(len(u)-5))
for p in range(1,129):
    streak=0
    for i in range(N-p):
        streak=streak+1 if x[i]==x[i+p] else 0
        if streak>=4*p+1:
            raise AssertionError(('periodic factor of length 5p+1',p,i))
print('VERIFY_OK recurrence_terms=65536 periods=128 witness_index=18 parity_algorithms=2')
