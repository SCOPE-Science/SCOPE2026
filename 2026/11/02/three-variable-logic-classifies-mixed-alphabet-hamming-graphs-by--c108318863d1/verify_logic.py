#!/usr/bin/env python3
"""Finite full fixed-point 3-variable logic comparison for Cartesian products of cliques.
Run with Python 3 standard library. A color on ordered triples represents the
complete set of 3-variable formulas at a refinement depth; quantifier counts
are represented by sets, not multisets.
"""
from itertools import product


def graph(sizes):
    points=list(product(*(range(q) for q in sizes)))
    edges=[[sum(a!=b for a,b in zip(x,y))==1 for y in points] for x in points]
    return points,edges


def pair_refine(items):
    graphs=[graph(item) for item in items]
    colors=[]
    for pts,E in graphs:
        n=len(pts)
        colors.append([tuple((int((a==b)),int(E[a][b])) for a,b in ((i,j),(i,k),(j,k))) for i,j,k in product(range(n),repeat=3)])
    keyset=sorted(set(x for arr in colors for x in arr))
    cdict={x:i for i,x in enumerate(keyset)}
    colors=[[cdict[x] for x in arr] for arr in colors]
    rounds=0
    while True:
        signatures=[]
        for current,(pts,_) in zip(colors,graphs):
            n=len(pts)
            # For each fixed pair, the reachable color-set when one variable is quantified.
            groups=[]
            for idx in range(3):
                group=[]
                for u in range(n):
                    for v in range(n):
                        if idx==0: vals=(current[(w*n+u)*n+v] for w in range(n))
                        elif idx==1: vals=(current[(u*n+w)*n+v] for w in range(n))
                        else: vals=(current[(u*n+v)*n+w] for w in range(n))
                        group.append(tuple(sorted(set(vals))))
                groups.append(group)
            signatures.append([(current[(a*n+b)*n+c], groups[0][b*n+c],groups[1][a*n+c],groups[2][a*n+b]) for a,b,c in product(range(n),repeat=3)])
        distinct=sorted(set(x for arr in signatures for x in arr))
        lookup={x:i for i,x in enumerate(distinct)}
        next_colors=[[lookup[x] for x in arr] for arr in signatures]
        rounds+=1
        # Because the old color is in the new key, equal partition size means stabilized.
        if len(distinct)==len(set(x for arr in colors for x in arr)):
            break
        assert rounds<50
        colors=next_colors
    spectra=[set(cs) for cs in next_colors]
    return rounds,[len(s) for s in spectra],[s==spectra[0] for s in spectra]


def pattern(items):
    b=sum(q==2 for q in items)
    s=sum(q>=3 for q in items)
    return (b,s)


def main():
    cases=[
      ((2,3),(2,4),True),
      ((2,3),(2,5),True),
      ((3,3),(3,4),True),
      ((3,3),(4,4),True),
      ((2,2,3),(2,2,4),True),
      ((2,3,3),(2,3,4),True),
      ((2,3),(3,3),False),
      ((2,2,3),(2,3,3),False),
      ((2,2,2),(2,2,3),False),
      ((2,2),(2,2,2),False),
      ((3,3),(3,3,3),False),
      ((2,3),(2,2,3),False),
    ]
    for A,B,want in cases:
      rounds,card,eq=pair_refine([A,B])
      assert eq==[True,want],(A,B,eq,card,rounds)
      print('PASS',A,B,'equal' if want else 'separate','patterns',pattern(A),pattern(B),'rounds',rounds,'triple-type-sizes',card)
    print('FULL_3_VARIABLE_REFINEMENT_OK',len(cases),'comparison_pairs')

if __name__=='__main__':main()
