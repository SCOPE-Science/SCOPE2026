#!/usr/bin/env python3
"""Exhaustive finite-field checks of idempotent derivations of a filiform Leibniz algebra."""
import itertools

def fld(q):
    if q==4:
        def mul(a,b):
            r=0
            for i in range(2):
                if (b>>i)&1:r^=a<<i
            for j in (2,):
                if (r>>j)&1:r^=7<<(j-2)
            return r
        return lambda a,b:a^b,mul
    if q in (2,3,5): return lambda a,b:(a+b)%q, lambda a,b:(a*b)%q
    raise ValueError(q)

def matrices(n,params,q):
    add,mul=fld(q)
    a,c0,b=params[0:3]
    c=[c0]+list(params[3:])
    # n-1 x n-1 Jordan chain N on e2..en; H diagonal 0..n-2
    D=[[0]*n for _ in range(n)]
    D[0][0]=a
    D[n-1][0]=b
    for j in range(n-1):
        D[j+1][j+1]=add(c0,mul(a,j%q if q!=4 else j%2))
        for h in range(1,n-1-j):D[1+j+h][1+j]=c[h]
    return D

def matmul(A,B,q):
    n=len(A); add,mul=fld(q)
    return [[sum_field([mul(A[i][k],B[k][j]) for k in range(n)],add) for j in range(n)] for i in range(n)]

def sum_field(xs,add):
    z=0
    for a in xs:z=add(z,a)
    return z

def is_deriv(D,q):
    n=len(D); add,mul=fld(q)
    for i in range(n):
        for j in range(n):
            # [e_i,e_j] = e_{i+1} when j=0 and 1<=i<n-1
            left=[0]*n
            if j==0 and 1<=i<n-1: left=[D[k][i+1] for k in range(n)]
            rhs=[0]*n
            # [D(e_i),e_j]
            if j==0:
                for k in range(2,n):rhs[k]=add(rhs[k],D[k-1][i])
            # [e_i,D(e_j)]
            if 1<=i<n-1:rhs[i+1]=add(rhs[i+1],D[0][j])
            if left!=rhs:return False
    return True

def matrix_rank(A,q):
    add,mul=fld(q)
    neg=(lambda a:(-a)%q) if q!=4 else (lambda a:a)
    B=[row[:] for row in A]
    rank=0
    for col in range(len(B[0])):
        pivot=next((i for i in range(rank,len(B)) if B[i][col]!=0),None)
        if pivot is None:continue
        B[rank],B[pivot]=B[pivot],B[rank]
        scale=next(z for z in range(1,q) if mul(B[rank][col],z)==1)
        B[rank]=[mul(x,scale) for x in B[rank]]
        for i in range(len(B)):
            if i!=rank and B[i][col]:
                t=neg(B[i][col]);B[i]=[add(x,mul(t,y)) for x,y in zip(B[i],B[rank])]
        rank+=1
        if rank==len(B):break
    return rank

def check(n,q,full=False):
    k=(n-1)//2
    expected=(q+1)*(q**k+1) if q%2==0 else q+1
    count=0;hist={}
    for pars in itertools.product(range(q),repeat=n+1):
        D=matrices(n,pars,q)
        if not is_deriv(D,q):raise AssertionError(('deriv',n,q,pars))
        if matmul(D,D,q)==D:
            count+=1
            r=matrix_rank(D,q)
            hist[r]=hist.get(r,0)+1
    assert count==expected,(n,q,count,expected)
    predicted_hist={}
    def term(r,v):predicted_hist[r]=predicted_hist.get(r,0)+v
    term(0,1);term(n-1,q)
    if q%2==0:
        term(1+k,q**(k+1))
        term(1+((n-1)+1)//2,q**k)
    assert hist==predicted_hist,(n,q,hist,predicted_hist)
    if full:
        full_count=0;deriv_count=0
        for entries in itertools.product(range(q),repeat=n*n):
            D=[list(entries[n*i:n*(i+1)]) for i in range(n)]
            if is_deriv(D,q):
                deriv_count+=1
                if matmul(D,D,q)==D:full_count+=1
        assert deriv_count==q**(n+1) and full_count==count,(n,q,deriv_count,full_count,count)
    print(f'n={n} q={q} all_derivations={q**(n+1)} projections={count} rank_histogram={sorted(hist.items())} predicted={expected} '+('FULL_MATRIX_EXHAUSTION' if full else 'PARAMETER_EXHAUSTION'))

if __name__=='__main__':
    for n,q,full in [(4,2,True),(4,3,False),(4,4,False),(4,5,False),(5,2,False),(5,3,False),(5,4,False),(6,2,False),(6,3,False),(6,4,False),(7,2,False)]:check(n,q,full)
    print('FILIFORM_LEIBNIZ_IDEMPOTENT_DERIVATIONS_OK 11_CASES')
