#!/usr/bin/env python3
"""Exact independent finite checks for dense strong chain accessibility relations.

Uses only Python standard library. Invoke: python verify_dense_chains.py
"""
from collections import Counter,defaultdict
from itertools import product


def stirling_row(m):
    table=[[0]*(m+1) for _ in range(m+1)]
    table[0][0]=1
    for i in range(1,m+1):
        for k in range(1,i+1):
            table[i][k]=table[i-1][k-1]+k*table[i-1][k]
    return table[m]


def trial(n):
    histogram=Counter()
    serial_histogram=Counter()
    witnessed_fibers=Counter()
    candidates=0
    for d in product(*(range(-1,z+1) for z in range(n))):
        candidates+=1
        # Interpret thresholds as a concrete binary accessibility relation.
        R=tuple(tuple(x<=d[z] for z in range(n)) for x in range(n))
        # Check strongness and prefix closure directly, independently of the theorem.
        assert all(not R[x][z] or x<=z for x in range(n) for z in range(n))
        assert all(not (x<=y and R[y][z]) or R[x][z]
                   for x in range(n) for y in range(n) for z in range(n))
        dense = all(not R[x][z] or any(R[x][y] and R[y][z]
                   for y in range(n)) for x in range(n) for z in range(n))
        local = all(d[z]<0 or d[d[z]]==d[z] for z in range(n))
        assert dense==local, (n,d,'density criterion')
        if not dense:
            continue
        roots=frozenset(x for x in range(n) if R[x][x])
        assert roots==frozenset(x for x in range(n) if d[x]==x)
        witnessed_fibers[roots]+=1
        histogram[len(roots)]+=1
        serial=all(any(R[x][y] for y in range(n)) for x in range(n))
        assert serial==(n-1 in roots)
        if serial:
            serial_histogram[len(roots)]+=1
        # An upset is [t,n-1], including empty t=n.
        for t in range(n+1):
            modal_from_relation=tuple(all(not R[x][y] or y>=t for y in range(n))
                                      for x in range(n))
            modal_from_roots=tuple(all(y>=t for y in roots if y>=x)
                                   for x in range(n))
            assert modal_from_relation==modal_from_roots, (n,d,t)
    # Verify each fixed-nucleus fiber against the independent product formula.
    for roots,fiber in witnessed_fibers.items():
        predicted=1
        for z in range(n):
            if z not in roots:
                predicted*=1+sum(1 for s in roots if s<z)
        assert fiber==predicted, (n, roots, fiber, predicted)
    expected={k:stirling_row(n+1)[k+1] for k in range(n+1)}
    assert dict(histogram)=={k:v for k,v in expected.items() if v},(n,histogram,expected)
    expected_serial={k:stirling_row(n)[k] for k in range(n+1)}
    assert dict(serial_histogram)=={k:v for k,v in expected_serial.items() if v}
    assert len(witnessed_fibers)==2**n
    # Distinct root sets must give distinct modal operators on the full upset algebra.
    signatures=set()
    for roots in witnessed_fibers:
        sig=tuple(tuple(all(y>=t for y in roots if y>=x) for x in range(n))
                  for t in range(n+1))
        signatures.add(sig)
    assert len(signatures)==2**n
    return candidates,sum(histogram.values()),sum(serial_histogram.values()),len(witnessed_fibers),dict(sorted(histogram.items()))

if __name__=='__main__':
    for n in range(1,8):
        print(n,trial(n))
    # Enumerate finite-chain closure operators independently in small sizes.
    # Any monotone extensive idempotent map is meet preserving on a chain.
    for m in range(2,7):
        nuclei=0
        for f in product(range(m),repeat=m):
            if all(f[i]>=i for i in range(m)) and \
                    all(f[i]<=f[i+1] for i in range(m-1)) and \
                    all(f[f[i]]==f[i] for i in range(m)):
                nuclei+=1
        assert nuclei==2**(m-1),(m,nuclei)
    print('VERIFY_OK')
