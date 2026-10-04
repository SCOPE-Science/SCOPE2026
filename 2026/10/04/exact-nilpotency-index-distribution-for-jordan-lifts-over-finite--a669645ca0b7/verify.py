from itertools import product
from collections import Counter

def zero(n): return [[0]*n for _ in range(n)]
def eye(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def add(A,B,q):
    return [[(A[i][j]+B[i][j])%q for j in range(len(A[0]))] for i in range(len(A))]
def mul(A,B,q):
    n=len(A); m=len(B[0]); k=len(B)
    return [[sum(A[i][t]*B[t][j] for t in range(k))%q for j in range(m)] for i in range(n)]
def iszero(A): return all(x==0 for row in A for x in row)
def jordan(n):
    J=zero(n)
    for i in range(n-1): J[i][i+1]=1
    return J

def dual_mul(X,Y,q):
    A,B=X; C,D=Y
    return (mul(A,C,q), add(mul(A,D,q),mul(B,C,q),q))
def dual_pow(X,e,q):
    n=len(X[0]); R=(eye(n),zero(n))
    while e:
        if e&1: R=dual_mul(R,X,q)
        X=dual_mul(X,X,q); e//=2
    return R
def index_of(J,B,q):
    X=(J,B)
    for e in range(1,2*len(J)+1):
        A,D=dual_pow(X,e,q)
        if iszero(A) and iszero(D): return e
    raise AssertionError('bound failed')

def expected(n,q):
    out={n:q**(n*n-n)}
    for j in range(1,n+1):
        out[n+j]=(q-1)*q**(n*n-n+j-1)
    return out

def run(n,q):
    J=jordan(n); c=Counter()
    for vals in product(range(q), repeat=n*n):
        B=[list(vals[i*n:(i+1)*n]) for i in range(n)]
        c[index_of(J,B,q)] += 1
    exp=expected(n,q)
    assert dict(sorted(c.items()))==exp, (n,q,c,exp)
    print(f'n={n} q={q} observed={dict(sorted(c.items()))} expected={exp}')

for n,q in [(1,2),(2,2),(3,2),(2,3)]: run(n,q)
print('VERIFY_OK')
