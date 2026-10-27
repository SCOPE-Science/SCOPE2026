"""Independent finite checks for commuting graphs of odd dihedral-quandle endomorphisms.
Run with Python 3 standard library only.
"""
from math import comb
from itertools import product

def graph(n):
    pts=[(u,b) for u in range(n) for b in range(n)]
    adj=[set() for _ in pts]
    for i,(u,b) in enumerate(pts):
        for j in range(i+1,len(pts)):
            v,d=pts[j]
            if (u*d-v*b)%n==0:
                adj[i].add(j);adj[j].add(i)
    return pts,adj

def peo(p,e):
    n=p**e
    if e==0:return [(0,0)]
    arr=[(u,b) for u in range(n) for b in range(n) if u%p!=0 or b%p!=0]
    if e==1:return arr+[(0,0)]
    base=p**(e-2)
    for u,b in peo(p,e-2):
        for a in range(p):
            for c in range(p):
                arr.append((p*(u+a*base),p*(b+c*base)))
    return arr

def test_peo(p,e):
    n=p**e
    pts,adj=graph(n)
    order=[u*n+b for u,b in peo(p,e)]
    assert len(order)==n*n and len(set(order))==n*n
    positions={v:i for i,v in enumerate(order)}
    for i,v in enumerate(order):
        later=[w for w in adj[v] if positions[w]>i]
        for j,w in enumerate(later):
            for z in later[j+1:]:
                assert z in adj[w],('not simplicial',n,pts[v],pts[w],pts[z])

def polynomial(p,e):
    if e==0:return [1,1]
    if e==1:return [((p+1)*comb(p,j) if j<=p else 0)- (p*comb(1,j) if j<=1 else 0) for j in range(p+1)]
    B=polynomial(p,e-2)
    n=p**e;s=p**(e-1);cliques=p**(e-1)*(p+1)
    out=[]
    for j in range(n+1):
        core=0
        for k,c in enumerate(B):
            for h in range(k+1):
                if p*p*h>=j:core+=c*(-1)**(k-h)*comb(k,h)*comb(p*p*h,j)
        attach=cliques*(comb(n,j)-(comb(s,j) if j<=s else 0))
        out.append(core+attach)
    while out[-1]==0:out.pop()
    return out

def maximal_cliques(adj):
    ans=[]
    def bronk(R,P,X):
        if not P and not X:
            ans.append(frozenset(R));return
        v=max(P|X,key=lambda u:len(P&adj[u])) if P or X else None
        for u in list(P-adj[v] if v is not None else P):
            bronk(R|{u},P&adj[u],X&adj[u]);P.remove(u);X.add(u)
    bronk(set(),set(range(len(adj))),set())
    return ans

def check_clique_distribution(n,p,e):
    pts,adj=graph(n)
    maximal=maximal_cliques(adj)
    assert len(maximal)==sum(p**j for j in range(e+1)),(n,len(maximal))
    assert all(len(x)==n for x in maximal)
    if n<=9:
        cs={frozenset()}
        for x in maximal:
            l=list(x)
            for mask in range(1,1<<len(l)):
                cs.add(frozenset(l[i] for i in range(len(l)) if mask>>i&1))
        sizes=[sum(len(x)==j for x in cs) for j in range(n+1)]
        assert sizes==polynomial(p,e),(n,sizes,polynomial(p,e))
    E=sum(len(s) for s in adj)//2
    assert E==polynomial(p,e)[2]
    return len(maximal),E

def check_affine(n):
    # Check the affine normal form by independently testing ALL n^n self maps.
    expected={tuple((a*x+b)%n for x in range(n)) for a in range(n) for b in range(n)}
    accepted=set()
    for f in product(range(n),repeat=n):
        if all(f[(2*y-x)%n]==(2*f[y]-f[x])%n for x in range(n) for y in range(n)):
            accepted.add(f)
    assert accepted==expected,(n,len(accepted),len(expected))

def check_induced_C4():
    n=15;v=[(10,0),(6,0),(0,10),(0,6)]
    for i,j in ((0,1),(1,2),(2,3),(3,0)):
        assert (v[i][0]*v[j][1]-v[j][0]*v[i][1])%n==0
    for i,j in ((0,2),(1,3)):
        assert (v[i][0]*v[j][1]-v[j][0]*v[i][1])%n!=0

if __name__=='__main__':
    for n in (3,5):check_affine(n)
    for p,e in ((3,1),(3,2),(3,3),(5,1),(5,2)):
        test_peo(p,e)
        print('PEO_OK',p,e)
    for p,e in ((3,1),(3,2),(5,1),(5,2)):
        print('MAX_CLIQUES_AND_EDGES',p,e,check_clique_distribution(p**e,p,e))
    check_induced_C4()
    print('VERIFY_OK dihedral commuting graph chordality and clique recurrence')
