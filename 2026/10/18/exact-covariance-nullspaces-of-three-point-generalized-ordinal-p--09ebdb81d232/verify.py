"""Exact rational checks for the asymptotic covariance of length-three weak-order pattern counts.

Run: python verify.py. Only the Python standard library is required.
"""
from fractions import Fraction as F
from itertools import product

PATTERNS = tuple(sorted({tuple(sorted(set(t)).index(v) for v in t) for t in product(range(3), repeat=3)}))
assert len(PATTERNS) == 13
IDX = {w:i for i,w in enumerate(PATTERNS)}

def pat(t):
    u = sorted(set(t))
    return tuple(u.index(v) for v in t)

def rank(a):
    a = [list(r) for r in a]
    m,n=len(a),len(a[0]); pivot=0
    for col in range(n):
        j=next((i for i in range(pivot,m) if a[i][col]), None)
        if j is None:continue
        a[pivot],a[j]=a[j],a[pivot]
        v=a[pivot][col]
        for c in range(col,n):a[pivot][c]/=v
        for i in range(pivot+1,m):
            v=a[i][col]
            if v:
                for c in range(col,n):a[i][c]-=v*a[pivot][c]
        pivot+=1
        if pivot==m:break
    return pivot

def exact_covariance(p):
    q=len(p); m=[F(0) for _ in range(13)]
    for w in product(range(q),repeat=3):
        wt=F(1)
        for x in w:wt*=p[x]
        m[IDX[pat(w)]]+=wt
    joint=[]
    for d in range(3):
        J=[[F(0) for _ in range(13)] for __ in range(13)]
        for w in product(range(q),repeat=3+d):
            wt=F(1)
            for x in w:wt*=p[x]
            J[IDX[pat(w[:3])]][IDX[pat(w[d:d+3])]]+=wt
        joint.append(J)
    S=[[F(0) for _ in range(13)] for __ in range(13)]
    for i in range(13):
        for j in range(13):
            S[i][j]=joint[0][i][j]+sum(joint[d][i][j]+joint[d][j][i] for d in (1,2))-5*m[i]*m[j]
    return S

def kernel_vectors(q):
    unit = [F(1)]*13
    up=[F((p[0]<p[1])-(p[1]<p[2])) for p in PATTERNS]
    down=[F((p[0]>p[1])-(p[1]>p[2])) for p in PATTERNS]
    ans=[unit,up,down]
    if q==2:
        v=[F(0)]*13
        v[IDX[(1,1,0)]]=F(1)
        v[IDX[(0,1,1)]]=F(-1)
        ans.append(v)
    return ans

def check(p):
    q=len(p)
    assert all(x>0 for x in p) and sum(p)==1
    S=exact_covariance(p)
    assert S==[list(x) for x in zip(*S)]
    r=rank(S)
    expected={1:0,2:3}.get(q,10)
    assert r==expected, (q,p,r,expected)
    for v in kernel_vectors(q):
        assert all(sum(S[i][j]*v[j] for j in range(13))==0 for i in range(13)),(q,p,v)
    print('q=',q,'p=',','.join(map(str,p)),'rank=',r,'expected=',expected)

if __name__=='__main__':
    check([F(1)])
    for a in [F(1,2),F(1,3),F(2,5)]:check([a,1-a])
    check([F(1,3)]*3)
    check([F(1,2),F(1,3),F(1,6)])
    check([F(1,10),F(1,5),F(7,10)])
    check([F(1,4)]*4)
    check([F(1,10),F(2,10),F(3,10),F(4,10)])
    print('All exact covariance/rank/coboundary checks passed.')
