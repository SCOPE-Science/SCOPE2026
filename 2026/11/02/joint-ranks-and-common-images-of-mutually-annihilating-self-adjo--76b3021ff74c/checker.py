"""Finite-field verification of rank-resolved zero-product self-adjoint tuples.

Run: python selfadjoint_zero_product_checker.py
Python standard library only. Exhausts all self-adjoint operators in specified small spaces,
using the original matrix identities, and compares rank-and-image-span distributions.
"""
from collections import Counter
from itertools import product
from math import prod


def field(q):
    if q != 9:
        return [[(a+b)%q for b in range(q)] for a in range(q)], [[(a*b)%q for b in range(q)] for a in range(q)]
    add, mul = [[0]*9 for _ in range(9)], [[0]*9 for _ in range(9)]
    for a in range(9):
        x,y=a%3,a//3
        for b in range(9):
            u,v=b%3,b//3
            add[a][b]=((x+u)%3)+3*((y+v)%3)
            mul[a][b]=((x*u+2*y*v)%3)+3*((x*v+y*u)%3)
    return add,mul


def gaussian(a, q, add, mul):
    a=[list(row) for row in a]
    if not a:return 0
    nr,nc=len(a),len(a[0]);row=0
    for col in range(nc):
        piv=next((i for i in range(row,nr) if a[i][col]),None)
        if piv is None:continue
        a[row],a[piv]=a[piv],a[row]
        inv=next(k for k in range(1,q) if mul[a[row][col]][k]==1)
        a[row]=[mul[inv][z] for z in a[row]]
        for rr in range(row+1,nr):
            if a[rr][col]:
                fac=a[rr][col]
                a[rr]=[add[x][neg(mul[fac][y],q)] for x,y in zip(a[rr],a[row])]
        row+=1
        if row==nr:break
    return row


def neg(a,q):
    if q!=9:return (-a)%q
    return (-a%3)+3*(-(a//3)%3)


def dotmat(a,b,n,add,mul):
    out=[0]*(n*n)
    for i in range(n):
        for k in range(n):
            x=a[i*n+k]
            if x:
                for j in range(n):
                    y=mul[x][b[k*n+j]]
                    out[i*n+j]=add[out[i*n+j]][y]
    return tuple(out)


def transpose_columns(a,n):
    return [[a[i*n+j] for j in range(n)] for i in range(n)]


def qbinom(n,k,q):
    if k<0 or k>n:return 0
    num=den=1
    for i in range(k):num*=q**(n-i)-1;den*=q**(i+1)-1
    return num//den


def nonsingular_symmetric(r,q):
    if r==0:return 1
    h=r//2
    return (q**(h*(h+1)))*prod(q**(2*i-1)-1 for i in range(1,h+1+(r%2)))


def symmetric_rank_count(d,r,q):
    return qbinom(d,r,q)*nonsingular_symmetric(r,q)


def isotropic_subspace_count(n,t,q,sign):
    if t==0:return 1
    num=den=1
    for i in range(t):
        d=n-2*i
        if d%2:
            points=(q**(d-1)-1)//(q-1)
        else:
            points=(q**(d-1)-1)//(q-1)+sign*q**((d-2)//2)
        num*=points;den*=(q**(t-i)-1)//(q-1)
    assert num%den==0
    return num//den


def predicted(n,q,sign,m):
    w=(n-1)//2 if n%2 else (n//2 if sign==1 else n//2-1)
    result=Counter()
    for t in range(w+1):
        iso=isotropic_subspace_count(n,t,q,sign)
        for ranks in product(range(t+1),repeat=m):
            inner=0
            for j in range(t+1):
                coeff=qbinom(t,j,q)*((-1)**(t-j))*q**((t-j)*(t-j-1)//2)
                inner+=coeff*prod(symmetric_rank_count(j,r,q) for r in ranks)
            if inner:
                assert inner>0,(t,ranks,inner)
                result[(t,*ranks)]+=iso*inner
    return result


def gram(n,kind):
    g=[[0]*n for _ in range(n)]
    for i in range(0,n-1,2):
        if kind=='minus' and i==n-2:break
        g[i][i+1]=g[i+1][i]=1
    if n%2:g[n-1][n-1]=1
    elif kind=='minus':g[-2][-2]=g[-1][-1]=1
    return tuple(x for row in g for x in row)


def verify(n,q,kind):
    add,mul=field(q);g=gram(n,kind)
    sign=-1 if kind=='minus' else 1
    if kind=='odd':sign=1
    assert dotmat(g,g,n,add,mul)==tuple(1 if i==j else 0 for i in range(n) for j in range(n))
    zero=(0,)*(n*n)
    matrix_data=[]
    for coeff in product(range(q),repeat=n*(n+1)//2):
        s=[0]*(n*n);idx=0
        for i in range(n):
            for j in range(i,n):
                s[i*n+j]=s[j*n+i]=coeff[idx];idx+=1
        a=dotmat(g,s,n,add,mul)
        if dotmat(a,a,n,add,mul)==zero:
            rank=gaussian(transpose_columns(a,n),q,add,mul)
            matrix_data.append((a,rank))
    hist1=Counter((r,r) for _,r in matrix_data)
    assert hist1==predicted(n,q,sign,1),(n,q,kind,hist1,predicted(n,q,sign,1))
    hist2=Counter()
    for a,r in matrix_data:
        for b,s in matrix_data:
            if dotmat(a,b,n,add,mul)!=zero:continue
            assert dotmat(b,a,n,add,mul)==zero
            concat=[[a[i*n+j] for j in range(n)]+[b[i*n+j] for j in range(n)] for i in range(n)]
            t=gaussian(concat,q,add,mul)
            hist2[(t,r,s)]+=1
    pred2=predicted(n,q,sign,2)
    assert hist2==pred2,(n,q,kind,(hist2-pred2),(pred2-hist2))
    return len(matrix_data),sum(hist2.values()),dict(sorted(Counter({r:sum(v for (t,rr),v in hist1.items() if r==rr) for r in range(n+1)}).items())),len(hist2)


def main():
    checks=[(2,3,'plus'),(2,3,'minus'),(3,3,'odd'),(3,5,'odd'),(4,3,'plus'),(4,3,'minus'),(2,9,'plus')]
    for n,q,kind in checks:
        operators,pairs,ranks,cells=verify(n,q,kind)
        print(f'n={n} q={q} type={kind} square_zero={operators} ordered_zero_product_pairs={pairs} ranks={ranks} nonzero_rank_span_cells={cells}')
    print('SELFADJOINT_ZERO_PRODUCT_RANK_CENSUS_OK 7_EXHAUSTIVE_CONFIGURATIONS')

if __name__=='__main__':main()
