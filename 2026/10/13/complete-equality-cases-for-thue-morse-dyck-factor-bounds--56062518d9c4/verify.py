#!/usr/bin/env python3
from fractions import Fraction as F

g0=[
[F(1),0,0,0,0,0,0],
[0,0,1,0,0,0,0],
[0,0,0,0,1,0,0],
[0,0,0,0,0,0,1],
[0,0,0,-2,3,-2,2],
[0,0,0,0,2,-2,2],
[0,0,0,F(1,2),F(5,4),F(-5,2),3],
]
g1=[
[0,1,0,0,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,0,1,0],
[0,0,0,F(3,4),F(11,8),-2,F(3,2)],
[0,0,0,F(1,2),F(1,4),0,1],
[0,0,0,F(-5,2),F(11,4),-2,3],
[0,0,0,F(-7,2),F(19,4),-5,5],
]
v=[F(1),0,0,0,0,0,0]
w=[F(1),F(1),F(2),F(3),F(2),F(4),F(6)]

def vmul(x,M):
    return [sum(x[i]*M[i][j] for i in range(7)) for j in range(7)]

def dmat(n):
    x=v[:]
    for ch in (bin(n)[2:] if n else "0"):
        x=vmul(x,g1 if ch=="1" else g0)
    y=sum(x[i]*w[i] for i in range(7))
    assert y.denominator==1
    return y.numerator

def q(n):
    if n==0:
        return 0
    b=bin(n)[2:]
    if len(b)==1:
        return 1
    return 2 if b.startswith("10") else 1

# Published first values.
table=[1,1,2,3,2,4,6,6,4,8,8,8,12,9,12,13,8,14,16,14,16]
assert [dmat(n) for n in range(len(table))]==table

# Published Lemma 5.1 recurrences, checked directly from the rank-7 representation.
for n in range(3,101):
    assert dmat(2*n)==2*dmat(n)
    assert dmat(4*n+3)==2*dmat(n)+dmat(2*n+1)+q(n)
    assert dmat(8*n+1)==2*dmat(2*n+1)+dmat(4*n+1)-q(n)
    assert dmat(8*n+5)==2*dmat(n)+dmat(2*n+1)+2*dmat(2*n+2)

# DFA consequence used in the proof.
for j in range(1,40):
    assert q(1<<j)==2

# Base range required by the induction.
upper_base=[n for n in range(1,29) if dmat(n)==n]
lower_base=[n for n in range(1,29) if 2*dmat(n)==n]
odd_base=[n for n in range(1,29,2) if 2*dmat(n)==n+3]
assert upper_base==[1,2,3,6,12,24]
assert lower_base==[4,8,16]
assert odd_base==[3,5]

# Direct finite factor enumeration as an independent regression check.
def tm_prefix(N):
    return ''.join(str(i.bit_count()&1) for i in range(N))
def is_dyck(s):
    bal=0
    for ch in s:
        bal += 1 if ch=="0" else -1
        if bal<0:
            return False
    return bal==0

for N in (4096,):
    T=tm_prefix(N)
    vals=[]
    for n in range(1,29):
        L=2*n
        fac={T[i:i+L] for i in range(N-L+1)}
        vals.append(sum(is_dyck(x) for x in fac))
    assert vals==[dmat(n) for n in range(1,29)]

# Large-range regression of the final equality classifications.
for n in range(1,5000):
    d=dmat(n)
    upper = (n in (1,2)) or (n%3==0 and (n//3)&((n//3)-1)==0)
    lower = n>=4 and (n & (n-1)==0)
    oddeq = n in (3,5)
    assert (d==n)==upper, ("upper",n,d)
    assert (2*d==n)==lower, ("lower",n,d)
    if n&1:
        assert (2*d==n+3)==oddeq, ("odd",n,d)

print(
    "VERIFY_OK "
    "rank7_table_n=0..20 "
    "lemma5_1_n=3..100 "
    "q_powers_two_j=1..39 "
    "base_n=1..28 "
    "direct_factor_prefix=4096 "
    "classification_n<5000"
)
