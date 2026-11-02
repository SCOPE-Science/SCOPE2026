#!/usr/bin/env python3
"""Exact independent tests of the period-two diffusion census on labelled bistars.

Run: python3 verify_bistar.py
Only Python standard library; no saved data, random seeds or remote dependencies.
"""
from collections import Counter
from itertools import product


def update(x, a, b):
    """Two hub vertices 0,1; a leaves at hub 0, b leaves at hub 1."""
    y = list(x)
    edges = [(0, 1)] + [(0, i) for i in range(2, 2+a)] + [(1, j) for j in range(2+a, 2+a+b)]
    for u, v in edges:
        if x[u] > x[v]:
            y[u] -= 1
            y[v] += 1
        elif x[u] < x[v]:
            y[u] += 1
            y[v] -= 1
    return tuple(y)


def formula_states(a, b):
    """Canonical primitive two-cycle representatives with hub zero at the first vertex."""
    n = a + b + 2
    for alpha, beta in product((1, -1), repeat=2):
        A, B = a+alpha, b-beta
        H = 1+a*alpha-b*beta
        if min(A,B,H) < 1:
            continue
        for h in range(1,H+1):
            for ds in product(range(1,A+1),repeat=a):
                for es in product(range(1,B+1),repeat=b):
                    x = (0,h)+tuple(alpha*d for d in ds)+tuple(h+beta*e for e in es)
                    # Exact minimum nonnegative resource threshold for BOTH cycle states.
                    if alpha==1 and beta==-1:
                        L = max(0,b+1-h)
                    elif alpha==1 and beta==1:
                        L = 0
                    elif alpha==-1 and beta==-1:
                        L = b+1-h
                    else:
                        raise AssertionError('forbidden orientation')
                    yield x,sum(x)+n*L
    if a == b:
        for ds in product(range(1,a+1),repeat=a):
            for es in product(range(1,a+1),repeat=a):
                x=(0,0)+tuple(ds)+tuple(es)
                yield x,sum(x)


def brute_states(a, b):
    """Exhausts all periodic configurations by proved degree-bound boxes; not formula orientations."""
    n=a+b+2
    M=a+b+1
    for h in range(-M,M+1):
        for ds in product(range(-a-1,a+2),repeat=a):
            for es in product(range(-b-1,b+2),repeat=b):
                x=(0,h)+tuple(ds)+tuple(h+v for v in es)
                if not (h>0 or (h==0 and all(d>0 for d in ds) and all(e>0 for e in es))):
                    continue
                y=update(x,a,b)
                if x==y or update(y,a,b)!=x:
                    continue
                # The first hub is at height zero in this representation.
                min_all=min(min(x),min(y))
                yield x,sum(x)-n*min_all


def closed_count(a,b):
    return ((a+b+1)*(a+1)**a*(b+1)**b
            + max(0,a-b+1)*(a+1)**a*(b-1)**b
            + max(0,b-a+1)*(a-1)**a*(b+1)**b
            + (a==b)*a**(a+b))


def checks(a,b):
    n=a+b+2
    f=dict(formula_states(a,b))
    assert len(f)==closed_count(a,b), ('closed formula',a,b,len(f),closed_count(a,b))
    for x,minimum in f.items():
        y=update(x,a,b)
        assert y!=x and update(y,a,b)==x, ('false formula state',a,b,x,y)
        assert minimum==sum(x)-n*min(min(x),min(y)), ('wrong threshold',a,b,x)
    z=dict(brute_states(a,b))
    assert z==f, ('exhaustive mismatch',a,b,set(z)-set(f),set(f)-set(z))
    residues=Counter(sum(x)%n for x in z)
    threshold=Counter(minimum for minimum in z.values())
    for S in range(0, min(50,4*n+10)):
        by_threshold=sum(v for t,v in threshold.items() if S>=t and (S-t)%n==0)
        by_residue=sum(1 for x,minS in f.items() if S>=minS and sum(x)%n==S%n)
        assert by_threshold==by_residue
    m=min(threshold)
    expected=n-2 if a==b else n-1
    assert m==expected, ('first_nonnegative',a,b,m,expected)
    print('CASE a=%d b=%d n=%d orbits_mod_translation=%d min_nonnegative=%d mod_counts=%s' %
          (a,b,n,len(z),m,[residues[k] for k in range(n)]))
    return len(z)


def main():
    cases=[(1,1),(1,2),(2,1),(1,3),(3,1),(2,2),(2,3),(3,2)]
    count=0
    for a,b in cases:
        count+=checks(a,b)
    print('BISTAR_DIFFUSION_ALL_CHECKS_PASSED cases=%d labelled_orbits_checked=%d' %(len(cases),count))

if __name__=='__main__':
    main()
