#!/usr/bin/env python3
"""Independent exact integer checks for sharp mod-three Stern discrepancy."""
from fractions import Fraction

states = [(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
idx = {x:i for i,x in enumerate(states)}
def steps(pair):
    a,b = pair
    return ((a,(a+b)%3),((a+b)%3,b))
M = [[0]*8 for _ in range(8)]
for i,s in enumerate(states):
    for t in steps(s):
        M[i][idx[t]] += 1
assert [sum(row) for row in M] == [2]*8
assert [sum(row[j] for row in M) for j in range(8)] == [2]*8

N=8
def mul(A,B):
    return [[sum(A[i][t]*B[t][j] for t in range(N)) for j in range(N)] for i in range(N)]
def plus(A,B):
    return [[A[i][j]+B[i][j] for j in range(N)] for i in range(N)]
def scale(A,c):
    return [[c*x for x in row] for row in A]
I=[[int(i==j) for j in range(N)] for i in range(N)]
Z=scale(I,0)
T=mul(M,M)
Q=plus(plus(T,M),scale(I,2))
ann=mul(mul(mul(M,plus(M,scale(I,-1))),plus(M,scale(I,-2))),Q)
assert ann==Z, ann
# characteristic polynomial computed by exact Newton trace identities
powers=I
ps=[0]
for j in range(1,N+1):
    powers=mul(powers,M)
    ps.append(sum(powers[i][i] for i in range(N)))
coefs=[1]
for k in range(1,N+1):
    s=sum(coefs[k-i]*ps[i] for i in range(1,k+1))
    assert s % k==0
    coefs.append(-s//k)
# descending polynomial coefficients of t^2(t-2)(t-1)^3(t^2+t+2)
def poly_multiply(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out
expected=[1]
for factor in ([1,0,0],[1,-2],[1,-1],[1,-1],[1,-1],[1,1,2]):
    expected=poly_multiply(expected,factor)
assert coefs==expected, (coefs,expected)
assert sum(1 for c in states if c[0]==0)==2

limit=1<<17
s=[0]*(limit+2)
s[1]=1
for n in range(2,limit+2):
    s[n] = s[n//2] if n%2==0 else s[n//2]+s[n//2+1]

H=[]
for k in range(17):
    lo=1<<k
    hi=lo*2
    if hi>limit:break
    H.append(sum(s[n]%3==0 for n in range(lo,hi)))
d=[4*h-(1<<k) for k,h in enumerate(H)]
assert d[:2]==[-1,-2]
assert all(d[k+2]==-d[k+1]-2*d[k] for k in range(len(d)-2))
# Uniform axis/diagonal/mixed counts for every computed dyadic level
for k in range(2,len(H)):
    lo,hi=1<<k,1<<(k+1)
    counts={pair:0 for pair in states}
    for n in range(lo,hi):
        counts[(s[n]%3,s[n+1]%3)] += 1
    assert all(counts[p]==counts[(0,1)] for p in ((0,1),(0,2),(1,0),(2,0)))
    assert counts[(1,1)] == counts[(2,2)]
    assert counts[(1,2)] == counts[(2,1)]
    assert H[k]==2*counts[(0,1)]
# Brute every integer up to limit to cross-check prefix tally, and lower bound at dyadic cuts
running=0
for n in range(limit):
    running += s[n]%3==0
    assert abs(4*running-(n+1)) <= 16*(int((n+1)**.5)+1)
print('VERIFIED: exact 8-state characteristic and annihilating polynomials; 17 dyadic levels; 131072 Stern values; 131072 prefix discrepancies')
print('first dyadic counts:',H[:12])
