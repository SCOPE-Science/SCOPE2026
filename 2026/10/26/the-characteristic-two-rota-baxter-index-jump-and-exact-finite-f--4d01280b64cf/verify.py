"""Exact finite-field checks for the characteristic-dependent Rota--Baxter classification.
Run with python3 verify.py; uses the standard library only.
"""
from itertools import product
from math import prod
from collections import defaultdict

def matmul(a,b,n,q):
    return tuple(sum(a[i*n+k]*b[k*n+j] for k in range(n))%q for i in range(n) for j in range(n))

def mv(a,v,n,q):
    return tuple(sum(a[i*n+j]*v[j] for j in range(n))%q for i in range(n))

def rank(a,n,q):
    A=[list(a[i*n:(i+1)*n]) for i in range(n)]
    r=0
    for j in range(n):
        p=next((i for i in range(r,n) if A[i][j]%q),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        z=pow(A[r][j],-1,q)
        A[r]=[x*z%q for x in A[r]]
        for i in range(n):
            if i!=r:
                z=A[i][j]
                A[i]=[(a-z*b)%q for a,b in zip(A[i],A[r])]
        r+=1
    return r

def inverse(a,n,q):
    A=[[a[i*n+j]%q for j in range(n)]+[int(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        p=next((i for i in range(j,n) if A[i][j]%q),None)
        if p is None: return None
        A[j],A[p]=A[p],A[j]
        z=pow(A[j][j],-1,q)
        A[j]=[x*z%q for x in A[j]]
        for i in range(n):
            if i!=j:
                z=A[i][j]
                A[i]=[(x-z*y)%q for x,y in zip(A[i],A[j])]
    return tuple(A[i][n+j] for i in range(n) for j in range(n))

def gaussian(n,k,q):
    if k<0 or k>n:return 0
    k=min(k,n-k)
    return prod(q**(n-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k))

def glorder(r,q):
    return prod(q**r-q**j for j in range(r))

def rb_test(P,n,q):
    d=n+1
    cols=[tuple(P[k*d+i] for k in range(d)) for i in range(d)]
    def times(a,b):
        return (a[0]*b[0]%q,)+tuple((a[0]*b[i]+a[i]*b[0])%q for i in range(1,d))
    def apply(a):
        return tuple(sum(cols[j][i]*a[j] for j in range(d))%q for i in range(d))
    for i in range(d):
        for j in range(i,d):
            lhs=times(cols[i],cols[j])
            e_i=[int(k==i) for k in range(d)]
            e_j=[int(k==j) for k in range(d)]
            x=times(e_i,cols[j]);y=times(cols[i],e_j)
            rhs=apply(tuple((x[k]+y[k])%q for k in range(d)))
            if lhs!=rhs:return False
    return True

def data_from_P(P,n):
    d=n+1
    v=tuple(P[(i+1)*d] for i in range(n))
    L=tuple(P[(i+1)*d+j+1] for i in range(n) for j in range(n))
    return (L,v)

def pred(P,n,q):
    d=n+1
    if any(P[j] for j in range(d)):return False
    L,v=data_from_P(P,n)
    if any(matmul(L,L,n,q)):return False
    if q!=2 and any(mv(L,v,n,q)):return False
    return True

def signature(L,v,n,q):
    r=rank(L,n,q)
    if not any(v):t='zero'
    elif any(mv(L,v,n,q)):t='outside_kernel'
    else:
        # v in image(L) iff augment with it does not enlarge the column span.
        M=[list(L[i*n:(i+1)*n])+[v[i]] for i in range(n)]
        r_aug=0
        for j in range(n+1):
            p=next((i for i in range(r_aug,n) if M[i][j]%q),None)
            if p is None:continue
            M[p],M[r_aug]=M[r_aug],M[p]
            pivot=pow(M[r_aug][j],-1,q)
            M[r_aug]=[x*pivot%q for x in M[r_aug]]
            for i in range(n):
                if i!=r_aug:
                    z=M[i][j];M[i]=[(a-z*b)%q for a,b in zip(M[i],M[r_aug])]
            r_aug+=1
        t='image_nonzero' if r_aug==r else 'kernel_nonimage'
    return r,t

def check(q,n,orbit_check=True):
    d=n+1; good=[]
    for P in product(range(q),repeat=d*d):
        actual=rb_test(P,n,q)
        expected=pred(P,n,q)
        if actual!=expected:raise AssertionError(('identity mismatch',q,n,P,actual,expected))
        if actual:good.append(data_from_P(P,n))
    N=lambda r:gaussian(n,r,q)*gaussian(n-r,r,q)*glorder(r,q)
    predicted=sum(N(r)*(q**n if q==2 else q**(n-r)) for r in range(n//2+1))
    assert predicted==len(good),(q,n,predicted,len(good))
    sigs=defaultdict(int)
    for L,v in good:sigs[signature(L,v,n,q)]+=1
    for r in range(n//2+1):
        ideal={'zero':1}
        if r:ideal['image_nonzero']=q**r-1
        if n>2*r:ideal['kernel_nonimage']=q**(n-r)-q**r
        if q==2 and r:ideal['outside_kernel']=q**n-q**(n-r)
        for typ,size in ideal.items():
            assert sigs[(r,typ)]==size*N(r),(q,n,r,typ,sigs[(r,typ)],size*N(r))
    assert len(sigs)==(n//2+1)+(n//2)+((n+1)//2)+(n//2 if q==2 else 0)
    if orbit_check:
        gs=[(g,inverse(g,n,q)) for g in product(range(q),repeat=n*n)]
        gs=[(g,h) for g,h in gs if h is not None]
        checked=set()
        for L,v in good:
            sig=signature(L,v,n,q)
            if sig in checked:continue
            orbit={(matmul(matmul(g,L,n,q),h,n,q),mv(g,v,n,q)) for g,h in gs}
            assert all(signature(L2,v2,n,q)==sig for L2,v2 in orbit)
            assert len(orbit)==sigs[sig],(q,n,sig,len(orbit),sigs[sig])
            checked.add(sig)
        assert len(checked)==len(sigs)
    print('q=',q,'n=',n,'operator_count=',len(good),'orbit_types=',len(sigs),'predicted=',predicted)
    if q==2:
        p2=sum(N(r)*q**(n-r) for r in range(n//2+1))
        print('  P^2=0:',p2,'P^2 !=0:',len(good)-p2)
    return True

if __name__=='__main__':
    check(2,1)
    check(3,1)
    check(2,2)
    check(3,2)
    check(2,3)
    print('VERIFY_OK')
