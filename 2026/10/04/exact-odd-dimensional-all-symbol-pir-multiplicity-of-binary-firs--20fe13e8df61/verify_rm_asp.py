#!/usr/bin/env python3
"""Finite checks for odd-dimensional binary RM(1,m) all-symbol PIR recovery."""

def col(m, x):
    return (1 << m) | x

def xor_all(xs):
    z = 0
    for x in xs:
        z ^= x
    return z

def check_plane(triple):
    a,b,c = triple
    assert len({a,b,c}) == 3 and 0 not in triple
    assert a ^ b ^ c == 0

def check_witness(m, planes):
    used=set()
    for U in planes:
        check_plane(U)
        assert not (used & set(U))
        used.update(U)
    expected=(2**m-5)//3
    assert len(planes)==expected
    assert len(used)==3*expected
    # For every target p, translated plane triples are disjoint recoveries.
    for p in range(2**m):
        seen={p}
        for U in planes:
            R={p^u for u in U}
            assert p not in R and len(R)==3
            assert not (seen & R)
            seen |= R
            assert xor_all(col(m,x) for x in R) == col(m,p)
        assert len(seen)==1+3*expected

def theorem_value(m):
    # Năstase--Sissokho formula for q=2,t=2,r=1:
    return (2**m - 2**3)//(2**2-1) + 1

W3=[(1,2,3)]
W5=[(1,2,3),(4,8,12),(5,10,15),(6,16,22),(7,18,21),
    (9,17,24),(11,20,31),(13,19,30),(14,23,25)]

check_witness(3,W3)
check_witness(5,W5)
for m in (3,5,7,9,11):
    assert m % 2 == 1
    a=(2**m-5)//3
    t=(2**m-2)//3
    assert theorem_value(m)==a
    assert t==a+1
    # A hypothetical t nontrivial triples would cover all but one nonzero vector.
    assert 3*t == 2**m-2
    # XOR of all nonzero vectors is zero for m>=2; each plane triple also XORs to zero.
    assert xor_all(range(1,2**m)) == 0
print('VERIFY_OK')
