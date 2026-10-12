#!/usr/bin/env python3
from itertools import product
from math import gcd

def phi(n):
    return sum(1 for k in range(1,n+1) if gcd(k,n)==1)

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def scalar_count(q,n):
    return sum(phi(d)*(q-1-min(d,n-1)) for d in divisors(q-1) if d>1)

def direct_scalar_count_prime(p,n):
    c=0
    for a in range(1,p):
        if a==1: continue
        for b in range(1,p):
            vals=[a-1]+[(pow(a,j,p)*b-1)%p for j in range(n-1)]
            if all(v%p for v in vals): c+=1
    return c

def predicted_fpf(q,n): return q**(2*n-3)*scalar_count(q,n)
def aut_order(q,n): return q**(2*n-3)*(q-1)**2

# Independent exhaustive recovery of Aut(L_4(F_2)) from all 2^16 matrices.
def det_mod(A,p):
    N=len(A); M=[row[:] for row in A]; det=1
    for c in range(N):
        piv=next((r for r in range(c,N) if M[r][c]%p),None)
        if piv is None:return 0
        if piv!=c:M[c],M[piv]=M[piv],M[c];det=-det
        v=M[c][c]%p; det=det*v%p; iv=pow(v,-1,p)
        for r in range(c+1,N):
            f=M[r][c]*iv%p
            for j in range(c,N):M[r][j]=(M[r][j]-f*M[c][j])%p
    return det%p

def bracket4(x,y,p):
    return [0,0,(x[0]*y[1]-x[1]*y[0])%p,(x[0]*y[2]-x[2]*y[0])%p]
def col(M,j): return [M[i][j] for i in range(len(M))]
def lincomb(M,x,p): return [sum(M[i][j]*x[j] for j in range(len(M)))%p for i in range(len(M))]
def is_aut4(M,p):
    if det_mod(M,p)==0:return False
    E=[[1 if i==j else 0 for i in range(4)] for j in range(4)]
    for i in range(4):
      for j in range(4):
        if lincomb(M,bracket4(E[i],E[j],p),p)!=bracket4(col(M,i),col(M,j),p):return False
    return True

def brute_f2():
    n=f=0
    for bits in product(range(2), repeat=16):
        M=[list(bits[4*i:4*i+4]) for i in range(4)]
        if is_aut4(M,2):
            n+=1
            MI=[[ (M[i][j]-(1 if i==j else 0))%2 for j in range(4)] for i in range(4)]
            if det_mod(MI,2):f+=1
    assert n==aut_order(2,4)==32 and f==predicted_fpf(2,4)==0
    return n,f

if __name__=='__main__':
    print('F2 exhaustive L4',brute_f2())
    for p in [2,3,5,7,11]:
        for n in [4,5,6,8]:
            d=direct_scalar_count_prime(p,n)
            s=scalar_count(p,n)
            assert d==s
            print(f'p={p} n={n} scalar={s} aut={aut_order(p,n)} fpf={predicted_fpf(p,n)}')
    # Non-prime prime powers exercise the divisor formula directly; no field implementation is needed
    # because the count only uses the cyclic multiplicative group of order q-1.
    for q in [4,8,9,16,25]:
        for n in [4,8,12]:
            print(f'q={q} n={n} scalar={scalar_count(q,n)} predicted_fpf={predicted_fpf(q,n)}')
    print('VERIFY_OK')
