#!/usr/bin/env python3
"""Exact independent checks for compatible relations on a two-level semilattice of finite groups."""
from collections import deque
from itertools import product, permutations
from math import prod


def cyclic(n):
    return [[(i+j) % n for j in range(n)] for i in range(n)]


def elementary(p, d):
    n = p**d
    def add(x,y):
        z=0; v=1
        for _ in range(d):
            z+=((x%p+y%p)%p)*v; x//=p;y//=p;v*=p
        return z
    return [[add(i,j) for j in range(n)] for i in range(n)]


def symmetric3():
    perms=[(0,1,2)]+[t for t in permutations(range(3)) if t!=(0,1,2)]
    idx={t:i for i,t in enumerate(perms)}
    return [[idx[tuple(a[b[k]] for k in range(3))] for b in perms] for a in perms]


def normals(m):
    g=len(m); ident=0
    # Use finite-subsemigroup characterization of subgroups, plus conjugation.
    units=[]
    for mask in range(1,1<<g,2):
        H=[x for x in range(g) if mask>>x&1]
        if not all(m[x][y] in H for x in H for y in H):continue
        if any(not any(m[x][y]==ident and m[y][x]==ident for y in H) for x in H):continue
        inv={x:next(y for y in range(g) if m[x][y]==ident and m[y][x]==ident) for x in H}
        invall={x:next(y for y in range(g) if m[x][y]==ident and m[y][x]==ident) for x in range(g)}
        if all(m[m[a][x]][invall[a]] in H for a in range(g) for x in H):units.append(frozenset(H))
    return units


def candidates(g):
    z=len(g); S=list(product((0,1),range(z))); n=len(S)
    normal=normals(g)
    def subgroup_rel(N,M,X,Y):
        pieces={(1,1):N,(0,0):M,(1,0):X,(0,1):Y}
        return frozenset(n*i+j for i,(a,x) in enumerate(S) for j,(b,y) in enumerate(S)
                         if pieces[(a,b)] is not None and g[x][next(k for k in range(z) if g[y][k]==0)] in pieces[(a,b)])
    result={}
    for N in normal:
        for M in normal:
            if not N.issubset(M):continue
            middle=[H for H in normal if N.issubset(H) and H.issubset(M)]
            for X in [None]+middle:
                for Y in [None]+middle:
                    R=subgroup_rel(N,M,X,Y)
                    assert R not in result
                    result[R]=(N,M,X,Y)
    mul=[[S.index((min(S[i][0],S[j][0]),g[S[i][1]][S[j][1]])) for j in range(n)] for i in range(n)]
    return S,mul,result,len(normal)


def closed(R,mul):
    n=len(mul)
    return all(mul[r//n][s//n]*n+mul[r%n][s%n] in R for r in R for s in R)


def congruence(R,mul):
    n=len(mul)
    if not all((i*n+i) in R for i in range(n)):return False
    if not all((j*n+i) in R for r in R for i,j in [(r//n,r%n)]):return False
    return all((i*n+k) in R for i in range(n) for j in range(n) for k in range(n)
               if (i*n+j) in R and (j*n+k) in R)


def closure(R, new, mul, op):
    if new in R: return R
    old=set(R); old.add(new)
    queue=deque([new]); seq=list(R);seq.append(new)
    while queue:
        r=queue.popleft()
        for s in tuple(seq):
            for x in (op[r][s], op[s][r]):
                if x not in old:
                    old.add(x);queue.append(x);seq.append(x)
    return frozenset(old)


def exhaustive_closed(mul):
    n=len(mul);n2=n*n
    op=[[mul[r//n][s//n]*n+mul[r%n][s%n] for s in range(n2)] for r in range(n2)]
    start=frozenset(i*n+i for i in range(n))
    todo=deque([start]);seen={start}
    while todo:
        R=todo.popleft()
        for pair in range(n2):
            if pair in R:continue
            C=closure(R,pair,mul,op)
            if C not in seen:
                seen.add(C);todo.append(C)
    return seen


def main():
    cases=[('trivial',cyclic(1),True),('C2',cyclic(2),True),('C3',cyclic(3),True),('C2xC2',elementary(2,2),True),('S3',symmetric3(),False)]
    for name,g,exhaustive in cases:
        S,mul,cands,k=candidates(g)
        assert all(closed(R,mul) for R in cands)
        nc=sum(congruence(R,mul) for R in cands)
        # Compare to a separately evaluated normal-lattice formula.
        ns=normals(g)
        P=sum(1 for N in ns for M in ns if N<=M)
        D=sum((1+sum(1 for X in ns if N<=X<=M))**2 for N in ns for M in ns if N<=M)
        assert len(cands)==D and nc==P+k
        if exhaustive:
            actual=exhaustive_closed(mul)
            assert actual==set(cands), (name,len(actual),len(cands))
        print(name, 'group_order',len(g),'normal_subgroups',k,'diagonal',D,'congruences',nc,'verified_exhaustive',exhaustive)
    # Independent finite-field flag formula, using the Gaussian-binomial recurrence.
    from functools import lru_cache
    @lru_cache(None)
    def qbin(n,k,p):
        if k<0 or k>n: return 0
        if k==0 or k==n: return 1
        return qbin(n-1,k-1,p)+p**k*qbin(n-1,k,p)
    for p in (2,3,5):
        for d in range(1,6):
            sigma=lambda t:sum(qbin(t,j,p) for j in range(t+1))
            flags=sum(qbin(d,m,p)*qbin(m,n,p) for m in range(d+1) for n in range(m+1))
            diag=sum(qbin(d,m,p)*qbin(m,n,p)*(1+sigma(m-n))**2 for m in range(d+1) for n in range(m+1))
            con=flags+sigma(d)
            assert 0<con<=diag
            if d==1:assert (con,diag)==(5,17)
            if p==2 and d==2:assert (con,diag)==(17,110)
            if p==3 and d==2:assert (con,diag)==(21,145)
            print('flag_formula',p,d,con,diag)
    print('VERIFY_OK')

if __name__=='__main__':main()
