"""Exact chain and cup tests for the antipodal orbit of Hamming scale-two Rips complexes."""
from collections import defaultdict,Counter
from itertools import combinations

def binary_rank(rows, columns):
    pivots={}
    for x in rows:
        while x:
            c=x.bit_length()-1
            if c not in pivots:
                pivots[c]=x
                break
            x^=pivots[c]
    return len(pivots)

def build(n):
    total=1<<n; mask=total-1;
    bydim=defaultdict(dict)
    original=[]
    # Recursive clique generation on distance <=2 graph.
    adj={v:set(w for w in range(total) if v!=w and (v^w).bit_count()<=2) for v in range(total)}
    def rec(face,candidates):
        if face:
            original.append(face)
            ordered=tuple(sorted(face,key=lambda u:(min(u,u^mask))))
            partner=tuple(u^mask for u in ordered)
            chosen=min(ordered,partner)
            orbitlabels=tuple(min(u,u^mask) for u in ordered)
            key=(orbitlabels,chosen)
            bydim[len(face)-1][key]=chosen
        for t,x in enumerate(candidates):
            rec(face+(x,),[y for y in candidates[t+1:] if y in adj[x]])
    rec((),list(range(total)))
    cells={d:sorted(v.values(),key=lambda x:tuple(min(u,u^mask) for u in x)+(x,)) for d,v in bydim.items()}
    def canon(face):
        ordered=tuple(sorted(face,key=lambda u:min(u,u^mask)))
        partner=tuple(u^mask for u in ordered)
        return min(ordered,partner)
    idx={d:{f:i for i,f in enumerate(fs)} for d,fs in cells.items()}
    boundaries={}
    for d in range(1,max(cells)+1):
        arr=[{} for _ in cells[d]]
        for j,f in enumerate(cells[d]):
            for i in range(d+1):
                sub=canon(f[:i]+f[i+1:]); k=idx[d-1][sub]
                arr[j][k]=arr[j].get(k,0)+(-1)**i
            arr[j]={k:v for k,v in arr[j].items() if v}
        boundaries[d]=arr
    # integer d^2 checks, using sparse lists
    for d in range(2,max(cells)+1):
        for col in boundaries[d]:
            bb=Counter()
            for j,x in col.items():
                for i,y in boundaries[d-1][j].items():bb[i]+=x*y
            assert not any(bb.values()),(n,d,bb)
    # GF2 boundary ranks using row-bits over cell columns
    ranks=[]; bettis=[]
    for d in range(1,max(cells)+1):
        rows=[0]*len(cells[d-1])
        for j,col in enumerate(boundaries[d]):
            for i,v in col.items():
                if v&1:rows[i]^=1<<j
        ranks.append(binary_rank(rows,len(cells[d])))
    c=[len(cells[d]) for d in range(max(cells)+1)]
    bettis=[c[i]-(ranks[i-1] if i else 0)-(ranks[i] if i<len(ranks) else 0) for i in range(len(c))]
    # x: cover-class mod2, represented by sheet discrepancy along lifted edge.
    x={e:(e[0]>>(n-1))^(e[1]>>(n-1)) for e in cells[1]}
    assert sum(x.values())>0
    for col in boundaries[2]:
        assert sum(x[cells[1][c]]*v for c,v in col.items())%2==0,(n,'cover cocycle')
    base0=[]
    for vertex in range(len(cells[0])):
        row=0
        for j,col in enumerate(boundaries[1]):
            if col.get(vertex,0)&1:row^=1<<j
        base0.append(row)
    xbit=sum(val<<j for j,val in enumerate(x[e] for e in cells[1]))
    assert binary_rank(base0+[xbit],len(cells[1]))==binary_rank(base0,len(cells[1]))+1
    # x cup x and x cup x cup x on globally orbit-ordered cells
    cup={}
    for power in [2,3]:
        vec=[]
        for f in cells[power]:
            eidx=[]
            for i in range(power):
                edge=canon((f[i],f[i+1]));eidx.append(x[edge])
            vec.append(int(all(eidx)))
        cup[power]=vec
        # verify cocycle
        if power<max(cells):
            for col in boundaries[power+1]:
                assert sum((v&1)*vec[k] for k,v in col.items())%2==0,(n,power)
        # Check nonboundary by coboundary span of C^{power-1}
        rows=[]
        for k in range(len(cells[power-1])):
            row=0
            for j,col in enumerate(boundaries[power]):
                if col.get(k,0)&1:row^=1<<j
            rows.append(row)
        target=sum(value<<j for j,value in enumerate(vec))
        cup[power]=(sum(vec),binary_rank(rows,len(vec)),binary_rank(rows+[target],len(vec)))
    return {'n':n,'original_faces':len(original),'original_by_dim':dict(sorted(Counter(len(f)-1 for f in original).items())),'quotient_cells':c,'mod2_boundary_ranks':ranks,'mod2_betti':bettis,'cup_square':cup[2],'cup_cube':cup[3],'integral_boundary_squared':0}

if __name__=='__main__':
    expected={4:([8,40,80,60,8],[7,32,47,8],[1,1,1,5,0],(12,32,33),(4,47,48)),
              5:([16,120,320,320,96,16],[15,104,215,80,16],[1,1,1,25,0,0],(32,104,105),(12,215,216))}
    for n in [4,5]:
        d=build(n)
        assert (d['quotient_cells'],d['mod2_boundary_ranks'],d['mod2_betti'],d['cup_square'],d['cup_cube']) == expected[n]
        print(d)
