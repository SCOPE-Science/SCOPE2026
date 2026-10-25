"""Independent finite-field checks of rank-one weight-zero Rota-Baxter operators.

Run with Python 3: python check.py
No nonstandard dependencies. All matrices are row-major tuples.
"""
from itertools import product

def matmul(a,b,n,q):
    return tuple(sum(a[i*n+k]*b[k*n+j] for k in range(n))%q
                 for i in range(n) for j in range(n))

def mulbasis(a,j,n,q,left):
    e=[0]*(n*n);e[j]=1
    return matmul(a,e,n,q) if left else matmul(e,a,n,q)

def dot(u,v,q):return sum(x*y for x,y in zip(u,v))%q

def is_rb(a,phi,n,q):
    sq=matmul(a,a,n,q)
    l=[dot(phi,mulbasis(a,j,n,q,True),q) for j in range(n*n)]
    r=[dot(phi,mulbasis(a,j,n,q,False),q) for j in range(n*n)]
    for i,j in product(range(n*n),repeat=2):
        z=(phi[i]*l[j]+r[i]*phi[j])%q
        if any((phi[i]*phi[j]*sq[t]-z*a[t])%q for t in range(n*n)):
            return False
    return True

def gaussian(n,k,q):
    numerator=1; denominator=1
    for i in range(k):
        numerator*=q**(n-i)-1
        denominator*=q**(k-i)-1
    assert numerator%denominator==0
    return numerator//denominator

def gl(r,q):
    z=1
    for i in range(r):z*=q**r-q**i
    return z

def expected(n,q):
    s1=sum(gaussian(n,r,q)*gaussian(n-r,r,q)*gl(r,q)*
           (q**((n-r)**2)-1)//(q-1) for r in range(1,n//2+1))
    s2=2*sum(gaussian(n,r,q)*q**(r*(n-r))*(q**(r*(n-r))-1)
             for r in range(1,n))
    return s1,s2

def exhaust_small(n,q):
    allvec=list(product(range(q),repeat=n*n))
    ops=set()
    types={"squarezero":0,"idempotent":0}
    for a in allvec[1:]:
      aa=matmul(a,a,n,q)
      for phi in allvec[1:]:
        if not is_rb(a,phi,n,q):continue
        key=tuple((x*y)%q for x in a for y in phi)
        if key in ops:continue
        ops.add(key)
        if all(x==0 for x in aa):types['squarezero']+=1
        else:types['idempotent']+=1
    z=sum(expected(n,q))
    assert len(ops)==z,(n,q,len(ops),z)
    print(f'n={n}, q={q}: exhaustive rank-one RB maps={len(ops)} (target {z}); image types={types}')

def verify_3_2():
    n=3;q=2
    N=1<<(n*n)
    vec=lambda s:tuple((s>>i)&1 for i in range(n*n))
    vv=[vec(k) for k in range(N)]
    count=0; classes=[0,0]
    for a in vv[1:]:
        aa=matmul(a,a,n,q)
        if any(aa) and aa!=a:continue
        is_nil=not any(aa)
        L=[mulbasis(a,j,n,q,True) for j in range(n*n)]
        RR=[mulbasis(a,j,n,q,False) for j in range(n*n)]
        for phi in vv[1:]:
            ll=[dot(phi,x,q) for x in L]
            rr=[dot(phi,x,q) for x in RR]
            ok=True
            for i,j in product(range(n*n),repeat=2):
                z=(phi[i]*ll[j]+rr[i]*phi[j])%q
                if any((phi[i]*phi[j]*aa[t]-z*a[t])%q for t in range(n*n)):
                    ok=False;break
            if ok:
                count+=1;classes[0 if is_nil else 1]+=1
                assert is_rb(a,phi,n,q)
    target=expected(3,2)
    assert tuple(classes)==target,(classes,target)
    print(f'n=3, q=2: exhaustive 261121 candidate pairs, RB maps={count}, image classes={classes}; target={target}')

if __name__=='__main__':
    exhaust_small(2,2)
    exhaust_small(2,3)
    verify_3_2()
    print('RANK_ONE_RB_OK')
