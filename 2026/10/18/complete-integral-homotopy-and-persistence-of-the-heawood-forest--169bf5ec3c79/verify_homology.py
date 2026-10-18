#!/usr/bin/env python3
"""Independent face enumeration and finite-field boundary-rank validation.

Uses component counting and Euler's forest identity, not the union/find of
verify_morse.py. Boundary ranks use sparse column elimination over GF(2).
"""
from collections import defaultdict,Counter
N=14
incidence={0,1,3}
edges={(i,7+j) for j in range(7) for i in range(7) if (i-j)%7 in incidence}
neighbor=[set() for _ in range(N)]
for a,b in edges:
    neighbor[a].add(b);neighbor[b].add(a)


def is_forest(vertices):
    chosen=set(vertices)
    remaining=chosen.copy()
    comps=0
    while remaining:
        comps+=1
        v=remaining.pop()
        reach={v}
        stack=[v]
        while stack:
            w=stack.pop()
            for u in neighbor[w]&chosen:
                if u not in reach:
                    reach.add(u)
                    remaining.discard(u)
                    stack.append(u)
    internal=sum((a in chosen and b in chosen) for a,b in edges)
    return internal==len(vertices)-comps

def build_stage(d):
    bydim=defaultdict(list)
    for mask in range(1,1<<N):
        verts=tuple(i for i in range(N) if (mask>>i)&1)
        if any(len(neighbor[i]&set(verts))>d for i in verts):
            continue
        if is_forest(verts):
            bydim[len(verts)-1].append(mask)
    return bydim

def ranks(bydim):
    answer={}
    for k in sorted(bydim):
        if k==0:continue
        lower={a:i for i,a in enumerate(bydim[k-1])}
        pivots={}
        for col_mask in bydim[k]:
            column={lower[col_mask^(1<<i)] for i in range(N)
                    if (col_mask>>i)&1}
            while column:
                pivot=max(column)
                if pivot in pivots:
                    column.symmetric_difference_update(pivots[pivot])
                else:
                    pivots[pivot]=column
                    break
        answer[k]=len(pivots)
    return answer

def main():
    assert len(edges)==21
    expected=[{3:6},{5:13},{6:1},{8:8}]
    for d in range(4):
        stage=build_stage(d)
        rr=ranks(stage)
        homology={k:len(stage[k])-rr.get(k,0)-rr.get(k+1,0)
                  for k in stage}
        homology[0]-=1
        homology={k:v for k,v in homology.items() if v}
        assert homology==expected[d],(d,homology)
        print('F_'+str(d), 'mod_2_reduced_homology='+str(homology),
              'ranks='+str(dict(sorted(rr.items()))))
    print('PASS: independent enumeration and mod-two boundary ranks.')

if __name__=='__main__':
    main()
