import numpy as np, itertools
edges=[(0,1),(0,4),(0,7),(1,2),(1,5),(2,3),(2,6),(3,4),(3,7),(4,5),(5,6),(6,7)]
E=len(edges)
covers_list=[[1,3,4,6,7],[1,2,4,6,7],[1,2,4,5,7],[0,2,4,5,7],[0,2,3,5,7],[0,2,3,5,6],[0,1,3,5,6],[0,1,3,4,6]]
C=np.zeros((8,8),dtype=int)
for i,c in enumerate(covers_list):
    for v in c: C[i,v]=1

def loads_for(r):
    L=[]
    for combo in itertools.combinations_with_replacement(range(E),r):
        b=[0]*8
        for e in combo:
            a1,b1=edges[e]; b[a1]+=1; b[b1]+=1
        L.append(b)
    L=np.array(L,dtype=np.int64)
    L=np.unique(L,axis=0)
    return L

def containment(m,r):
    # enumerate box 0..m (minimal counterexample bound)
    # returns (holds, witness or None, counts)
    L=loads_for(r)
    # iterate odometer; (m+1)^8 vectors
    total=(m+1)**8
    print(f"m={m} r={r}: box size {total}, loads {len(L)}",flush=True)
    grids=np.indices((m+1,)*8).reshape(8,-1).T
    W=C@grids.T
    mask=np.all(W>=m,axis=0)
    cand=grids[mask]
    print(f"  sym candidates: {len(cand)}",flush=True)
    CH=20000
    for s in range(0,len(cand),CH):
        blk=cand[s:s+CH]
        dom=(blk[:,None,:]>=L[None,:,:]).all(axis=2)
        inI=dom.any(axis=1)
        bad=np.where(~inI)[0]
        if len(bad)>0:
            w=blk[bad[0]].tolist()
            return False, w, len(cand)
    return True, None, len(cand)

for m in [2,3,4,5]:
    for r in [2,3,4]:
        if r>m: continue
        holds,w,nc=containment(m,r)
        print(f"RESULT I^({m}) vs I^{r}: {'HOLDS' if holds else f'FAILS e.g. {w}'} (ncand={nc})",flush=True)
