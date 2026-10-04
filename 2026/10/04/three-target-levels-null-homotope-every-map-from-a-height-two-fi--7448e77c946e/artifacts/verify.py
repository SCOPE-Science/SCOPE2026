from itertools import product


def weak_order(level_sizes):
    level=[]
    for i,s in enumerate(level_sizes):
        level.extend([i]*s)
    n=len(level)
    le=[[False]*n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            le[a][b]=(a==b) or (level[a]<level[b])
    blocks=[]; off=0
    for s in level_sizes:
        blocks.append(list(range(off,off+s))); off+=s
    return level,le,blocks


def source_poset(l,u,mask):
    # l minimal-side points, u maximal-side points; arbitrary bipartite relations.
    n=l+u
    le=[[False]*n for _ in range(n)]
    for i in range(n): le[i][i]=True
    bit=0
    for i in range(l):
        for j in range(u):
            if (mask>>bit)&1:
                le[i][l+j]=True
            bit+=1
    return le


def monotone_maps(src,tgt):
    ns=len(src); nt=len(tgt)
    rel=[(i,j) for i in range(ns) for j in range(ns) if i!=j and src[i][j]]
    for f in product(range(nt), repeat=ns):
        if all(tgt[f[i]][f[j]] for i,j in rel):
            yield f


def le_map(f,g,tgt):
    return all(tgt[a][b] for a,b in zip(f,g))


def construct(f,l,level,blocks):
    h=len(blocks)
    c=blocks[h-3][0]
    b=blocks[h-2][0]
    t=blocks[h-1][0]
    f1=list(f)
    for x in range(l):
        if level[f1[x]]>=h-2:
            f1[x]=c
    f2=f1[:]
    for x in range(l,len(f)):
        if level[f2[x]]==h-1:
            f2[x]=b
    ct=tuple([t]*len(f))
    return tuple(f1),tuple(f2),ct


def is_monotone(f,src,tgt):
    return all(not src[i][j] or tgt[f[i]][f[j]] for i in range(len(f)) for j in range(len(f)))

checked=0
maps_checked=0
for l in (1,2):
    for u in (1,2):
        for mask in range(1<<(l*u)):
            src=source_poset(l,u,mask)
            for sizes in ((1,1,1),(2,1,2),(2,2,2),(1,2,1,1)):
                level,tgt,blocks=weak_order(sizes)
                for f in monotone_maps(src,tgt):
                    f1,f2,ct=construct(f,l,level,blocks)
                    assert is_monotone(f1,src,tgt)
                    assert is_monotone(f2,src,tgt)
                    assert is_monotone(ct,src,tgt)
                    assert le_map(f1,f,tgt)
                    assert le_map(f2,f1,tgt)
                    assert le_map(f2,ct,tgt)
                    maps_checked+=1
                checked+=1

# Sharpness at two target levels: identity of the four-point crown has nonzero H_1,
# while a constant map has zero H_1. Here we check only the finite combinatorial
# premise: the identity is not pointwise comparable to any constant.
level,tgt,blocks=weak_order((2,2))
idmap=(0,1,2,3)
for t in range(4):
    c=(t,t,t,t)
    assert not le_map(idmap,c,tgt) or idmap==c
    assert not le_map(c,idmap,tgt) or idmap==c
print(f'VERIFY_OK source_cases={checked} maps={maps_checked} sharp_height2=checked')
