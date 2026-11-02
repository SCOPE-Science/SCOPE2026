#!/usr/bin/env python3
"""Reproduce finite checks for a binomial-parity Mersenne-stratum valuation theorem."""

def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]

def mpow(a,n):
    z=[[int(i==j) for j in range(4)] for i in range(4)]
    while n:
        if n&1: z=mm(z,a)
        a=mm(a,a);n//=2
    return z

def mulvec(a,v):
    return [sum(a[i][j]*v[j] for j in range(4)) for i in range(4)]

def v2(n):
    assert n>0
    return (n&-n).bit_length()-1

M=[[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,-1,1,1]]
A=mpow(M,10)
assert A==[[9,-4,8,12],[12,-3,8,20],[20,-8,17,28],[28,-8,20,45]]
B=[[(A[i][j]-int(i==j))//4 for j in range(4)] for i in range(4)]
assert all((A[i][j]-int(i==j))%4==0 for i in range(4) for j in range(4))
s={0:1,1:2,2:2,3:3}
for n in range(-1,-7,-1):
    s[n]=s[n+4]-s[n+3]-s[n+2]+s[n+1]
assert (s[-6],s[-1])==(0,0)
assert (mulvec(B,[s[-6+i] for i in range(4)])[0],mulvec(B,[s[-1+i] for i in range(4)])[0])==(1,9)

for n in range(4,1401):
    s[n]=s[n-1]+s[n-2]-s[n-3]+s[n-4]
for r in range(1,140):
    for shift in (-6,-1):
        index=10*r+shift
        assert v2(s[index])==2+v2(r),(r,shift,s[index])

def choose_odd(n,k):
    return 0<=k<=n and (k&~n)==0

def binomial_parity_sum(n):
    return sum(1 for k in range(n+1) if choose_odd(n,k) and choose_odd(n+5*k,2*k))
for ell in (0,1,2,3,4,5,6,7,8,9,14):
    assert binomial_parity_sum((1<<ell)-1)==s[ell],ell
print('VERIFY_OK matrix10=1 negative_zeros=-6,-1 leading_quotients=1,9 recurrence_instances=278 binary_parity_ell=0..9,14 first_cases=1,4,9,14')
