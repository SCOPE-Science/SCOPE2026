"""Standalone finite tests for the derivation-dimension distribution of perfect evolution algebras.

Run using Python 3 standard library; source elements are square structure matrices
and full derivation linear systems (no graph-criterion shortcut).
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import factorial


def gl(n,q):
    v=1
    for j in range(n):
        v*=q**n-q**j
    return v


def matrix_rank(mat, p, width=None):
    if not mat:
        return 0
    a=[list(row) for row in mat]
    cols=width if width is not None else len(a[0]); rows=len(a)
    rank=0
    for col in range(cols):
        pivot=next((j for j in range(rank,rows) if a[j][col]%p),None)
        if pivot is None: continue
        a[rank],a[pivot]=a[pivot],a[rank]
        inv=pow(a[rank][col]%p,-1,p)
        for k in range(col,cols): a[rank][k]=(a[rank][k]*inv)%p
        for i in range(rank+1,rows):
            fac=a[i][col]%p
            if fac:
                for k in range(col,cols): a[i][k]=(a[i][k]-fac*a[rank][k])%p
        rank+=1
        if rank==rows: break
    return rank


def full_derivation_dim(a,p):
    n=len(a); equations=[]
    ix=lambda k,j:k*n+j
    for i in range(n):
        for j in range(i+1,n):
            for ell in range(n):
                row=[0]*(n*n)
                row[ix(j,i)]+=a[j][ell]
                row[ix(i,j)]+=a[i][ell]
                equations.append(row)
    for i in range(n):
        for ell in range(n):
            row=[0]*(n*n)
            for j in range(n): row[ix(ell,j)]+=a[i][j]
            row[ix(i,i)]-=2*a[i][ell]
            equations.append(row)
    return n*n-matrix_rank(equations,p,n*n)


def add(a,b):
    n=max(len(a),len(b)); return [ (a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)]

def mul_scalar(a,s):return [v*s for v in a]


def predicted(nmax,p,q):
    if p==2:
        return [[gl(n,q)]+[0]*n for n in range(nmax+1)]
    r=1; residue=2%p
    while residue!=1:
        residue=2*residue%p; r+=1
    mmax=nmax//r
    f=[Fraction(gl(m,q)**r,factorial(m)**r) for m in range(mmax+1)]
    l=[Fraction(0)]*(mmax+1)
    for m in range(1,mmax+1):
        l[m]=f[m]-sum(Fraction(j,m)*l[j]*f[m-j] for j in range(1,m))
    active_indices={r*m for m in range(1,mmax+1)}
    exp_series=[[Fraction(1)]]+[[Fraction(0)] for _ in range(nmax)]
    for n in range(1,nmax+1):
        acc=[Fraction(0)]
        for k in range(1,n+1):
            if k not in active_indices: continue
            poly=[Fraction(0)]*(len(exp_series[n-k])+1)
            for i,a in enumerate(exp_series[n-k]):
                poly[i]-=a
                poly[i+1]+=a
            acc=add(acc,mul_scalar(poly, Fraction(k,n)*l[k//r]/r))
        exp_series[n]=acc
    out=[]
    for n in range(nmax+1):
        total=[Fraction(0)]
        for a in range(n+1):
            total=add(total,mul_scalar(exp_series[n-a],Fraction(gl(a,q),factorial(a))))
        total=mul_scalar(total,factorial(n))
        assert all(v.denominator==1 for v in total),(n,total)
        ints=[int(v) for v in total]+[0]*(n+1-len(total))
        assert sum(ints)==gl(n,q),(n,p,q,ints,gl(n,q))
        out.append(ints)
    return out


def main():
    total=0
    configs=[(3,1),(3,2),(3,3),(5,1),(5,2),(7,1),(7,2),(2,1),(2,2),(2,3)]
    for p,n in configs:
        predicted_counts=predicted(n,p,p)[n]
        counts=Counter()
        for entries in product(range(p),repeat=n*n):
            a=[entries[i*n:(i+1)*n] for i in range(n)]
            if matrix_rank(a,p,n)!=n:continue
            counts[full_derivation_dim(a,p)]+=1
            total+=1
        actual=[counts[i] for i in range(n+1)]
        assert actual==predicted_counts,(p,n,actual,predicted_counts)
        print('CHECK',p,n,actual)
    assert predicted(4,3,3)[4]==[gl(4,3)-7920,7872,48,0,0]
    assert predicted(3,3,3)[3]==[gl(3,3)-24,24,0,0]
    assert predicted(4,5,5)[4][1]==6*4**4
    print('ALL_PERFECT_EVOLUTION_DERIVATION_PROFILE_CHECKS_PASSED',len(configs),total)
if __name__=='__main__': main()
