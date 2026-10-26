"""Finite exact-arithmetic checks for ideal chains in modular Alexander quandle algebras."""
from itertools import combinations, product
from math import comb

def rank(rows,p):
    a=[list(x) for x in rows]
    if not a:return 0
    n=len(a[0]);r=0
    for c in range(n):
        t=next((i for i in range(r,len(a)) if a[i][c]%p),None)
        if t is None:continue
        a[r],a[t]=a[t],a[r];v=pow(a[r][c],-1,p)
        a[r]=[x*v%p for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]%p:
                v=a[i][c];a[i]=[(x-v*y)%p for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r

def add(a,b,p):return [(x+y)%p for x,y in zip(a,b)]
def mul(a,b,p,m):
    out=[0]*m
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:out[(i+j)%m]=(out[(i+j)%m]+x*y)%p
    return out

def basis_z(p,m):
    return [[(comb(k,j)*(-1)**(k-j))%p if j<=k else 0 for j in range(m)] for k in range(m)]

def auto(v,t,p,m):
    out=[0]*m
    for i,x in enumerate(v):out[t*i%m]=(out[t*i%m]+x)%p
    return out

def star(a,b,t,p,m):return mul(auto(a,t,p,m),auto(b,(1-t)%m,p,m),p,m)

def is_ideal(rows,side,t,p,m):
    if not rows:return True
    for x in rows:
        for j in range(m):
            e=[int(i==j) for i in range(m)]
            z=star(x,e,t,p,m) if side=='right' else star(e,x,t,p,m)
            if rank(rows+[z],p)!=rank(rows,p):return False
    return True

def all_subspaces3(p):
    n=3
    yield []
    for r in range(1,n+1):
        for pivs in combinations(range(n),r):
            free=[c for c in range(n) if c not in pivs]
            positions=[(i,c) for i in range(r) for c in free if c>pivs[i]]
            for vs in product(range(p),repeat=len(positions)):
                rows=[[int(c==pivs[i]) for c in range(n)] for i in range(r)]
                for (i,c),v in zip(positions,vs):rows[i][c]=v
                yield rows

def run(p,r,t):
    m=p**r
    z=basis_z(p,m)
    assert t%p and (1-t)%p
    assert rank(z,p)==m
    for k in range(m+1):
        for side in ('left','right'):
            assert is_ideal(z[k:],side,t,p,m),(p,m,k,side)
    for i in range(m+1):
        for j in range(m+1):
            wanted=max(0,m-i-j)
            if not wanted:continue
            products=[star(a,b,t,p,m) for a in z[i:] for b in z[j:]]
            assert rank(products,p)==wanted,(p,m,i,j)
    if m==3:
        subs=list(all_subspaces3(p))
        assert len(subs)==28,len(subs)
        for side in ('left','right'):
            good=[s for s in subs if is_ideal(s,side,t,p,m)]
            assert len(good)==m+1,(side,len(good))
            assert all(any(rank(s+z[k:],p)==rank(s,p)==m-k for k in range(m+1)) for s in good)
    print('CHECK_OK',p,m,'t',t,'ideal_chain',m+1,'powers_checked')

if __name__=='__main__':
    for args in ((3,1,2),(5,1,2),(3,2,2)):
        run(*args)
