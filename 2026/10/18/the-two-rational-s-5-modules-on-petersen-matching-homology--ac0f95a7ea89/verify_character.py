"""Direct oriented-chain computation for the Petersen matching complex.

Runs using Python standard library only. A second independent program verifies
all rational ranks by exact arithmetic and obtains characters from fixed chains.
"""
from itertools import combinations, permutations
from collections import Counter

MOD=1000003
points=tuple(combinations(range(5),2))
pid={s:i for i,s in enumerate(points)}
edges=tuple((i,j) for i in range(10) for j in range(i+1,10)
            if not set(points[i]).intersection(points[j]))
assert len(edges)==15
edge_id={e:i for i,e in enumerate(edges)}
faces={0:[()]}
for k in range(1,6):
    faces[k]=[f for f in combinations(range(15),k)
              if len({v for a in f for v in edges[a]})==2*k]
face_id={k:{f:i for i,f in enumerate(faces[k])} for k in faces}
assert tuple(len(faces[i]) for i in range(6))==(1,15,75,145,90,6)

def boundary_image(k):
    """Reduced column-echelon basis of image(boundary C[k+1] -> C[k])."""
    pivots=[];basis=[]
    for f in faces[k+1]:
        v=[0]*len(faces[k])
        for j in range(k+1):
            v[face_id[k][f[:j]+f[j+1:]]]=1 if j%2==0 else MOD-1
        for row,b in zip(pivots,basis):
            a=v[row]
            if a:v=[(x-a*y)%MOD for x,y in zip(v,b)]
        if any(v):
            row=next(i for i,x in enumerate(v) if x)
            inv=pow(v[row],-1,MOD)
            basis.append([x*inv%MOD for x in v]);pivots.append(row)
    return pivots,basis

images={k:boundary_image(k) for k in range(5)}
assert [len(images[i][0]) for i in range(5)]==[1,14,61,79,6]

def edge_action(g):
    perm=[pid[tuple(sorted(g[i] for i in t))] for t in points]
    return [edge_id[tuple(sorted(perm[i] for i in e))] for e in edges]

def action(k,perm):
    result=[]
    for f in faces[k]:
        seq=[perm[a] for a in f]
        s=-1 if sum(seq[i]>seq[j] for i in range(len(seq))
                    for j in range(i+1,len(seq)))%2 else 1
        result.append((face_id[k][tuple(sorted(seq))],s))
    return result

def trace_image(k,Act):
    pivots,basis=images[k]
    trace=0
    for target_index,v in enumerate(basis):
        image=[0]*len(v)
        for j,x in enumerate(v):
            if x:
                dest,sign=Act[j]
                image[dest]=(image[dest]+sign*x)%MOD
        for i,(row,b) in enumerate(zip(pivots,basis)):
            scalar=image[row]
            if scalar:
                if i==target_index:trace=(trace+scalar)%MOD
                image=[(x-scalar*y)%MOD for x,y in zip(image,b)]
        assert not any(image)
    return trace

def typ(g):
    out=[]; seen=set()
    for i in range(5):
        if i not in seen:
            j=i;k=0
            while j not in seen:seen.add(j);k+=1;j=g[j]
            out.append(k)
    return tuple(sorted(out,reverse=True))

def signed(v):
    x=v%MOD
    return x if x<=MOD//2 else x-MOD

answer={}
for g in permutations(range(5)):
    t=typ(g)
    if t in answer:continue
    P=edge_action(g)
    chain=[sum(s for i,(j,s) in enumerate(action(k,P)) if i==j)
           for k in range(6)]
    traces=[trace_image(k,action(k,P)) for k in range(5)]+[0]
    hom=[signed(chain[k]-traces[k]-(traces[k-1] if k else 0))
         for k in range(6)]
    answer[t]=(hom[3],hom[4])

expect={
(1,1,1,1,1):(5,5),
(2,1,1,1):(-3,1),
(2,2,1):(1,1),
(3,1,1):(2,-1),
(3,2):(0,1),
(4,1):(-1,-1),
(5,):(0,0),
}
assert answer==expect,(answer,expect)
print('f-vector (including empty face):',[len(faces[k]) for k in range(6)])
print('boundary ranks modulo',MOD,':',[len(images[k][0]) for k in range(5)])
print('character pairs H2,H3:',answer)
print('DIRECT_CHAIN_CHECK_OK')
