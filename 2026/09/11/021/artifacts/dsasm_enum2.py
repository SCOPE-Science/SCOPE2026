from collections import Counter

def gen_rows_below(below):
    m = len(below)-1
    a = [0]*m
    def rec(j, lo):
        if j==m:
            yield tuple(a); return
        hi = below[j+1]
        start = max(lo, below[j])
        for v in range(start, hi+1):
            a[j]=v
            yield from rec(j+1, v+1)
    yield from rec(0, 1)

def gen_triangles(n):
    if n==1:
        yield ((1,),); return
    rows=[None]*n
    rows[n-1]=tuple(range(1,n+1))
    def rec2(k):
        # rows[k] set; choose rows[k-1]; k>=1
        if k==1:
            b=rows[1]
            for v in range(b[0], b[1]+1):
                rows[0]=(v,)
                yield tuple(rows)
            return
        for a in gen_rows_below(list(rows[k])):
            rows[k-1]=a
            yield from rec2(k-1)
    yield from rec2(n-1)

def tri_to_asm(tri):
    n=len(tri)
    A=[[0]*n for _ in range(n)]
    prev=set()
    for i,row in enumerate(tri):
        cur=set(row)
        for j in range(n):
            A[i][j]= (1 if (j+1 in cur) else 0)-(1 if (j+1 in prev) else 0)
        prev=cur
    return A

def check_asm(A):
    n=len(A)
    for i in range(n):
        # row nonzero alternation 1,-1,...,1
        nz=[A[i][j] for j in range(n) if A[i][j]!=0]
        if not nz or nz[0]!=1 or nz[-1]!=1: return False
        for k in range(len(nz)-1):
            if nz[k]==nz[k+1]: return False
        if sum(A[i])!=1: return False
    for j in range(n):
        nz=[A[i][j] for i in range(n) if A[i][j]!=0]
        if not nz or nz[0]!=1 or nz[-1]!=1: return False
        for k in range(len(nz)-1):
            if nz[k]==nz[k+1]: return False
        if sum(A[i][j] for i in range(n))!=1: return False
    return True

def stats_direct(A):
    n=len(A)
    M=sum(1 for i in range(n) for j in range(n) if A[i][j]==-1)
    I=sum(A[i][j]*A[ip][jp] for i in range(n) for ip in range(i+1,n) for j in range(n) for jp in range(j+1))
    return I,M

def stats_struct(A):
    n=len(A)
    R=sum(1 for i in range(n) for j in range(i+1,n) if A[i][j]!=0)
    S=sum(1 for i in range(n) if A[i][i]!=0)
    P=sum(A[i][j]*A[ip][jp] for i in range(n) for ip in range(i+1,n) for j in range(n) for jp in range(j+1) if j>i and False) # placeholder
    # P = sum over i<i'<j, j'<=j
    P=sum(A[i][j]*A[ip][jp] for i in range(n) for ip in range(i+1,n) for j in range(n) for jp in range(j+1) if i<ip and ip<j and True)
    # careful: condition i<i'<j and j'<=j. i.e. ip<j (j index j+1>ip)
    P=sum(A[i][j]*A[ip][jp] for i in range(n) for ip in range(i+1,n) for j in range(ip+1,n+1) for jp in range(1,j+1) if True for (i,j,ip,jp) in [0]*0) if False else None
    P=0
    for i in range(n):
        for ip in range(i+1,n):
            for j in range(ip+2,n+1):  # j (1-based) > i'=ip+1
                for jp in range(1,j+1):
                    P+=A[i][j-1]*A[ip][jp-1]
    Sp=sum(1 for i in range(n) if A[i][i]==1); Sm=sum(1 for i in range(n) if A[i][i]==-1)
    I2=2*P+(n-Sp-Sm)//2
    M2=R+(Sp+Sm-n)//2
    return P,R,Sp,Sm,I2,M2

def census(n, verbose=False):
    tot=0; ds=0; bad=0
    joint=Counter(); marg=Counter()
    for tri in gen_triangles(n):
        tot+=1
        A=tri_to_asm(tri)
        if not check_asm(A):
            bad+=1
            if verbose: print("BAD", tri, A)
            continue
        if all(A[i][j]==A[j][i] for i in range(n) for j in range(n)):
            I,M=stats_direct(A)
            P,R,Sp,Sm,I2,M2=stats_struct(A)
            assert I==I2, (A,I,I2,P,Sp,Sm)
            assert M==M2, (A,M,M2,R,Sp,Sm)
            ds+=1; joint[(I,M)]+=1; marg[M]+=1
    return tot,ds,bad,joint,marg

import time
for n in range(1,7):
    t=time.time()
    tot,ds,bad,joint,marg=census(n)
    print(f"n={n} ASM={tot} DSASM={ds} bad={bad} marg={dict(sorted(marg.items()))} t={time.time()-t:.1f}s", flush=True)
