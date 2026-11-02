"""Standalone finite checks for orders of bipartite symplectic torus shears.

Run: python verify.py
Requires numpy; the mathematical proof does not depend on this script.
"""
import math
import numpy as np
from itertools import product


def predicted(a, b, s):
    assert a >= 1 and b >= 1 and s >= 1
    z = a*b
    def v2(x):
        return (x & -x).bit_length()-1
    if a % 2 == b % 2 == 0:
        return 1 << s
    if z % 2 == 0:
        if z % 4 == 0:
            return 1 << (s+1)
        return 4 * (1 << max(0, s-v2(z+2)))
    if z % 4 == 1:
        return 3 * (1 << max(0, s-v2(z+3)))
    if s == 1:
        return 3
    return 6 * (1 << max(0, s-1-v2(z+1)))


def matrix(a,b,m):
    n=a+b
    A=np.zeros((n,n),dtype=np.int64)
    A[:a,a:]=1
    A[a:,:a]=1
    I=np.eye(n,dtype=np.int64)
    return np.block([[I,A],[A,(I+A@A)%m]])%m


def power(M,k,m):
    d=M.shape[0]
    Z=np.eye(d,dtype=np.int64)
    while k:
        if k&1: Z=Z@M%m
        k//=2
        if k: M=M@M%m
    return Z


def step(x,a,b,m):
    n=a+b
    out=[]
    pa=sum(x[:a])%m
    pb=sum(x[a:n])%m
    qa=sum(x[n:n+a])%m
    qb=sum(x[n+a:])%m
    out.extend((v+qb)%m for v in x[:a])
    out.extend((v+qa)%m for v in x[a:n])
    out.extend((v+pb+b*qa)%m for v in x[n:n+a])
    out.extend((v+pa+a*qb)%m for v in x[n+a:])
    return tuple(out)


def main():
    n_mat=0
    n_scalar=0
    for a in range(1,8):
        for b in range(1,8):
            for s in range(1,11):
                mod=1<<s
                M=matrix(a,b,mod)
                L=predicted(a,b,s)
                I=np.eye(2*(a+b),dtype=np.int64)
                assert np.array_equal(power(M,L,mod),I), (a,b,s,L,'not identity')
                for prime in (2,3):
                    if L%prime == 0:
                        assert not np.array_equal(power(M,L//prime,mod),I), (a,b,s,L,prime,'not minimal')
                n_mat+=1
                if a+b<=6:
                    q0,q1=0,1
                    pprev=0
                    # Check the independent scalar criterion for several arbitrary exponents.
                    for t in range(1,16):
                        z=a*b
                        qnext=(z+2)*q1-q0
                        p=(q1-q0-1)//z
                        scalar=(q1%mod==0 and math.gcd(a,b)*p%mod==0)
                        direct=np.array_equal(power(M,t,mod),I)
                        assert scalar==direct,(a,b,s,t,scalar,direct)
                        q0,q1=q1,qnext
                        n_scalar+=1
    n_orbits=0
    for a,b,m in [(1,1,2),(1,1,4),(1,1,8),
                  (1,2,2),(1,2,4),(1,2,8),
                  (1,3,2),(1,3,4),(2,2,2),(2,2,4),
                  (2,3,2),(3,3,2)]:
        L=predicted(a,b,int(math.log2(m)))
        countmax=0
        for v in product(range(m),repeat=2*(a+b)):
            w=step(v,a,b,m)
            k=1
            while w!=v:
                w=step(w,a,b,m); k+=1
                assert k<=L
            assert L%k==0
            if k==L: countmax+=1
            n_orbits+=1
        assert countmax>0,(a,b,m,'no full-length orbit')
    print('VERIFIED: 490 matrix-order instances for a,b=1..7 and s=1..10')
    print(f'VERIFIED: {n_scalar} matrix-vs-recurrence congruence comparisons')
    print(f'VERIFIED: {n_orbits} directly enumerated initial configurations, all periodic')
    print('VERIFIED: each enumerated model realizes a cycle of full predicted order')

if __name__=='__main__':
    main()
