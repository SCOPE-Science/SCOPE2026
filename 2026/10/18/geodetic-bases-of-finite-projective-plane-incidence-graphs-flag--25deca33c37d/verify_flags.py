"""Independent field-and-flag verification for projective planes of orders 2,3,4,5.
Checks plane axioms, geodesic intervals and all optimal flag-witness overlaps.
Run: python3 verify_flags.py
"""
from itertools import product
from collections import Counter,deque


def field(q):
    if q==4:
        add=lambda a,b:a^b
        def mul(a,b):
            out=0
            while b:
                if b&1:out^=a
                b>>=1;a<<=1
                if a&4:a^=7
            return out
    else:
        add=lambda a,b:(a+b)%q
        mul=lambda a,b:(a*b)%q
    return add,mul


def plane(q):
    add,mul=field(q)
    def inv(x):return next(y for y in range(1,q) if mul(x,y)==1)
    def normalize(x):
        scalar=inv(next(y for y in x if y));return tuple(mul(scalar,y) for y in x)
    vecs=sorted({normalize(t) for t in product(range(q),repeat=3) if any(t)})
    v=len(vecs)
    incid=[[False]*v for _ in range(v)]
    for p,x in enumerate(vecs):
        for l,y in enumerate(vecs):
            s=0
            for a,b in zip(x,y):s=add(s,mul(a,b))
            incid[p][l]=(s==0)
    assert v==q*q+q+1
    for row in incid:assert sum(row)==q+1
    for l in range(v):assert sum(incid[p][l] for p in range(v))==q+1
    for x in range(v):
        for y in range(x+1,v):
            assert sum(incid[x][l] and incid[y][l] for l in range(v))==1
            assert sum(incid[p][x] and incid[p][y] for p in range(v))==1
    return incid


def check(q):
    I=plane(q);v=len(I);n=2*v
    graph=[set() for _ in range(n)]
    for p in range(v):
        for l in range(v):
            if I[p][l]:graph[p].add(v+l);graph[v+l].add(p)
    dist=[]
    for start in range(n):
        d=[-1]*n;d[start]=0;queue=deque([start])
        while queue:
            x=queue.popleft()
            for y in graph[x]:
                if d[y]<0:d[y]=d[x]+1;queue.append(y)
        assert -1 not in d
        dist.append(d)
    intm={}
    for i in range(n):
        for j in range(i+1,n):
            intm[i,j]={k for k in range(n) if dist[i][k]+dist[k][j]==dist[i][j]}
    pairs=[]
    for x in range(v):
        for l in range(v):
            if I[x][l]:
                points={p for p in range(v) if I[p][l] and p!=x}
                lines={v+j for j in range(v) if I[x][j] and j!=l}
                S=frozenset(points|lines)
                cover=set(S)
                for i in S:
                    for j in S:
                        if i<j:cover|=intm[i,j]
                assert len(S)==2*q and len(cover)==n
                pairs.append(((x,l),S))
    assert len(pairs)==v*(q+1)
    assert len({S for _,S in pairs})==len(pairs)
    hist=Counter()
    for i in range(len(pairs)):
        (x,l),S=pairs[i]
        local=Counter()
        for j in range(len(pairs)):
            if i==j:continue
            (y,m),T=pairs[j]
            val=len(S-T)
            if x==y or l==m:assert val==q+1;typ='same'
            elif not I[x][m] and not I[y][l]:assert val==2*q-2;typ='opposite'
            else:assert val==2*q;typ='cross'
            local[typ]+=1
            if i<j:hist[val]+=1
        assert local==Counter({'same':2*q,'opposite':q**3,'cross':2*q*q})
    minmove=min(hist)
    assert minmove==min(q+1,2*q-2)
    for limit, expected in ((minmove-1,1),(minmove,len(pairs))):
        discovered={0};stack=[0]
        while stack:
            i=stack.pop()
            for j in range(len(pairs)):
                if j not in discovered and len(pairs[i][1]-pairs[j][1])<=limit:
                    discovered.add(j);stack.append(j)
        assert len(discovered)==expected
    print('q=',q,'incidence_vertices=',n,'flag_bases=',len(pairs),'pair_distances=',sorted(hist.items()),'threshold=',minmove)

if __name__=='__main__':
    for q in (2,3,4,5):check(q)
    print('ALL FLAG AND INTERVAL CHECKS PASS')
