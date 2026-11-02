"""Independent finite-field checks for square-zero matrices over dual numbers."""
from itertools import product
from collections import defaultdict
from math import prod

def matmul(a, b, n, p):
    return tuple(sum(a[i*n+k]*b[k*n+j] for k in range(n)) % p
                 for i in range(n) for j in range(n))

def rank(a, n, p):
    rows=[list(a[i*n:(i+1)*n]) for i in range(n)]
    return matrix_rank(rows,p)

def matrix_rank(a, p):
    if not a: return 0
    a=[row[:] for row in a]
    m=len(a); n=len(a[0]); r=0
    for j in range(n):
        s=next((i for i in range(r,m) if a[i][j]),None)
        if s is None: continue
        a[r],a[s]=a[s],a[r]
        inv=pow(a[r][j],-1,p)
        a[r]=[(v*inv)%p for v in a[r]]
        for i in range(r+1,m):
            c=a[i][j]
            if c:
                a[i]=[(x-c*y)%p for x,y in zip(a[i],a[r])]
        r+=1
        if r==m: break
    return r

def gaussian(n, r, q):
    # Products first: avoid intermediate nonintegral Gaussian ratios.
    a=prod(q**(n-i)-1 for i in range(r))
    b=prod(q**(r-i)-1 for i in range(r))
    return a//b

def gl(r,q):
    return prod(q**r-q**i for i in range(r))

def predicted(n,q):
    return {r:gaussian(n,r,q)*gaussian(n-r,r,q)*gl(r,q)*q**((n-r)**2+r*r)
            for r in range(n//2+1)}

def check(q,n,strict=False):
    z=(0,)*(n*n)
    units=[]
    byrank=defaultdict(int)
    for a in product(range(q),repeat=n*n):
        if matmul(a,a,n,q)!=z: continue
        r=rank(a,n,q)
        # Independent construction of matrix of B -> AB+BA, and kernel dimension.
        cols=[]
        for k in range(n*n):
            e=tuple(1 if i==k else 0 for i in range(n*n))
            ae=matmul(a,e,n,q); ea=matmul(e,a,n,q)
            cols.append(tuple((x+y)%q for x,y in zip(ae,ea)))
        linear=[[cols[k][j] for k in range(n*n)] for j in range(n*n)]
        nullity=n*n-matrix_rank(linear,q)
        assert nullity==(n-r)**2+r*r,(n,q,r,nullity)
        byrank[r]+=q**nullity
    assert dict(byrank)==predicted(n,q),(q,n,dict(byrank),predicted(n,q))
    if strict:
        byrank2=defaultdict(int)
        for a in product(range(q),repeat=n*n):
            if matmul(a,a,n,q)!=z: continue
            r=rank(a,n,q)
            for b in product(range(q),repeat=n*n):
                ab=matmul(a,b,n,q); ba=matmul(b,a,n,q)
                if all((ab[i]+ba[i])%q==0 for i in range(n*n)):
                    byrank2[r]+=1
        assert dict(byrank2)==dict(byrank)
    return len(byrank),sum(byrank.values())

def gf4_mul(x,y):
    # F4 = F2[z] / (z*z+z+1), represented by two bits.
    a0,a1=x&1,(x>>1)&1
    b0,b1=y&1,(y>>1)&1
    c0=(a0*b0)^(a1*b1)
    c1=(a0*b1)^(a1*b0)^(a1*b1)
    return c0|(c1<<1)

def gf4_rank2(a):
    d=gf4_mul(a[0],a[3])^gf4_mul(a[1],a[2])
    if d: return 2
    return 1 if any(a) else 0

def gf4_mul2(a,b):
    return tuple(gf4_mul(a[i*2],b[j])^gf4_mul(a[i*2+1],b[2+j])
                 for i in range(2) for j in range(2))

def check_gf4():
    zero=(0,)*4
    counts=defaultdict(int)
    for a in product(range(4),repeat=4):
        if gf4_mul2(a,a)!=zero: continue
        for b in product(range(4),repeat=4):
            ab,ba=gf4_mul2(a,b),gf4_mul2(b,a)
            if all(x^y==0 for x,y in zip(ab,ba)):
                counts[gf4_rank2(a)]+=1
    assert dict(counts)==predicted(2,4),(dict(counts),predicted(2,4))
    print('CHECK 4 2',sum(counts.values()),'GF4_exhaustive')

if __name__=='__main__':

    for q,n,s in [(2,1,True),(3,1,True),(2,2,True),(3,2,True),
                  (2,3,True),(3,3,False),(2,4,False)]:
        kinds,count=check(q,n,s)
        print('CHECK',q,n,kinds,count,'exhaustive_B' if s else 'linear_kernel')
    check_gf4()
    print('VERIFY_OK')
