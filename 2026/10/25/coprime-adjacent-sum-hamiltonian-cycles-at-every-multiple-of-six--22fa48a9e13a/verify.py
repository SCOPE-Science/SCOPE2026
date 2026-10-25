#!/usr/bin/env python3
"""Check an explicit cyclic arithmetic-permutation construction."""
from math import gcd

def small_cycle(m):
    if m==6:return [0,2,4,1,3,5]
    if m==9:return [0,2,7,5,8,6,4,1,3]
    assert m>=10
    if m%2==0:
        r=m//2
        return [0,2]+list(range(5,2*r-4,2))+[2*r-2,2*r-4,2*r-1,2*r-3]+list(range(2*r-6,3,-2))+[1,3]
    r=(m-1)//2
    return [0,2]+list(range(5,2*r-4,2))+[2*r-2,2*r,2*r-3,2*r-1]+list(range(2*r-4,3,-2))+[1,3]

def construct(n):
    assert n>=6 and n%6==0
    if n==6:return [0,4,2,1,3,5,6]
    m=n//2
    q=small_cycle(m)
    z=[0]
    for x in q[1:]:
        z.extend([n-x,x])
    z.append(n)
    j=z.index(m-3)
    assert z[j-1]==m+3
    z.insert(j,m)
    return z

def check(n):
    z=construct(n)
    assert len(z)==n+1 and z[0]==0 and z[-1]==n
    assert set(z)==set(range(n+1)),(n,len(z),len(set(z)))
    for a,b in zip(z,z[1:]+[z[0]]):
        assert gcd(a+b,n-1)==1 and gcd(a+b,n+1)==1,(n,a,b,a+b)
    if n>=24:
        q=small_cycle(n//2)
        assert len(q)==n//2 and set(q)==set(range(n//2)) and q[0]==0
        assert all(abs(a-b) in (2,3) for a,b in zip(q,q[1:]+q[:1])),(n,q)
    return z

def main():
    for n in range(6,6001,6):check(n)
    print('VERIFY_OK multiples_of_six=1000 n<=6000 explicit_permutations_verified, difference_2_3_cycle m>=12, exact_small_cases')
    print('n=24:',check(24))
if __name__=='__main__':main()
