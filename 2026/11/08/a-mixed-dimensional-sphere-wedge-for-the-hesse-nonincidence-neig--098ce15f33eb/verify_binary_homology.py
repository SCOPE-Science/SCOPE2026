"""Independent mod-two boundary computation for the nine-point affine-plane nonincidence complexes."""
from itertools import product
from collections import defaultdict

def rank_mod_two(columns):
    pivots={}
    for col in columns:
        while col:
            p=col.bit_length()-1
            if p in pivots: col^=pivots[p]
            else: pivots[p]=col;break
    return len(pivots)

def make_faces():
    points=list(product(range(3),repeat=2))
    line_sets=[]
    for a,b in ((1,0),(0,1),(1,1),(1,2)):
        for c in range(3):
            line_sets.append(frozenset(i for i,(x,y) in enumerate(points) if (a*x+b*y)%3==c))
    assert len(set(line_sets))==12
    output=[]
    for side in ('point','line'):
        if side=='point':
            n=9
            facet_sets=[set(range(9))-set(L) for L in line_sets]
        else:
            n=12
            facet_sets=[{j for j,L in enumerate(line_sets) if i not in L} for i in range(9)]
        faces=set()
        for bitmask in range(1,1<<n):
            supp={j for j in range(n) if bitmask>>j&1}
            if any(supp<=fac for fac in facet_sets): faces.add(bitmask)
        output.append((side,faces))
    return output

def calculate(faces):
    levels=defaultdict(list)
    for s in faces: levels[s.bit_count()-1].append(s)
    dimensions=sorted(levels)
    ranks={}
    for d in dimensions[1:]:
        lower={s:j for j,s in enumerate(levels[d-1])}
        columns=[]
        for s in levels[d]:
            col=0
            for b in range(s.bit_length()):
                if s>>b&1:col^=1<<lower[s^(1<<b)]
            columns.append(col)
        ranks[d]=rank_mod_two(columns)
    betti={d:len(levels[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in dimensions}
    betti[0]-=1
    return {d:betti[d] for d in dimensions if betti[d]},ranks

if __name__=='__main__':
    for name,faces in make_faces():
        betti,ranks=calculate(faces)
        print(name,'nonempty_faces',len(faces),'mod2_boundary_ranks',sorted(ranks.items()),'reduced_betti',betti)
        assert betti=={3:11,4:1}
        if name=='point':assert ranks=={1:8,2:28,3:56,4:59,5:12}
        if name=='line':assert ranks=={1:11,2:55,3:161,4:278,5:189,6:63,7:9}
    print('BINARY_HOMOLOGY_VERIFIED')
