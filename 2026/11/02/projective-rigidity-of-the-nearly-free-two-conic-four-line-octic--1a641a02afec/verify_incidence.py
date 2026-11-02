#!/usr/bin/env python3
"""Exhaust the abstract pair-incidence assignments with prescribed Tjurina number.

This is a redundant finite check. Projective realizability and uniqueness
are established geometrically, not inferred from this enumeration.
"""
from itertools import combinations,product
edges=list(combinations(range(4),2))
patterns=[]
for n3 in (4,5,6):
    t=10-n3
    for z in (0,1):
        for concurrent in ([None] if z==0 else list(combinations(range(4),3))):
            available=[e for e in edges if concurrent is None or not set(e)<=set(concurrent)]
            for y in range(n3-z+1):
                x=n3-z-y
                if y>len(available):continue
                for ye in combinations(available,y):
                    for colors in product(range(2),repeat=y):
                        triples=list(zip(ye,colors))
                        for xs in product(range(4),repeat=x):
                            if tuple(sorted(xs))!=xs:continue
                            for cc in range(3):
                                if x+2*cc>4:continue
                                used={(q,l):0 for q in range(2) for l in range(4)}
                                for (i,j),q in triples:
                                    used[q,i]+=1;used[q,j]+=1
                                for l in xs:
                                    used[0,l]+=1;used[1,l]+=1
                                if any(v>2 for v in used.values()):continue
                                eligible=[kl for kl,v in used.items() if v==0]
                                if t-cc<0 or t-cc>len(eligible):continue
                                for tang in combinations(eligible,t-cc):
                                    if cc==2 and any((0,l) in tang and (1,l) in tang for l in range(4)):
                                        continue
                                    nodes_cc=4-x-2*cc
                                    nodes_cl=sum(2-v-2*(kl in tang) for kl,v in used.items())
                                    nodes_ll=6-y-3*z
                                    if min(nodes_cc,nodes_cl,nodes_ll)<0:continue
                                    if nodes_cc+nodes_cl+nodes_ll!=6-n3:continue
                                    patterns.append((n3,z,x,y,cc,triples,tang))
assert len(patterns)==6,patterns
assert all((n3,z,x,y,cc)==(4,0,0,4,2) for n3,z,x,y,cc,*_ in patterns)
print('ABSTRACT_TWO_CONIC_FOUR_LINE_INCIDENCE_OK: 6 labeled candidates, one four-cycle type')
