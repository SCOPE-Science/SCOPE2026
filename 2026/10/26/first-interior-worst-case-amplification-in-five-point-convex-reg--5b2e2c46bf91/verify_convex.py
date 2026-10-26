"""Exact rational checks for coordinatewise stability of discrete convex regression.
Uses only Python's standard library. All assertions are finite checks.
"""
from fractions import Fraction as F
from itertools import combinations

checks = 0

def ok(condition, description):
    global checks
    assert condition, description
    checks += 1

def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]

def inverse(a):
    n=len(a)
    z=[list(map(F,row))+eye(n)[i] for i,row in enumerate(a)]
    for k in range(n):
        pivot=next(i for i in range(k,n) if z[i][k])
        z[k],z[pivot]=z[pivot],z[k]
        factor=z[k][k]
        z[k]=[v/factor for v in z[k]]
        for i in range(n):
            if i!=k:
                factor=z[i][k]
                z[i]=[a-factor*b for a,b in zip(z[i],z[k])]
    return [row[n:] for row in z]

def projection(n,active):
    d=[]
    for k in active:
        row=[F(0)]*n
        row[k:k+3]=[F(1),F(-2),F(1)]
        d.append(row)
    if not d:
        return eye(n)
    m=len(d)
    gram=[[sum(d[i][h]*d[j][h] for h in range(n)) for j in range(m)] for i in range(m)]
    inv=inverse(gram)
    return [[F(int(i==j))-sum(d[h][i]*inv[h][k]*d[k][j] for h in range(m) for k in range(m)) for j in range(n)] for i in range(n)]

def matsum_rows(p):
    return [sum(map(abs,row)) for row in p]

def matvec(p,v):
    return [sum(a*b for a,b in zip(row,v)) for row in p]

expected={2:F(1),3:F(4,3),4:F(7,5),5:F(11,7),6:F(91,57),7:F(83,51)}
for n in range(2,9):
    sharp=F(0)
    winners=[]
    for mask in range(1<<(n-2)):
        active=[k for k in range(n-2) if mask & (1<<k)]
        P=projection(n,active)
        for i in range(n):
            for j in range(n):
                ok(P[i][j]==P[j][i], f'symmetry {n}/{mask}')
                ok(sum(P[i][k]*P[k][j] for k in range(n))==P[i][j], f'idempotence {n}/{mask}')
        rows=matsum_rows(P)
        m=max(rows)
        if m>sharp:
            sharp=m
            winners=[(mask,[i for i,s in enumerate(rows) if s==m])]
        elif m==sharp:
            winners.append((mask,[i for i,s in enumerate(rows) if s==m]))
    if n in expected:
        ok(sharp==expected[n],f'optimal norm {n}')
    if n==5:
        ok(winners==[(5,[2])], 'unique active set and maximizing output index')
        specific=projection(5,[0,2])
        expected_p=[[29,12,-5,-2,1],[12,11,10,4,-2],[-5,10,25,10,-5],[-2,4,10,11,12],[1,-2,-5,12,29]]
        ok(specific==[[F(v,35) for v in row] for row in expected_p], 'exact five-point projector')
        x=list(map(F,[0,0,0,1,2]))
        y=list(map(F,[-1,2,-2,3,1]))
        v=list(map(F,[-1,1,1,1,-1]))
        eps=F(1,4)
        xp=matvec(specific,y)
        xq=matvec(specific,[a+eps*b for a,b in zip(y,v)])
        ok(xp==x,'first KKT fit')
        ok(xq[2]-xp[2]==F(11,28),'sharp center amplification at finite distance')
        for z in [xp,xq]:
            d=[z[k]-2*z[k+1]+z[k+2] for k in range(3)]
            ok(d[0]==0 and d[2]==0 and d[1]>0, 'feasibility / strict inactivity')
        ok(max(abs(eps*vv) for vv in v)==eps, 'input sup norm')
    if n>=5:
        P=projection(n,[0,2])
        ok(max(matsum_rows(P))==F(11,7),'stable embedded five-point face')
    print(f'n={n}  max={sharp}  winning_faces={winners[:8]}')
print(f'PASS {checks} exact-rational assertions')
