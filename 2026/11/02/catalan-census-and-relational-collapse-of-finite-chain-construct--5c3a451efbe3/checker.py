#!/usr/bin/env python3
"""Exact finite tests of neighbourhood-chain observational normal forms.
Uses only Python's standard library; random tests have a fixed seed.
"""
from itertools import product, combinations_with_replacement
from math import comb
from random import Random


def row_families(n):
    nonempty = tuple(range(1, 1 << n))
    for mask in range(1, 1 << len(nonempty)):
        fam = tuple(nonempty[i] for i in range(len(nonempty)) if mask & (1 << i))
        alpha = max((u & -u).bit_length()-1 for u in fam)
        gamma = min(u.bit_length()-1 for u in fam)
        yield fam, alpha, gamma


def outputs(rows, n):
    """Direct interpretation for every persistent atomic valuation."""
    r=[]
    for t in range(n+1):
        x=((1<<n)-1) ^ ((1<<t)-1)
        box=[]; diamond=[]
        for w in range(n):
            box.append(all(any(u & ~x == 0 for u in fam) for fam in rows[w:]))
            diamond.append(all(all(u & x for u in fam) for fam in rows[w:]))
        r.append((tuple(box),tuple(diamond)))
    return tuple(r)


def endpoint_signature(rows,n):
    alpha=[max((u&-u).bit_length()-1 for u in fam) for fam in rows]
    gamma=[min(u.bit_length()-1 for u in fam) for fam in rows]
    a=tuple(min(alpha[w:]) for w in range(n))
    c=tuple(min(gamma[w:]) for w in range(n))
    return a,c


def expected_output(a,c,n):
    return tuple((tuple(t<=x for x in a), tuple(t<=y for y in c))
                 for t in range(n+1))


def normal_rows(a,c):
    rows=[]
    for x,y in zip(a,c):
        if x<=y:
            rows.append((sum(1<<j for j in range(x,y+1)),))
        else:
            rows.append((1<<x,1<<y))
    return tuple(rows)


def is_weak_inc(seq):
    return all(x<=y for x,y in zip(seq,seq[1:]))


def test(n, sample_count):
    fams=list(row_families(n))
    assert len(fams)== (1 << ((1 << n)-1))-1
    for fam,b,d in fams:
        assert 0<=b<n and 0<=d<n
        if b<=d:
            assert outputs((fam,)*n,n)==expected_output((b,)*n,(d,)*n,n)
    # n<=2: every raw frame. n=3,4: deterministic samples + all rows.
    rng=Random(261029+n)
    if n<=2:
        frames=product((f[0] for f in fams),repeat=n)
    else:
        frames=(tuple(fams[rng.randrange(len(fams))][0] for _ in range(n))
                for _ in range(sample_count))
    checked=0
    for rows in frames:
        a,c=endpoint_signature(rows,n)
        assert is_weak_inc(a) and is_weak_inc(c)
        observed=outputs(rows,n)
        assert observed==expected_output(a,c,n)
        assert observed==outputs(normal_rows(a,c),n)
        assert all(x<=y for x,y in zip(a,c)) == all(
            not any(box[w] and not dia[w] for w in range(n))
            for box,dia in observed)
        checked+=1
    # Count every possible distinct ordered pair of modal operators.
    seq=list(combinations_with_replacement(range(n),n))
    all_types={(a,c) for a in seq for c in seq}
    d_types={(a,c) for a,c in all_types if all(x<=y for x,y in zip(a,c))}
    expected_all=comb(2*n-1,n)**2
    expected_d=comb(2*n-1,n)*comb(2*n,n)//(n+1)
    assert len(all_types)==expected_all
    assert len(d_types)==expected_d
    for a,c in all_types:
        assert endpoint_signature(normal_rows(a,c),n)==(a,c)
    return len(fams),checked,expected_all,expected_d


for n,k in [(1,0),(2,0),(3,30000),(4,8000)]:
    family_count,frame_count,all_types,d_types=test(n,k)
    print(f'n={n} row_families={family_count} frames_tested={frame_count} '
          f'NP_types={all_types} NPD_types={d_types}')

# An explicit D-valid frame not satisfying pairwise intersections.
fam=((1<<0)|(1<<2),1<<1)
rows=(fam,)*3
a,c=endpoint_signature(rows,3)
assert a==c==(1,1,1)
assert not (fam[0]&fam[1])
assert outputs(rows,3)==outputs(normal_rows(a,c),3)
print('ALL_CHECKS_OK')
