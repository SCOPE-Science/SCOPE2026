"""Separate cellwise refinement and binomial-path checks for Ferrers covers."""
from math import comb
from random import Random
from collections import defaultdict


def rand_partition(rng, n):
    parts=[]
    mx=n
    while n:
        x=rng.randint(1,min(mx,n))
        parts.append(x)
        mx=x
        n-=x
    return tuple(parts)


def one(lam):
    verts={(i,j) for i,w in enumerate(lam) for j in range(w)}
    prv={p:tuple(q for q in ((p[0]-1,p[1]),(p[0],p[1]-1)) if q in verts) for p in verts}
    nex={p:tuple(q for q in ((p[0]+1,p[1]),(p[0],p[1]+1)) if q in verts) for p in verts}
    rank=sorted(verts,key=lambda x:(sum(x),x))
    paths={}
    for p in rank:
        paths[p]=1 if p==(0,0) else sum(paths[q] for q in prv[p])
        assert paths[p]==comb(p[0]+p[1],p[0]), (lam,p)
    colours={p:0 for p in verts}
    for step in range(len(verts)+1):
        token={p:(colours[p],tuple(sorted(colours[q] for q in prv[p])),
                  tuple(sorted(colours[q] for q in nex[p]))) for p in verts}
        ids={t:k for k,t in enumerate(sorted(set(token.values())))}
        new={p:ids[token[p]] for p in verts}
        if all(new[p]==colours[p] for p in verts):
            break
        colours=new
    else:
        raise AssertionError('did not stabilize')
    conjugate=tuple(sum(row>j for row in lam) for j in range(lam[0]))
    fibers=defaultdict(set)
    for p,c in colours.items():fibers[c].add(p)
    for same in fibers.values():
        p=next(iter(same))
        expected={p,p[::-1]} if conjugate==lam else {p}
        assert same==expected,(lam,same,expected)
    return len(verts),len(fibers),step


def run():
    rng=Random(20261017)
    suite=[(1,),(2,1),(4,3,1),(4,2,2),(8,8,5,3,1),(10,9,8,7,6,5,4,3,2,1)]
    for n in range(10,130,2):
        suite.extend(rand_partition(rng,n) for _ in range(30))
    total=0
    for lam in suite:
        count,nc,step=one(lam)
        total+=count
    print('INDEPENDENT_PASS', 'shapes',len(suite),'total_cells',total,
          'max_size',max(sum(lam) for lam in suite))

if __name__=='__main__':run()
