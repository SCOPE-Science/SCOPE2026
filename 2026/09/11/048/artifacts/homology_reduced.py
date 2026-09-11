# The collapse sequence removed cells in free-face pairs; remaining complex is NOT a subcomplex (remaining cells don't form a subcomplex in general after collapses? Actually elementary collapse removes a free face AND its unique coface; the remaining set IS a subcomplex? Removing a free face r and its coface j: any face of remaining cells remains (faces of j other than r remain; r's faces remain). Yes remaining is a subcomplex and a deformation retract. Good.
# But our greedy removed MANY pairs simultaneously in each sweep: simultaneous removal of multiple free-face pairs is valid iff each removed face's unique coface is also removed and cofaces distinct and faces distinct (matching), and no removed coface contains another removed face... Standard: a matching of free faces can be collapsed in any order if they are disjoint pairs? Need care: after removing one pair, another pair's freeness may break (its face may gain... no, removing cofaces can only DECREASE coface counts, so a face with cof==1 keeps cof<=1; but its unique coface might be removed as another pair's coface? We ensured distinct cofaces. Could its unique coface contain another removed FACE? That would make the coface have 2 removed faces but it's removed anyway; order: collapse pairs in some order; when we collapse pair (r,j), we need r to be free at that moment, i.e., j the only remaining coface of r. Since we only decrease cofaces, r stays free (cof<=1, and j still present). And j still contains r. So any order works. Good — simultaneous matching collapse is valid (it's a Morse matching with identity acyclicity since all pairs are (k-1,k) with freeness).
# Across iterations, sequential validity holds. So remaining subcomplex ~= homotopy equivalent. 
# Now compute homology of remaining subcomplex directly: build boundary matrices restricted to remaining cells. But careful: boundary of a remaining k-cell may include removed (k-1)-cells — NO: remaining is a subcomplex so all faces of remaining cells are remaining. Verify!
import pickle, numpy as np
with open("mats.pkl","rb") as f:
    D=pickle.load(f)
cells=D["cells"]; edges=D["edges"]
with open("collapse_state.pkl","rb") as f:
    S=pickle.load(f)
remaining=S["remaining"]
idx=[{c:i for i,c in enumerate(cells[k])} for k in range(6)]
def faces_of(k, cell):
    es,vs=cell; vs=list(vs)
    out=[]
    for i,e in enumerate(es):
        u,v=edges[e]
        rest=tuple(x for ii,x in enumerate(es) if ii!=i)
        for w in (u,v):
            out.append((rest,tuple(sorted(vs+[w]))))
    return out
# verify subcomplex
for k in range(1,6):
    rem=remaining[k]; remm=remaining[k-1]
    for j in rem:
        for fc in faces_of(k, cells[k][j]):
            if idx[k-1][fc] not in remm:
                print("NOT SUBCOMPLEX", k, j); raise SystemExit
print("subcomplex OK")
# homology of remaining: C0=202,C1=467,C2=266
M1=D["d1"]; M2=D["d2"]
r0=sorted(remaining[0]); r1=sorted(remaining[1]); r2=sorted(remaining[2])
m1={v:i for i,v in enumerate(r0)}; m2={v:i for i,v in enumerate(r1)}; m3={v:i for i,v in enumerate(r2)}
A1=np.zeros((len(r0),len(r1)),dtype=np.int64)
for jj,j in enumerate(r1):
    col=M1[:,j]
    for i in np.nonzero(col)[0]:
        A1[m1[i],jj]=col[i]
A2=np.zeros((len(r1),len(r2)),dtype=np.int64)
for jj,j in enumerate(r2):
    col=M2[:,j]
    for i in np.nonzero(col)[0]:
        A2[m2[i],jj]=col[i]
print("A1",A1.shape,"A2",A2.shape)
print("ranks",np.linalg.matrix_rank(A1.astype(float)),np.linalg.matrix_rank(A2.astype(float)))
print("b0",len(r0)-np.linalg.matrix_rank(A1.astype(float)))
print("b1",len(r1)-np.linalg.matrix_rank(A1.astype(float))-np.linalg.matrix_rank(A2.astype(float)))
print("b2",len(r2)-np.linalg.matrix_rank(A2.astype(float)))
# mod p
def rankmod(M,p):
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
        for i in range(rows):
            if i!=rr and B[i,c]!=0:
                B[i]=(B[i]-B[i,c]*B[rr])%p
        rr+=1
        if rr==rows: break
    return rr
for p in [2,3,5]:
    a=rankmod(A1,p); b=rankmod(A2,p)
    print(p, a, b, "H1dim", len(r1)-a-b, "H2dim", len(r2)-b)
