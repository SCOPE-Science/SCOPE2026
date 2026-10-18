"""Direct and quotient structural check of matched-arc two-chord polygons."""
from collections import Counter
from verify_2conn_bipartite_outerplanar import graph,refine,orbit_partition

def partition_counts(n,ell):
    g=graph(n,((0,ell),(2*ell,3*ell)))
    col,r=refine(g)
    orb,auts=orbit_partition(n,((0,ell),(2*ell,3*ell)))
    return len(set(col)),len(set(orb)),r,auts,sorted(Counter(col).values()),sorted(Counter(orb).values())

for ell in range(3,82,2):
    n=4*ell;h=(ell-1)//2
    observed=partition_counts(n,ell)
    expected=(h+1,2*h+1,h,4,[4]+[8]*h,[4]*(2*h+1))
    assert observed == expected,(ell,observed,expected)
    if ell<=13 or ell>=77:
        print(f'ell={ell} vertices={n}: stable={observed[0]} orbits={observed[1]} rounds={observed[2]} auts={observed[3]}')
print('FAMILY_FINITE_TESTS_PASS 40 odd lengths ell=3..81')
