import pickle, itertools, time
with open("mats.pkl","rb") as f:
    D=pickle.load(f)
cells=D["cells"]; edges=D["edges"]
n=5
with open("collapse_state.pkl","rb") as f:
    S=pickle.load(f)
remaining=S["remaining"]
rem0=set(remaining[0]); rem1=set(remaining[1])
ord0=[]
for j in rem0:
    es,vs=cells[0][j]
    for perm in itertools.permutations(range(n)):
        code=tuple(vs[perm[l]] for l in range(n))
        ord0.append(code)
o0={c:i for i,c in enumerate(ord0)}
print("ord0",len(ord0),flush=True)
R=len(ord0)
parent=list(range(R))
def find(a):
    while parent[a]!=a:
        parent[a]=parent[parent[a]]; a=parent[a]
    return a
def union(a,b):
    ra,rb=find(a),find(b)
    if ra!=rb: parent[ra]=rb
ncols=0; nfail=0
for j in rem1:
    es,vs=cells[1][j]
    e=es[0]; u,v=edges[e]
    for l in range(n):
        for rest in itertools.permutations(vs):
            # faces
            f1=[""]*n; f2=[""]*n
            ri=0
            for m in range(n):
                if m==l: continue
                f1[m]=rest[ri]; f2[m]=rest[ri]; ri+=1
            f1[l]=u; f2[l]=v
            f1=tuple(f1); f2=tuple(f2)
            r1=o0.get(f1); r2=o0.get(f2)
            if r1 is None or r2 is None:
                nfail+=1
                continue
            union(r1,r2); ncols+=1
print("cols",ncols,"nfail",nfail,flush=True)
comps=len(set(find(i) for i in range(R)))
print("components",comps,"rank_d1 =",R-comps,flush=True)
