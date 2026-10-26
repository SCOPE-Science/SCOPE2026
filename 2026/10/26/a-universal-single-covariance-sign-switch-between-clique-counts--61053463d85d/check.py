"""Exact finite-instance checks for the clique–induced-motif covariance identity.

Only small finite checks: the general statement is proved analytically.
"""
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial


def edges(v):
    return list(combinations(range(v), 2))


def graph_mask(v, edge_list):
    edges_list = edges(v)
    return sum(1 << edges_list.index(tuple(sorted(e))) for e in edge_list)


def orbit(v, mask):
    ee = edges(v)
    orbit_set = set()
    for perm in permutations(range(v)):
        relabeled = 0
        for j,(a,b) in enumerate(ee):
            if mask >> j & 1:
                relabeled |= 1 << ee.index(tuple(sorted((perm[a],perm[b]))))
        orbit_set.add(relabeled)
    return orbit_set


def cliques(v, mask, size):
    es = edges(v)
    emap = {p:j for j,p in enumerate(es)}
    return sum(all(mask >> emap[a,b] & 1 for a,b in combinations(S,2))
               for S in combinations(range(v), size))


def theory(n, m, mask, r, p):
    e = mask.bit_count()
    q = 1-p
    R = comb(r,2)
    F = sum(comb(n-m,r-s) *
            (cliques(m,mask,s)*p**(R-comb(s,2)) - comb(m,s)*p**R)
            for s in range(2,min(m,r)+1)
            if 0 <= r-s <= n-m)
    E_X = Fraction(comb(n,m)*len(orbit(m,mask)),1) * p**e * q**(comb(m,2)-e)
    return E_X*F


def brute(n, m, mask, r, p):
    ed = edges(n)
    E = len(ed)
    edge_to_bit = {pair:j for j,pair in enumerate(ed)}
    subset_maps=[]
    orbit_masks=orbit(m,mask)
    for sub in combinations(range(n),m):
        subset_maps.append(tuple(edge_to_bit[sub[a],sub[b]] for a,b in edges(m)))
    clique_maps=[]
    for sub in combinations(range(n),r):
        clique_maps.append(tuple(edge_to_bit[sub[a],sub[b]] for a,b in edges(r)))
    clique_filter=(1 << comb(r,2))-1
    den=p.denominator**E
    pn,qn=p.numerator,p.denominator-p.numerator
    SX=ST=SXT=0
    for gm in range(1<<E):
        k=gm.bit_count()
        wt=pn**k*qn**(E-k)
        x=0
        for bm in subset_maps:
            submask=sum(1<<j for j,b in enumerate(bm) if gm>>b & 1)
            if submask in orbit_masks:
                x+=1
        t=sum(all(gm>>b & 1 for b in bm) for bm in clique_maps)
        SX += wt*x
        ST += wt*t
        SXT += wt*x*t
    EX=Fraction(SX,den)
    ET=Fraction(ST,den)
    return Fraction(SXT,den)-EX*ET


def run():
    items=[
        (3,[(0,[]),(1,[(0,1)]),(3,[(0,1),(0,2),(1,2)])]),
        (4,[(0,[]),(2,[(0,1),(1,2)]),(3,[(0,1),(1,2),(2,3)]),
            (4,[(0,1),(1,2),(2,3),(3,0)]),
            (5,[(0,1),(0,2),(0,3),(1,2),(1,3)]),
            (6,list(combinations(range(4),2))) ]),
        (5,[(5,[(0,1),(1,2),(2,3),(3,4),(4,0)]),
            (5,[(0,1),(0,2),(0,3),(1,2),(1,3)])])
    ]
    checks=0
    for m,types in items:
        for typ,elist in types:
            hmask=graph_mask(m,elist)
            for n in range(m,7):
                for r in range(3,min(4,m)+1):
                    for p in (Fraction(1,3),Fraction(1,2),Fraction(2,3)):
                        expected=theory(n,m,hmask,r,p)
                        actual=brute(n,m,hmask,r,p)
                        assert actual==expected,(n,m,r,typ,p,expected,actual)
                        checks+=1
    print('PASS',checks,'exact covariance identities')
    print('Additional signed comparisons for order-five motifs:')
    m=5
    C5=graph_mask(m,[(0,1),(1,2),(2,3),(3,4),(4,0)])
    diamond_isolated=graph_mask(m,[(0,1),(0,2),(0,3),(1,2),(1,3)])
    for n,r in [(6,3),(7,4)]:
        for name,hmask in [('cycle',C5),('diamond+isolated',diamond_isolated)]:
            z=theory(n,m,hmask,r,Fraction(1,2))
            assert (z < 0 if name=='cycle' else z > 0)
            print('n=',n,'r=',r,'motif=',name,'cov=',z)

if __name__=='__main__':run()
