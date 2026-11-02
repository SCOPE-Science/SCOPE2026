#!/usr/bin/env python3
"""Finite-field/projective checks for a family of characteristic-two plane curves.

All computations are over F_2, using sets of monomials for sparse polynomials.
The finite enumeration supports, but does not prove, the geometric infinite-family results.
"""
from itertools import product


def add(*polys):
    out=set()
    for poly in polys:
        out.symmetric_difference_update(poly)
    return out


def mul(a,b):
    out=set()
    for i in a:
        for j in b:
            k=tuple(x+y for x,y in zip(i,j))
            if k in out: out.remove(k)
            else: out.add(k)
    return out


def power(a,n):
    out={(0,0,0)}
    while n:
        if n&1: out=mul(out,a)
        a=mul(a,a);n//=2
    return out

X={(1,0,0)};Y={(0,1,0)};Z={(0,0,1)}

def form(row):
    return add(*(a for a,b in zip((X,Y,Z),row) if b))

def curve(q):
    return add(mul(power(Z,2),power(Y,q)),power(X,q+2),mul(X,power(Z,q+1)))

def transform(q,m):
    x,y,z=(form(row) for row in m)
    return add(mul(power(z,2),power(y,q)),power(x,q+2),mul(x,power(z,q+1)))

def invertible(m):
    v=[sum(m[i][j]<<j for j in range(3)) for i in range(3)]
    rank=0
    for bit in range(3):
        piv=next((j for j in range(rank,3) if v[j]&(1<<bit)),None)
        if piv is None:continue
        v[rank],v[piv]=v[piv],v[rank]
        for j in range(3):
            if j!=rank and v[j]&(1<<bit):v[j]^=v[rank]
        rank+=1
    return rank==3


def gf2_rank(rows):
    pivots={}
    for r in rows:
        while r:
            k=r.bit_length()-1
            if k not in pivots:
                pivots[k]=r
                break
            r^=pivots[k]
    return len(pivots)


def lie_dimension(q):
    # 9 basis directions from the general infinitesimal 3x3 matrix,
    # plus lambda to account for scaling of the defining equation.
    F=curve(q)
    basis=[]
    for i in range(3):
        for j in range(3):
            v=[set(),set(),set()]
            v[i]=[X,Y,Z][j]
            basis.append(add(mul(power(Z,q+1),v[0]),mul(mul(X,power(Z,q)),v[2])))
    basis.append(F)
    monoms=sorted(set().union(*basis))
    eqn=[]
    for mon in monoms:
        eqn.append(sum((int(mon in poly)<<j) for j,poly in enumerate(basis)))
    # kernel dim of 10 variables minus rank; quotient by scalar matrix dimension 1.
    return 10-gf2_rank(eqn)-1


def main():
    matrices=[]
    for bits in product((0,1),repeat=9):
        mat=[bits[0:3],bits[3:6],bits[6:9]]
        if invertible(mat):matrices.append(mat)
    assert len(matrices)==168
    for q in (2,4,8,16):
        F=curve(q)
        stabilizers=[m for m in matrices if transform(q,m)==F]
        expected=2 if q==2 else 1
        assert len(stabilizers)==expected,(q,len(stabilizers),stabilizers)
        ld=lie_dimension(q)
        assert ld==3,(q,ld)
        assert len(F)==3
        print(f'q={q}: PGL3(F2) stabilizer count={len(stabilizers)}, Lie dimension={ld}')
    print('VERIFY_OK')

if __name__=='__main__':main()
