"""Reproducible finite checks for weight-zero Rota--Baxter operators on square-zero local algebras.
Uses only Python standard library; this is a finite check, not a substitute for a general proof.
"""
from itertools import product
from math import prod


def matmul(a,b,q):
    n=len(a)
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(n))%q for j in range(n)) for i in range(n))

def matvec(a,v,q):
    return tuple(sum(a[i][k]*v[k] for k in range(len(v)))%q for i in range(len(v)))

def matrank(a,q):
    m=[list(row) for row in a]; r=0
    for j in range(len(m[0]) if m else 0):
        h=next((i for i in range(r,len(m)) if m[i][j]%q),None)
        if h is None: continue
        m[r],m[h]=m[h],m[r]
        inv=pow(m[r][j],-1,q); m[r]=[(inv*x)%q for x in m[r]]
        for i in range(len(m)):
            if i!=r and m[i][j]%q:
                t=m[i][j]; m[i]=[(x-t*y)%q for x,y in zip(m[i],m[r])]
        r+=1
    return r

def elem_mul(x,y,q):
    return (x[0]*y[0]%q,)+tuple((x[0]*b+y[0]*a)%q for a,b in zip(x[1:],y[1:]))

def add(x,y,q):return tuple((a+b)%q for a,b in zip(x,y))
def apply(cols,x,q):return tuple(sum(cols[j][i]*x[j] for j in range(len(x)))%q for i in range(len(x)))

def is_rb(cols,q):
    m=len(cols); basis=[tuple(int(j==i) for j in range(m)) for i in range(m)]
    for i in range(m):
        for j in range(i,m):
            lhs=elem_mul(cols[i],cols[j],q)
            mid=add(elem_mul(cols[i],basis[j],q),elem_mul(basis[i],cols[j],q),q)
            if lhs!=apply(cols,mid,q):return False
    return True

def is_predicted(cols,q):
    n=len(cols)-1
    if cols[0][0] or any(col[0] for col in cols[1:]):return False
    u=cols[0][1:]
    T=tuple(tuple(cols[j+1][i+1] for j in range(n)) for i in range(n))
    if any(any(v for v in row) for row in matmul(T,T,q)):return False
    if q!=2 and any(matvec(T,u,q)):return False
    return True

def gaussian(n,k,q):
    if k<0 or k>n:return 0
    num=prod(q**(n-i)-1 for i in range(k))
    den=prod(q**(k-i)-1 for i in range(k))
    return num//den

def gl_order(n,q):return prod(q**n-q**j for j in range(n))
def H(n,r,q):return gaussian(n,r,q)*gaussian(n-r,r,q)*gl_order(r,q)

def predicted_count(n,q):
    return sum(H(n,r,q)*(q**n if q==2 else q**(n-r)) for r in range(n//2+1))

def predicted_orbit_sizes(n,q):
    z=[]
    for r in range(n//2+1):
        h=H(n,r,q);z.append(h)
        if r>0:z.append(h*(q**r-1))
        if n>2*r:z.append(h*(q**(n-r)-q**r))
        if q==2 and r>0:z.append(h*(q**n-q**(n-r)))
    return sorted(z)

def ops_for(q,n):
    m=n+1
    for v in product(range(q),repeat=m*m):
        cols=tuple(tuple(v[j*m+i] for i in range(m)) for j in range(m))
        if is_rb(cols,q):yield cols

def orbit_sizes(q,n,found):
    nmat=list(product(range(q),repeat=n*n)); GL=[]
    for dat in nmat:
        M=tuple(tuple(dat[i*n+j] for j in range(n)) for i in range(n))
        if matrank(M,q)==n:GL.append(M)
    def encode(cols):return tuple(z for col in cols for z in col)
    def transform(cols,g):
        # Conjugate the operator on 1+V by the algebra automorphism with radical matrix g.
        # New u=gu, new T determined by gTg^{-1}; compute g^{-1} by finite enumeration.
        inv=next(h for h in GL if matmul(g,h,q)==tuple(tuple(int(i==j) for j in range(n)) for i in range(n)))
        T=tuple(tuple(cols[j+1][i+1] for j in range(n)) for i in range(n))
        U=matvec(g,cols[0][1:],q)
        newT=matmul(matmul(g,T,q),inv,q)
        return ((0,)+U,)+tuple((0,)+tuple(newT[i][j] for i in range(n)) for j in range(n))
    remaining=set(map(encode,found)); sizes=[]
    while remaining:
        x=next(iter(remaining));m=n+1;cols=tuple(tuple(x[j*m+i] for i in range(m)) for j in range(m))
        orbit={encode(transform(cols,g)) for g in GL}
        assert orbit <= set(map(encode,found))
        assert orbit<=remaining
        sizes.append(len(orbit));remaining-=orbit
    return sorted(sizes)

def run():
    for q,n in [(2,1),(3,1),(2,2),(3,2),(2,3)]:
        actual=list(ops_for(q,n))
        assert all(is_predicted(z,q) for z in actual), (q,n,'false positives')
        predicted=predicted_count(n,q)
        assert len(actual)==predicted, (q,n,len(actual),predicted)
        # Check all predicted operators actually satisfy the identity by counting equality.
        predicted_ops=0
        for v in product(range(q),repeat=(n+1)*(n+1)):
            cols=tuple(tuple(v[j*(n+1)+i] for i in range(n+1)) for j in range(n+1))
            if is_predicted(cols,q):predicted_ops+=1
        assert predicted_ops==len(actual),(q,n,predicted_ops,len(actual))
        if n<=2 or (q,n)==(2,3):
            actual_sizes=orbit_sizes(q,n,actual)
            expected_sizes=predicted_orbit_sizes(n,q)
            assert actual_sizes==expected_sizes,(q,n,actual_sizes,expected_sizes)
        print('EXHAUSTIVE_RB_AND_ORBITS_OK',q,n,'operators',len(actual),'orbit_sizes',predicted_orbit_sizes(n,q))
    print('CHECKER_OK')

if __name__=='__main__':run()
