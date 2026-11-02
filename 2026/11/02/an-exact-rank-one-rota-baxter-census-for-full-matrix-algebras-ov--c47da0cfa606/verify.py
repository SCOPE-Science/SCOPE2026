#!/usr/bin/env python3
"""Independent small-field census for the rank-one Rota--Baxter theorem.
All test configurations are exhaustive over field matrices unless noted.
Run: python3 verify.py
"""
from itertools import product
from math import prod


def field(q):
    assert q in (2,3,4,5)
    if q == 4:
        # Binary polynomial basis modulo T^2+T+1.
        add = lambda a,b: a ^ b
        def mul(a,b):
            z=0
            while b:
                if b&1:z ^= a
                b >>= 1
                a <<= 1
                if a&4:a ^= 7
            return z
    else:
        add = lambda a,b:(a+b)%q
        mul = lambda a,b:(a*b)%q
    def neg(x):
        for y in range(q):
            if add(x,y)==0:return y
        raise AssertionError
    return add,mul,neg


def matmul(A,B,n,add,mul):
    return tuple(sum_field((mul(A[i*n+k],B[k*n+j]) for k in range(n)),add)
                 for i in range(n) for j in range(n))


def sum_field(elements,add):
    s=0
    for x in elements:s=add(s,x)
    return s


def gl(n,q):
    return prod(q**n-q**i for i in range(n))


def gaussian(n,r,q):
    return prod(q**(n-i)-1 for i in range(r))//prod(q**(r-i)-1 for i in range(r))


def formula(n,q):
    nilp = 0
    for r in range(1,n//2+1):
        s=n-2*r
        class_size=gl(n,q)//(q**(r*r+2*r*s)*gl(r,q)*gl(s,q))
        assert class_size%(q-1)==0
        nilp += class_size//(q-1)*(q**((n-r)**2)-1)
    idem=sum(gaussian(n,r,q)*q**(r*(n-r))*2*(q**(r*(n-r))-1)
             for r in range(1,n))
    return (nilp, idem)


def direct_rb(A,B,AA,BA,AB,n,add,mul):
    for i in range(n):
      for j in range(n):
        fx=B[j*n+i]
        hx=AB[j*n+i]
        for k in range(n):
          for l in range(n):
            fy=B[l*n+k]
            gy=BA[l*n+k]
            lhs=mul(fx,fy)
            rhs=add(mul(fx,gy),mul(fy,hx))
            for a,aa in zip(A,AA):
                if mul(lhs,aa)!=mul(rhs,a):return False
    return True


def verify(n,q,all_direct):
    add,mul,neg=field(q)
    total=0; nilp=0; idem=0; direct_tests=0
    mats=product(range(q),repeat=n*n)
    Bs=list(product(range(q),repeat=n*n))
    for A in mats:
        if not any(A):continue
        # Select a single representative of each matrix line.
        first=next(x for x in A if x)
        if first!=1:continue
        AA=matmul(A,A,n,add,mul)
        lambdas=[z for z in range(q) if all(mul(z,x)==y for x,y in zip(A,AA))]
        if len(lambdas)!=1:continue
        lam=lambdas[0]
        for B in Bs:
            if not any(B):continue
            BA=matmul(B,A,n,add,mul)
            AB=matmul(A,B,n,add,mul)
            allowed=any(all(mul(mu,x)==y for x,y in zip(B,BA)) and
                        all(mul(add(lam,neg(mu)),x)==y for x,y in zip(B,AB))
                        for mu in range(q))
            if all_direct or allowed:
                assert direct_rb(A,B,AA,BA,AB,n,add,mul)==allowed
                direct_tests+=1
            if allowed:
                total+=1
                if lam==0:nilp+=1
                else:idem+=1
    target=formula(n,q)
    assert (nilp,idem)==target, (n,q,(nilp,idem),target)
    return (n,q,nilp,idem,total,direct_tests)


def main():
    results=[verify(2,2,True),verify(2,3,True),verify(2,4,True),
             verify(2,5,False),verify(3,2,False)]
    for r in results:print('FIELD_TEST',*r)
    print('RANK_ONE_MATRIX_RB_EXACT_CENSUS_OK',len(results),sum(r[-1] for r in results))

if __name__=='__main__':main()
