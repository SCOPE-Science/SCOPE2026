#!/usr/bin/env python3
"""Independent coordinate-support vs direct vertex enumeration checks.
No network, random seeds, or third-party packages required.
"""
from itertools import product


def classify(q):return int(q==2)

def colored_dist(x,y,sizes):
    bi=sum(a!=b and q==2 for a,b,q in zip(x,y,sizes))
    non=sum(a!=b and q>=3 for a,b,q in zip(x,y,sizes))
    return (bi,non)


def coordinate_support(b,s,rb,rs):
    # In a binary coordinate with differing anchors c matches exactly one.
    # In a nonbinary differing coordinate c may match neither anchor.
    state={(0,0,0,0)}
    for typ,ndiff,nall in ((True,rb,b),(False,rs,s)):
        for j in range(nall):
            differs=j<ndiff
            local=([(0,1),(1,0)] if differs else [(0,0),(1,1)]) if typ else ([(0,1),(1,0),(1,1)] if differs else [(0,0),(1,1)])
            nxt=set()
            for b1,n1,b2,n2 in state:
                for a1,a2 in local:
                    if typ: nxt.add((b1+a1,n1,b2+a2,n2))
                    else: nxt.add((b1,n1+a1,b2,n2+a2))
            state=nxt
    return state


def direct_support(sizes,x,y,points):
    return {(*colored_dist(x,z,sizes),*colored_dist(y,z,sizes)) for z in points}


def check(sizes):
    points=list(product(*(range(q) for q in sizes)))
    b=sum(q==2 for q in sizes); s=len(sizes)-b
    total=0
    profile_counts={}
    for x in points:
        for y in points:
            rb,rs=colored_dist(x,y,sizes)
            expected=coordinate_support(b,s,rb,rs)
            actual=direct_support(sizes,x,y,points)
            assert actual==expected,(sizes,x,y,actual^expected)
            profile_counts[(rb,rs)]=len(expected)
            total+=1
    # Every colored pair profile is realized.
    assert len(profile_counts)==(b+1)*(s+1)
    print('PASS',sizes,'vertices',len(points),'ordered-pairs',total,'colored-profiles',len(profile_counts),'total-support-entries',sum(profile_counts.values()))
    return total


def main():
    arrays=[(2,),(3,),(4,),(2,2),(2,3),(2,4),(3,3),(3,4),(4,5),(2,2,3),(2,2,4),(2,3,3),(2,3,4),(3,3,4),(2,2,3,4)]
    total=sum(check(a) for a in arrays)
    print('COLORED_DISTANCE_SUPPORT_OK',len(arrays),'graphs',total,'ordered-pairs')

if __name__=='__main__':main()
