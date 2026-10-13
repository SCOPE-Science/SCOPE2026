"""Independent finite checks for commuting maximal-rank square-zero pairs.
Compatible with CPython stdlib only. All matrix entries represented as integers in finite fields.
"""
from itertools import product
from math import prod

def field(q):
    if q==4:
        add=lambda a,b:a^b
        def mul(a,b):
            u=0
            for i in range(2):
                if (b>>i)&1:u^=a<<i
            for j in (2,):
                if (u>>j)&1:u ^= 0b111<<(j-2)
            return u
        neg=lambda a:a
    else:
        add=lambda a,b:(a+b)%q
        mul=lambda a,b:(a*b)%q
        neg=lambda a:(-a)%q
    return add,mul,neg

def matmul(A,B,q):
    add,mul,_=field(q); n=len(A)
    return tuple(tuple(_sum((mul(A[i][k],B[k][j]) for k in range(n)),add) for j in range(n)) for i in range(n))
def _sum(xs,add):
    s=0
    for x in xs:s=add(s,x)
    return s

def matadd(A,B,q):
    add,_,_=field(q); return tuple(tuple(add(a,b) for a,b in zip(rowa,rowb)) for rowa,rowb in zip(A,B))
def matrank(A,q):
    add,mul,neg=field(q); A=[list(x) for x in A]; n=len(A); p=len(A[0]); row=0
    for col in range(p):
        pivot=next((r for r in range(row,n) if A[r][col]),None)
        if pivot is None: continue
        A[row],A[pivot]=A[pivot],A[row]
        inv=next(v for v in range(1,q) if mul(v,A[row][col])==1)
        A[row]=[mul(v,inv) for v in A[row]]
        for r in range(n):
            if r!=row and A[r][col]:
                w=neg(A[r][col]); A[r]=[add(A[r][c],mul(w,A[row][c])) for c in range(p)]
        row+=1
        if row==n:break
    return row

def A_canonical(m,r):
    A=[[0]*m for _ in range(m)]
    for j in range(r):A[j][r+j]=1
    return tuple(tuple(row) for row in A)
def mats(m,q):
    for z in product(range(q),repeat=m*m):yield tuple(tuple(z[i*m:(i+1)*m]) for i in range(m))
def gl(q,m):
    return prod(q**m-q**j for j in range(m))
def gauss(n,k,q):
    if k<0 or k>n:return 0
    a=b=1
    for j in range(k):a*=q**(n-j)-1;b*=q**(k-j)-1
    return a//b
def predicted(m,q,r):
    return gauss(m,r,q)*gauss(m-r,r,q)*gl(q,r)*q**(2*r*(m-r))*gl(q,m-2*r)
def blockY(A,B,m):
    Z=(0,)*m
    return tuple(A[i]+B[i] for i in range(m))+tuple(Z+A[i] for i in range(m))
def check_one(m,q,check_all_A=True):
    ZERO=tuple((0,)*m for _ in range(m))
    counts_A={}
    if check_all_A:
        for A in mats(m,q):
            if matmul(A,A,q)==ZERO:
                r=matrank(A,q);counts_A[r]=counts_A.get(r,0)+1
        for r,c in counts_A.items():
            want=gauss(m,r,q)*gauss(m-r,r,q)*gl(q,r)
            assert c==want,(m,q,'A',r,c,want)
    tallies={}
    for r in range(m//2+1):
        A=A_canonical(m,r)
        Bcount=0
        for B in mats(m,q):
            if matadd(matmul(A,B,q),matmul(B,A,q),q)!=ZERO:continue
            Y=blockY(A,B,m)
            if matrank(Y,q)==m:Bcount+=1
        expected=q**(2*r*(m-r))*gl(q,m-2*r)
        assert Bcount==expected,(m,q,r,Bcount,expected)
        tallies[r]=predicted(m,q,r)
    print('PASS m=%d q=%d A strata=%s B canonical=%s full-rank Y strata=%s'%(m,q,counts_A,{r:tallies[r]//(gauss(m,r,q)*gauss(m-r,r,q)*gl(q,r)) for r in tallies},tallies))

if __name__=='__main__':
    for m,q in ((1,2),(2,2),(2,3),(2,4),(2,5),(3,2),(3,3)):
        check_one(m,q,check_all_A=(m,q)!=(3,3))
    check_one(4,2,check_all_A=False)
    print('VERIFY_OK')
