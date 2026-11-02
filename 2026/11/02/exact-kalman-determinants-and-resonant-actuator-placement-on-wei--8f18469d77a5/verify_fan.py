"""Self-contained exact and numerical checks for weighted fan controllability."""
from fractions import Fraction
from math import cos, pi, gcd, prod, isclose
from itertools import combinations

CHECKS = 0

def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)

def fan_integer_laplacian(n, a, b):
    # b times the Laplacian with unit path weights and spoke weight a/b.
    N = n + 1
    L = [[0] * N for _ in range(N)]
    for j in range(1, n):
        L[j][j] += b; L[j + 1][j + 1] += b
        L[j][j + 1] -= b; L[j + 1][j] -= b
    for j in range(1, N):
        L[0][0] += a; L[j][j] += a
        L[0][j] -= a; L[j][0] -= a
    return L

def matvec(A, x):
    return [sum(a * z for a, z in zip(row, x)) for row in A]

def kalman(A, inputs):
    N = len(A)
    # Columns interleaved by Krylov order for all input indices.
    blocks = []
    x = []
    for j in inputs:
        c = [0] * N; c[j] = 1; x.append(c)
    for _ in range(N):
        blocks.extend(x)
        x = [matvec(A, v) for v in x]
    return [[c[i] for c in blocks] for i in range(N)]

def bareiss_det(A):
    a = [r[:] for r in A]
    n = len(a)
    sign = 1
    old = 1
    for k in range(n-1):
        if not a[k][k]:
            alt = next((i for i in range(k+1,n) if a[i][k]), None)
            if alt is None:return 0
            a[k],a[alt]=a[alt],a[k]
            sign=-sign
        piv=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*piv-a[i][k]*a[k][j]
                assert num%old==0
                a[i][j]=num//old
            a[i][k]=0
        old=piv
    return sign*a[-1][-1]

def exact_rank(A):
    A = [[Fraction(z) for z in r] for r in A]
    m=len(A); n=len(A[0]); row=0
    for col in range(n):
        piv=next((i for i in range(row,m) if A[i][col]),None)
        if piv is None:continue
        A[piv],A[row]=A[row],A[piv]
        v=A[row][col]
        A[row]=[z/v for z in A[row]]
        for i in range(row+1,m):
            factor=A[i][col]
            if factor:
                A[i]=[x-factor*y for x,y in zip(A[i],A[row])]
        row+=1
        if row==m:break
    return row

def q(n, z):
    # monic polynomial whose zeros are the nonzero path-Laplacian eigenvalues
    u0=Fraction(1)
    u1=2-z
    if n==2:return -u1
    for _ in range(2,n):u0,u1=u1,(2-z)*u1-u0
    return (-1)**(n-1)*u1

def expected_abs_det(n, a, b):
    t=Fraction(a,b)
    return abs(t*q(n,-t)*q(n,n*t)/n)

for n in range(3,10):
    for a,b in [(1,6),(1,3),(2,5),(1,2),(1,1),(7,4)]:
        L=fan_integer_laplacian(n,a,b)
        desired=expected_abs_det(n,a,b)
        exponent=n*(n+1)//2
        for j in range(n+1):
            got=abs(bareiss_det(kalman(L,[j])))
            expected=desired if j and gcd(2*j-1,n)==1 else 0
            check(Fraction(got,b**exponent)==expected,
                  ('exact determinant',n,a,b,j,got,expected))

for n in range(3,56):
    for j in range(1,n+1):
        A=2*j-1
        missing=sum((A*k)%(2*n)==n for k in range(1,n))
        check(missing==(gcd(A,n)-1)//2,('zero modes',n,j,missing))
    for j in range(1,n+1):
        for ell in range(j+1,n+1):
            A=2*j-1; B=2*ell-1
            common=any((A*k)%(2*n)==n and (B*k)%(2*n)==n for k in range(1,n))
            check(common==(gcd(gcd(n,A),B)>1),('joint zeros',n,j,ell))

for n in range(3,33):
    for j in range(1,n+1):
        if gcd(2*j-1,n)==1:
            c=prod(abs(cos((j-.5)*k*pi/n)) for k in range(1,n))
            check(isclose(c,n**.5/(2**(n-1)),rel_tol=3e-7,abs_tol=1e-12),('trig product',n,j,c))

# Verify complete PBH tests for two inputs by exact rational ranks, including
# the resonances n=3 (t=1/3 and t=1), n=4 (t=1/2), n=6 (t=1/6, 1/2).
for n, test_rates in [(3,[(1,3),(1,1),(1,2)]),
                      (4,[(1,2),(1,3)]),
                      (5,[(1,1),(2,5)]),
                      (6,[(1,6),(1,2),(1,3)]),
                      (7,[(2,5)])]:
    for a,b in test_rates:
        L=fan_integer_laplacian(n,a,b)
        critical=[]
        for k in range(1,n):
            # root exact only when cos rational. Check known rational resonances.
            if n==3 and (k,a,b) in [(1,1,3),(2,1,1)]:critical.append(k)
            if n==4 and (k,a,b)==(2,1,2):critical.append(k)
            if n==6 and (k,a,b) in [(2,1,6),(3,1,3),(4,1,2)]:critical.append(k)
        for j in range(1,n+1):
            for ell in range(j+1,n+1):
                A=2*j-1;B=2*ell-1
                predicted=gcd(gcd(n,A),B)==1
                if critical:
                    k=critical[0]
                    predicted=predicted and k*(j-ell)%(2*n)!=0 and k*(j+ell-1)%(2*n)!=0
                check((exact_rank(kalman(L,[j,ell]))==n+1)==predicted,
                      ('2-path PBH',n,a,b,j,ell,predicted))
        for j in range(1,n+1):
            predicted=gcd(2*j-1,n)==1
            check((exact_rank(kalman(L,[0,j]))==n+1)==predicted,
                  ('apex-path PBH',n,a,b,j,predicted))

print('PASS',CHECKS,'finite exact and supplementary checks')
