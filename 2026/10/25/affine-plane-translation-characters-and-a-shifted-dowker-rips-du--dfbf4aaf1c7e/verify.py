#!/usr/bin/env python3
"""Exact finite checks of affine-plane incidence and Dowker--Rips characters.

Run with Python 3. No external dependencies. Small examples corroborate,
but do not replace, the general chain and representation proofs.
"""
from itertools import combinations, product
from math import comb


def field(q):
    if q == 4:
        def add(a, b): return a ^ b
        def mul(a, b):
            ans = 0
            while b:
                if b & 1: ans ^= a
                b >>= 1
                a <<= 1
                if a & 4: a ^= 7  # u^2+u+1=0
            return ans
    else:
        assert q in (2, 3, 5)
        def add(a, b): return (a+b) % q
        def mul(a, b): return (a*b) % q
    return add, mul


def data(q):
    add, mul = field(q)
    pts = list(product(range(q), repeat=2))
    directions = list(range(q+1))  # slopes 0,...,q-1, vertical q
    lines = []
    for d in directions:
        for b in range(q):
            if d == q:
                points = frozenset((b, y) for y in range(q))
            else:
                points = frozenset((x, add(mul(d,x), b)) for x in range(q))
            lines.append((d,b,points))
    labels = {(d,b):d*q+b for d in directions for b in range(q)}
    assert len({L[2] for L in lines}) == q*(q+1)
    assert all(sum(p in L[2] for L in lines) == q+1 for p in pts)
    assert all(sum(p in L[2] and z in L[2] for L in lines) == 1 for p,z in combinations(pts,2))
    assert all((len(lines[i][2]&lines[j][2]) == (0 if lines[i][0]==lines[j][0] else 1))
               for i,j in combinations(range(len(lines)),2))
    faces=[]
    for k in range(1,q+2):
        for dirs in combinations(directions,k):
            for bs in product(range(q),repeat=k):
                faces.append(tuple(sorted(labels[d,b] for d,b in zip(dirs,bs))))
    bydim={k:[f for f in faces if len(f)==k+1] for k in range(q+1)}
    assert all(len(bydim[k])==comb(q+1,k+1)*q**(k+1) for k in range(q+1))
    return pts, lines, faces, bydim, add, mul


def rank_mod2(cols):
    pivots={}
    for x in cols:
        while x:
            p=x.bit_length()-1
            if p not in pivots:
                pivots[p]=x
                break
            x ^= pivots[p]
    return len(pivots)


def homology_check(q, bydim):
    ranks={0:0,q+1:0}
    for k in range(1,q+1):
        ids={f:j for j,f in enumerate(bydim[k-1])}
        cols=[]
        for f in bydim[k]:
            col=0
            for s in combinations(f,k): col ^= (1<<ids[s])
            cols.append(col)
        ranks[k]=rank_mod2(cols)
    betti=[len(bydim[k])-ranks[k]-ranks[k+1]-(1 if k==0 else 0) for k in range(q+1)]
    expected=[0]*q+[(q-1)**(q+1)]
    assert betti==expected,(q,betti,expected)
    return betti


def parity(items):
    return -1 if sum(items[i]>items[j] for i in range(len(items)) for j in range(i+1,len(items)))%2 else 1


def formula_character(perm, q):
    n=q+1
    # Every parallel class goes to exactly one other class.
    dirperm=[perm[d*q]//q for d in range(n)]
    assert len(set(dirperm))==n
    assert all(perm[d*q+b]//q==dirperm[d] for d in range(n) for b in range(q))
    seen=set(); ans=parity(dirperm)
    for d in range(n):
        if d in seen: continue
        cyc=[]; x=d
        while x not in seen:
            cyc.append(x); seen.add(x); x=dirperm[x]
        assert x==d
        fixes=0
        for b in range(q):
            k=d*q+b
            for _ in cyc: k=perm[k]
            fixes += (k==d*q+b)
        ans *= fixes-1
    return ans


def lefschetz_character(perm,q,bydim):
    L=0
    for k in range(q+1):
        for face in bydim[k]:
            mapped=tuple(perm[v] for v in face)
            if tuple(sorted(mapped))==face:
                L+=(-1)**k*parity(mapped)
    # Unreduced trace has degree-zero contribution 1; only other homology is H_q.
    return (-1)**q*(L-1)


def affine_perm(q, lines, add, mul, A, b):
    idx={line[2]:i for i,line in enumerate(lines)}
    def mp(p):
        x,y=p
        return (add(add(mul(A[0],x),mul(A[1],y)),b[0]),
                add(add(mul(A[2],x),mul(A[3],y)),b[1]))
    perm=[idx[frozenset(mp(p) for p in line[2])] for line in lines]
    assert len(set(perm))==len(perm)
    return perm


def run():
    all_checks=0
    for q in (2,3,4,5):
        pts,lines,faces,bydim,add,mul=data(q)
        if q<=4:
            betti=homology_check(q,bydim)
            print('q=',q,'integral-compatible mod2 betti',betti)
        else:
            print('q=',q,'combinatorial simplex count',len(faces))
        # Finite field invertibility; for q<=3 exhaust all invertible linear
        # transformations and all translations, including identity.
        matrices=[]
        for A in product(range(q),repeat=4):
            determinant=add(mul(A[0],A[3]), mul(A[1],A[2]) if q==4 or q==2 else -mul(A[1],A[2])%q)
            if q==4 or q==2:
                determinant=add(mul(A[0],A[3]),mul(A[1],A[2]))
            if determinant!=0: matrices.append(A)
        if q<=3:
            cases=product(matrices, product(range(q),repeat=2))
        else:
            ident=(1,0,0,1)
            swap=(0,1,1,0)
            shear=(1,1,0,1)
            cases=((A,b) for A in (ident,swap,shear) for b in product(range(q),repeat=2))
        checks=0
        for A,b in cases:
            perm=affine_perm(q,lines,add,mul,A,b)
            ans=formula_character(perm,q)
            if q<=3:
                actual=lefschetz_character(perm,q,bydim)
                assert ans==actual,(q,A,b,ans,actual)
            if A==(1,0,0,1):
                expect=(q-1)**(q+1) if b==(0,0) else (q-1)*(-1)**q
                assert ans==expect,(q,b,ans,expect)
            checks+=1
        all_checks+=checks
        print('q=',q,'affine character tests',checks,
              'translation-invariants', ((q-1)**(q+1)+(q*q-1)*(q-1)*(-1)**q)//(q*q))
    assert all_checks>=500
    print('VERIFY_OK',all_checks)


if __name__=='__main__': run()
