#!/usr/bin/env python3
"""Standalone finite-field checks for triangular zero-product strata."""
from collections import Counter, defaultdict
from itertools import product


def operations(q):
    if q in (2, 3, 5):
        return (lambda a,b:(a+b)%q), (lambda a,b:a*b%q)
    if q == 4:  # GF(2)[z]/(z*z+z+1), elements 0,1,z,z+1
        def mul(a,b):
            x=0
            for bit in range(2):
                if (b>>bit)&1:
                    x ^= a<<bit
            if x&8: x ^= 0b1110  # z^3 = z^2 + z -> reduction
            if x&4: x ^= 0b111   # z^2 = z + 1
            return x
        return (lambda a,b:a^b),mul
    raise ValueError(q)


def rank(M,q):
    add,mul=operations(q)
    subtract=(lambda a,b:(a-b)%q) if q in (2,3,5) else (lambda a,b:a^b)
    A=[row[:] for row in M]
    nr=len(A); nc=len(A[0]) if A else 0
    inv={a:next(b for b in range(1,q) if mul(a,b)==1) for a in range(1,q)}
    k=0
    for j in range(nc):
        p=next((i for i in range(k,nr) if A[i][j]!=0),None)
        if p is None:continue
        A[k],A[p]=A[p],A[k]
        v=inv[A[k][j]]
        for c in range(j,nc): A[k][c]=mul(A[k][c],v)
        for i in range(k+1,nr):
            t=A[i][j]
            for c in range(j,nc): A[i][c]=subtract(A[i][c],mul(t,A[k][c]))
        k+=1
        if k==nr:break
    return k


def matrices(n,q):
    positions=[(i,j) for i in range(n) for j in range(i,n)]
    for values in product(range(q),repeat=len(positions)):
        A=[[0]*n for _ in range(n)]
        for (i,j),v in zip(positions,values):A[i][j]=v
        yield A


def ann_index(A,q):
    n=len(A)
    return sum(j-rank([r[:j] for r in A[:j]],q) for j in range(1,n+1))


def recurrence(n,q):
    D={(0,0):1}
    for j in range(1,n+1):
        E=defaultdict(int)
        for (k,h),num in D.items():
            E[k,h+k]+=num*(q**j-q**(j-1-k))
            E[k+1,h+k+1]+=num*q**(j-1-k)
        D=E
    return Counter({h:sum(v for (k,hh),v in D.items() if hh==h)
                    for k,h in D})


def zero_product(A,B,q):
    add,mul=operations(q);n=len(A)
    for i in range(n):
        for j in range(i,n):
            s=0
            for k in range(i,j+1): s=add(s,mul(A[i][k],B[k][j]))
            if s:return False
    return True


def check(n,q,check_pairs=False):
    pred=recurrence(n,q)
    direct=Counter(ann_index(A,q) for A in matrices(n,q))
    assert direct==pred,(n,q,pred,direct)
    m=n*(n+1)//2
    assert sum(pred.values())==q**m
    assert pred[0]==(q-1)**n*q**(n*(n-1)//2)
    assert pred[m]==1
    if n>=2:assert pred[m-1]==q**n-1
    count=sum(v*q**h for h,v in pred.items())
    if check_pairs:
        mats=list(matrices(n,q))
        brute=sum(zero_product(A,B,q) for A in mats for B in mats)
        assert count==brute,(n,q,count,brute)
    return count,len(direct)


def top_degree(n):
    D={0:(0,1)}
    for j in range(1,n+1):
        E={}
        for k,(d,c) in D.items():
            for kn,increment in ((k,j+k),(k+1,j)):
                v=d+increment
                if kn not in E or E[kn][0]<v:E[kn]=(v,c)
                elif E[kn][0]==v:E[kn]=(v,E[kn][1]+c)
        D=E
    degree=max(v[0] for v in D.values())
    leading=sum(c for d,c in D.values() if d==degree)
    return degree,leading


def main():
    results=[]
    for n,q,pairs in ((1,2,True),(2,2,True),(2,3,True),(2,4,True),
                      (3,2,True),(3,3,False),(3,4,False),(4,2,False),
                      (5,2,False)):
        z,num=check(n,q,pairs)
        results.append((n,q,z,num,pairs))
    for n in range(1,41):
        d,c=top_degree(n)
        assert (d,c)==(n*(n+1)//2+n*n//4, 1 if n%2==0 else 2)
    for n,q,z,t,pair in results:
        print(f'n={n},q={q}: profiles={t},ordered_zero_products={z},literal_pair_test={pair}')
    print('VERIFY_OK_TRIANGULAR_ZERO_PRODUCTS 9_FINITE_CASES 40_TOP_DEGREES')

if __name__=='__main__':main()
