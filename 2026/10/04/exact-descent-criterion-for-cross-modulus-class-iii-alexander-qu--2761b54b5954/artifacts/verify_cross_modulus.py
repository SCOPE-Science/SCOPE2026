#!/usr/bin/env python3
from itertools import product
from math import gcd, lcm


def descent(rs, ks):
    return all(((1-ks[i])*rs[j]) % rs[i] == 0
               for i in range(len(rs)) for j in range(len(rs)))


def units(rs, ks):
    return all(gcd(ks[j], rs[i]) == 1
               for i in range(len(rs)) for j in range(len(rs)))


def compact(rs, ks):
    N = 1
    for r in rs:
        N = lcm(N, r)
    ds = []
    for ri in rs:
        d = 1
        for rj in rs:
            d = lcm(d, ri // gcd(ri, rj))
        ds.append(d)
    return (all((ks[i]-1) % ds[i] == 0 for i in range(len(rs))),
            all(gcd(k, N) == 1 for k in ks), N, tuple(ds))


def op(rs, ks, x, y):
    i,a = x; j,b = y
    return (i, (ks[j]*a + (1-ks[i])*b) % rs[i])


def check_quandle(rs, ks):
    X = [(i,a) for i,r in enumerate(rs) for a in range(r)]
    # idempotence
    for x in X:
        if op(rs,ks,x,x) != x:
            return False
    # each right translation is a permutation
    for y in X:
        vals = [op(rs,ks,x,y) for x in X]
        if len(set(vals)) != len(X):
            return False
    # right self-distributivity
    for x in X:
        for y in X:
            for z in X:
                if op(rs,ks,op(rs,ks,x,y),z) != op(rs,ks,op(rs,ks,x,z),op(rs,ks,y,z)):
                    return False
    return True


def representative_witness(rs, ks):
    for i in range(len(rs)):
        for j in range(len(rs)):
            if ((1-ks[i])*rs[j]) % rs[i] != 0:
                # b=0 and b'=r_j are the same class in Z_{r_j}.
                v0 = (ks[j]*0 + (1-ks[i])*0) % rs[i]
                v1 = (ks[j]*0 + (1-ks[i])*rs[j]) % rs[i]
                assert v0 != v1
                return (i,j,v0,v1)
    return None

# Exhaustive two-fiber regression over small moduli and all source-admissible own-fiber units.
systems = 0
criterion_true = 0
checked_quandles = 0
failure_witnesses = 0
for r0 in range(1,9):
    for r1 in range(1,9):
        rs=(r0,r1)
        K0=[k for k in range(1,max(2,r0+1)) if gcd(k,r0)==1]
        K1=[k for k in range(1,max(2,r1+1)) if gcd(k,r1)==1]
        for ks in product(K0,K1):
            systems += 1
            D = descent(rs,ks)
            U = units(rs,ks)
            D2,U2,N,ds = compact(rs,ks)
            assert D == D2
            assert U == U2
            if D and U:
                criterion_true += 1
                assert check_quandle(rs,ks)
                checked_quandles += 1
            elif not D:
                assert representative_witness(rs,ks) is not None
                failure_witnesses += 1
            elif D and not U:
                # A nonunit scalar k_j makes the right translation on some target fiber nonbijective.
                found=False
                for i,ri in enumerate(rs):
                    for j,kj in enumerate(ks):
                        if gcd(kj,ri) != 1:
                            vals={(kj*a) % ri for a in range(ri)}
                            assert len(vals) < ri
                            found=True
                            break
                    if found: break
                assert found

# Source examples.
assert descent((2,4),(1,3)) and units((2,4),(1,3))
assert compact((2,4),(1,3))[2:] == (4,(1,2))
for k in (2,3,4):
    assert not descent((1,5),(1,k))
    assert units((1,5),(1,k))
    assert representative_witness((1,5),(1,k)) is not None

print('VERIFY_OK '
      f'systems={systems} criterion_true={criterion_true} '
      f'checked_quandles={checked_quandles} descent_failure_witnesses={failure_witnesses} '
      'example7.3=PASS example7.5_k2_k3_k4=FAIL_DESCENT')
