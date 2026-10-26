"""Exact rational verification of sharp edge-flow amplification on unweighted ladders.
Uses only the Python standard library. It checks the stated block decomposition
against an independently assembled graph-incidence projection.
"""
from fractions import Fraction as F
from math import sqrt

checks = 0

def ck(assertion, detail=''):
    global checks
    checks += 1
    if not assertion:
        raise AssertionError(f'check {checks}: {detail}')

def transpose(a):
    return list(map(list, zip(*a)))

def matmul(a, b):
    t = transpose(b)
    return [[sum(x * y for x,y in zip(row,col)) for col in t] for row in a]

def invert(a):
    n = len(a)
    aug = [list(row) + [F(i == j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        pivot = next((i for i in range(j,n) if aug[i][j]), None)
        if pivot is None: raise AssertionError('singular')
        aug[j],aug[pivot] = aug[pivot],aug[j]
        invp = 1 / aug[j][j]
        aug[j] = [x * invp for x in aug[j]]
        for i in range(n):
            if i != j and aug[i][j]:
                factor = aug[i][j]
                aug[i] = [v - factor * w for v,w in zip(aug[i],aug[j])]
    return [row[n:] for row in aug]

def identity(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]

def hodge_pred(n):
    B = [[F(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        B[i][i] = F(3 if i in (0,n-1) else 4)
        if i < n-1: B[i][i+1]=B[i+1][i]=F(-1)
    G = invert(B)
    D = [[F((j==h+1)-(j==h)) for j in range(n)] for h in range(n-1)]
    DG = matmul(D,G)
    Q = matmul(DG,transpose(D))
    dim = 3*n-2
    P = [[F(0) for _ in range(dim)] for _ in range(dim)]
    for i in range(n):
        for j in range(n):P[i][j]=2*G[i][j]
        for h in range(n-1):
            P[i][n+h] = P[n+h][i] = DG[h][i]
            P[i][n+n-1+h] = P[n+n-1+h][i] = -DG[h][i]
    for h in range(n-1):
        for k in range(n-1):
            base=F(h==k)
            P[n+h][n+k]=(base+Q[h][k])/2
            P[n+n-1+h][n+n-1+k]=(base+Q[h][k])/2
            P[n+h][n+n-1+k]=(base-Q[h][k])/2
            P[n+n-1+h][n+k]=(base-Q[h][k])/2
    return P,G,DG,Q

def from_incidence(n):
    v = 2*n
    edges=[]
    for j in range(n): edges.append((n+j,j)) # lower -> upper
    for j in range(n-1):edges.append((j,j+1))
    for j in range(n-1):edges.append((n+j,n+j+1))
    A = []
    for u,w in edges:
        row=[F(0)]*(v-1)
        if u<v-1:row[u]=F(-1)
        if w<v-1:row[w]=F(1)
        A.append(row)
    return matmul(matmul(A,invert(matmul(transpose(A),A))),transpose(A))

for n in range(2,23):
    P,G,DG,Q=hodge_pred(n)
    if n <= 11:
        independently_assembled=from_incidence(n)
        for rowa,rowb in zip(P,independently_assembled):
            for a,b in zip(rowa,rowb): ck(a==b,f'block/graph n={n}')
    dim=3*n-2
    for i in range(dim):
        for j in range(dim): ck(P[i][j]==P[j][i],f'symmetry n={n}')
    for i in range(dim):
        for j in range(dim):
            ck(sum(P[i][k]*P[k][j] for k in range(dim))==P[i][j],f'idempotence n={n}')
    norm=max(sum(abs(x) for x in row) for row in P)
    center=(n-1)//2
    K=[[2*x for x in row] for row in G]
    R=F(1)+2*K[center][center]-K[0][center]-K[-1][center]
    ck(norm==R,f'central rung sharp n={n}: {norm}, {R}')
    for i in range(n):
        direct=sum(abs(v) for v in P[i]); formula=F(1)+2*K[i][i]-K[0][i]-K[-1][i]
        ck(direct==formula,f'rung variation n={n}')
    for h in range(n-1):
        r1=DG[h][0]
        rn=DG[h][n-1]
        rail=F(2)-(rn-r1)
        ck(sum(abs(x) for x in P[n+h])==rail,f'rail row formula n={n}')
        ck(rail < 2,f'rail strict sub-2 n={n}')
    if n>=5: ck(R>2,f'cutoff n={n}')
    if n>2:
        for i in range((n-1)//2):
            ck(sum(abs(x) for x in P[i])<sum(abs(x) for x in P[i+1]),f'unimodal n={n}')
    signs=[F(1) for i in range(n)]
    signs.extend(F(1 if h<center else -1) for h in range(n-1))
    signs.extend(F(-1 if h<center else 1) for h in range(n-1))
    ck(sum(P[center][i]*signs[i] for i in range(dim))==norm, f'sign attainment n={n}')
    if n <= 9:
        print('n',n,'sharp=',norm,'edge_count=',dim)
print('ALL EXACT CHECKS PASSED:',checks)
