#!/usr/bin/env python3
from itertools import combinations


def parity(x):
    return x.bit_count() & 1


def dot(x, y):
    return parity(x & y)


def det3(M):
    a,b,c = M[0]
    d,e,f = M[1]
    g,h,i = M[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def fourier_det(E, B):
    M = [[1 if dot(x,b)==0 else -1 for b in B] for x in E]
    return det3(M)


def rank_f2(vs, d):
    rows = list(vs)
    r = 0
    for bit in range(d-1, -1, -1):
        pivot = next((j for j in range(r, len(rows)) if (rows[j] >> bit) & 1), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        for j in range(len(rows)):
            if j != r and ((rows[j] >> bit) & 1):
                rows[j] ^= rows[r]
        r += 1
    return r


def span2(a,b):
    return frozenset((0,a,b,a^b))


def basis_of_plane(U):
    nz = sorted(x for x in U if x)
    a = nz[0]
    b = next(x for x in nz[1:] if x != a)
    return (a,b)


def affine_direction(E):
    x0,x1,x2 = E
    return span2(x1^x0, x2^x0)


def is_basis_partner(E, B):
    return fourier_det(E,B) != 0


def projection_condition(E,B):
    x0,x1,x2 = E
    a,b = x1^x0, x2^x0
    vals = {(dot(a,xi), dot(b,xi)) for xi in B}
    return len(vals) == 3


def count_common(d, U1, U2):
    a1,b1 = basis_of_plane(U1)
    a2,b2 = basis_of_plane(U2)
    E1=(0,a1,b1); E2=(0,a2,b2)
    total=0
    for B in combinations(range(1<<d),3):
        c1=projection_condition(E1,B)
        c2=projection_condition(E2,B)
        # exact determinant cross-check of the structural criterion
        assert c1 == is_basis_partner(E1,B)
        assert c2 == is_basis_partner(E2,B)
        if c1 and c2:
            total += 1
    r=rank_f2(list(U1|U2), d)
    m={2:4,3:16,4:96}[r]
    expected=m*(2**(3*(d-r)))
    assert total == expected, (d,r,total,expected)
    return r,total


def all_planes(d):
    out=set()
    nonzero=range(1,1<<d)
    for a,b in combinations(nonzero,2):
        if a!=b:
            U=span2(a,b)
            if len(U)==4:
                out.add(U)
    return sorted(out, key=lambda U: tuple(sorted(U)))


def canonical_checks():
    rows=[]
    for d in range(2,7):
        e=[1<<j for j in range(d)]
        U1=span2(e[0],e[1])
        rows.append((d,)+count_common(d,U1,U1))
        if d>=3:
            U2=span2(e[0],e[2])
            rows.append((d,)+count_common(d,U1,U2))
        if d>=4:
            U2=span2(e[2],e[3])
            rows.append((d,)+count_common(d,U1,U2))
    return rows


def exhaustive_d3_sets():
    d=3
    sets=list(combinations(range(1<<d),3))
    Bsets=sets
    checked=0
    for i,E1 in enumerate(sets):
        U1=affine_direction(E1)
        for E2 in sets[i:]:
            U2=affine_direction(E2)
            r=rank_f2(list(U1|U2),d)
            expected={2:4,3:16}[r] * (2**(3*(d-r)))
            total=0
            for B in Bsets:
                c1=projection_condition(E1,B)
                c2=projection_condition(E2,B)
                assert c1 == is_basis_partner(E1,B)
                assert c2 == is_basis_partner(E2,B)
                if c1 and c2:
                    total += 1
            assert total==expected, (E1,E2,r,total,expected)
            checked += 1
    return checked


def exhaustive_d4_planes():
    d=4
    planes=all_planes(d)
    assert len(planes)==35
    checked=0
    dist={2:0,3:0,4:0}
    for i,U1 in enumerate(planes):
        for U2 in planes[i:]:
            r,total=count_common(d,U1,U2)
            dist[r]+=1
            checked+=1
    assert checked==630
    assert sum(dist.values())==630
    return checked,dist

if __name__ == '__main__':
    rows=canonical_checks()
    d3=exhaustive_d3_sets()
    d4,dist=exhaustive_d4_planes()
    print('canonical_counts=' + repr(rows))
    print('d4_pair_ranks=' + repr(dist))
    print(f'VERIFY_OK canonical_cases={len(rows)} all_d3_pairs={d3} all_d4_plane_pairs={d4}')
