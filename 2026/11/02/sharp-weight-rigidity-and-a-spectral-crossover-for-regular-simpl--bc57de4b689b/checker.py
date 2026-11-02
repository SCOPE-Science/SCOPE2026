"""Exact-integer consistency checks for the triangular-graph frame theorem.

This finite checker is supplementary: its finite range does not prove the
all-dimension statements, which follow from the incidence-matrix argument.
"""
from itertools import combinations

checks = 0

def check(test, label):
    global checks
    checks += 1
    assert test, label


def mm(A, B):
    nr, nc, mid = len(A), len(B[0]), len(B)
    out = [[0] * nc for _ in range(nr)]
    for i in range(nr):
        for k in range(mid):
            aik = A[i][k]
            if aik:
                for j in range(nc):
                    out[i][j] += aik * B[k][j]
    return out


def add(*items):
    return [[sum(A[i][j] for A in items) for j in range(len(items[0][i]))]
            for i in range(len(items[0]))]


def shift(A, v):
    return [[A[i][j] - (v if i == j else 0)
             for j in range(len(A))] for i in range(len(A))]


def matvec(A, v):
    return [sum(x * y for x, y in zip(row, v)) for row in A]


def inner(x, y):
    return sum(a*b for a,b in zip(x,y))


def run(m):
    n = m + 1
    E = list(combinations(range(n), 2))
    N = len(E)
    D = m*m - 1
    ae, be, ce = 2*(m-1), m-3, 4
    L = 4*(m-2)*(m-1)
    T = (m-5)*(m-3)
    U = 8
    A = [[ae if i == j else be if len(set(e) & set(f)) == 1 else ce
          for j,f in enumerate(E)] for i,e in enumerate(E)]
    adj = [[1 if i != j and len(set(e) & set(f)) == 1 else 0
            for j,f in enumerate(E)] for i,e in enumerate(E)]
    inc = [[int(v in e) for e in E] for v in range(n)]
    # Gram of unsigned incidence: Q^T Q = 2I + Adj.
    incT = [list(c) for c in zip(*inc)]
    qtq = mm(incT,inc)
    qqt = mm(inc,incT)
    for i in range(N):
        for j in range(N):
            check(qtq[i][j] == adj[i][j] + (2 if i==j else 0), ('incidence',m,i,j))
            check(A[i][j] == (2*(m-3) if i==j else 0) +(m-7)*adj[i][j] + 4, ('gram',m,i,j))
        check(sum(A[i]) == L, ('row',m,i))
    for i in range(n):
        for j in range(n):
            check(qqt[i][j] == (n-2 if i==j else 0) + 1, ('vertex-incidence',m,i,j))
    check(sum(A[i][i] for i in range(N)) == L + m*T + (N-m-1)*U, ('trace',m))
    check(sum(A[i][j]*A[j][i] for i in range(N) for j in range(N)) == L*L+m*T*T+(N-m-1)*U*U, ('trace2',m))
    check(L>max(T,U), ('gap',m))
    check((T-U)*(m+1)==(m-7)*D, ('crossover',m))
    # Check an explicit *sharp* nonnegative perturbation of the uniform weight.
    z=[0]*N
    if m<=7:
        for e,v in [((0,1),1),((2,3),1),((0,2),-1),((1,3),-1)]:
            z[E.index(e)]=v
        mu = U
    else:
        z=[int(0 in e)-int(1 in e) for e in E]
        mu=T
    check(sum(z)==0 and inner(z,z)>0,('witness',m))
    check(matvec(A,z)==[mu*zi for zi in z],('witness-eigen',m))
    # Let w=1+z/2, t=w/||w||. Multiplying by 4 eliminates fractions.
    w4 = [2+zi for zi in z]
    check(min(w4)>=0,('positive',m))
    den=inner(w4,w4)
    top=sum(w4)*sum(w4)//N  # exactly 4N, because sum z=0
    check((sum(w4)**2)%N==0,('normalization',m))
    quad=inner(w4,matvec(A,w4))
    check(L*den-quad==(L-mu)*(den-top),('sharp-identity',m))
    if m <= 11:
        X = mm(shift(A,L),shift(A,T))
        Y = mm(X,shift(A,U))
        for i in range(N):
            for j in range(N):
                check(Y[i][j]==0,('annihilator',m,i,j))

for m in range(4,19):
    run(m)
print('PASS:',checks,'exact-integer assertions, m=4,...,18')
