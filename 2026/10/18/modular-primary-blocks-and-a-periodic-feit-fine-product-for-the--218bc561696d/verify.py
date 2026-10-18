"""Finite-field verification of the Jordan-plane matrix-pair enumeration.

Run with Python 3.9 or later.  Exhaustive Y enumeration; the affine X fiber
is computed by modular row reduction, not by enumerating X.
"""
from itertools import product
from fractions import Fraction
from math import prod

def rank(rows, p):
    a = [list(row) for row in rows]
    m=len(a)
    if not m: return 0
    n=len(a[0]); r=0
    for j in range(n):
        k=next((i for i in range(r,m) if a[i][j]%p),None)
        if k is None: continue
        a[k],a[r]=a[r],a[k]
        z=pow(a[r][j]%p,-1,p)
        a[r]=[(z*v)%p for v in a[r]]
        for i in range(r+1,m):
            if a[i][j]%p:
                z=a[i][j]
                a[i]=[(u-z*v)%p for u,v in zip(a[i],a[r])]
        r+=1
        if r==m: break
    return r

def partition(n, largest=None):
    if not n:
        yield ()
        return
    if largest is None: largest=n
    for j in range(min(n, largest),0,-1):
        for rest in partition(n-j,j):
            yield (j,)+rest

def gl(n,q):
    return prod(q**n-q**i for i in range(n))

def predicted(n,q,p):
    res=Fraction(0)
    for la in partition(n):
        mult={j:la.count(j) for j in set(la)}
        w=Fraction(q**sum(m for j,m in mult.items() if j%p==0))
        for m in mult.values():
            for h in range(1,m+1):
                w/=Fraction(q**h-1,q**h)
        res+=w
    ans=gl(n,q)*res
    assert ans.denominator==1
    return int(ans)

def eval_y(Y,n,p):
    Y2=[sum(Y[i*n+k]*Y[k*n+j] for k in range(n))%p for i in range(n) for j in range(n)]
    dim=n*n
    A=[[0]*dim for _ in range(dim)]
    for a in range(n):
        for b in range(n):
            col=a*n+b
            for i in range(n):
                for j in range(n):
                    A[i*n+j][col]=((Y[b*n+j] if i==a else 0)-(Y[i*n+a] if j==b else 0))%p
    r=rank(A,p)
    ra=rank([row+[Y2[i]] for i,row in enumerate(A)],p)
    return (p**(dim-r) if r==ra else 0),r==ra

def nilpotent(Y,n,p):
    A=list(Y)
    for _ in range(n):
        if not any(A): return True
        A=[sum(A[i*n+k]*Y[k*n+j] for k in range(n))%p for i in range(n) for j in range(n)]
    return not any(A)

def mul4(x,y):
    z=0
    while y:
        if y&1: z^=x
        y>>=1
        x<<=1
        if x&4: x^=7  # t^2=t+1 in the four-element field
    return z

def rank4(rows):
    a=[list(r) for r in rows]
    m=len(a);n=len(a[0]); r=0
    for j in range(n):
        k=next((i for i in range(r,m) if a[i][j]),None)
        if k is None:continue
        a[k],a[r]=a[r],a[k]
        z=next(z for z in (1,2,3) if mul4(a[r][j],z)==1)
        a[r]=[mul4(z,x) for x in a[r]]
        for i in range(r+1,m):
            z=a[i][j]
            if z:a[i]=[x^mul4(z,y) for x,y in zip(a[i],a[r])]
        r+=1
    return r

def eval_y4(Y):
    n=2; dim=4
    Y2=[mul4(Y[i*n],Y[j])^mul4(Y[i*n+1],Y[n+j]) for i in range(n) for j in range(n)]
    A=[[0]*dim for _ in range(dim)]
    for a in range(n):
        for b in range(n):
            col=a*n+b
            for i in range(n):
                for j in range(n):
                    A[i*n+j][col]=(Y[b*n+j] if i==a else 0)^(Y[i*n+a] if j==b else 0)
    r=rank4(A); ra=rank4([row+[Y2[i]] for i,row in enumerate(A)])
    return (4**(dim-r) if r==ra else 0)

def main():
    for q,n in [(2,1),(2,2),(3,2),(2,3),(3,3)]:
        p=q
        total=0;non=0;admissible=0
        for Y in product(range(q), repeat=n*n):
            fiber,ok=eval_y(Y,n,p)
            total+=fiber
            if ok: admissible+=1
            if fiber and not nilpotent(Y,n,p): non+=fiber
        theory=predicted(n,q,p)
        assert theory==total,(q,n,theory,total)
        if n<p: assert non==0
        if n==p: assert non==q*gl(p,q),(q,n,non,q*gl(p,q))
        print(f'q={q} n={n} pairs={total} nonnilpotent_Y_pairs={non} admissible_Y={admissible}')
    total4=sum(eval_y4(Y) for Y in product(range(4),repeat=4))
    assert total4==predicted(2,4,2)==1216
    print(f'q=4 n=2 pairs={total4}')
    print('VERIFY_OK')

if __name__=='__main__': main()
