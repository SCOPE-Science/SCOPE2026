#!/usr/bin/env python3
from itertools import product
N=30
# Enumerate words in 2,3 by recursion; c[s] counts completed macro-edge words of total length s.
c=[0]*(N+1)
def rec(total):
    c[total]+=1
    for w in (2,3):
        if total+w<=N:
            rec(total+w)
rec(0)
# Four terminal states: branch offset 0; length-2 offset 1; length-3 offsets 1,2.
q=[]
for n in range(N+1):
    val=c[n]
    if n>=1: val += 2*c[n-1]
    if n>=2: val += c[n-2]
    q.append(val)
expected=[1,2,2,3,4,5,7,9,12,16,21,28,37,49,65]
assert q[:len(expected)]==expected,(q[:len(expected)],expected)
for n in range(3,N+1):
    assert q[n]==q[n-2]+q[n-3]
# Independent coefficient recurrence from (1-z^2-z^3)Q=(1+z)^2.
r=[0]*(N+1)
for n in range(N+1):
    rhs=(1 if n in (0,2) else 2 if n==1 else 0)
    r[n]=rhs+(r[n-2] if n>=2 else 0)+(r[n-3] if n>=3 else 0)
assert r==q
# Standard Padovan normalization P0=P1=P2=1; q_n=P_{n+2}.
P=[1,1,1]
for n in range(3,N+3): P.append(P[n-2]+P[n-3])
assert all(q[n]==P[n+2] for n in range(N+1))
# Plastic constant by Newton iteration.
rho=1.3
for _ in range(20): rho -= (rho**3-rho-1)/(3*rho*rho-1)
assert abs(rho-1.324717957244746)<1e-12
ratio=q[-1]/q[-2]
assert abs(ratio-rho)<1e-3
print('radial orbit counts:',q[:15])
print('q_30 =',q[30])
print('q_30/q_29 = %.12f'%ratio)
print('plastic constant = %.12f'%rho)
print('VERIFY_OK')
