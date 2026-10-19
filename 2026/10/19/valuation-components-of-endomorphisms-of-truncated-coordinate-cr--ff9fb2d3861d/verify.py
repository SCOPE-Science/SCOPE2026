#!/usr/bin/env python3
"""Independent finite-field and valuation-lattice checks for truncated coordinate-cross endomorphisms."""
from itertools import product
from math import factorial

def is_zero_prod(a,b,p):
    d=len(a)
    return all(sum(a[i]*b[j-i] for i in range(0,j+1))%p==0 for j in range(d-1))

def good_column(col,p):
    return all(is_zero_prod(col[i],col[j],p) for i in range(len(col)) for j in range(i+1,len(col)))

def predicted_column(r,d,q):
    N=d+1
    h=N//2
    upper=h if N%2 else h-1
    return q**(r*h)+r*(q-1)*sum(q**(N-1+(r-2)*a) for a in range(1,upper+1))

def components(r,d):
    N=d+1;h=N//2
    C=set()
    for i in range(r):
        for a in range(1,h+1 if N%2 else h):
            C.add(tuple(a if j==i else N-a for j in range(r)))
    if N%2==0:C.add((h,)*r)
    return C

def val(a):
    return next((i+1 for i,x in enumerate(a) if x),len(a)+1)

def rank_mod(A,p):
    B=[list(row) for row in A]; nr=len(B);nc=len(B[0]); k=0
    for j in range(nc):
        i=next((i for i in range(k,nr) if B[i][j]%p),None)
        if i is None:continue
        B[k],B[i]=B[i],B[k]; inv=pow(B[k][j],-1,p)
        B[k]=[(z*inv)%p for z in B[k]]
        for i2 in range(nr):
            if i2!=k:
                c=B[i2][j];B[i2]=[(a-c*b)%p for a,b in zip(B[i2],B[k])]
        k+=1
        if k==nr:break
    return k

def main():
    cases=[(2,2,2),(2,3,2),(2,4,2),(3,2,2),(3,3,2),(4,2,2),(2,2,3),(2,3,3),(3,2,3),(2,2,5)]
    for r,d,p in cases:
        pol=list(product(range(p),repeat=d))
        count=0
        for col in product(pol, repeat=r):
            count+=good_column(col,p)
        expected=predicted_column(r,d,p)
        assert count==expected,(r,d,p,count,expected)
        print('COLUMN',r,d,p,count)
    whole_cases=[(2,2,2),(2,2,3),(2,3,2),(3,2,2)]
    for r,d,p in whole_cases:
        pol=list(product(range(p),repeat=d))
        possibilities=list(product(pol,repeat=r))
        good=[x for x in possibilities if good_column(x,p)]
        # Build all r output columns. This enumerates actual generator images, not a power of the column-count formula.
        nEnd=nAut=0
        for cols in product(good,repeat=r):
            nEnd+=1
            L=[[cols[j][i][0] for j in range(r)] for i in range(r)]
            if rank_mod(L,p)==r:nAut+=1
        expected_end=predicted_column(r,d,p)**r
        expected_aut=factorial(r)*(p-1)**r*p**(r*(d+r-2))
        assert (nEnd,nAut)==(expected_end,expected_aut),(r,d,p,nEnd,nAut,expected_end,expected_aut)
        print('FULL',r,d,p,nEnd,nAut)
    # Exhaust all order-vector strata and independently obtain coordinatewise-minimal strata.
    for r in range(2,6):
        for d in range(2,7):
            N=d+1
            admissible={a for a in product(range(1,N+1),repeat=r)
                        if all(a[i]+a[j]>=N for i in range(r) for j in range(i+1,r))}
            minimal={a for a in admissible if not any(all(b[i]<=a[i] for i in range(r)) and b!=a for b in admissible)}
            predicted=components(r,d)
            assert minimal==predicted,(r,d,minimal,predicted)
            assert ((len(minimal)==r*(N//2)) if N%2 else (len(minimal)==r*(N//2-1)+1))
            dims=[sum(N-a for a in x) for x in minimal]
            assert (len(set(dims))==1)==(r==2 or d==2)
    print('VAL_LATTICE_OK')
    print('VERIFY_OK_CROSS_ENDOMORPHISMS')

if __name__=='__main__':main()
