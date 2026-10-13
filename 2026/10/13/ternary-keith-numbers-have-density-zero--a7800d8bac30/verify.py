#!/usr/bin/env python3
from math import comb, log

# Exact admissible alpha window.
assert 3*7 > 20
assert 2**20 < 3**13

alpha_num, alpha_den = 7, 20

# Zero-rich ternary strings: finite shadows of the exponential tail.
tails=[]
for n in (40,80,120,160,200):
    j0=(alpha_num*n + alpha_den-1)//alpha_den
    count=sum(comb(n,j)*(2**(n-j)) for j in range(j0,n+1))
    ratio=count/(3**n)
    tails.append((n,j0,ratio))
assert all(tails[i+1][2] < tails[i][2] for i in range(len(tails)-1))

def ternary_digits(N,n=None):
    digs=[]
    x=N
    while x:
        digs.append(x%3); x//=3
    if not digs: digs=[0]
    digs=digs[::-1]
    if n is not None and len(digs)<n:
        digs=[0]*(n-len(digs))+digs
    return digs

def is_keith3(N):
    digs=ternary_digits(N)
    n=len(digs)
    if n<2: return False
    seq=digs[:]
    s=sum(seq)
    while s < N:
        seq.append(s)
        s=sum(seq[-n:])
    return s==N

counts=[]
examples=[]
for n in range(2,11):
    lo,hi=3**(n-1),3**n
    vals=[N for N in range(lo,hi) if is_keith3(N)]
    counts.append((n,len(vals)))
    if vals: examples.append((n,vals[:8]))

print('VERIFY_OK', 'alpha=7/20', f'2^20={2**20}', f'3^13={3**13}', 'tails='+repr(tails), 'counts='+repr(counts), 'examples='+repr(examples))
