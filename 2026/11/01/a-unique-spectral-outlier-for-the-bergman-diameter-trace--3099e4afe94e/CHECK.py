"""Reproducible numerical checks for the Bergman diameter spectral theorem.
These finite checks supplement but do not replace the analytical argument.
Run with Python 3 and its standard library.
"""
import math

count=0

def check(test, name):
    global count
    assert test, name
    count+=1

def entry(n,m):
    if (n+m)%2:
        return 0.0
    return 2*math.sqrt((n+1)*(m+1))/((n+m+1)*(n+m+2))

for N in (8,24,60):
    for n in range(N):
        check(abs(entry(n,n)-2*(n+1)/((2*n+1)*(2*n+2)))<1e-14, 'diagonal')
        for m in range(N):
            check(abs(entry(n,m)-entry(m,n))<1e-14,'symmetry')
            check((entry(n,m)==0.0)==((n+m)%2==1),'parity')

bound=1+math.sqrt(4*math.log(2)-1-math.pi**2/6)
low=3/5+math.sqrt(219)/30
check(low>1,'strict outlier lower bound')
check(1.35<bound<1.36,'bound range')
check(abs(entry(0,2)-math.sqrt(3)/6)<1e-14,'two-dimensional coupling')
check(abs(entry(2,2)-1/5)<1e-14,'two-dimensional diagonal')

# Actual matrix eigenvalue approximate by power iteration of nonnegative blocks.
def eigmax(N):
    A=[[entry(i,j) for j in range(N)] for i in range(N)]
    v=[1/math.sqrt(N)]*N
    for k in range(180):
        u=[sum(a*b for a,b in zip(row,v)) for row in A]
        scale=math.sqrt(sum(x*x for x in u))
        v=[x/scale for x in u]
    return sum(v[i]*sum(A[i][j]*v[j] for j in range(N)) for i in range(N))

for N in (12,24,60):
    e=eigmax(N)
    check(low-1e-10 <= e < bound,'matrix leading eigenvalue')

for n in range(1,121):
    terms=sum(entry(n,m)*math.sqrt((n+1)/(m+1)) for m in range(1,1201))
    if n%2:
        upper=(n+1)*math.log((n+2)/(n+1))
    else:
        upper=(n+1)*math.log((n+3)/(n+2))
    check(terms < upper+1e-11 and upper<1, 'Schur inequality')

# The singular Weyl-sequence Rayleigh quotient converges to the edge 1.
ray=[]
for M in (4,8,16,32):
    I=range(M,M*M+1)
    h=sum(1/(2*i+1) for i in I)
    q=sum(2/((2*i+2*j+1)*(2*i+2*j+2)) for i in I for j in I)
    ray.append(q/h)
    check(0<q/h<1,'Weyl Rayleigh quotient')
check(all(ray[i]<ray[i+1] for i in range(3)), 'Weyl quotient increasing in chosen sample')

b2=sum(1/((j+1)**2*(2*j+1)) for j in range(1,150000))
check(abs(b2-(4*math.log(2)-1-math.pi**2/6))<1e-8, 'offdiagonal Hilbert-Schmidt norm')
print('PASS',count,'deterministic numerical assertions')
print('finite leading eigenvalues:',[(n,round(eigmax(n),12)) for n in (12,24,60)])
print('Weyl Rayleigh samples:',list(zip((4,8,16,32),[round(q,9) for q in ray])))
print('certified lower and upper:',low,bound)
