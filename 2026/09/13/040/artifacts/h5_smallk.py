import itertools, sys
sys.path.insert(0,'output/artifacts')
# reuse functions from h5_explore by exec
exec(open('output/artifacts/h5_explore.py').read().split("def gen_reps")[0])
# Now we need gen_reps + orbit sums for k=3,4 (reps use labels up to 4; orbit sums with support>k give zero, fine)
def gen_reps():
    allreps=[]
    for etype in (0,1):
        for j0 in range(5):
            for l0 in range(5):
                for m0 in range(5):
                    if not (l0<m0): continue
                    for p0 in range(5):
                        for q0 in range(5):
                            if not (p0<q0): continue
                            allreps.append((etype,j0,(l0,m0),(p0,q0)))
    def canon(rep):
        etype,j0,(l0,m0),(p0,q0)=rep
        best=None
        for (l,m) in ((l0,m0),(m0,l0)):
            for (p,q) in ((p0,q0),(q0,p0)):
                roles=[j0,l,m,p,q]
                mp={}; nxt=0; code=[]
                for v in roles:
                    if v not in mp: mp[v]=nxt; nxt+=1
                    code.append(mp[v])
                code=tuple(code)
                if best is None or code<best: best=code
        return (etype,best)
    seen={}
    for rep in allreps:
        c=canon(rep)
        if c not in seen:
            seen[c]=rep
    return list(seen.values())

reps=gen_reps()
for k in [3,4,5]:
    maps=build_index_maps(k)
    w_index,wlist,dW,s_index,slist,nS,a6_index,a6list=maps
    print(f"=== k={k} dW={dW} nS={nS} nA6={len(a6list)}")
    dom=[orbit_sum_C5(k,rep,maps) for rep in reps]
    rdom,Gdom=rank_of_dicts(dom)
    print(f"  inv(C5) rank={rdom}")
    imgs=[orbit_sum_Dimage(k,rep,maps) for rep in reps]
    rimg,_=rank_of_dicts(imgs)
    print(f"  rank(D(invC5))={rimg} => ker={rdom-rimg}")
