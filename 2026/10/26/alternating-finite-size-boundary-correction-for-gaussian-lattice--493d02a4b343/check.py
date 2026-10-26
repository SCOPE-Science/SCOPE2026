"""Exact finite algebra and numeric edge-limit checks for Gaussian lattice interpolation."""
from fractions import Fraction as F
from decimal import Decimal, localcontext

checks = 0

def demand(condition, label):
    global checks
    assert condition, label
    checks += 1

def qbin(n, k, q):
    if k < 0 or k > n: return F(0)
    z = F(1)
    for j in range(1, k+1): z *= (1 - q**(n-j+1))/(1-q**j)
    return z

def r(n,p):
    return sum(((-p)**j * qbin(n,j,p*p) for j in range(n+1)), F(0))

def h(n,p):
    x = F(1)
    for j in range(1,n+1):x*= 1 - p**(2*j)
    return x

def pol(n,p):
    return [(-1)**(n-k) * p**(n-k) * qbin(n,k,p*p) for k in range(n+1)]

def linear(a,b):
    n=len(b); A=[[F(x) for x in row]+[F(b[i])] for i,row in enumerate(a)]
    for j in range(n):
        demand(A[j][j]!=0,'nonzero pivot')
        z=A[j][j]; A[j]=[v/z for v in A[j]]
        for k in range(n):
            if k==j: continue
            c=A[k][j]
            if c: A[k]=[A[k][s]-c*A[j][s] for s in range(n+1)]
    return [v[-1] for v in A]

for p in (F(1,6),F(1,4),F(2,5),F(1,2),F(3,5)):
    for n in range(0,9):
        P=pol(n,p)
        demand(P[-1]==1,'monic')
        demand(sum(P)==r(n,p),'value at one')
        for j in range(n):
            demand(sum(P[k]*p**((k-j)**2) for k in range(n+1))==0,'orthogonal')
        demand(sum(P[k]*p**((k-n)**2) for k in range(n+1))==h(n,p),'norm')
    for N in range(1,10):
        M=[[p**((i-j)**2) for j in range(N)] for i in range(N)]
        x=linear(M,[F(1)]*N)
        left=sum(x,F(0))
        right=sum((r(n,p)**2/h(n,p) for n in range(N)),F(0))
        demand(left==right,'exact Gram Christoffel identity')

# Pure decimal calculation: tails are not proofs of the infinite theorem.
with localcontext() as ctx:
    ctx.prec=70
    for literal in ('0.2','0.45','0.7'):
        p=Decimal(literal);q=p*p
        nmax=180
        # Gauss binomial rows, no unstable alternating binomial explosion at small n.
        row=[Decimal(1)]
        R=[];H=[];hval=Decimal(1)
        for n in range(nmax):
            if n>0:
                old=row
                row=[Decimal(1)]+[old[k]+q**(n-k)*old[k-1] for k in range(1,n)]+[Decimal(1)]
                hval*=1-q**n
            R.append(sum(((-p)**j)*row[j] for j in range(n+1)))
            H.append(hval)
        T=Decimal(1)+2*sum(p**(j*j) for j in range(1,100))
        terms=[R[n]**2/H[n] for n in range(nmax)]
        C=sum((z-1/T for z in terms),Decimal(0))
        coef=2*p/((1+p)**2*T)
        for N in (17,20,23,27,30):
            I=sum(terms[:N],Decimal(0))
            rem=I-Decimal(N)/T-C+coef*(-p)**N
            demand(abs(rem)<Decimal(500)*p**(2*N),'O(p^2N) edge magnitude numerical only')
        for n in (20,24,28):
            U=Decimal(1)
            for k in range(100): U/=1+p**(2*k+1)
            target=U*p/(1+p)
            normed=(R[n]-U)/(-p)**n
            demand(abs(normed-target)<Decimal(100)*p**n,'signed first pole consistency')
print('VERIFY_OK',checks,'assertions')
