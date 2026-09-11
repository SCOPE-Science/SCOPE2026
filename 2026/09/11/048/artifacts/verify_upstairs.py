import pickle, itertools, time
with open("mats.pkl","rb") as f:
    D=pickle.load(f)
cells=D["cells"]; edges=D["edges"]
n=5
with open("collapse_state.pkl","rb") as f:
    S=pickle.load(f)
remaining=S["remaining"]
rem0=set(remaining[0]); rem1=set(remaining[1]); rem2=set(remaining[2])
# rebuild ord1 index (fixed encoding: plain ints / ("e",e))
ord1=[]
for j in rem1:
    es,vs=cells[1][j]
    e=es[0]
    for l in range(n):
        for rest in itertools.permutations(vs):
            code=[""]*n
            code[l]=("e",e)
            ri=0
            for m in range(n):
                if m==l: continue
                code[m]=rest[ri]; ri+=1
            ord1.append(tuple(code))
o1={c:i for i,c in enumerate(ord1)}
ord0=[]
for j in rem0:
    es,vs=cells[0][j]
    for perm in itertools.permutations(range(n)):
        ord0.append(tuple(vs[perm[l]] for l in range(n)))
o0={c:i for i,c in enumerate(ord0)}
print("idx built", len(ord0), len(ord1), flush=True)
# d2 columns with signs; check d1d2=0 per column: d1(face) = [u-cell] - [v-cell] as formal vector; represent 0-cellsimler
# d1d2(col) = sum_faces sign*(o0[u-face]-o0[v-face]); accumulate dict, check empty.
t0=time.time()
nb=0
for j in rem2:
    es,vs=cells[2][j]
    e0,e1=es
    for l0 in range(n):
        for l1 in range(n):
            if l1==l0: continue
            for rest in itertools.permutations(vs):
                code=[""]*n
                code[l0]=("e",e0); code[l1]=("e",e1)
                ri=0
                for m in range(n):
                    if m==l0 or m==l1: continue
                    code[m]=rest[ri]; ri+=1
                co=tuple(code)
                labs=sorted([l0,l1])
                acc={}
                for t,l in enumerate(labs):
                    ee=e0 if l==l0 else e1
                    u,v=edges[ee]
                    s=(-1)**t
                    for sgn,w in ((1,u),(-1,v)):
                        fc=list(co); fc[l]=w; fc=tuple(fc)
                        # d1 of ordered 1-cell fc: single edge? fc is a 1-cell only if it still has one edge particle; the OTHER edge particle remains -> fc has 1 edge + 4 verts? fc: replaced one edge by vertex, other edge stays => 1-cell ✓
                        # find its edge particle and endpoints
                        el=None
                        for m in range(n):
                            if isinstance(fc[m],tuple):
                                el=m; break
                        eu,ev=edges[fc[el][1]]
                        g1=list(fc); g1[el]=eu; g1=tuple(g1)
                        g2=list(fc); g2[el]=ev; g2=tuple(g2)
                        acc[g1]=acc.get(g1,0)+s*sgn*1
                        acc[g2]=acc.get(g2,0)+s*sgn*(-1)
                # check all zero; also all keys in o0
                for k2,v2 in acc.items():
                    if v2!=0:
                        print("D2 FAIL",j); raise SystemExit
                    if k2 not in o0:
                        print("FACE MISSING"); raise SystemExit
                nb+=1
print("d1d2=0 OK over ZZ signs, cols checked:",nb,"time",time.time()-t0,flush=True)
