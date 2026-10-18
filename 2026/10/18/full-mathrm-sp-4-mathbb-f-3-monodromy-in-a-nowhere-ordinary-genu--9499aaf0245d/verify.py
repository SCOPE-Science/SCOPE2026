#!/usr/bin/env python3
"""Exact finite arithmetic for the genus-two characteristic-seven family.

The topology, tame specialization and infinite geometric claims in RESULT.md
are mathematical arguments, not consequences of this finite computation.
"""
from collections import deque
from math import prod

P=7
# Expand (x^5 + a*x + t)^3 as a sparse polynomial in (deg_x,deg_a,deg_t).
base={(5,0,0):1,(1,1,0):1,(0,0,1):1}
f={(0,0,0):1}
for _ in range(3):
    nxt={}
    for u,v in f.items():
        for w,z in base.items():
            key=tuple(u[i]+w[i] for i in range(3))
            nxt[key]=(nxt.get(key,0)+v*z)%P
    f=nxt

def coefficient(xdeg):
    return {(a,t):c for (x,a,t),c in f.items() if x==xdeg and c%P}
H=[[coefficient(7*i-j) for j in (1,2)] for i in (1,2)]
assert H==[[{(1,1):6},{(0,2):3}],[{},{}]],H
assert 256%7==4 and 3125%7==3
# Critical condition f'=5x^4+a=0; for a=1, x^4=4 and t=2x;
# therefore all critical t have t^4=16*4=64=1 (mod 7).
assert (-pow(5,-1,7))%7==4 and (2**4*4)%7==1
# Check Frobenius semi-linear stable rank 1 for t != 0: H11*H11^7 !=0.
for t in range(1,7):
    top=(6*t)%7
    assert top*pow(top,7,7)%7 != 0

# Symplectic A4 intersection form and four Picard-Lefschetz transvections
n=4;p=3
omega=[[0]*n for _ in range(n)]
for i in range(n-1):
    omega[i][i+1]=1
    omega[i+1][i]=-1
I=tuple(int(i==j) for i in range(n) for j in range(n))
G=[]
for i in range(n):
    a=[[int(r==c) for c in range(n)] for r in range(n)]
    for j in range(n):a[i][j]=(a[i][j]+omega[j][i])%p
    G.append(tuple(e for row in a for e in row))
def multiply(a,b):
    return tuple(sum(a[4*i+k]*b[4*k+j] for k in range(4))%p for i in range(4) for j in range(4))
def transpose(a):return tuple(a[4*j+i] for i in range(4) for j in range(4))
OM=tuple(e%3 for row in omega for e in row)
for g in G:
    assert multiply(multiply(transpose(g),OM),g)==OM
seen={I}; pending=deque([I])
while pending:
    current=pending.popleft()
    for g in G:
        h=multiply(current,g)
        if h not in seen:
            seen.add(h);pending.append(h)
order=3**4*(3**2-1)*(3**4-1)
assert len(seen)==order==51840
assert order%7!=0
print('VERIFY_OK', 'H=',H,'Sp4(F3)_order=',order,'prime_to_7=',order%7!=0)
