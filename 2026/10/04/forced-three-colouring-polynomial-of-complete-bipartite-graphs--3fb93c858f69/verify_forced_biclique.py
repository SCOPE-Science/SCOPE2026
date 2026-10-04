#!/usr/bin/env python3
from itertools import product
from math import comb

COLORS = {1,2,3}

def forces(m,n,assignment):
    vals=list(assignment)
    # A partial assignment that forces a proper coloring must itself be proper.
    for i in range(m):
        if vals[i]:
            for j in range(m,m+n):
                if vals[j] and vals[i]==vals[j]:
                    return False
    while True:
        moved=False
        for v in range(m+n):
            if vals[v] != 0:
                continue
            neigh = range(m,m+n) if v < m else range(0,m)
            seen={vals[u] for u in neigh if vals[u] != 0}
            if len(seen)==3:
                return False
            if len(seen)==2:
                vals[v]=(COLORS-seen).pop()
                moved=True
                break
        if not moved:
            break
    return all(vals)

def classified(m,n,assignment):
    A=assignment[:m]
    B=assignment[m:]
    aset={x for x in A if x}
    bset={x for x in B if x}
    proper=aset.isdisjoint(bset)
    if not proper:
        return False
    # Class I: A is fully initially colored with exactly two colors; any
    # initially colored B vertex has the remaining third color.
    if all(A) and len(aset)==2 and len(bset) <= 1 and bset.isdisjoint(aset):
        return True
    # Class II: symmetric.
    if all(B) and len(bset)==2 and len(aset) <= 1 and aset.isdisjoint(bset):
        return True
    # Class III: total proper coloring, both sides monochromatic.
    if all(A) and all(B) and len(aset)==1 and len(bset)==1 and aset.isdisjoint(bset):
        return True
    return False

def formula_counts(m,n):
    N=m+n
    out=[0]*(N+1)
    # Class I.
    for j in range(n+1):
        out[m+j] += 3*(2**m-2)*comb(n,j)
    # Class II.
    for i in range(m+1):
        out[n+i] += 3*(2**n-2)*comb(m,i)
    # Class III.
    out[N] += 6
    return out

def main():
    total_assignments=0
    forcing_assignments=0
    types=0
    for m in range(1,6):
        for n in range(1,6):
            types += 1
            coeff=[0]*(m+n+1)
            for a in product(range(4), repeat=m+n):
                total_assignments += 1
                f=forces(m,n,a)
                c=classified(m,n,a)
                if f != c:
                    raise AssertionError((m,n,a,f,c))
                if f:
                    forcing_assignments += 1
                    coeff[sum(x != 0 for x in a)] += 1
            expected=formula_counts(m,n)
            if coeff != expected:
                raise AssertionError((m,n,coeff,expected))
    # Explicit source-paper consistency checks for the correctly stated K_{1,3}
    # specialization and for the direct K_{1,2} count.
    if formula_counts(1,2) != [0,0,6,12]:
        raise AssertionError("K12 coefficient check")
    if formula_counts(1,3) != [0,0,0,18,24]:
        raise AssertionError("K13 coefficient check")
    print(f"ALL CHECKS PASSED; biclique_types={types}; partial_assignments={total_assignments}; forcing_assignments={forcing_assignments}")

if __name__ == '__main__':
    main()
