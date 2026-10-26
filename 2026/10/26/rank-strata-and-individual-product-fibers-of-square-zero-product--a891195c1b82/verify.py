"""Independent finite-field checks of the rank distribution of square-zero products of idempotents."""
from itertools import product
from math import prod

def rank(A, p):
    a=[list(row) for row in A]
    h=len(a); w=len(a[0]) if a else 0
    j=0
    for c in range(w):
        pivot=next((i for i in range(j,h) if a[i][c]%p),None)
        if pivot is None: continue
        a[j],a[pivot]=a[pivot],a[j]
        inv=pow(a[j][c],-1,p)
        a[j]=[x*inv%p for x in a[j]]
        for i in range(j+1,h):
            f=a[i][c]%p
            if f: a[i]=[(x-f*y)%p for x,y in zip(a[i],a[j])]
        j+=1
        if j==h: break
    return j

def mul(A,B,p):
    return tuple(tuple(sum(A[i][j]*B[j][k] for j in range(len(B)))%p for k in range(len(B[0]))) for i in range(len(A)))

def choose_q(n,k,q):
    if k<0 or k>n:return 0
    return prod(q**(n-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k)) if k else 1

def count(n,r,s,b,q):
    if not (0<=r<=n and 0<=s<=n-r and 0<=b<=min(r,s)):return 0
    return choose_q(n-r,s,q)*choose_q(r,b,q)*prod(q**s-q**i for i in range(b))*q**(s*(n-s)-b*b)

def verify(n,p):
    mats=(tuple(tuple(v[i*n:(i+1)*n]) for i in range(n)) for v in product(range(p),repeat=n*n))
    f_by_s={s:[] for s in range(n+1)}
    for f in mats:
        if mul(f,f,p)==f: f_by_s[rank(f,p)].append(f)
    checks=0
    for r in range(n+1):
        e=tuple(tuple(int(i==j and i<r) for j in range(n)) for i in range(n))
        tally={}
        for s,fs in f_by_s.items():
            for f in fs:
                ef=mul(e,f,p)
                if all(not x for row in mul(ef,ef,p) for x in row):
                    key=(s,rank(ef,p))
                    tally[key]=tally.get(key,0)+1
        for s in range(n+1):
            for b in range(n+1):
                actual=tally.get((s,b),0)
                predicted=count(n,r,s,b,p)
                assert actual==predicted,(n,p,r,s,b,actual,predicted)
                checks+=1
    return checks,{s:len(fs) for s,fs in f_by_s.items()}

if __name__=='__main__':
    total=0
    for n,p in [(1,2),(2,2),(3,2),(4,2),(2,3),(3,3),(2,5)]:
        c,v=verify(n,p)
        total+=c
        print('verified',n,p,'cases',c,'idempotents by rank',v)
    print('VERIFY_OK_IDEMPOTENT_SQUARE_ZERO_PRODUCT',total)

def sqzero_count(n,b,q):
    if 2*b>n or b<0: return 0
    return choose_q(n,b,q)*choose_q(n-b,b,q)*prod(q**b-q**i for i in range(b))

def check_individual_product_fibers(n,p):
    allm=[tuple(tuple(v[i*n:(i+1)*n]) for i in range(n)) for v in product(range(p),repeat=n*n)]
    idem=[(f,rank(f,p)) for f in allm if mul(f,f,p)==f]
    squarezero={f:rank(f,p) for f in allm if not any(z for row in mul(f,f,p) for z in row)}
    assert sum(sqzero_count(n,b,p) for b in range(n//2+1))==len(squarezero)
    observed={}
    for e,r in idem:
        for f,s in idem:
            z=mul(e,f,p)
            if z in squarezero:
                key=(z,r,s)
                observed[key]=observed.get(key,0)+1
    checks=0
    for z,b in squarezero.items():
        for r in range(n+1):
            for s in range(n+1):
                predicted=(choose_q(n,r,p)*p**(r*(n-r))*count(n,r,s,b,p))
                den=sqzero_count(n,b,p)
                assert predicted%den==0
                actual=observed.get((z,r,s),0)
                assert actual==predicted//den,(n,p,z,b,r,s,actual,predicted//den)
                checks+=1
    return checks,len(squarezero),len(idem)

if __name__=='__main__':
    zchecks=0
    for n,p in [(1,2),(2,2),(3,2),(2,3),(3,3),(2,5)]:
        c,nz,ni=check_individual_product_fibers(n,p)
        zchecks+=c
        print('individual-fiber checks',n,p,c,'square-zero products',nz,'idempotents',ni)
    print('VERIFY_OK_IDEMPOTENT_SQUARE_ZERO_FIBERS',zchecks)
