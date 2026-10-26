#!/usr/bin/env python3
"""Self-contained exact enumerator and certificate for three-colour rich-neighbour cycle edge-colourings."""
from itertools import product
from collections import deque

SIGNS=(-1,1)
STATES=[(a,b,c,r) for (a,b,c) in product(SIGNS,repeat=3) for r in range(3)]
INDEX={v:i for i,v in enumerate(STATES)}
SIZE=len(STATES)

def adjacency():
    M=[[0]*SIZE for _ in range(SIZE)]
    for i,(a,b,c,r) in enumerate(STATES):
        for d in SIGNS:
            if a==b or c==d:
                M[i][INDEX[(b,c,d,(r+d)%3)]]+=1
    return M

def matmul(A,B):
    n=len(A)
    C=[[0]*n for _ in range(n)]
    for i in range(n):
        ci=C[i]
        for k,ak in enumerate(A[i]):
            if ak:
                for j,bkj in enumerate(B[k]):
                    if bkj:ci[j]+=ak*bkj
    return C

def trace(A):return sum(A[i][i] for i in range(len(A)))

def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):c[i+j]+=u*v
    return c

def brute(n):
    count=0
    for c in product(range(3),repeat=n):
        if any(c[i]==c[(i+1)%n] for i in range(n)):continue
        rich=[c[(i-1)%n]!=c[(i+1)%n] for i in range(n)]
        if all(rich[(i-1)%n] or rich[(i+1)%n] for i in range(n)):
            count+=1
    return count

def reachable(M,initial):
    seen={initial};todo=deque([initial])
    while todo:
        i=todo.popleft()
        for j,x in enumerate(M[i]):
            if x and j not in seen:seen.add(j);todo.append(j)
    return len(seen)

def verify():
    M=adjacency()
    assert SIZE==24
    assert all(reachable(M,i)==SIZE for i in range(SIZE))
    print('strongly_connected_states=24')
    # Newton identities recover the exact integer characteristic polynomial.
    powers=[];A=[[int(i==j) for j in range(SIZE)] for i in range(SIZE)]
    for n in range(1,25):
        A=matmul(A,M);powers.append(trace(A))
    coef=[1]
    for k in range(1,25):
        numerator=sum(coef[k-j]*powers[j-1] for j in range(1,k+1))
        assert numerator%k==0
        coef.append(-(numerator//k))
    factor=[1]
    for pol,multiplicity in [([1,-1],1),([1,1],1),([1,0,1],1),([1,-1,-1],1),([1,-1,1],1),([1,1,1,0,1,-1,-1,0,1],2)]:
        for _ in range(multiplicity):
            factor=poly_mul(factor,pol)
    assert factor==coef,(coef,factor)
    print('characteristic_polynomial_factorization=verified_exact_integer')
    for n in range(3,11):
        assert powers[n-1]==brute(n),(n,powers[n-1],brute(n))
    print('direct_labeled_color_enumeration_n=3..10: matched')
    assert powers[2]>0 and powers[4]>0
    print('closed_walk_lengths=3,5; primitive=yes')
    for n in range(3,25):
        print('N(%d)=%d'%(n,powers[n-1]))
    print('VERIFY_OK')

if __name__=='__main__':verify()
