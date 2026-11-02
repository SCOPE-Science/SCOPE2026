#!/usr/bin/env python3
"""Exact finite polynomial certificates for the five-color binary-partition congruence."""
from math import comb

R = (48, 49, 52, 53)
Q = [1,2,1,0,6,4,6,0,7,6,7,0,4,0,4,0,5,2,5,0,2,4,2,0,3,6,3,0,0,0,0,0]
H = {0:1,1:4,3:4,4:6,5:4,7:4,8:3,12:4,16:7,17:4,19:4,20:6,21:4,23:4,24:5}
P = {0:28,1:16,3:16,4:8,5:16,7:16,8:20,12:16,16:4,17:16,19:16,20:8,21:16,23:16,24:12}

def mul(a,b,mod):
    z = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:
                    z[i+j] = (z[i+j]+x*y)%mod
    return z

def eq(a,b,mod):
    return all(((a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0))%mod==0 for i in range(max(len(a),len(b))))

# The single finite identity Q(x)(1+x^32)=(1-x)^6 Q(x^2) modulo 8
lhs=mul(Q,[1]+[0]*31+[1],8)
rhs=mul([(-1)**j*comb(6,j)%8 for j in range(7)],[Q[i//2] if i%2==0 else 0 for i in range(2*len(Q)-1)],8)
assert eq(lhs,rhs,8), 'T^6 Mahler identity'

hv=[H.get(j,0) for j in range(25)]
assert eq(mul([(-1)**j*comb(30,j)%8 for j in range(31)],Q,8),mul(hv,[1]+[0]*31+[-1],8),8), 'H rational identity'

p=[1]
for j in range(6):
    d=2**j
    f=[int(k%d==0) for k in range(64-d+1)]
    for _ in range(5):
        p=mul(p,f,32)
assert len(p)-1==1605
pv=[P.get(j,0) for j in range(25)]
for r in R:
    assert [p[r+64*j] for j in range(25)]==pv, 'one of four numerator sections'
for j in range(25):
    assert (pv[j]-16*(-1)**j*comb(24,j)-12*H.get(j,0))%32==0,'numerator linear identity'

# Independent coefficient recurrence for B(x)^5, from (1-x)^5 F(x)=F(x^2).
N=32768
b=[0]*N
b[0]=1
for n in range(1,N):
    b[n]=(int(n%2==0)*b[n//2]+5*b[n-1]-10*(b[n-2] if n>=2 else 0)+10*(b[n-3] if n>=3 else 0)-5*(b[n-4] if n>=4 else 0)+(b[n-5] if n>=5 else 0))%32
for r in R:
    for k in range((N-1-r)//64+1):
        parity=(-1)**(k.bit_count())
        assert b[64*k+r]==(16+12*parity)%32,'coefficient recurrence'
print('VERIFY_OK finite_polynomial_degree=1605 sections=4 mahler_modulus=8 target_modulus=32 checked_coefficients=32768')
