"""Exact integer modular checks for two complete-graph cat-map families.
Run: python3 verify.py. No third-party dependencies.
The quotient-ring calculation is exhaustive in n modulo 8; full matrices
provide an independently implemented finite-size cross-check.
"""


def predicted(n, s, loop):
    assert n >= 2 and s >= 1
    if loop:
        return 2**s if n % 2 == 0 else 3 * 2**max(0, s-2)
    return 3 * 2**(s-1) if n % 4 in (0, 3) else 3 * 2**max(0, s-2)


# The abstract element e satisfies e^2 = n*e; an entry is (a,b)=a+b*e.
def aadd(a,b,mod=8): return ((a[0]+b[0])%mod,(a[1]+b[1])%mod)
def amul(a,b,n,mod=8):
    return ((a[0]*b[0])%mod,
            (a[0]*b[1]+a[1]*b[0]+n*a[1]*b[1])%mod)

def mmul(A,B,n,mod=8):
    return [[aadd(amul(A[i][0],B[0][j],n,mod),
                  amul(A[i][1],B[1][j],n,mod),mod)
             for j in range(2)] for i in range(2)]

def mpow(A,k,n,mod=8):
    I=[[(1,0),(0,0)],[(0,0),(1,0)]]
    Z=I
    while k:
        if k & 1: Z=mmul(Z,A,n,mod)
        A=mmul(A,A,n,mod);k//=2
    return Z

def abstract(n,loop):
    e=(0,1); c=e if loop else (7,1)
    c2=amul(c,c,n)
    return [[(1,0),c],[c,aadd((1,0),c2)]]

def valuation_mod8(A):
    I=[[(1,0),(0,0)],[(0,0),(1,0)]]
    coeffs=[]
    for i in range(2):
        for j in range(2):
            for r in range(2): coeffs.append((A[i][j][r]-I[i][j][r])%8)
    for v in range(3):
        if any(c % 2**(v+1) for c in coeffs): return v
    return 3 # means at least 3; proof needs exact valuation only <3.

n_assert=0
for n in range(8):
    for loop in (False,True):
        A=abstract(n,loop)
        v2=valuation_mod8(mpow(A,2,n))
        v3=valuation_mod8(mpow(A,3,n))
        v4=valuation_mod8(mpow(A,4,n))
        v6=valuation_mod8(mpow(A,6,n))
        if loop and n%2==0:
            assert (v2,v4)==(1,2)
            n_assert+=2
        elif loop and n%2==1:
            assert v3==2
            n_assert+=1
        elif not loop and n%4 in (1,2):
            assert v3==2
            n_assert+=1
        else:
            assert (v3,v6)==(1,2)
            n_assert+=2
        assert valuation_mod8(A)==0 # nonidentity modulo 2 in every case
        n_assert+=1

# Separate dense-integer-matrix implementation, not using the formal quotient.
def matmul(A,B,q):
    m=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(m))%q
             for j in range(m)] for i in range(m)]

def pow_mod(A,t,q):
    m=len(A)
    E=[[int(i==j) for j in range(m)] for i in range(m)]
    while t:
        if t&1: E=matmul(E,A,q)
        A=matmul(A,A,q);t>>=1
    return E

def dense_matrix(n,loop):
    C=[[int(loop or i!=j) for j in range(n)] for i in range(n)]
    C2=[[sum(C[i][k]*C[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    m=2*n
    return [[int(i==j) if i<n and j<n else
             C[i][j-n] if i<n and j>=n else
             C[i-n][j] if i>=n and j<n else
             int(i-n==j-n)+C2[i-n][j-n]
             for j in range(m)] for i in range(m)]

for n in range(2,15):
    for loop in (False,True):
        A=dense_matrix(n,loop)
        I=[[int(i==j) for j in range(2*n)] for i in range(2*n)]
        for s in range(1,9):
            q=2**s;t=predicted(n,s,loop)
            assert pow_mod(A,t,q)==I,(n,loop,s,t)
            n_assert+=1
            if t%2==0:
                assert pow_mod(A,t//2,q)!=I,(n,loop,s,t//2)
                n_assert+=1
            if t%3==0:
                assert pow_mod(A,t//3,q)!=I,(n,loop,s,t//3)
                n_assert+=1
print('VERIFY_OK; exact assertions:',n_assert)
