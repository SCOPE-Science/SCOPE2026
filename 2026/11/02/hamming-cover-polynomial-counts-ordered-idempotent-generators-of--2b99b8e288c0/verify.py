#!/usr/bin/env python3
"""Independent small-field enumeration of idempotent algebra generating tuples."""
from itertools import product
from math import prod

def structure(n,covers):
    rel={(i,i) for i in range(n)}|set(covers)
    while True:
        more=rel|{(i,k) for (i,j) in rel for (j2,k) in rel if j==j2}
        if more==rel:break
        rel=more
    cells=sorted(rel)
    index={a:i for i,a in enumerate(cells)}
    mult=[(index[(i,j)],index[(j,k)],index[(i,k)]) for (i,j) in cells for (j2,k) in cells if j==j2]
    cover=set(covers)
    assert all((i,j) in rel for i,j in cover)
    for i,j in cover:
        assert not any((i,h) in rel and (h,j) in rel for h in range(n) if h!=i and h!=j)
    return cells,mult,rel,cover

def predict(n,covers,p,k):
    cells,mul,rel,cover=structure(n,covers)
    N=0
    for cs in product(range(1<<k),repeat=n):
        if len(set(cs))<n:continue
        total=1
        for i,j in rel:
            if i==j:continue
            h=(cs[i]^cs[j]).bit_count()
            if (i,j) in cover:
                total*=p**h-p if h>=1 else 0
            else:
                total*=p**h
        N+=total
    return N

def explicit(n,covers,p,k):
    cells,mult,rel,cover=structure(n,covers)
    d=len(cells)
    def multiply(x,y):
        z=[0]*d
        for i,j,t in mult:
            z[t]=(z[t]+x[i]*y[j])%p
        return tuple(z)
    one=tuple(int(i==j) for i,j in cells)
    E=[v for v in product(range(p),repeat=d) if multiply(v,v)==v]
    def fullspan(gens):
        piv={}
        frontier=[one]
        while frontier:
            w=list(frontier.pop())
            for a in range(d):
                if not w[a]:continue
                if a in piv:
                    fac=w[a]
                    w=[(w[b]-fac*piv[a][b])%p for b in range(d)]
                else:
                    inv=pow(w[a],-1,p)
                    w=[(v*inv)%p for v in w]
                    piv[a]=w
                    if len(piv)==d:return True
                    frontier.extend(multiply(tuple(w),g) for g in gens)
                    break
        return len(piv)==d
    count=sum(1 for gens in product(E,repeat=k) if fullspan(gens))
    return count,len(E),p**d

def main():
    cases=[
        (2,[(0,1)],2,2),
        (2,[(0,1)],3,2),
        (3,[(0,1),(1,2)],2,2),
        (3,[(0,1),(1,2)],2,3),
        (3,[(0,1),(0,2)],2,2),
        (3,[(0,1),(0,2)],2,3),
        (3,[(0,1),(1,2)],3,2),
        (3,[],2,2),
        (4,[],2,2),
        (4,[(0,1),(0,2),(1,3),(2,3)],2,2),
        (4,[(0,1),(1,2),(2,3)],2,2),
    ]
    for n,cover,p,k in cases:
        x=predict(n,cover,p,k)
        y,num,total=explicit(n,cover,p,k)
        assert x==y,(n,cover,p,k,x,y)
        print(f'OK n={n} covers={cover} F_{p} k={k}: generating={y}; idempotents={num}; algebra_size={total}')
    print('VERIFY_OK: 11 exhaustive configurations')
if __name__=='__main__':main()
