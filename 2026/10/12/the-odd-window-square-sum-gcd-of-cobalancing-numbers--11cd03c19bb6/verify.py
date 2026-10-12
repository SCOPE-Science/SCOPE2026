#!/usr/bin/env python3
"""Exact finite regression checks for an odd-window cobalancing gcd theorem.

The infinite statement is established in RESULT.md; these checks are diagnostic.
"""
from math import gcd
MAXK=501
N=MAXK+12
b=[0,0]; a=[0,0]; B=[0,1]; Q=[1,1]
for n in range(2,N):
    b.append(6*b[-1]-b[-2]+2)
    a.append(6*a[-1]-a[-2]+1)
    B.append(6*B[-1]-B[-2])
    Q.append(2*Q[-1]+Q[-2])
assert all(b[n]==2*a[n] for n in range(N))
assert [a[i]%7 for i in range(18)]==[0,0,1]*6

def G(x,y): return 4*y*y-12*x*y+5*x-9*y
for n in range(N-2):
    assert 64*a[n+1]**2==G(a[n+1],a[n+2])-G(a[n],a[n+1])+5
for k in range(1,MAXK+1,2):
    h=(k-1)//2
    E=Q[k]
    assert E%2==1
    for n in range(8):
        assert a[n+k]-a[n]==E*B[n+h]
    s=sum(a[i]**2 for i in range(1,k+1))
    assert 64*s==5*k+G(a[k],a[k+1])
    assert gcd(s,E)==gcd(k,E)
    # All first eight windows are checked; this is not an infinite-gcd proof.
    gs=0
    for n in range(8):
        gs=gcd(gs,sum(b[i]**2 for i in range(n+1,n+k+1)))
    assert gs==4*gcd(k,E),(k,gs,4*gcd(k,E))
    hu=0
    for n in range(1,9):
        hu=gcd(hu,B[n+h]*(a[n+k]+a[n]))
    assert hu in (1,7)
print('VERIFY_OK')
print('odd_k_tested=251; range=1..501')
print('window_starts_tested=8_per_k')
print('integer_recurrence_and_telescoping=PASS')
print('odd_shift_factorization=PASS')
print('modulo_7_periodicity=PASS')
print('finite_gcd_and_endpoint_regressions=PASS')
print('infinite_proof=RESULT.md')
