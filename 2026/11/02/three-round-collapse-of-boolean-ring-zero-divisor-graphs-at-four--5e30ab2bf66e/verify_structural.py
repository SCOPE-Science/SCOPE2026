#!/usr/bin/env python3
"""Orbit-independent combinatorial check of nine pair-extension classes.
Each pair is represented by 4 cell cardinalities for complements, A-only, B-only, both.
The third vertex is enumerated by all ways of splitting each cell.
"""
from itertools import product

PATTERNS={(0,0),(0,1),(1,0),(1,1)}

def compositions(n):
    for a in range(n+1):
      for b in range(n-a+1):
        for c in range(n-a-b+1):
          yield (a,b,c,n-a-b-c)

def valid(c,n):
    d,a,b,s=c
    return 0<a+s<n and 0<b+s<n

def name(c):
    d,a,b,s=c
    if a==b==0:return 'equal'
    if s==0:
        if d:return 'disjoint_proper'
        if a==1:return 'disjoint_full_A_singleton'
        if b==1:return 'disjoint_full_B_singleton'
        return 'disjoint_full_both_large'
    if a==0:return 'A_proper_subset_B'
    if b==0:return 'B_proper_subset_A'
    if d:return 'overlap_incomparable_proper'
    return 'overlap_incomparable_full'

EXPECTED={
 'equal':{(0,0),(1,1)},
 'disjoint_proper':PATTERNS,
 'disjoint_full_A_singleton':{(0,0),(1,0)},
 'disjoint_full_B_singleton':{(0,0),(0,1)},
 'disjoint_full_both_large':{(0,0),(1,0),(0,1)},
 'A_proper_subset_B':{(0,0),(1,0),(1,1)},
 'B_proper_subset_A':{(0,0),(0,1),(1,1)},
 'overlap_incomparable_proper':PATTERNS,
 'overlap_incomparable_full':{(0,0),(1,0),(0,1)},
}
POINT={
 'singleton': {'equal','A_proper_subset_B','disjoint_full_A_singleton','disjoint_proper'},
 'middle': {'equal','A_proper_subset_B','B_proper_subset_A','overlap_incomparable_full',
            'overlap_incomparable_proper','disjoint_full_both_large','disjoint_proper'},
 'co_singleton': {'equal','B_proper_subset_A','overlap_incomparable_full','disjoint_full_B_singleton'},
}

def extension_patterns(c,n):
    d,a,b,s=c;out=set()
    for sd,sa,sb,ss in product(*(range(x+1) for x in c)):
        # the third set C has size sd+sa+sb+ss, is a vertex and is distinct from A and B
        size=sd+sa+sb+ss
        if not 0<size<n:continue
        # A = a-only + both; B = b-only + both
        if (sd,sa,sb,ss)==(0,a,0,s):continue  # C=A
        if (sd,sa,sb,ss)==(0,0,b,s):continue  # C=B
        out.add((int(sa+ss==0),int(sb+ss==0)))
    return out


def main():
    for n in range(4,13):
        supports={'singleton':set(),'middle':set(),'co_singleton':set()}
        tested=0
        for c in compositions(n):
            if not valid(c,n):continue
            tested+=1
            typ=name(c)
            assert typ in EXPECTED,(n,c,typ)
            actual=extension_patterns(c,n)
            assert actual==EXPECTED[typ],(n,c,typ,actual,EXPECTED[typ])
            s=c[1]+c[3]
            category='singleton' if s==1 else ('co_singleton' if s==n-1 else 'middle')
            supports[category].add(typ)
        assert supports==POINT,(n,supports,POINT)
        print(f'n={n}, valid ordered pair orbits={tested}, nine pair classes and three point classes: PASS')
    print('PASS: all four-cell pair profiles and pointed profiles agree with the claimed tables.')

if __name__=='__main__':main()
