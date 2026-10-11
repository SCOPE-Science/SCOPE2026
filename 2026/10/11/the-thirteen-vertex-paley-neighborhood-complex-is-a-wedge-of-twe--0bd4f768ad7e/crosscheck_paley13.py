#!/usr/bin/env python3
"""Independent complex construction and exact simplicial homology over several fields."""
from collections import defaultdict
P=13
SQ={int(t*t%P) for t in range(1,P)}
assert SQ=={1,3,4,9,10,12}

def construct():
    fs=[]
    for m in range(1,1<<P):
        for center in range(P):
            if all(((v-center)%P in SQ) for v in range(P) if m>>v&1):
                fs.append(m)
                break
    return fs

def ranks_for_prime(simplices,p):
    bydim=defaultdict(list)
    for m in simplices: bydim[m.bit_count()-1].append(m)
    ranks={}
    for d in range(1,max(bydim)+1):
        irow={face:j for j,face in enumerate(bydim[d-1])}
        pivots={}
        for mask in bydim[d]:
            vec={}
            verts=[v for v in range(P) if mask>>v&1]
            for pos,v in enumerate(verts):
                row=irow[mask^(1<<v)]
                coeff=1 if pos%2==0 else p-1
                vec[row]=coeff
            while vec:
                row=min(vec)
                a=vec[row]
                if row in pivots:
                    pivot=pivots[row]
                    for j,b in pivot.items():
                        z=(vec.get(j,0)-a*b)%p
                        if z:vec[j]=z
                        else:vec.pop(j,None)
                else:
                    inv=pow(a,-1,p)
                    pivots[row]={j:(b*inv)%p for j,b in vec.items() if b%p}
                    break
        ranks[d]=len(pivots)
    return bydim,ranks

def main():
    fs=construct()
    assert len(fs)==598
    coloring=(0,1,2,1,2,0,3,0,1,4,2,4,3)
    for u in range(P):
        for v in range(u+1,P):
            if (u-v)%P in SQ:
                assert coloring[u]!=coloring[v]
    nonneighbors=[x for x in range(1,P) if x not in SQ]
    assert len(nonneighbors)==6
    from itertools import combinations
    assert not any(all((u-v)%P not in SQ for u,v in combinations(C,2)) for C in combinations(nonneighbors,3))
    print('COLORING_OK','alpha_upper_bound',3,'colors',5,'coloring',coloring)
    for p in (2,3,5,101):
        bydim,r=ranks_for_prime(fs,p)
        assert [len(bydim[d]) for d in range(6)]==[13,78,221,195,78,13]
        betti=[]
        for d in range(6):
            z=len(bydim[d])-r.get(d,0)-r.get(d+1,0)
            if d==0:z-=1
            betti.append(z)
        assert betti==[0,0,25,0,0,0],(p,betti,r)
        print('HOMOLOGY_OK','prime',p,'ranks',r,'reduced_betti',betti)
if __name__=='__main__':main()
