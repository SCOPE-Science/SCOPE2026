from itertools import product
from math import prod

def matmul(A,B,p):
    n=len(A); m=len(B[0]); k=len(B)
    return [[sum(A[i][t]*B[t][j] for t in range(k))%p for j in range(m)] for i in range(n)]
def matsub(A,B,p): return [[(A[i][j]-B[i][j])%p for j in range(len(A))] for i in range(len(A))]
def eye(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def rank(A,p):
    a=[row[:] for row in A]; m=len(a); n=len(a[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if a[i][c]%p),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]
        inv=pow(a[r][c],-1,p)
        a[r]=[(x*inv)%p for x in a[r]]
        for i in range(m):
            if i!=r and a[i][c]%p:
                z=a[i][c]%p; a[i]=[(a[i][j]-z*a[r][j])%p for j in range(n)]
        r+=1
        if r==m: break
    return r
def inv(A,p): return rank(A,p)==len(A)
def comm(A,B,p): return matmul(A,B,p)==matmul(B,A,p)
def idem(E,p): return matmul(E,E,p)==E

def all_mats(n,p):
    for xs in product(range(p), repeat=n*n):
        yield [list(xs[i*n:(i+1)*n]) for i in range(n)]
def strong_count(A,p):
    n=len(A); return sum(1 for E in all_mats(n,p) if idem(E,p) and comm(A,E,p) and inv(matsub(A,E,p),p))
def block_diag(*Bs):
    n=sum(len(B) for B in Bs); A=[[0]*n for _ in range(n)]; s=0
    for B in Bs:
        for i in range(len(B)):
            for j in range(len(B)): A[s+i][s+j]=B[i][j]
        s+=len(B)
    return A

def qbinom(n,r,Q):
    if r<0 or r>n:return 0
    num=den=1
    for i in range(r): num*=Q**(n-i)-1; den*=Q**(r-i)-1
    return num//den
def H(m,k,Q): return sum(qbinom(k,r,Q)*Q**((2*m-1)*r*(k-r)) for r in range(k+1))

# Matrix-level checks.
checks=[]
for p,alpha in [(3,2),(5,2)]:
    A=[[alpha,0],[0,alpha]]
    checks.append((f'scalar p={p}',strong_count(A,p),H(1,2,p)))
A=[[2,1],[0,2]]
checks.append(('Jordan2(2) p=3',strong_count(A,3),H(2,1,3)))
A=block_diag([[0]],[[1]],[[2]])
checks.append(('0+1+2 p=3',strong_count(A,3),2))
C=[[0,1],[2,0]] # char poly x^2+1 over F3
A=block_diag([[2]],C)
checks.append(('linear+irreducible quadratic p=3',strong_count(A,3),4))
C2=[[0,1],[1,1]] # char poly x^2+x+1 over F2
A=block_diag(C2,C2)
checks.append(('two copies irreducible quadratic p=2',strong_count(A,2),H(1,2,4)))
for name,got,want in checks:
    assert got==want,(name,got,want)
    print(name,got)

# All 2x2 matrices: unique strong-clean iff A-A^2 is nilpotent.
def nilpotent(A,p):
    X=eye(len(A))
    # Cayley-Hamilton: nilpotent iff A^n=0 for n x n.
    X=A
    for _ in range(1,len(A)):
        X=matmul(X,A,p)
    return X==[[0]*len(A) for _ in range(len(A))]
for p in (2,3):
    total=unique=0
    for A in all_mats(2,p):
        c=strong_count(A,p); B=matsub(A,matmul(A,A,p),p)
        assert (c==1)==nilpotent(B,p),(p,A,c,B)
        total+=1; unique+=(c==1)
    print('unique_criterion',p,total,unique)

# Direct idempotent census in M_2(F_p[u]/u^m).
def add(a,b,p): return tuple((x+y)%p for x,y in zip(a,b))
def mul(a,b,p,m):
    c=[0]*m
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<m: c[i+j]=(c[i+j]+x*y)%p
    return tuple(c)
def ring_elems(p,m): return list(product(range(p),repeat=m))
def mat2mulR(A,B,p,m):
    z=(0,)*m
    return [[add(mul(A[i][0],B[0][j],p,m),mul(A[i][1],B[1][j],p,m),p) for j in range(2)] for i in range(2)]
def local_idem_count(p,m):
    es=ring_elems(p,m); z=(0,)*m
    count=0
    for xs in product(es,repeat=4):
        A=[[xs[0],xs[1]],[xs[2],xs[3]]]
        if mat2mulR(A,A,p,m)==A: count+=1
    return count
for p,m in [(3,2),(2,3)]:
    got=local_idem_count(p,m); want=H(m,2,p)
    assert got==want,(p,m,got,want)
    print('local_idempotents',p,m,got)
print('VERIFY_OK')
