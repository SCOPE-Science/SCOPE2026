"""Direct finite-field sanity checks for zero-product tuples (prime fields only)."""
from itertools import product
from math import comb

def matmul(a,b,n,q):
    return tuple(sum(a[i*n+k]*b[k*n+j] for k in range(n))%q for i in range(n) for j in range(n))

def rank(a,n,q):
    a=[list(a[i*n:(i+1)*n]) for i in range(n)]
    r=0
    for c in range(n):
        pivot=next((i for i in range(r,n) if a[i][c]%q),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][c],-1,q)
        a[r]=[(v*inv)%q for v in a[r]]
        for i in range(n):
            if i!=r:
                v=a[i][c]; a[i]=[(x-v*y)%q for x,y in zip(a[i],a[r])]
        r+=1
    return r

def gl(n,q):
    ans=1
    for i in range(n): ans*=q**n-q**i
    return ans

def experiment(n,q,k):
    mats=list(product(range(q),repeat=n*n)); N=len(mats)
    ranks=[rank(a,n,q) for a in mats]
    mult_zero=[[not any(matmul(a,b,n,q)) and not any(matmul(b,a,n,q)) for b in mats] for a in mats]
    rank_counts={}; all_count=0; unit=0
    z=(0,)*(n*n)
    def visit(chosen,s):
        nonlocal all_count,unit
        if len(chosen)==k:
            all_count+=1
            if rank(s,n,q)==n:
                unit+=1
                r=tuple(ranks[i] for i in chosen)
                rank_counts[r]=rank_counts.get(r,0)+1
            return
        for i in range(N):
            if all(mult_zero[i][j] for j in chosen):
                t=tuple((a+b)%q for a,b in zip(s,mats[i]))
                visit(chosen+[i],t)
    visit([],z)
    if n==2:
        expected=comb(n+k-1,k-1)*gl(n,q)+1+(q+1)*(q**k-1)+k*q*(q*q-1)
        assert all_count==expected,(n,q,k,all_count,expected)
    assert unit==comb(n+k-1,k-1)*gl(n,q),(n,q,k,unit)
    for r in product(range(n+1),repeat=k):
        expect=gl(n,q) if sum(r)==n else 0
        assert rank_counts.get(r,0)==expect,(n,q,k,r,rank_counts.get(r),expect)
    print('PASS',{'n':n,'q':q,'k':k,'all':all_count,'unit':unit,'profiles':len(rank_counts)})

if __name__=='__main__':
    for k in [1,2,3,4,5]: experiment(2,2,k)
    for k in [1,2,3]: experiment(2,3,k)
    experiment(3,2,2)
    print('VERIFY_OK')
