from itertools import combinations, product
from math import comb, factorial, ceil, log2

def upsets(m,n):
    # min worlds 0..m-1, max worlds m..m+n-1
    W=(1<<(m+n))-1; MAX=((1<<n)-1)<<m
    return [v for v in range(W+1) if not (v&((1<<m)-1)) or (v&MAX)==MAX]

def ops(m,n):
    U=upsets(m,n); W=(1<<(m+n))-1
    future=[1<<i for i in range(m+n)]
    for i in range(m):future[i] |= ((1<<n)-1)<<m
    past=[1<<i for i in range(m+n)]
    for i in range(m,m+n):past[i] |= (1<<m)-1
    def implication(a,b):
        bad=a & ~b; bad2=0
        for i in range(m+n):
            if (future[i]&bad):bad2|=1<<i
        return W&~bad2
    def coimp(a,b):
        bad=a &~b; o=0
        for i in range(m+n):
            if (past[i]&bad):o|=1<<i
        return o
    return U,W,implication,coimp

def gen(m,n,values):
    U,W,imp,coimp=ops(m,n)
    A=set(values+[0,W])
    while True:
        old=len(A)
        A1=list(A)
        for a in A1:
            for b in A1:
                A.update([a&b,a|b,imp(a,b),coimp(a,b)])
        if len(A)==old:return A

def sig(m,n,values):
    MIN=(1<<m)-1; MAX=((1<<n)-1)<<m
    low=[j for j,a in enumerate(values) if (a&MIN)==0]
    high=[j for j,a in enumerate(values) if (a&MIN)!=0]
    cols_top=set(tuple(bool(a&(1<<(m+i))) for j in low for a in [values[j]]) for i in range(n))
    cols_bot=set(tuple(bool(a&(1<<i)) for j in high for a in [values[j]]) for i in range(m))
    a,b=len(cols_top),len(cols_bot)
    if all(v in (0,(1<<(m+n))-1) for v in values):return 2,a,b
    return (1<<a)+(1<<b)-1,a,b

def fall(N,r):
    if N<r:return 0
    o=1
    for i in range(r):o*=N-i
    return o

def formula(m,n,k):
    o=0
    for r in range(k+1):
        q=k-r
        b=sum((-1)**j*comb(q,j)*fall(2**(q-j),m) for j in range(q+1))
        o+=comb(k,r)*fall(2**r,n)*b
    if m==n==1:o-=2**k
    return o

if __name__=='__main__':
    comparisons=0; sums=0
    for m,n,k in product(range(1,4),range(1,4),range(4)):
        U,W,_,_=ops(m,n)
        ct=0
        for vals in product(U,repeat=k):
            actual=len(gen(m,n,list(vals)))
            pred,a,b=sig(m,n,list(vals))
            assert actual==pred,(m,n,k,vals,actual,pred,a,b)
            ct+=(actual==len(U)); comparisons+=1
        f=formula(m,n,k)
        assert ct==f,(m,n,k,ct,f)
        sums+=1
        print(f'm={m} n={n} k={k} #complete={ct} #patterns={len(U)**k}',flush=True)
    print(f'BI_HEIGHT_VERIFY_OK semantic={comparisons} counts={sums}')
