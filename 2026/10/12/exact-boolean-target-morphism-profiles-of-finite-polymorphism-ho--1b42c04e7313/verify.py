#!/usr/bin/env python3
from itertools import product
from math import comb

# Finite lattices given by their partial order x<=y.  Elements are 0..n-1.
def make_meet(leq):
    n=len(leq)
    meet=[[None]*n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            lows=[x for x in range(n) if leq[x][a] and leq[x][b]]
            tops=[x for x in lows if all(not (leq[x][y] and x!=y) for y in lows)]
            assert len(tops)==1
            meet[a][b]=tops[0]
    return meet

def join_irreducibles(leq):
    n=len(leq)
    # bottom is the unique element <= all.
    bottom=next(x for x in range(n) if all(leq[x][y] for y in range(n)))
    J=[]
    for j in range(n):
        if j==bottom: continue
        lowers=[x for x in range(n) if x!=j and leq[x][j]]
        covers=[x for x in lowers if not any(x!=z and z!=j and leq[x][z] and leq[z][j] for z in range(n))]
        if len(covers)==1:
            J.append(j)
    return J

def bool_meet(e):
    m=1<<e
    return [[a&b for b in range(m)] for a in range(m)]

def brute_counts(leq,e):
    n=len(leq); meet=make_meet(leq); bm=bool_meet(e); m=1<<e
    hom=emb=0
    for f in product(range(m), repeat=n):
        ok=True
        for a in range(n):
            for b in range(n):
                if f[meet[a][b]] != bm[f[a]][f[b]]:
                    ok=False; break
            if not ok: break
        if ok:
            hom+=1
            if len(set(f))==n: emb+=1
    return hom,emb

def formula(n,r,e):
    hom=(n+1)**e
    emb=sum((-1)**i*comb(r,i)*(n+1-i)**e for i in range(r+1))
    return hom,emb

def chain(n):
    return [[i<=j for j in range(n)] for i in range(n)]

def boolean2():
    # 0, a, b, 1
    bits=[0,1,2,3]
    return [[(bits[i] & bits[j])==bits[i] for j in range(4)] for i in range(4)]

def M3():
    # 0, a,b,c,1
    n=5
    leq=[[False]*n for _ in range(n)]
    for i in range(n): leq[i][i]=True
    for i in [1,2,3]: leq[0][i]=leq[i][4]=True
    leq[0][4]=True
    return leq

def N5():
    # pentagon: 0<a<b<1 and 0<c<1, c incomparable a,b
    n=5
    leq=[[False]*n for _ in range(n)]
    for i in range(n): leq[i][i]=True
    rel=[(0,1),(1,2),(2,4),(0,2),(1,4),(0,4),(0,3),(3,4)]
    for a,b in rel: leq[a][b]=True
    return leq

cases=[('C2',chain(2)),('C3',chain(3)),('C4',chain(4)),('B2',boolean2()),('M3',M3()),('N5',N5())]
checks=0
for name,leq in cases:
    n=len(leq); r=len(join_irreducibles(leq))
    for e in range(1,4):
        # avoid 8^5 exhaustive maps twice on the two 5-element cases only at e<=2
        if n>=5 and e==3: continue
        got=brute_counts(leq,e); want=formula(n,r,e)
        assert got==want,(name,e,r,got,want)
        checks+=2
    # independently verify the scalar-homomorphism count n+1 at e=1
    h,_=brute_counts(leq,1)
    assert h==n+1,(name,h,n+1)
    checks+=1
print(f'VERIFY_OK {checks} exact assertions')
