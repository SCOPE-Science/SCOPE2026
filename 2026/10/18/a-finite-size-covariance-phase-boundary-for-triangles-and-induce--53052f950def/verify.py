"""Exact checks for the triangle / chordless-hole covariance theorem.

Usage: python3 verify.py ; Python standard library only.
The theorem is proved by compatible-overlap counting; enumerations here are finite checks.
"""
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial

N_CHECKS = 0

def check(a, b, label):
    global N_CHECKS
    assert a == b, (label, a, b)
    N_CHECKS += 1


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def covariance_formula(n, ell, p):
    q = ell * (ell - 3) // 2
    c = factorial(ell - 1) // 2
    return (choose(n, 3) * c * p ** (ell + 2) * (1-p) ** q
            * (3 * choose(n-3, ell-2) * (Fraction(2, ell-1)-p)
               - choose(n-3, ell-3) * p))


def threshold(n, ell):
    if n == ell:
        return Fraction(0)
    return Fraction(6 * (n-ell), (ell-1) * (3*n-2*ell-2))


def circular_orders(vertices):
    vertices = tuple(vertices)
    first = min(vertices)
    others = tuple(x for x in vertices if x != first)
    for arr in permutations(others):
        # identify clockwise/counterclockwise representations
        if arr[0] < arr[-1]:
            yield (first,) + arr


def masks(n, ell):
    edges = list(combinations(range(n),2))
    edge_index = {e:i for i,e in enumerate(edges)}
    tris = []
    for vs in combinations(range(n), 3):
        tris.append(sum(1<<edge_index[e] for e in combinations(vs,2)))
    holes = []
    for vs in combinations(range(n), ell):
        allpairs = sum(1<<edge_index[e] for e in combinations(vs, 2))
        for path in circular_orders(vs):
            cyc = sum(1<<edge_index[tuple(sorted((path[j],path[(j+1)%ell])))] for j in range(ell))
            holes.append((cyc,allpairs))
    check(len(tris), choose(n,3), 'triangle count')
    check(len(holes), choose(n,ell)*factorial(ell-1)//2, 'cycle count')
    return edges, tris, holes


def exhaustive_covariance(n,ell,p):
    edges,tris,holes=masks(n,ell)
    m=len(edges)
    # Compute E[T], E[H], E[TH] by weighted exhaustive independent-edge states.
    w=[p**k * (1-p)**(m-k) for k in range(m+1)]
    et=eh=eth=Fraction(0)
    for mask in range(1<<m):
        t=sum((mask&tri)==tri for tri in tris)
        h=sum((mask&full)==cyc for cyc,full in holes)
        prob=w[mask.bit_count()]
        et+=t*prob
        eh+=h*prob
        eth+=t*h*prob
    return eth-et*eh


def compatible_pair_checks(n,ell):
    _,tris,holes=masks(n,ell)
    # For a fixed triangle, all induced cycles with two or three common
    # vertices are checked via the required and forbidden edge bitsets.
    tri=tris[0]
    tri_vertices={i for i in range(n) if any((tri>>k)&1 and i in edge for k,edge in enumerate(combinations(range(n),2)))}
    for h_req,h_all in holes:
        hole_vertices={i for i in range(n) if any((h_all>>k)&1 and i in edge for k,edge in enumerate(combinations(range(n),2)))}
        overlap=len(tri_vertices&hole_vertices)
        if overlap==3:
            check((tri & (h_all ^ h_req)) != 0, True, 'three-shared-vertices incompatible')
        if overlap==2:
            shared=tuple(sorted(tri_vertices&hole_vertices))
            ix=list(combinations(range(n),2)).index(shared)
            compatible=((tri & (h_all ^ h_req)) == 0)
            check(compatible,bool(h_req&(1<<ix)),'two shared vertices compatible iff adjacent')


def main():
    # Direct exhaustive probability-space tests, independent of overlap derivation.
    for n,ell,ps in [(4,4,[Fraction(1,3)]),
                      (5,4,[Fraction(1,5),Fraction(2,5),Fraction(4,5)]),
                      (5,5,[Fraction(2,5)]),
                      (6,4,[Fraction(1,3),Fraction(1,2),Fraction(3,4)]),
                      (6,5,[Fraction(2,5)]),
                      (6,6,[Fraction(1,2)])]:
        for p in ps:
            check(exhaustive_covariance(n,ell,p),covariance_formula(n,ell,p),
                  ('exact enumeration covariance', n,ell,str(p)))
    # Independently check compatibility of intersecting motif patterns.
    for n,ell in [(5,4),(6,5),(6,4)]:
        compatible_pair_checks(n,ell)
    # Exact sign classification at all tested sizes, and ordering in both parameters.
    for n in range(4,45):
        for ell in range(4,n+1):
            root=threshold(n,ell)
            check(0 <= root < 1, True, 'root range')
            for p in (root/2 if root else Fraction(1,4),
                      root if root else Fraction(1,3),
                      (root+1)/2 if root else Fraction(3,4)):
                c=covariance_formula(n,ell,p)
                expected=0 if root==p else (1 if root>p else -1)
                check((c>0)-(c<0),expected, 'root sign law')
            if ell<n:
                check(threshold(n,ell) < Fraction(2,ell-1),True,'finite root below asymptotic')
                check(threshold(n,ell) < threshold(n+1,ell),True,'root increases with n')
            if ell+1 <= n:
                check(threshold(n,ell)>threshold(n,ell+1),True,'root decreases with ell')
    print('PASS: %d exact checks' % N_CHECKS)

if __name__=='__main__':
    main()
