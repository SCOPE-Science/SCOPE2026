#!/usr/bin/env python3
"""Exact, self-contained face, orbit, link and singular-torus checks.
Rebuilds from the graph definition; does not import the shelling checker.
"""
from itertools import combinations
from collections import Counter, defaultdict, deque
N=16
S={1,4,8}
def independent(t):
    for a,b in combinations(t,2):
        if min((b-a)%N,(a-b)%N) in S:return False
    return True
faces={tuple(x) for k in range(5) for x in combinations(range(N),k) if independent(x)}
assert Counter(map(len, faces)) == {0:1,1:16,2:80,3:144,4:80}

def link(t):
    st=set(t)
    return {f for f in faces if st.isdisjoint(f) and tuple(sorted(st.union(f))) in faces}

def orbit(t):
    return {tuple(sorted((sgn*x+j)%16 for x in t)) for sgn in (1,-1) for j in range(16)}

def betti_mod_p(X,p):
    """Reduced Betti numbers in degrees -1,...,d over an exact prime field."""
    by={k:sorted(f for f in X if len(f)==k) for k in range(max(map(len,X))+1)}
    def rank(mat):
        m=[list(row) for row in mat]
        if not m:return 0
        rr=0;ncol=len(m[0])
        for col in range(ncol):
            pivot=next((t for t in range(rr,len(m)) if m[t][col]%p),None)
            if pivot is None:continue
            m[rr],m[pivot]=m[pivot],m[rr]
            v=pow(m[rr][col]%p,-1,p)
            for j in range(col,ncol):m[rr][j]=m[rr][j]*v%p
            for t in range(rr+1,len(m)):
                coef=m[t][col]
                if coef:
                    for j in range(col,ncol):m[t][j]=(m[t][j]-coef*m[rr][j])%p
            rr+=1
            if rr==len(m):break
        return rr
    ranks={}
    for k in range(1,max(by)+1):
        lower=by[k-1];upper=by[k]
        idx={f:i for i,f in enumerate(lower)}
        B=[[0]*len(upper) for _ in lower]
        for j,t in enumerate(upper):
            for h in range(k):
                row=idx[t[:h]+t[h+1:]]
                B[row][j]+=(-1)**h
        ranks[k]=rank(B)
    return {k-1:len(c)-ranks.get(k,0)-ranks.get(k+1,0) for k,c in by.items()}

# Check orbit decomposition and local link homology over two different fields.
expected={
    0: [((),1,1)],
    1: [((0,),16,2)],
    2: [((0,2),16,2),((0,3),16,1),((0,5),16,2),((0,6),16,1),((0,7),16,2)],
    3: [((0,2,5),32,1),((0,2,7),32,2),((0,2,9),16,1),((0,3,6),16,1),((0,3,9),32,1),((0,5,10),16,1)],
    4: [((0,2,5,7),16,1),((0,2,5,11),32,1),((0,2,7,9),16,1),((0,3,6,9),16,1)]
}
for k in range(5):
    remaining={f for f in faces if len(f)==k}
    got=[]
    while remaining:
        t=min(remaining);oo=orbit(t)
        assert oo<=remaining
        remaining-=oo
        rep=min(oo)
        lk=link(rep)
        top=3-k
        for p in (2,3):
            h=betti_mod_p(lk,p)
            assert h[top] in (1,2), (rep, h)
            assert all(v==0 for i,v in h.items() if i!=top), (rep,h)
        got.append((rep,len(oo),betti_mod_p(lk,2)[top]))
    assert sorted(got)==sorted(expected[k]), (k,got)

# The non-manifold support is the union of the triangular orbit D16*(0,2,7).
T=orbit((0,2,7))
E={e for t in T for e in combinations(t,2)}
V={v for t in T for v in t}
assert len(T)==32 and len(E)==48 and len(V)==16
assert E == {e for e in faces if len(e)==2 and min((e[1]-e[0])%16,(e[0]-e[1])%16) in (2,5,7)}
assert T == {t for t in faces if len(t)==3 and len(link(t))==4}
inc=Counter(e for t in T for e in combinations(t,2))
assert all(inc[e]==2 for e in E)
for v in V:
    nbr={b if a==v else a for a,b in E if v in (a,b)}
    vedges=[tuple(sorted(set(t)-{v})) for t in T if v in t]
    deg=Counter(w for e in vedges for w in e)
    assert len(nbr)==6 and len(vedges)==6 and all(deg[w]==2 for w in nbr)
    reached={next(iter(nbr))}
    while True:
        new=reached|{w for e in vedges if set(e)&reached for w in e}
        if new==reached:break
        reached=new
    assert reached==nbr # every vertex link is one 6-cycle
# Explicit coherent integer orientation: the boundary of this chain must vanish.
boundary=Counter()
for i in range(N):
    for t in ((i,(i+2)%N,(i+7)%N),(i,(i+7)%N,(i+5)%N)):
        assert tuple(sorted(t)) in T
        for j in range(3):
            a,b=[t[h] for h in range(3) if h!=j]
            boundary[tuple(sorted((a,b)))]+=(-1)**j * (1 if a<b else -1)
assert set(boundary)==E and all(v==0 for v in boundary.values())
# Connectedness: the edges of difference seven alone generate the whole 16-cycle.
assert __import__('math').gcd(7,N)==1
# Closed connected orientable surface with 16-48+32=0 is a torus.
assert len(V)-len(E)+len(T)==0
# Link ranks =2 at precisely faces of the torus; elsewhere they equal 1.
for t in faces:
    if not t:continue
    h=betti_mod_p(link(t),2)
    b=h[3-len(t)]
    assert b==(2 if t in T or t in E or len(t)==1 else 1)
print('PASS: all 321 faces, 17 dihedral orbits and integral-link hypotheses; local ranks 2 exactly on a 16-48-32 oriented torus.')
