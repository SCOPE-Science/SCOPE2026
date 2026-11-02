#!/usr/bin/env python3
"""Reproduce sample constructions for the tripled-diagonal distance-three theorem.
All checks use only Python integer arithmetic and the standard library.
This finite verifier does not replace the all-parameter proof.
"""
from itertools import product


def gf4_mul(a, b):
    # GF(4) = F2[w]/(w^2+w+1), elements encoded a0+2*a1*w.
    x, y = a & 1, (a >> 1) & 1
    u, v = b & 1, (b >> 1) & 1
    return (x*u ^ y*v) | ((x*v ^ y*u ^ y*v) << 1)


def gf4_inv(a):
    assert a in (1,2,3)
    return next(b for b in (1,2,3) if gf4_mul(a,b) == 1)


def norm(line):
    pivot = next(x for x in line if x)
    scale = gf4_inv(pivot)
    return tuple(gf4_mul(x,scale) for x in line)


def bits(line):
    return sum(digit << (2*j) for j,digit in enumerate(line))


def rank(vectors, rows):
    basis = [0]*rows
    for x in vectors:
        while x:
            i = x.bit_length()-1
            if basis[i]: x ^= basis[i]
            else:
                basis[i]=x; break
    return sum(bool(x) for x in basis)


def construction(r):
    assert r >= 3 and r%2 == 1
    t=(r+1)//2
    n=(1<<r)-2
    assert n%3==0
    m=n//3
    basis=[tuple(1 if i == j else 0 for i in range(t)) for j in range(t)]
    points=set(norm(v) for v in product(range(4),repeat=t) if any(v))
    choices=basis+sorted(points.difference(basis))[:m-t]
    assert len(choices)==m and len(set(choices))==m
    triples=[tuple(bits(tuple(gf4_mul(z,v) for v in line)) for z in (1,2,3)) for line in choices]
    # Order columns in three blocks, matching iota_3(u)=(u,u,u).
    cols=[triples[i][j] for j in range(3) for i in range(m)]
    assert all(a^b^c==0 for a,b,c in triples)
    assert 0 not in cols and len(set(cols))==n
    assert rank(cols,r+1)==r+1
    # Check every basis vector of the entire m-dimensional tripled diagonal.
    for i in range(m): assert cols[i]^cols[m+i]^cols[2*m+i]==0
    return (r,n,m,n-r-1, len(points))


def optimal_dim_r3_no_tripled_diagonal():
    # For length six, any rank-three parity-check matrix with distance >=3
    # comprises six out of the seven distinct nonzero 3-bit columns.
    full=set(range(1,8))
    for omitted in full:
        selected=full-{omitted}
        assert len(selected)==6
        assert rank(selected,3)==3
        assert set().union(selected)==selected
        assert __import__('functools').reduce(int.__xor__,selected,0)==omitted
        # Every all-one vector, necessarily in any full-tripled-diagonal
        # subspace, therefore has nonzero syndrome.
    return len(full)


def test_gf4():
    for a,b,c in product(range(4),repeat=3):
        assert gf4_mul(a,b)==gf4_mul(b,a)
        assert gf4_mul(gf4_mul(a,b),c)==gf4_mul(a,gf4_mul(b,c))
        assert gf4_mul(a,b^c)==gf4_mul(a,b)^gf4_mul(a,c)
    assert gf4_mul(2,2)==3 and gf4_mul(2,3)==1


def main():
    test_gf4()
    for r in (3,5,7,9):
        print('r,n,m,constrained_dimension,available_F4_lines',*construction(r))
    print('all_rank_3_length_6_parity_checks_exclude_all_ones',optimal_dim_r3_no_tripled_diagonal())
    print('VERIFY_OK')

if __name__=='__main__': main()
