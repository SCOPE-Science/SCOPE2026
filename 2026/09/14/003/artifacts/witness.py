import numpy as np, itertools
edges=[(0,1),(0,4),(0,7),(1,2),(1,5),(2,3),(2,6),(3,4),(3,7),(4,5),(5,6),(6,7)]
E=len(edges)
# all multisets of 3 edges: combinations_with_replacement
loads=[]
for combo in itertools.combinations_with_replacement(range(E),3):
    b=[0]*8
    for e in combo:
        a1,b1=edges[e]
        b[a1]+=1; b[b1]+=1
    loads.append(b)
loads=np.array(loads, dtype=np.int64)  # 364 x 8
uniq=np.unique(loads,axis=0)
print("num load patterns:",len(loads),"unique:",len(uniq))
cand=np.load("output/artifacts/cand_I4.npy")
print("cand shape",cand.shape)
# chunked domination check
N=len(cand); found=None
CH=20000
n_in_I3=0
noncover=[]
for s in range(0,N,CH):
    blk=cand[s:s+CH]  # B x 8
    # dom[B,364] = all(blk[:,None,:]>=loads[None,:,:],axis=2)
    dom=(blk[:,None,:]>=loads[None,:,:]).all(axis=2)
    inI3=dom.any(axis=1)
    n_in_I3+=int(inI3.sum())
    idx=np.where(~inI3)[0]
    for j in idx:
        noncover.append(blk[j].tolist())
    print(f"chunk {s}-{s+len(blk)}: inI3 so far {n_in_I3}, non-I3 so far {len(noncover)}")
    if len(noncover)>10:
        break
print("n_in_I3 counted, noncover examples:",noncover[:10])
