#!/usr/bin/env python3
"""Exact finite checks for the weighted rectangular-rook controllability theorem.

No external dependencies. Exhaustive on small boards and deterministic samples
on larger boards. The finite checks support, but do not replace, the proof.
"""
from itertools import product
from random import Random

PRIME = 2305843009213693951
ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def rank_mod(M):
    if not M:
        return 0
    A = [[x % PRIME for x in row] for row in M]
    nr, nc = len(A), len(A[0]); r = 0
    for j in range(nc):
        pivot = next((i for i in range(r, nr) if A[i][j]), None)
        if pivot is None:
            continue
        A[pivot], A[r] = A[r], A[pivot]
        inv = pow(A[r][j], -1, PRIME)
        for i in range(r + 1, nr):
            scale = A[i][j] * inv % PRIME
            if scale:
                for k in range(j, nc):
                    A[i][k] = (A[i][k] - scale * A[r][k]) % PRIME
        r += 1
        if r == nr:
            break
    return r


def basis(p, q):
    # Four explicit invariant subspaces, as lists of column vectors.
    f = [[int(i == k) - int(i == p - 1) for i in range(p)]
         for k in range(p - 1)]
    g = [[int(j == k) - int(j == q - 1) for j in range(q)]
         for k in range(q - 1)]
    const = [[1 for _ in range(p * q)]]
    row = [[v[i] for i in range(p) for j in range(q)] for v in f]
    col = [[v[j] for i in range(p) for j in range(q)] for v in g]
    interaction = [[x[i]*y[j] for i in range(p) for j in range(q)]
                   for x in f for y in g]
    return const, row, col, interaction


def forest(n, edges):
    par = list(range(n))
    def root(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for x,y in edges:
        rx,ry = root(x),root(y)
        if rx == ry:
            return False
        par[rx] = ry
    return True


def parts(n, edges):
    par = list(range(n))
    def root(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for x,y in edges:
        par[root(x)] = root(y)
    comps={}
    for i in range(n):
        comps.setdefault(root(i), []).append(i)
    return list(comps.values())


def combinatorial(p,q,S,resonance):
    S=set(S)
    H=[(i,p+j) for i in range(p) for j in range(q) if (i,j) not in S]
    if not forest(p+q,H):
        return False
    if not resonance:
        return True
    F=parts(p+q,[(i,p+j) for i,j in S])
    if len(F)>2:
        return False
    if len(F)==1:
        return True
    r1=sum(v<p for v in F[0]); s1=sum(v>=p for v in F[0])
    r2=sum(v<p for v in F[1]); s2=sum(v>=p for v in F[1])
    return r1*s2 != r2*s1


def algebraic(p,q,S,resonance):
    const,row,col,interaction=basis(p,q)
    cols = [const, row+col if resonance else row, interaction]
    if not resonance:
        cols.append(col)
    indexes=[i*q+j for i,j in S]
    return all(rank_mod([[v[idx] for v in V] for idx in indexes])==len(V)
               for V in cols)


def laplacian(p,q,a,b):
    N=p*q; L=[[0]*N for _ in range(N)]
    for i in range(p):
        for j in range(q):
            x=i*q+j
            for ii in range(p):
                if ii!=i:
                    y=ii*q+j;L[x][x]+=a;L[x][y]-=a
            for jj in range(q):
                if jj!=j:
                    y=i*q+jj;L[x][x]+=b;L[x][y]-=b
    return L


def eigencheck(p,q,a,b):
    L=laplacian(p,q,a,b)
    E=basis(p,q)
    for vectors, lam in zip(E, [0,a*p,b*q,a*p+b*q]):
        for v in vectors:
            check(all(sum(row[k]*v[k] for k in range(p*q))==lam*v[i]
                      for i,row in enumerate(L)),
                  ('eigen',p,q,a,b,lam,v))


def constructions(p,q):
    base={(i,j) for i in range(p-1) for j in range(q-1)}
    if p==2:
        resonance={(0,j) for j in range(q)}
    elif q==2:
        resonance={(i,0) for i in range(p)}
    else:
        exclusions=[0,1]+[0]*(p-3)
        resonance={(i,j) for i in range(p-1) for j in range(q)
                   if j!=exclusions[i]}
    return base, resonance


def main():
    for p,q in [(2,2),(2,3),(2,4),(3,3),(3,4)]:
        eigencheck(p,q,1,100)   # nonresonant
        eigencheck(p,q,q,p)     # resonant
        N=p*q; mins=[N+1,N+1]
        feasible=[0,0]
        for mask in range(1<<N):
            S=[(i,j) for i in range(p) for j in range(q)
               if (mask >> (i*q+j))&1]
            for t in (0,1):
                expect=combinatorial(p,q,S,bool(t))
                actual=algebraic(p,q,S,bool(t))
                check(expect==actual,('criterion',p,q,mask,t))
                if actual:
                    mins[t]=min(mins[t],len(S));feasible[t]+=1
        expected_nonres=(p-1)*(q-1)
        expected_res= (p-1)*(q-1) if min(p,q)>=3 else max(p,q)
        check(mins==[expected_nonres,expected_res],('minimum',p,q,mins))
        base,exc=constructions(p,q)
        check(combinatorial(p,q,base,False),('base',p,q))
        check(combinatorial(p,q,exc,True),('resonant',p,q))
        check(len(base)==expected_nonres and len(exc)==expected_res,
              ('sizes',p,q))
        print('board',p,q,'all masks',1<<N,
              'minimum (nonres,res)',mins,'feasible counts',feasible)
    rng=Random(20261016)
    for p,q in [(4,4),(4,5),(5,7),(7,3)]:
        eigencheck(p,q,1,100)
        eigencheck(p,q,q,p)
        base,exc=constructions(p,q)
        check(algebraic(p,q,base,False),('larger-base',p,q))
        check(algebraic(p,q,exc,True),('larger-res',p,q))
        for _ in range(150):
            S=[(i,j) for i in range(p) for j in range(q)
               if rng.getrandbits(1)]
            for resonant in (False,True):
                check(combinatorial(p,q,S,resonant)==algebraic(p,q,S,resonant),
                      ('sample',p,q,resonant,S))
    print('ALL CHECKS PASSED:',ASSERTIONS)


if __name__=='__main__':
    main()
