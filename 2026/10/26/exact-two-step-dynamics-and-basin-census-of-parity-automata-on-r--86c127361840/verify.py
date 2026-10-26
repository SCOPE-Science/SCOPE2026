#!/usr/bin/env python3
"""Independent Boolean-state and matrix-rank checks for parity rule on Hamming products."""
from itertools import product
from math import prod

def predicted(ns):
    d=len(ns); N=prod(ns); even=[a for a in ns if a%2==0]; odd=[a for a in ns if a%2]
    A=prod(even); B=prod(a-2 for a in even); C=prod(odd); D=prod(a-2 for a in odd)
    delta=d%2
    W=(C-(-1)**delta*D)//2
    assert (C-(-1)**delta*D)%2==0
    Q=C-W
    R=(A-B)//2
    assert (A-B)%2==0
    rp=W*A
    rf=W*(A+B)//2
    return {'N':N,'periodic':1<<rp,'fixed':1<<rf,
            'p2':(1<<rp)-(1<<rf),
            'd0':1<<rp,'d1':(1<<(N-Q*R))-(1<<rp),
            'd2':(1<<N)-(1<<(N-Q*R)),
            'rank_periodic':rp,'rank_fixed':rf,'rank_preentry':Q*R}

def rows_for(ns):
    coords=list(product(*[range(a) for a in ns]))
    masks=[]
    for x in coords:
        mask=0
        for j,y in enumerate(coords):
            if sum(a!=b for a,b in zip(x,y))==1:mask|=1<<j
        masks.append(mask)
    return masks

def f(x,rows):
    y=0
    for j,mask in enumerate(rows):
        y |= ((x&mask).bit_count()&1)<<j
    return y

def gf2_rank(bit_rows):
    basis={}
    for r in bit_rows:
        while r:
            k=r.bit_length()-1
            if k not in basis:
                basis[k]=r
                break
            r ^= basis[k]
    return len(basis)

def certify(ns,full=True):
    p=predicted(ns); N=p['N']; rows=rows_for(ns)
    matrix_rank=gf2_rank(rows)
    if full:
        maps=[f(x,rows) for x in range(1<<N)]
        g=[maps[y] for y in maps]
        h=[g[y] for y in g]
        assert all(g[g[x]]==g[x] for x in range(1<<N)),('F4!=F2',ns)
        periodic={x for x in range(1<<N) if g[x]==x}
        fixed={x for x in range(1<<N) if maps[x]==x}
        d0=len(periodic)
        d1=sum(1 for x in range(1<<N) if x not in periodic and maps[x] in periodic)
        d2=(1<<N)-d0-d1
        actual=dict(periodic=len(periodic),fixed=len(fixed),p2=len(periodic)-len(fixed),d0=d0,d1=d1,d2=d2)
        for k,v in actual.items(): assert p[k]==v,(ns,k,p[k],v)
    else:
        import random
        rng=random.Random(40981+N+sum(ns))
        for _ in range(500):
            x=rng.getrandbits(N)
            x1=f(x,rows);x2=f(x1,rows)
            assert f(f(x2,rows),rows)==x2,(ns,'F4!=F2')
    return matrix_rank

def main():
    cases=[]
    for d in range(1,5):
        for ns in product((1,2,3,4),repeat=d):
            N=prod(ns)
            if N<=12:cases.append(ns)
    # Remove coordinate permutations to avoid redundant workloads, while retaining parity classes.
    cases=[ns for ns in cases if tuple(sorted(ns))==ns]
    counts=[]
    for ns in cases:
        rank=certify(ns,True)
        counts.append((ns,rank))
    larger=[(2,3,4),(2,2,5),(2,2,2,2),(3,3,3),(2,3,3),(4,4,2),(1,2,3,4)]
    for ns in larger:
        certify(ns,prod(ns)<=16)
    # Exact rank checks: F^2 image rank and fixed intersection.
    for ns in cases:
        N=prod(ns)
        if N>12:continue
        rows=rows_for(ns)
        basis=list(1<<i for i in range(N))
        rP=gf2_rank([f(f(x,rows),rows) for x in basis])
        p=predicted(ns)
        assert rP==p['rank_periodic'],(ns,'rP',rP,p)
        # rank of (F^3+F^2) restricted to eventual image
        s=gf2_rank([f(f(f(x,rows),rows),rows)^f(f(x,rows),rows) for x in basis])
        assert p['rank_periodic']-s==p['rank_fixed'],(ns,'rf',s,p)
    print('VERIFY_OK')
    print('Full-state exhaustively checked distinct dimension multisets:',len(cases))
    print('Full-state tests covered cases with N at most 16, up to 65536 states per case')
    print('Additional random identity tests on larger graphs:',len(larger))
    print('Check includes all four 2D parity classes and odd-dimensional all-even case')
    print('Examples:')
    for ns in [(2,2),(2,3),(3,3),(2,2,2),(2,2,3),(3,3,3),(2,3,4)]:
        pp=predicted(ns)
        print(ns,{k:pp[k] for k in ('N','fixed','periodic','d0','d1','d2')})
if __name__=='__main__':main()
