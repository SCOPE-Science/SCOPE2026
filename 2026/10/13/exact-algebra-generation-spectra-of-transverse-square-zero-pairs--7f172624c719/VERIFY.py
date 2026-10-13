"""Finite-field checks for transverse square-zero generator algebras.
Only prime fields are needed for the tests; the theorem includes all finite fields.
"""
from itertools import product
from collections import Counter

def matrix_mul(A,B,n,p):
    return tuple(sum(A[i*n+k]*B[k*n+j] for k in range(n))%p for i in range(n) for j in range(n))

def identity(n):
    return tuple(int(i==j) for i in range(n) for j in range(n))

def rank(vectors,p):
    pivots={}
    for v in vectors:
        w=list(v)
        for col in sorted(pivots):
            if w[col]:
                mult=w[col]
                w=[(a-mult*b)%p for a,b in zip(w,pivots[col])]
        if any(w):
            col=next(i for i,z in enumerate(w) if z)
            inv=pow(w[col],-1,p)
            pivots[col]=[(z*inv)%p for z in w]
    return len(pivots)

def minpol_degree(C,m,p):
    P=identity(m); powers=[]
    while True:
        if rank(powers+[P],p)==len(powers):
            return len(powers)
        powers.append(P)
        P=matrix_mul(P,C,m,p)

def generated_dim(X,Y,n,p):
    found=[]; queue=[identity(n)]
    while queue:
        A=queue.pop(0)
        if rank(found+[A],p)==len(found):
            continue
        found.append(A)
        queue.extend((matrix_mul(A,X,n,p),matrix_mul(A,Y,n,p)))
    return len(found)

def canonical_pair(C,m,p):
    n=2*m
    X=[0]*(n*n);Y=[0]*(n*n)
    for i in range(m):
        X[i*n+m+i]=1
        for j in range(m):Y[(m+i)*n+j]=C[i*m+j]
    return tuple(X),tuple(Y)

def gauss_qbin(n,k,q):
    a=1;b=1
    for i in range(k):a*=q**(n-i)-1;b*=q**(k-i)-1
    return a//b

def gl_order(m,p):
    v=1
    for j in range(m):v*=p**m-p**j
    return v

def field_tests():
    for p,m in ((2,1),(3,1),(5,1),(2,2),(3,2),(5,2),(2,3)):
        n=2*m
        hist=Counter()
        for C in product(range(p),repeat=m*m):
            if rank([C[i*m:(i+1)*m] for i in range(m)],p)!=m:continue
            d=minpol_degree(C,m,p)
            X,Y=canonical_pair(C,m,p)
            actual=generated_dim(X,Y,n,p)
            assert actual==4*d,(p,m,C,d,actual)
            hist[d]+=1
        assert sum(hist.values())==gl_order(m,p)
        if m==2:
            assert hist[1]==p-1 and hist[2]==gl_order(m,p)-(p-1)
            factor=gauss_qbin(2*m,m,p)*p**(m*m)*gl_order(m,p)
            assert sum(factor*count for count in hist.values())==gauss_qbin(2*m,m,p)*p**(m*m)*gl_order(m,p)**2
        print('GL_TEST',p,m,dict(sorted(hist.items())))

def bitmul(a,b,n=4):
    z=0
    for i in range(n):
        row=(a>>(n*i))&((1<<n)-1)
        r=0
        for j in range(n):
            if row>>j&1:r^=(b>>(n*j))&((1<<n)-1)
        z|=r<<(n*i)
    return z

def bitrank(a,n=4):
    rows=[(a>>(n*i))&((1<<n)-1) for i in range(n)]
    piv=0
    for j in range(n):
        for k in range(piv,n):
            if rows[k]>>j&1:
                rows[piv],rows[k]=rows[k],rows[piv];break
        else:continue
        for k in range(n):
            if k!=piv and (rows[k]>>j)&1:rows[k]^=rows[piv]
        piv+=1
    return piv

def bitimage(a,n=4):
    cols=[sum(((a>>(i*n+j))&1)<<i for i in range(n)) for j in range(n)]
    s={0}
    for v in cols:s|={w^v for w in tuple(s)}
    return s

def bitalgdim(X,Y,n=4):
    red={};queue=[sum(1<<(i*n+i) for i in range(n))]
    for A in queue:
        w=A
        while w:
            b=w.bit_length()-1
            if b not in red:break
            w^=red[b]
        if not w:continue
        red[b]=w
        queue.append(bitmul(A,X,n));queue.append(bitmul(A,Y,n))
    return len(red)

def exhaustive_four_binary():
    X=(1<<1)|(1<<(2*4+3))
    U=bitimage(X)
    hist=Counter()
    for Y in range(1<<16):
        if bitmul(Y,Y)!=0 or bitrank(Y)!=2 or len(bitimage(Y)&U)!=1:continue
        hist[bitalgdim(X,Y)]+=1
    assert hist=={4:16,8:80},hist
    N_X=gauss_qbin(4,2,2)*gl_order(2,2)
    assert N_X==210 and N_X*hist[8]==16800 and N_X*hist[4]==3360
    print('FULL_BINARY_FIXED_X',dict(hist),'TOTAL_EXTREMAL_PAIRS',N_X*hist[8])

if __name__=='__main__':
    field_tests(); exhaustive_four_binary();print('VERIFY_OK')
