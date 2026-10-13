#!/usr/bin/env python3
"""Reproduce finite checks for odd-squarefree OSOME residue theorem; Python stdlib only."""
from math import isqrt

N = 420
ways = [0] * (N + 1)
stat = [0] * (N + 1)
ways[0] = 1
for m in range(1, N + 1):
    # Arbitrarily many unmarked copies of part m, then 0/1 marked first copy.
    for n in range(m, N + 1):
        ways[n] += ways[n - m]
        stat[n] += stat[n - m]
    weight = m if m % 2 else -m
    for n in range(N, m - 1, -1):
        stat[n] += stat[n - m] + weight * ways[n - m]
        ways[n] += ways[n - m]

A = [0] * (N + 1)
for j in range(1, isqrt(N) + 1):
    A[j*j] = (-1)**j
P = [0] * (N + 1)
P[0] = 1
for n in range(1, N + 1):
    P[n] = -2 * sum(A[k] * P[n-k] for k in range(1, n+1) if A[k])
assert P == ways

def mul(a,b):
    c = [0] * (N+1)
    for i,ai in enumerate(a):
        if not ai: continue
        for j,bj in enumerate(b[:N+1-i]):
            if bj: c[i+j]+=ai*bj
    return c

T = [2*a for a in A]
T[0] = 1
T3 = mul(mul(T,T),T)
assert all((P[n]-T3[n]) % 8 == 0 for n in range(N+1))
S2 = [(P[n]-T3[n])//8 for n in range(N+1)]
assert S2 == stat

def is_prime(n):
    return n > 1 and all(n%d for d in range(2,isqrt(n)+1))
def is_squarefree(n):
    return all(n%(d*d) for d in range(2,isqrt(n)+1))
def chi4(d):
    return 1 if d%4==1 else (-1 if d%4==3 else 0)
def chi8(d):
    return 1 if d%8 in (1,3) else (-1 if d%8 in (5,7) else 0)
def divs(n):
    return [d for d in range(1,n+1) if n%d==0]

# Entire mod-4 character formula, at every positive index, including squares.
for n in range(1,N+1):
    delta_square = int(isqrt(n)**2 == n)
    delta_twicesquare = int(n % 2 == 0 and isqrt(n//2)**2 == n//2)
    delta_foursquare = int(n % 4 == 0 and isqrt(n//4)**2 == n//4)
    c4 = sum(chi4(d) for d in divs(n))
    c8 = sum(chi8(d) for d in divs(n))
    predicted = ((-1 if n % 2 == 0 else 1)*c4-c8+delta_square
                 +delta_twicesquare+2*delta_foursquare) % 4
    assert stat[n] % 4 == predicted,(n,stat[n],predicted)

squarefree_count=0
prime_count=0
for n in range(3,N+1,2):
    if not is_squarefree(n): continue
    squarefree_count+=1
    d=divs(n)
    claim=sum(chi4(t)-chi8(t) for t in d) % 4
    assert stat[n] % 4 == claim,(n,stat[n],claim)
    pred=2 if is_prime(n) and n%8 in (3,5) else 0
    assert stat[n] % 4 == pred,(n,stat[n],pred)
    prime_count+=is_prime(n)
# Independently reconstruct classical norm representation counts.
for n in range(1,N+1,2):
    r2 = sum(1 for x in range(-isqrt(n), isqrt(n)+1) for y in range(-isqrt(n), isqrt(n)+1) if x*x+y*y==n)
    r8 = sum(1 for x in range(-isqrt(n), isqrt(n)+1) for y in range(-isqrt(n//2), isqrt(n//2)+1) if x*x+2*y*y==n)
    assert r2 == 4*sum(chi4(d) for d in divs(n)),(n,r2)
    assert r8 == 2*sum(chi8(d) for d in divs(n)),(n,r8)
assert stat[9] % 4 == 3
print(f'VERIFY_OK max_index={N} direct_marked_overpartitions=all theta_identity=all full_character_mod4=all odd_squarefree={squarefree_count} prime_cases={prime_count} classical_norm_counts={(N+1)//2} nonsquarefree_boundary_n9={stat[9]%4}')
