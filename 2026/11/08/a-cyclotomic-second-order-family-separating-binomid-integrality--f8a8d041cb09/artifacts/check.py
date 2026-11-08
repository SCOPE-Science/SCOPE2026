#!/usr/bin/env python3
"""Finite corroboration of an exact classification of binomid recurrences.
No finite output is offered as a substitute for the all-index proof.
"""
from math import prod

def seq(q,t,nmax):
    x=[-(t+1),q]
    for n in range(nmax-1): x.append(-q*x[-1]-q*q*x[-2])
    return x

def exact_binomid(q,t,N):
    x=seq(q,t,N)
    F=[1]
    for i in range(1,N+1): F.append(F[-1]*x[i])
    return all((F[n]%(F[k]*F[n-k])==0) for n in range(N+1) for k in range(n+1))

def exact_divisible(q,t,N):
    x=seq(q,t,N)
    return all(x[n]%x[m]==0 for m in range(1,N+1) for n in range(m,N+1,m))

count=0
for q in range(2,15):
    for t in range(1,151):
        # Test actual large-integer products, not just the symbolic residue formula.
        b=exact_binomid(q,t,23)
        d=exact_divisible(q,t,23)
        assert b==(q**4%t==0),('binomid',q,t,b)
        assert d==(q**2%t==0),('divisible',q,t,d)
        x=seq(q,t,23)
        assert all(x[3*j+1]==q**(3*j+1) for j in range(7))
        assert all(x[3*j+2]==t*q**(3*j+2) for j in range(7))
        assert all(x[3*j+3]==-(t+1)*q**(3*j+3) for j in range(7))
        count+=1

for q,t in ((2,8),(2,16),(3,27),(6,216),(11,1331)):
    assert exact_binomid(q,t,100) and not exact_divisible(q,t,100)

x=seq(2,8,7)
assert x[:7]==[-9,2,32,-72,16,256,-576]
assert (x[3]*x[4])//(x[1]*x[2]) == -18
assert x[4]%x[2] != 0
print(f'PASS: {count} full parameter pairs, exact generalized binomials and index divisibility through n=23')
print('PASS: five nondivisible binomid families through n=100')
print('PASS: characteristic recurrence and closed form for all tested indices')
print('PASS: minimal witness q=2,t=8: f1=2,f2=32,f3=-72,f4=16, [4,2]_f=-18')
