"""Exact rational tests for Euclidean geometry of cycle resistance metrics.
The universal proof is analytic; finite examples are independent corroboration.
Requires Python 3 standard library only.
"""
from fractions import Fraction as F
from math import cos, pi, sin, log


def inverse(A):
    n=len(A)
    X=[[F(A[i][j]) for j in range(n)]+[F(i==j) for j in range(n)] for i in range(n)]
    for k in range(n):
        j=next(i for i in range(k,n) if X[i][k])
        X[k],X[j]=X[j],X[k]
        pivot=X[k][k]
        X[k]=[v/pivot for v in X[k]]
        for i in range(n):
            if i != k:
                t=X[i][k]
                X[i]=[a-t*b for a,b in zip(X[i],X[k])]
    return [x[n:] for x in X]


def determinant(M):
    n=len(M)
    X=[[F(v) for v in row] for row in M]
    result=F(1)
    for k in range(n):
        j=next((i for i in range(k,n) if X[i][k]),None)
        if j is None: return F(0)
        if j!=k: X[k],X[j]=X[j],X[k];result=-result
        pivot=X[k][k];result*=pivot
        for i in range(k+1,n):
            t=X[i][k]/pivot
            for l in range(k+1,n): X[i][l]-=t*X[k][l]
            X[i][k]=F(0)
    return result


def resistances(weights):
    n=len(weights);L=[[F(0) for j in range(n)] for i in range(n)]
    for i,r in enumerate(weights):
        j=(i+1)%n;c=1/r
        L[i][i]+=c;L[j][j]+=c;L[i][j]-=c;L[j][i]-=c
    Q=inverse([row[:-1] for row in L[:-1]])
    rmat=[[F(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            a=Q[i][i] if i<n-1 else 0
            b=Q[j][j] if j<n-1 else 0
            c=Q[i][j] if i<n-1 and j<n-1 else 0
            rmat[i][j]=a+b-2*c
    return rmat


def gram_minor(rmat):
    n=len(rmat)
    return [[(rmat[0][i]**2+rmat[0][j]**2-rmat[i][j]**2)/2 for j in range(1,n)] for i in range(1,n)]


def chebyshev_two(n):
    a,b=1,2
    if n==0: return 1
    if n==1: return 2
    for _ in range(2,n+1): a,b=b,4*b-a
    return b

weights_cases = [
    [F(1)]*n for n in range(3,10)
] + [
    [F(1),F(2),F(3)],
    [F(2),F(5),F(3),F(7)],
    [F(1,2),F(3,4),F(5,6),F(7,8),F(9,10)],
    [F(1),F(1,3),F(2),F(7),F(3,2),F(5)],
    [F(1),F(1),F(1,4),F(4),F(2),F(5),F(2,3)],
]
for weights in weights_cases:
    n=len(weights); perimeter=sum(weights); t=[F(0)]
    for r in weights[:-1]:t.append(t[-1]+r)
    distances=resistances(weights)
    for i in range(n):
        for j in range(n):
            arc=abs(t[i]-t[j])
            expected=arc*(perimeter-arc)/perimeter
            assert distances[i][j]==expected,(n,i,j,distances[i][j],expected)
    G=gram_minor(distances)
    for k in range(1,n):
        assert determinant([row[:k] for row in G[:k]])>0,(weights,k)
print('EXACT_OK weighted_cycle_resistance_and_strict_Euclidean_cases=',len(weights_cases))

for n in range(3,10):
    distances=resistances([F(1)]*n)
    E=gram_minor(distances)
    exact=determinant(E)
    target=F(2**(n-1)*(chebyshev_two(n)-(-1)**n),3*n**(n+2))
    assert exact==target,(n,exact,target)
print('EXACT_OK simplex_Gram_determinants_n=3..9')

for n in range(3,32):
    d=[F(k*(n-k),n) for k in range(n)]
    for j in range(1,n):
        trig=sum(float(d[k]**2)*cos(2*pi*j*k/n) for k in range(n))
        s2=sin(pi*j/n)**2
        target=-(3-2*s2)/(2*n*s2*s2)
        assert abs(trig-target)<1e-8,(n,j,trig,target)
print('FOURIER_OK exact_formula_numeric_replay_n=3..31')

for n in [4,8,16,32,64,128,256,1000]:
    ratio=2*(n-2)/(n-1)
    upper=2*log(2)/log(ratio)
    assert upper>2
    if n>4: assert upper<previous
    previous=upper
print('BOUND_OK power_triangle_obstructions_and_convergence_to_2')
print('ALL_CYCLE_RESISTANCE_CHECKS_OK')
