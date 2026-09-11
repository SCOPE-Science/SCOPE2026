import itertools, math
A=0;B=1
a=[2,3,4]; b=[5,6,7]; c=[8,9,10]
edges=[]
def chain(A,inters,B):
    p=A
    for v in inters:
        edges.append((p,v)); p=v
    edges.append((p,B))
chain(A,a,B); chain(A,b,B); chain(A,c,B)
V=11;E=len(edges);n=5
verts=list(range(V))
cells={k: [] for k in range(6)}
index={k: {} for k in range(6)}
for k in range(6):
    for es in itertools.combinations(range(E),k):
        used=set(); ok=True
        for e in es:
            x,y=edges[e]
            if x in used or y in used: ok=False; break
            used.add(x);used.add(y)
        if not ok: continue
        blocked=set(used)
        avail=[v for v in verts if v not in blocked]
        for vs in itertools.combinations(avail,n-k):
            cell=(tuple(sorted(es)),tuple(vs))
            index[k][cell]=len(cells[k]); cells[k].append(cell)
    print(k,len(cells[k]),flush=True)

# boundary: d(cell with edges es=(e0<...<e_{k-1}), verts vs) = sum_i (-1)^i [ (es without ei, vs+u(ei)) - (es without ei, vs+v(ei)) ]
# where edge ei=(u,v) endpoints; replacing edge by each endpoint, keep vs sorted. Sign convention standard for Abrams model.
# Need integer sparse matrices for d3: 1785x920? Actually d_k: C_k -> C_{k-1}, so d3 is 1785 rows x 920 cols.
import numpy as np

def boundary_matrix(k):
    # returns dense integer matrix rows=C_{k-1}, cols=C_k
    R=len(cells[k-1]); C=len(cells[k])
    M=np.zeros((R,C),dtype=np.int64)
    for j,cell in enumerate(cells[k]):
        es,vs=cell
        vs=list(vs)
        for i,e in enumerate(es):
            u,v=edges[e]
            es_rest=tuple(x for ii,x in enumerate(es) if ii!=i)
            for (sgn,w) in ((+1,u),(-1,v)):
                # insert w into vs keeping sorted; need w not already in vs (guaranteed since w was blocked? Actually u,v not in vs because blocked; but after removing ei, u,v become free, and vs doesn't contain them. ok)
                lst=sorted(vs+[w])
                key=(es_rest,tuple(lst))
                r=index[k-1].get(key)
                if r is None:
                    raise RuntimeError("missing face")
                M[r,j]+= sgn*((-1)**i)
    return M

for k in [1,2,3]:
    M=boundary_matrix(k)
    print("d%d shape"%k, M.shape, "nnz", int((M!=0).sum()), flush=True)

# check d2 d3 = 0 on a sample
M2=boundary_matrix(2); M1=boundary_matrix(1)
print("d1d2 max", abs(M1@M2).max())
M3=boundary_matrix(3)
print("d2d3 max", abs(M2@M3).max())
# save
import pickle
with open("mats.pkl","wb") as f:
    pickle.dump({"d1":M1,"d2":M2,"d3":M3,"cells":cells,"edges":edges},f)
print("saved")
