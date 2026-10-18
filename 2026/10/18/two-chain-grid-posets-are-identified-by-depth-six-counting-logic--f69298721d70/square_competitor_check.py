#!/usr/bin/env python3
"""Independent finite reconstruction: enumerate every counting-equitable
comparison block for two equal-chain products with side <=4, reject
nontransitive structures, check the survivors up to isomorphism.
"""
from itertools import combinations,product


def exercise(n):
    pts=[(i,j) for i in range(1,n+1) for j in range(1,n+1)]
    idx={p:k for k,p in enumerate(pts)}
    orbit={}
    for i in range(1,n+1):
        for j in range(i,n+1):
            orbit[(i,j)]=[idx[(i,j)]] if i==j else [idx[(i,j)],idx[(j,i)]]
    classes=list(orbit)
    ref=[[int(i<=k and j<=l) for k,l in pts] for i,j in pts]
    option=[]
    for c,d in combinations(classes,2):
        A,B=orbit[c],orbit[d]
        if len(A)!=2 or len(B)!=2:continue
        AB=[[ref[x][y] for y in B] for x in A]
        BA=[[ref[x][y] for y in A] for x in B]
        if [sum(r) for r in AB]==[1,1] and [sum(r) for r in zip(*AB)]==[1,1]:
            assert not any(map(any,BA)),(c,d)
            option.append((A,B))
        elif [sum(r) for r in BA]==[1,1] and [sum(r) for r in zip(*BA)]==[1,1]:
            assert not any(map(any,AB)),(c,d)
            option.append((B,A))
        else:
            assert len(set(map(sum,AB)))==1 and len(set(map(sum,BA)))==1
    good=0
    for flips in product((0,1),repeat=len(option)):
        candidate=[row[:] for row in ref]
        for bit,(A,B) in zip(flips,option):
            if bit:
                for x in A:
                    for y in B:
                        candidate[x][y]=1-candidate[x][y]
        is_poset=all(not(candidate[i][j] and candidate[j][k]) or candidate[i][k]
                     for i in range(n*n) for j in range(n*n) for k in range(n*n))
        if not is_poset:continue
        good+=1
        # Any isomorphism must preserve all orbit-color classes.
        # Enumerate independent flips of their two members.
        double=[o for o in orbit.values() if len(o)==2]
        exists=False
        for flipmap in product((0,1),repeat=len(double)):
            perm=list(range(n*n))
            for switch,pair in zip(flipmap,double):
                if switch:perm[pair[0]],perm[pair[1]]=perm[pair[1]],perm[pair[0]]
            if all(candidate[i][j]==ref[perm[i]][perm[j]] for i in range(n*n) for j in range(n*n)):
                exists=True;break
        assert exists,('COUNTEREXAMPLE',n,flips)
    assert good>0
    return len(option),2**len(option),good

if __name__=='__main__':
    for n in range(2,5):
        blocks,total,survivors=exercise(n)
        print(f'n={n}: {blocks} variable matching blocks, {total} equitable candidates, {survivors} transitive, all isomorphic to the grid')
    print('PASS square competitor exhaustive reconstruction through side length 4')
