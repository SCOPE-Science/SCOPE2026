"""Reproducible direct-matrix check of Otto classes in bipartite antichain monoids.
Only Python standard library. In all cases every Otto pair is checked against an
independently computed classification. Finite checks are not the general proof.
"""
from collections import Counter, defaultdict
from itertools import product
from math import prod


def field(q):
    if q in (2, 3):
        add=lambda x,y:(x+y)%q
        mul=lambda x,y:(x*y)%q
    elif q==4:
        add=lambda x,y:x^y
        def mul(x,y):
            z=0
            for i in range(2):
                if y&(1<<i): z^=x<<i
            if z&8: z^=0b1100
            if z&4: z^=0b0111
            return z
    else: raise ValueError('supported fields are 2, 3, 4')
    inv={x:next(y for y in range(1,q) if mul(x,y)==1) for x in range(1,q)}
    return add,mul,inv


def run(q, neighbor_sets):
    """neighbor_sets[j] lists minimal-vertex indices covered by maximal j."""
    k=max((u for ns in neighbor_sets for u in ns),default=-1)+1
    m=len(neighbor_sets); n=k+m
    assert k>0 and m>0 and all(tuple(sorted(set(ns)))==tuple(ns) for ns in neighbor_sets)
    add,mul,inv=field(q)
    columns=[list(product(range(q),repeat=1+len(ns))) for ns in neighbor_sets]
    objs=list(product(*columns))
    N=len(objs)
    def matrix(x):
        mat=[[0]*n for _ in range(n)]
        for i in range(k): mat[i][i]=1
        for j,(ns,c) in enumerate(zip(neighbor_sets,x)):
            mat[k+j][k+j]=c[0]
            for u,b in zip(ns,c[1:]): mat[u][k+j]=b
        return tuple(tuple(row) for row in mat)
    mats=[matrix(x) for x in objs]
    idx={mat:i for i,mat in enumerate(mats)}
    assert len(idx)==N
    table=[[None]*N for _ in range(N)]
    for i,a in enumerate(mats):
        for j,b in enumerate(mats):
            c=tuple(tuple(sum((mul(a[r][h],b[h][s]) for h in range(n)),0)%q
                          if q in (2,3) else
                          __import__('functools').reduce(add,(mul(a[r][h],b[h][s]) for h in range(n)),0)
                          for s in range(n)) for r in range(n))
            if c not in idx: raise AssertionError('not closed')
            table[i][j]=idx[c]
    def signature(x):
        tags=[]
        for c in x:
            t,b=c[0],c[1:]
            if t!=1 or not any(b): tags.append(('*',))
            else:
                a=next(z for z in b if z)
                tags.append(('P',)+tuple(mul(inv[a],z) for z in b))
        return tuple(tags)
    signatures=[signature(x) for x in objs]
    # Direct witness search, without assuming or using the coordinate theorem.
    directed=[[any(table[i][g]==table[g][j] for g in range(N))
              for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            actual=directed[i][j] and directed[j][i]
            predicted=signatures[i]==signatures[j]
            if actual!=predicted:
                raise AssertionError((q,neighbor_sets,objs[i],objs[j],actual,predicted))
    blocks=defaultdict(int)
    for sig in signatures: blocks[sig]+=1
    ds=[len(ns) for ns in neighbor_sets]
    ai=[(q**d-1)//(q-1) for d in ds]
    Bi=[1+(q-1)*q**d for d in ds]
    assert len(blocks)==prod(1+a for a in ai)
    assert Counter(blocks.values())==Counter(
        prod((q-1) if sig[j][0]=='P' else Bi[j] for j in range(m))
        for sig in blocks)
    eidx={i for i in range(N) if table[i][i]==i}
    assert len(eidx)==prod(1+q**d for d in ds)
    center=tuple(('*',) for _ in range(m))
    biggest={i for i in range(N) if signatures[i]==center}
    assert eidx<=biggest and len(biggest)==prod(Bi)
    assert (eidx==biggest)==(q==2)
    print('q=%s neighbor_sets=%s elements=%d Otto_classes=%d '
          'class_sizes=%s idempotents=%d idempotent_class=%d PASS' %
          (q,neighbor_sets,N,len(blocks),dict(sorted(Counter(blocks.values()).items())),
           len(eidx),len(biggest)))

if __name__=='__main__':
    tests=[
      (2,((0,),)),(3,((0,),)),(4,((0,),)),
      (2,((0,1),)),(3,((0,1),)),(4,((0,1),)),
      (2,((0,),(1,))), (2,((0,),(0,1))),
      (2,((0,1),(0,1))),(3,((0,),(0,))),
    ]
    for q,ns in tests: run(q,ns)
    print('ALL_EXACT_CHECKS_PASSED')
