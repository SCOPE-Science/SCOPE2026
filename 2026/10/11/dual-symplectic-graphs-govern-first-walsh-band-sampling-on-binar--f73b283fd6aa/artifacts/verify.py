#!/usr/bin/env python3
"""Exact finite checks for quadratic Walsh restriction and its Seidel transfer.

All arithmetic is integral. No external packages are required.
"""
from collections import Counter
from itertools import combinations
from fractions import Fraction


def inverse_binary(rows, n):
    a = [rows[i] | (1 << (n+i)) for i in range(n)]
    for j in range(n):
        piv = next((r for r in range(j,n) if (a[r] >> j)&1), None)
        if piv is None: return None
        a[j],a[piv]=a[piv],a[j]
        for r in range(n):
            if r != j and ((a[r]>>j)&1): a[r] ^= a[j]
    assert [v & ((1<<n)-1) for v in a] == [1<<i for i in range(n)]
    return [v>>n for v in a]


def graph_rows(mask,n):
    edges=list(combinations(range(n),2)); rows=[0]*n
    for k,(i,j) in enumerate(edges):
        if (mask>>k)&1:
            rows[i]|=1<<j; rows[j]|=1<<i
    return rows


def quadratic(x, B, n, lin=0):
    v=(lin & x).bit_count()&1
    for i in range(n):
        if (x>>i)&1:
            v ^= (B[i] & x & ~((1<<(i+1))-1)).bit_count()&1
    return v


def seidel(A,n):
    return [[1 if i==0 or j==0 or not ((A[i-1]>>(j-1))&1) else -1
             for j in range(n+1)] for i in range(n+1)]


def matmul(a,b):
    n=len(a);return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def characteristic(a):
    n=len(a); powers=[[int(i==j) for j in range(n)] for i in range(n)]
    coeff=[1]
    for k in range(1,n+1):
        powers=matmul(powers,a)
        # Faddeev-LeVerrier recurrence from successive traces.
        # Keep the independent trace series for exact divisibility checks.
        if k==1: traces=[]
        traces.append(sum(powers[i][i] for i in range(n)))
        z=-sum(coeff[k-j]*traces[j-1] for j in range(1,k+1))
        assert z%k==0
        coeff.append(z//k)
    return tuple(coeff)


def rank(a):
    a=[[Fraction(v) for v in row] for row in a]
    r=0
    for j in range(len(a[0])):
        piv=next((i for i in range(r,len(a)) if a[i][j]),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r]; z=a[r][j]
        a[r]=[v/z for v in a[r]]
        for i in range(len(a)):
            if i != r:
                z=a[i][j]; a[i]=[u-z*v for u,v in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r


def test(A,n,lin):
    B=inverse_binary(A,n)
    assert B is not None and B==inverse_binary(A,n)
    m=n//2
    g=lambda x:quadratic(x,B,n,lin)
    q0=[x for x in range(1<<n) if not g(x)]
    gauss=sum(1-2*g(x) for x in range(1<<n))
    assert abs(gauss)==1<<m
    eps=gauss//(1<<m)
    idx=[0]+[1<<i for i in range(n)]
    # A=B^{-1}; dual quadratic is g(Au) for u in the Fourier index space.
    ds=[]
    for u in idx:
        au=0
        for i in range(n):
            if (A[i]&u).bit_count()&1: au |=1<<i
        ds.append(1-2*g(au))
    S=seidel(A,n)
    actual=[[sum(1-2*((x & (u^v)).bit_count()&1) for x in q0)
             for v in idx] for u in idx]
    factor=1<<(m-1)
    for i in range(n+1):
        for j in range(n+1):
            expected=factor*((1<<m)*(i==j)+eps*ds[i]*S[i][j]*ds[j])
            assert actual[i][j]==expected,(n,A,lin,i,j,actual[i][j],expected)
    assert len(q0)==(1<<(n-1))+eps*(1<<(m-1))
    # Difference-set property: |Q0 intersect (Q0+h)| is independent of h!=0.
    z=set(q0)
    for h in range(1,1<<n):
        assert sum(x^h in z for x in q0)==(1<<(n-2))+eps*(1<<(m-1))
    rr=rank(actual)
    assert rr== (1 if m==1 and eps==-1 else n+1)
    return eps


def run():
    counts=Counter();cases=0; epsilon_counts=Counter()
    expected={
       (1,-5,0,24,-16,-16):15,
       (1,-5,0,20,0,-16):12,
       (1,-5,0,40,-80,48):1,
    }
    for n in (2,4):
        for mask in range(1 << (n*(n-1)//2)):
            A=graph_rows(mask,n)
            if inverse_binary(A,n) is None:continue
            if n==4: counts[characteristic(seidel(A,n))]+=1
            for lin in range(1<<n):
                epsilon_counts[(n,test(A,n,lin))]+=1;cases+=1
    assert counts==expected,(counts,expected)
    assert epsilon_counts[(2,-1)] and epsilon_counts[(2,1)]
    assert epsilon_counts[(4,-1)] and epsilon_counts[(4,1)]
    # Six-dimensional examples across nonmatching graphs and both Arf signs.
    n=6; found={-1:0,1:0}
    for mask in range(1<<15):
        A=graph_rows(mask,n)
        if inverse_binary(A,n) is None:continue
        for lin in (0,1,3,7):
            ep=test(A,n,lin);found[ep]+=1;cases+=1
        if min(found.values())>=6:break
    assert min(found.values())>=6
    print(f'VERIFY_OK exact_quadrics={cases} four_vertex_graphs=28 three_Seidel_polynomials=15,12,1 difference_set_and_rank=PASS signed_Gram_identity=PASS')

if __name__=='__main__':run()
