#!/usr/bin/env python3
"""Exact finite arithmetic checks supporting the stated theorem; not an infinite proof."""
p=103
M=p**8
C=[[0,1,0],[0,0,1],[1,1,1]]
def matmul(A,B,q):
    return [[sum(A[i][k]*B[k][j] for k in range(3))%q for j in range(3)] for i in range(3)]
def matpow(A,n,q):
    R=[[int(i==j) for j in range(3)] for i in range(3)]
    while n:
        if n&1:R=matmul(R,A,q)
        A=matmul(A,A,q);n>>=1
    return R
assert matpow(C,17,p)==[[46,0,0],[0,46,0],[0,0,46]]
def val(x):
    if x==0:return 10**9
    k=0
    while x%p==0:
        x//=p;k+=1
    return k
T=[0,1,1]
for n in range(2,30001):T.append((T[-1]+T[-2]+T[-3])%M)
assert T[13]==927 and T[16]==5768 and T[17]==10609
assert [r for r in range(17) if T[r]%p==0]==[0,13,16]
# Reversed recurrence at negative integer indices (exact integer arithmetic).
s={0:0,1:1,2:1}
for n in range(-1,-18,-1):
    s[n]=s[n+3]-s[n+2]-s[n+1]
assert [s[i] for i in (-1,-4,-17)]==[0,0,0]
for n in range(1,30000):
    r=n%17
    v=(2+val(n)+val(n+17) if r==0 else
       1+val(n+4) if r==13 else
       1+val(n+1) if r==16 else 0)
    assert min(v,8)==min(val(T[n]),8),(n,v,val(T[n]))
print('PASS: C^17 scalar mod103; exact boundary and negative zeros; 29999 indices mod103^8')
