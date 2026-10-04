#!/usr/bin/env python3
from itertools import combinations, product

# A finite poset is represented by a reflexive <= matrix.
def transitive_closure(n, rel):
    le=[[False]*n for _ in range(n)]
    for i in range(n): le[i][i]=True
    for a,b in rel: le[a][b]=True
    for k in range(n):
        for i in range(n):
            if le[i][k]:
                for j in range(n):
                    if le[k][j]: le[i][j]=True
    return le

def join_with_discrete(leX, n):
    m=len(leX); N=m+n
    le=[[False]*N for _ in range(N)]
    for i in range(N): le[i][i]=True
    for i in range(m):
        for j in range(m): le[i][j]=leX[i][j]
    for x in range(m):
        for t in range(m,N): le[x][t]=True
    return le, list(range(m,N))

def monotone(f, leA, leB):
    for i in range(len(leA)):
        for j in range(len(leA)):
            if leA[i][j] and not leB[f[i]][f[j]]:
                return False
    return True

def beat_points(le):
    n=len(le); out=[]
    for x in range(n):
        upper=[y for y in range(n) if y!=x and le[x][y]]
        lower=[y for y in range(n) if y!=x and le[y][x]]
        # up beat: strict upper set has a least element
        up=False
        for u in upper:
            if all(le[u][v] for v in upper): up=True; break
        down=False
        for d in lower:
            if all(le[v][d] for v in lower): down=True; break
        if up or down: out.append(x)
    return out

def induced(le, keep):
    return [[le[i][j] for j in keep] for i in keep]

def core_size(le):
    le=[row[:] for row in le]
    while True:
        bs=beat_points(le)
        if not bs: return len(le)
        x=bs[0]
        keep=[i for i in range(len(le)) if i!=x]
        le=induced(le,keep)

def check_base(name, leX, ns=(2,3,4)):
    m=len(leX)
    # The sampled bases are known noncontractible and their two-point joins
    # must retain a nontrivial Stong core.
    leY,topsY=join_with_discrete(leX,2)
    assert core_size(leY)>1
    for n in ns:
        leZ,tops=join_with_discrete(leX,n)
        maxpairs=list(product(tops,tops))
        assert len(maxpairs)==n*n
        # Every two distinct maximal pairs differ in at least one coordinate.
        for p,q in combinations(maxpairs,2):
            assert p[0]!=q[0] or p[1]!=q[1]
        # For every choice of two top points, collapsing all other new maxima
        # to the first selected one is an order-preserving retraction.
        for b,d in combinations(tops,2):
            Ykeep=list(range(m))+[b,d]
            idx={old:i for i,old in enumerate(Ykeep)}
            leSub=induced(leZ,Ykeep)
            r=[]
            for z in range(m+n):
                if z in idx: r.append(idx[z])
                else: r.append(idx[b])
            assert monotone(r,leZ,leSub)
            for old in Ykeep:
                assert r[old]==idx[old]
        print(f'{name}: n={n} maximal_pairs={n*n} two_top_retractions=OK')

# Two-point antichain.
D2=transitive_closure(2,[])
# Four-point crown/minimal circle: 0,1 below 2,3.
C4=transitive_closure(4,[(0,2),(0,3),(1,2),(1,3)])
# Six-point minimal 2-sphere: three ordered two-point levels.
S2=transitive_closure(6,[(i,j) for i in (0,1) for j in (2,3,4,5)] + [(i,j) for i in (2,3) for j in (4,5)])

for name,base in [('D2',D2),('C4',C4),('S2',S2)]:
    check_base(name,base)
print('VERIFY_OK')
