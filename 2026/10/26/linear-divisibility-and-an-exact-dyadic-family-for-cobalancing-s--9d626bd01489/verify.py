"""Standalone exact-integer checks accompanying the cobalancing-square theorem.
The infinite assertions use the elementary recurrence proof in RESULT.md.
"""
from math import gcd
from functools import reduce

A=((6,-1,2),(1,0,0),(0,0,1))

def matmul(x,y,mod):
    return tuple(tuple(sum(x[i][h]*y[h][j] for h in range(3))%mod for j in range(3)) for i in range(3))

def matpow(x,n,mod):
    y=((1,0,0),(0,1,0),(0,0,1))
    while n:
        if n&1: y=matmul(y,x,mod)
        x=matmul(x,x,mod)
        n//=2
    return y

b=[0,0]
for _ in range(2,850):
    b.append(6*b[-1]-b[-2]+2)
assert all(v%2==0 for v in b)
assert all(b[n]%4==(0,0,2,2)[n%4] for n in range(len(b)))
assert all(b[n]%3==(0,0,2,2)[n%4] for n in range(len(b)))
assert all(b[n]%5==(0,0,2,4,4,2)[n%6] for n in range(len(b)))

for n in range(400):
    assert b[n+4]**2-40*b[n+3]**2+206*b[n+2]**2-40*b[n+1]**2+b[n]**2==40
    assert sum(b[n+i]**2 for i in range(1,5))%16==8
    assert sum(b[n+i]**2 for i in range(1,13))%15==0

for m in range(2,16):
    mod=2**(m+1)
    mat=matpow(A,2**m,mod)
    target=((1+2**m,2**m,2**m),(2**m,1+2**m,2**m),(0,0,1))
    assert mat==tuple(tuple(z%mod for z in row) for row in target)

pref=[0]
for v in b: pref.append(pref[-1]+v*v)
def h(k,n): return pref[n+k+1]-pref[n+1]
for k in range(1,420):
    exact=reduce(gcd,[h(k,n) for n in range(120)])
    finite=reduce(gcd,[40*k]+[h(k,n) for n in range(4)])
    assert exact==finite, (k,exact,finite)
    assert 40*k%exact==0
for r in range(6):
    k=12*(2**r)
    assert reduce(gcd,[h(k,n) for n in range(120)])==10*k
    assert all(h(k,n)% (2**(r+4))==2**(r+3) for n in range(120))
print('PASS: recurrence polynomial, binary lift matrices, local periods, exact finite GCD reduction through k=419, and infinite-family instances r=0..5')
