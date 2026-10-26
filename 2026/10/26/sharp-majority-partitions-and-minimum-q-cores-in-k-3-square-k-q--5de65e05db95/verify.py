"""Independent finite checks of dense-core bound and majority partitions in K3 x Kq x Kq."""
from itertools import product, combinations
from math import comb

def adjacency(q):
    vv=list(product(range(3),range(q),range(q)))
    idx={v:i for i,v in enumerate(vv)}
    nb=[]
    for v in vv:
        nb.append(set(idx[w] for w in vv if sum(x!=y for x,y in zip(v,w))==1))
    return vv,nb

def partition(q):
    pieces=[]
    for i in range(3):
        for j in range(0, q-1,2):
            pieces.append({(i,j,z) for z in range(q)}|{(i,j+1,z) for z in range(q)})
    if q%2:
        pieces.append({(i,q-1,z) for i in range(3) for z in range(q)})
    return pieces

def rectangles(q):
    sizes=(3,q,q)
    out=[]
    for d in ((0,1,2) if q==3 else (1,2)):
        for e in range(3):
            if e==d: continue
            f=3-d-e
            for pair in combinations(range(sizes[e]),2):
                for singleton in range(sizes[f]):
                    block=set()
                    for long_v in range(q):
                        for pair_v in pair:
                            xyz=[0,0,0]
                            xyz[d]=long_v;xyz[e]=pair_v;xyz[f]=singleton
                            block.add(tuple(xyz))
                    out.append(frozenset(block))
    return set(out)

def check(q):
    vv,nb=adjacency(q);idx={v:i for i,v in enumerate(vv)}
    blocks=partition(q)
    assert len(blocks)==3*q//2
    assert len(set.union(*blocks))==len(vv)
    assert sum(map(len,blocks))==len(vv)
    for p in blocks:
        ix={idx[v] for v in p}
        assert min(len(nb[v]&ix) for v in ix)>=q
    rects=rectangles(q)
    assert len(rects)==3*q*(q+1), (q,len(rects))
    for r in rects:
        inds={idx[v] for v in r}
        assert len(inds)==2*q and min(len(nb[x]&inds) for x in inds)==q
    # Check algebraic optimization over ALL permitted local-neighbour populations.
    for a in range(3):
        for b in range(q):
            for c in range(q):
                k=a+b+c
                if q<=k<=2*q-2:
                    r=k-q+1
                    assert a*a+b*b+c*c <= (q-1)**2+r*r
                    assert k+1+(q*k-a*a-b*b-c*c+1)//2>=2*q
                    if k+1+(q*k-a*a-b*b-c*c+1)//2==2*q:
                        assert k==q and sorted((a,b,c))==[0,1,q-1]
    print('q',q,'blocks',len(blocks),'rectangles',len(rects),'OK')

for q in range(4,15): check(q)
# Independently enumerate ALL small ternary subgraphs (sizes 1..6):
vv,nb=adjacency(3)
allmask=(1<<len(vv))-1
adjmask=[sum(1<<j for j in adj) for adj in nb]
small=0;core6=[]
for k in range(1,7):
    for sub in combinations(range(len(vv)),k):
        mask=sum(1<<i for i in sub)
        if min((adjmask[i]&mask).bit_count() for i in sub)>=3:
            assert k==6
            core6.append(frozenset(vv[i] for i in sub))
        else:
            small+=1
assert set(core6)==rectangles(3), (len(core6),len(rectangles(3)))
print('q=3 exhaustive tested',small+len(core6),'subsets of sizes 1..6; min cores',len(core6),'OK')
print('VERIFY_OK')
