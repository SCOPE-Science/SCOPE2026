"""Exhaustive face and simplicial boundary checks for two matched parts."""
from itertools import combinations
from math import comb


def gf2_rank(columns):
    pivots={}
    for v in columns:
        while v:
            i=v.bit_length()-1
            if i not in pivots:pivots[i]=v;break
            v^=pivots[i]
    return len(pivots)


def homology(k,l,s):
    n=2*k+2*l+s; groups=[list(range(2*k)),list(range(2*k,2*k+2*l))]
    groups.extend([[2*k+2*l+i] for i in range(s)])
    edges={(2*i,2*i+1) for i in range(k+l)}
    for u in range(len(groups)):
        for v in range(u+1,len(groups)):
            edges.update((min(a,b),max(a,b)) for a in groups[u] for b in groups[v])
    triangles=[sum(1<<x for x in t) for t in combinations(range(n),3) if all((min(a,b),max(a,b)) in edges for a,b in combinations(t,2))]
    faces=[f for f in range(1,1<<n) if all((f&t)!=t for t in triangles)]
    layers={}
    for f in faces:layers.setdefault(f.bit_count()-1,[]).append(f)
    ranks={}
    for d in sorted(layers):
        if d==0:continue
        ix={f:i for i,f in enumerate(layers[d-1])}
        cols=[]
        for f in layers[d]:
            col=0
            for i in range(n):
                if f & (1<<i):col^=1<<ix[f^(1<<i)]
            cols.append(col)
        ranks[d]=gf2_rank(cols)
    bettis={d:len(fs)-ranks.get(d,0)-ranks.get(d+1,0)-(d==0) for d,fs in layers.items()}
    return {d:b for d,b in bettis.items() if b},len(faces),len(triangles)


def verify():
    cnt=0;total=0
    for k in (2,3):
        for l in (2,3):
            for s in range(4):
                if 2*k+2*l+s>13:continue
                b,n,t=homology(k,l,s)
                expected={1:comb(s+1,2),k:s+1,l:s+1,k+l-1:1}
                if k==l:expected[k]=2*(s+1)
                assert b=={d:x for d,x in expected.items() if x},(k,l,s,b,expected)
                cnt+=1;total+=n
    print(f'EXHAUSTIVE_BETTI_OK cases={cnt} total_nonempty_faces={total}')
    print('VERIFY_OK')
if __name__=='__main__':verify()
