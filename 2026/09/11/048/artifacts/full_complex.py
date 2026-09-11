import pickle, itertools, numpy as np
with open("mats.pkl","rb") as f:
    D=pickle.load(f)
cells=D["cells"]; edges=D["edges"]
V=11
def bmat(k):
    # C_k -> C_{k-1}
    R=len(cells[k-1]); C=len(cells[k])
    idx={c:i for i,c in enumerate(cells[k-1])}
    M=np.zeros((R,C),dtype=np.int64)
    for j,cell in enumerate(cells[k]):
        es,vs=cell; vs=list(vs)
        for i,e in enumerate(es):
            u,v=edges[e]
            rest=tuple(x for ii,x in enumerate(es) if ii!=i)
            for sgn,w in ((1,u),(-1,v)):
                lst=tuple(sorted(vs+[w]))
                r=idx.get((rest,lst))
                if r is None: raise RuntimeError("missing")
                M[r,j]+=sgn*((-1)**i)
    return M
for k in [4,5]:
    M=bmat(k)
    print("d%d"%k,M.shape,"nnz",int((M!=0).sum()))
    import pickle as pk
    with open("d%d.pkl"%k,"wb") as f: pk.dump(M,f)
    print("rank float",np.linalg.matrix_rank(M.astype(float)))
    # mod p ranks via integer gaussian elim vectorized
    for p in [2,3]:
        B=(M%p).astype(np.int64)%p
        rows,cols=B.shape; rr=0
        for c in range(cols):
            piv=-1
            for i in range(rr,rows):
                if B[i,c]%p!=0: piv=i; break
            if piv<0: continue
            B[[rr,piv]]=B[[piv,rr]]
            inv=pow(int(B[rr,c]),-1,p)
            B[rr]=(B[rr]*inv)%p
            # eliminate other rows
            for i in range(rows):
                if i!=rr and B[i,c]!=0:
                    B[i]=(B[i]-B[i,c]*B[rr])%p
            rr+=1
            if rr==rows: break
        print("  mod",p,"rank",rr)
