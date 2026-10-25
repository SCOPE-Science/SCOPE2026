#!/usr/bin/env python3
"""Exact finite certificates for the binary (1,3,4)-pseudoperiod shift."""
from itertools import product
from collections import deque

SHIFTS = (1,3,4)
FORBIDDEN = {''.join(w) for w in product('01',repeat=5)
             if all(w[0] != w[d] for d in SHIFTS)}
assert FORBIDDEN == {'01011','01111','10000','10100'}
N=16
A=[[0]*N for _ in range(N)]
for state in range(N):
    for bit in '01':
        window=f'{state:04b}'+bit
        if window not in FORBIDDEN:
            A[state][(2*state+int(bit))%N]+=1
assert sum(map(sum,A))==28

def mmul(X,Y):
    n=len(X); m=len(Y[0]);h=len(Y)
    return [[sum(X[i][k]*Y[k][j] for k in range(h)) for j in range(m)] for i in range(n)]
def identity(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]
def trace(X): return sum(X[i][i] for i in range(len(X)))
def poly_product(P,Q):
    out=[0]*(len(P)+len(Q)-1)
    for i,a in enumerate(P):
        for j,b in enumerate(Q):out[i+j]+=a*b
    return out

# Newton identities determine the monic characteristic polynomial from
# integer traces, with an exact divisibility check at every coefficient.
T=[];power=identity(N)
for k in range(1,N+1):
    power=mmul(power,A)
    T.append(trace(power))
coeff=[1]
for k in range(1,N+1):
    numerator=-sum(coeff[k-j]*T[j-1] for j in range(1,k+1))
    assert numerator%k==0
    coeff.append(numerator//k)
expected=[1]
for part in ([1,0,0,0,0],[1,-1],[1,-1],[1,-1],
             [1,1],[1,-1,-1],[1,1,1],[1,0,1,0,-1]):
    expected=poly_product(expected,part)
assert coeff==expected, (coeff,expected)

# Mutually reachable classes, including the unique 12-state core.
def reach(v):
    seen={v};q=deque([v])
    while q:
        u=q.popleft()
        for z in range(N):
            if A[u][z] and z not in seen:seen.add(z);q.append(z)
    return seen
R=[reach(i) for i in range(N)]
classes=[];unseen=set(range(N))
while unseen:
    v=min(unseen)
    C=frozenset(x for x in unseen if x in R[v] and v in R[x])
    classes.append(C);unseen-=C
expected_classes={frozenset({0}),frozenset({15}),frozenset({5,10}),
    frozenset({1,2,3,4,6,7,8,9,11,12,13,14})}
assert set(classes)==expected_classes
core=sorted(next(C for C in classes if len(C)==12))
B=[[A[i][j] for j in core] for i in core]
# An explicit power with all positive entries witnesses primitivity.
BP=identity(len(B));positive_power=None
for k in range(1,100):
    BP=mmul(BP,B)
    if min(map(min,BP))>0:positive_power=k;break
assert positive_power is not None

# Direct independent cyclic-word enumeration for n=1,...,12.
M=identity(N)
for length in range(1,13):
    M=mmul(M,A)
    cycles=trace(M)
    brute=0
    for word in product('01',repeat=length):
        if all(any(word[i]==word[(i+shift)%length] for shift in SHIFTS)
               for i in range(length)):
            brute+=1
    assert cycles==brute,(length,cycles,brute)
# Linear-word enumeration via transfer counts and direct forbidden tests.
row=[1]*N
for length in range(4,15):
    count=sum(row)
    brute=sum(all(''.join(w[j:j+5]) not in FORBIDDEN
                  for j in range(length-4))
              for w in product('01',repeat=length))
    assert count==brute,(length,count,brute)
    row=[sum(row[i]*A[i][j] for i in range(N)) for j in range(N)]
assert [sum([1]*16),28]==[16,28]
print('PSEUDOPERIOD_134_ENTROPY_ZETA_PASS',
      'states=16 edges=28 components=4 core=12',
      'primitive_power='+str(positive_power),
      'periodic_n=1..12 linear_n=4..14',
      'charpoly_degree='+str(len(coeff)-1))
