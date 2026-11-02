#!/usr/bin/env python3
"""Exact finite over-approximation of the incidence constraints for 3 conics + 3 lines.
All curves are smooth and all singularities must be A1, A3 or D4.
This verifier is auxiliary; the unrestricted geometric proof is in RESULT.md.
"""
from itertools import combinations, combinations_with_replacement, product

C = range(3)
L = range(3)
cpairs = list(combinations(C,2))
vertices = [(0,1),(0,2),(1,2)]
ctype = [(i,j,l) for i,j in cpairs for l in L]
passed = 0
cases = []

for mode in ('concurrent', 'triangle'):
    zlist = [0] if mode=='concurrent' else [2,3]
    for z in zlist:
        w = int(mode=='concurrent')
        for chosen in ([()] if mode=='concurrent' else combinations(range(3),z)):
            for assigned in ([()] if mode=='concurrent' else product(C,repeat=z)):
                at_vertex = dict(zip(chosen,assigned))
                nLL = 0 if mode=='concurrent' else 3-z
                nCC = 1-nLL # no C-L nodes: C-L intersection count has even residual
                if nCC < 0: continue
                xplusy = 4-z-w
                for x in range(xplusy+1):
                    y = xplusy-x
                    wanted_lc = 9-y-z
                    wanted_cc = 10-wanted_lc
                    if not 0<=wanted_lc<=9 or not 0<=wanted_cc<=6: continue
                    for mask in combinations([(c,l) for c in C for l in L],wanted_lc):
                        tset = set(mask)
                        if mode=='concurrent' and any(sum((c,l) in tset for l in L)>2 for c in C):
                            continue
                        lcounts = {(c,l):2*int((c,l) in tset) for c in C for l in L}
                        for vid,c in at_vertex.items():
                            for l in vertices[vid]: lcounts[(c,l)] += 1
                        if max(lcounts.values())>2: continue
                        for cc in product(range(3),repeat=3):
                            if sum(cc)!=wanted_cc: continue
                            tcc = dict(zip(cpairs,cc))
                            if x>0 and max(cc)==2: continue # every C-C pair meets transversely at the C-C-C triple
                            if any(tcc[(a,b)]==2 and any((a,l) in tset and (b,l) in tset for l in L) for a,b in cpairs):
                                continue # published double-contact/common-tangent lemma
                            capacities={pair:4-2*tcc[pair]-x for pair in cpairs}
                            if min(capacities.values())<0: continue
                            available=[(a,b,l) for a,b,l in ctype if (a,l) not in tset and (b,l) not in tset]
                            for extra in combinations_with_replacement(available,y):
                                remain=lcounts.copy()
                                for a,b,l in extra:
                                    remain[(a,l)]+=1; remain[(b,l)]+=1
                                if any(v!=2 for v in remain.values()): continue
                                unused=capacities.copy()
                                for a,b,l in extra: unused[(a,b)]-=1
                                if min(unused.values())<0 or sum(unused.values())!=nCC: continue
                                passed+=1
                                cases.append((mode,z,chosen,assigned,x,y,mask,cc,extra,unused))
                                break

assert passed==0, (passed,cases[:1])
print('EXACT_THREE_CONIC_THREE_LINE_INCIDENCE_INFEASIBLE_OK')
print('All triangle/concurrent line types, all CLL assignments, all 9 line-conic tangency bits,')
print('all three conic-pair 0/1/2 tacnode counts, and all CCL triple allocations exhausted.')
