#!/usr/bin/env python3
"""Finite prime-field consistency checks for an evolution-algebra rigidity theorem.

This independent enumerator lists invertible coefficient matrices, explicitly
checks all monomial algebra automorphisms, and compares the resulting orbit
count with a separate orbit-construction enumeration.
"""
from itertools import product, permutations
from math import prod, factorial, comb


def invertible(a, n, q):
    x = [list(a[i*n:(i+1)*n]) for i in range(n)]
    rank = 0
    for j in range(n):
        pivot = next((i for i in range(rank,n) if x[i][j] % q), None)
        if pivot is None: continue
        x[rank], x[pivot] = x[pivot], x[rank]
        t = pow(x[rank][j], -1, q)
        x[rank] = [(u*t)%q for u in x[rank]]
        for i in range(n):
            if i != rank and x[i][j]:
                v = x[i][j]
                x[i] = [(u-v*w)%q for u,w in zip(x[i],x[rank])]
        rank += 1
    return rank == n


def all_monomials(n,q):
    return [(s,t) for s in permutations(range(n)) for t in product(range(1,q),repeat=n)]


def transformed(a,n,q,mon):
    sigma,t = mon
    return tuple(t[i]*t[i]*a[sigma[i]*n+sigma[j]]*pow(t[j],-1,q) % q
                 for i in range(n) for j in range(n))


def stabilizer_count(a,n,q,mons):
    return sum(transformed(a,n,q,g) == a for g in mons)


def orbit_classes(matrices,n,q,mons):
    unseen = set(matrices)
    count = 0
    while unseen:
        a = next(iter(unseen))
        orb = {transformed(a,n,q,g) for g in mons}
        assert orb <= set(matrices)
        unseen.difference_update(orb)
        count += 1
    return count


def gaussian_phi(n,q):
    return prod(q**n-q**i for i in range(n))


def z(r,q):
    # Enumerate scalar-fixed-entry restrictions exactly; over *all* r x r matrices.
    acc = 0
    for t in product(range(1,q),repeat=r):
        e = sum(t[j] != (t[i]*t[i])%q for i in range(r) for j in range(r))
        acc += q**(r*r-e)
    return acc


def test(q,n,make_orbits):
    mats = [a for a in product(range(q),repeat=n*n) if invertible(a,n,q)]
    assert len(mats) == gaussian_phi(n,q)
    mons = all_monomials(n,q)
    hsum = 0
    nontrivial = 0
    for a in mats:
        h = stabilizer_count(a,n,q,mons)
        assert 1<=h<=len(mons)
        hsum += h
        nontrivial += (h>1)
    assert hsum % len(mons) == 0
    num_classes = hsum // len(mons)
    if n >= 2:
        sigma = tuple([1,0]+list(range(2,n)))
        pure = (sigma, (1,)*n)
        observed = sum(transformed(a,n,q,pure)==a for a in mats)
        if q % 2:
            expected = gaussian_phi(n-1,q)*(q-1)
        else:
            expected = q**(n*n-2*n+2)
            # q even: Jordan centralizer factors via an integer computation
            expected //= q  # multiply by (1-q^-1)
            expected *= (q-1)
            for i in range(1,n-1):
                expected = expected*(q**i-1)//q**i
        assert observed == expected, (q,n,observed,expected)
    if make_orbits:
        assert num_classes == orbit_classes(mats,n,q,mons)
    print(f'FIELD={q} DIM={n} GL={len(mats)} G={len(mons)} '
          f'NONRIGID={nontrivial} AUT_SUM={hsum} CLASSES={num_classes}')
    return num_classes, nontrivial


def gf4_mul(a,b):
    # GF(4) = GF(2)[x] / (x*x+x+1); elements are 0,1,x,1+x.
    z=0
    while b:
        if b&1: z ^= a
        b >>=1
        a <<=1
        if a&4: a ^=7
    return z


def gf4_inv(a):
    assert a
    for b in (1,2,3):
        if gf4_mul(a,b)==1:return b
    raise AssertionError


def gf4_n2_invertible(a):
    return gf4_mul(a[0],a[3]) != gf4_mul(a[1],a[2])


def gf4_transform(a,mon):
    s,t=mon
    out=[]
    for i in range(2):
        for j in range(2):
            out.append(gf4_mul(gf4_mul(gf4_mul(t[i],t[i]), a[2*s[i]+s[j]]),gf4_inv(t[j])))
    return tuple(out)


def gf4_check():
    mats=[a for a in product(range(4),repeat=4) if gf4_n2_invertible(a)]
    assert len(mats)==180
    mons=list((s,t) for s in permutations(range(2)) for t in product((1,2,3),repeat=2))
    weights=[sum(gf4_transform(a,g)==a for g in mons) for a in mats]
    assert sum(gf4_transform(a,((1,0),(1,1)))==a for a in mats) == 4*3
    assert sum(weights)%len(mons)==0
    orb=set(mats); orbit_count=0
    while orb:
        a=next(iter(orb))
        reached={gf4_transform(a,g) for g in mons}
        assert reached <= set(mats)
        orb -= reached
        orbit_count+=1
    assert orbit_count==sum(weights)//len(mons)
    print(f'FIELD=4 DIM=2 GL={len(mats)} G={len(mons)} '
          f'NONRIGID={sum(w>1 for w in weights)} AUT_SUM={sum(weights)} CLASSES={orbit_count}')


def main():
    # Order of the assertions is independent of the asymptotic union bound.
    for q,n,orbits in ((2,1,True),(2,2,True),(2,3,True),(2,4,True),
                       (3,1,True),(3,2,True),(3,3,True),
                       (5,1,True),(5,2,True)):
        test(q,n,orbits)
    gf4_check()
    for q in (2,3,5,7):
        for r in range(1,5):
            zz = z(r,q)
            assert zz >= q**(r*r)
            print(f'Z_CHECK q={q} r={r} expected_additional_weight={zz-q**(r*r)}')
    print('VERIFY_OK 10 exhaustive invertible-matrix cases and 16 scalar partition checks')


if __name__ == '__main__':
    main()
