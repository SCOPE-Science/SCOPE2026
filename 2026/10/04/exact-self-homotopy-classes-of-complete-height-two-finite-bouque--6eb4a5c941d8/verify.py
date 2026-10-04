from itertools import product


def leq(x,y,q):
    if x == y:
        return True
    return x in (0,1) and y >= 2


def maps(q):
    n=q+2
    out=[]
    for f in product(range(n), repeat=n):
        ok=True
        for m in (0,1):
            for c in range(2,n):
                if not leq(f[m], f[c], q):
                    ok=False; break
            if not ok: break
        if ok: out.append(f)
    return out


def essential(f,q):
    return set(f[:2]) == {0,1} and len(set(f[2:])) >= 2


def edge_index(q):
    return {(m,c): i for i,(m,c) in enumerate((m,c) for m in (0,1) for c in range(2,q+2))}


def h1_nonzero(f,q):
    idx=edge_index(q)
    c0=2
    for cj in range(3,q+2):
        vec=[0]*(2*q)
        # z_j = (0,c0) - (1,c0) + (1,cj) - (0,cj)
        for coeff,(u,v) in [(1,(0,c0)),(-1,(1,c0)),(1,(1,cj)),(-1,(0,cj))]:
            a,b=f[u],f[v]
            if a == b:
                continue
            assert a in (0,1) and b >= 2 and leq(a,b,q)
            vec[idx[(a,b)]] += coeff
        if any(vec):
            return True
    return False


def comparable(f,g,q):
    return all(leq(f[i],g[i],q) for i in range(q+2)) or all(leq(g[i],f[i],q) for i in range(q+2))


class DSU:
    def __init__(self,n): self.p=list(range(n)); self.sz=[1]*n
    def find(self,a):
        while self.p[a]!=a:
            self.p[a]=self.p[self.p[a]]; a=self.p[a]
        return a
    def union(self,a,b):
        a,b=self.find(a),self.find(b)
        if a==b:return
        if self.sz[a]<self.sz[b]:a,b=b,a
        self.p[b]=a; self.sz[a]+=self.sz[b]


def check(q):
    fs=maps(q)
    total=2*(q+1)**q+2*q**q+5*q
    ess=2*(q**q-q)
    null=2*(q+1)**q+7*q
    assert len(fs)==total
    flags=[essential(f,q) for f in fs]
    assert sum(flags)==ess
    assert all(h1_nonzero(f,q)==essential(f,q) for f in fs)

    # Essential maps are isolated in the pointwise order.
    for i,f in enumerate(fs):
        if flags[i]:
            for j,g in enumerate(fs):
                if i!=j:
                    assert not comparable(f,g,q)

    # Components of the function-space comparability graph.
    d=DSU(len(fs))
    for i in range(len(fs)):
        for j in range(i+1,len(fs)):
            if comparable(fs[i],fs[j],q): d.union(i,j)
    comps={}
    for i in range(len(fs)):
        comps.setdefault(d.find(i),[]).append(i)
    sizes=sorted((len(v) for v in comps.values()), reverse=True)
    assert len(comps)==1+ess
    assert sizes[0]==null and all(s==1 for s in sizes[1:])
    big=max(comps.values(), key=len)
    assert all(not flags[i] for i in big) and len(big)==sum(not x for x in flags)
    print(f'q={q}: total={total}, essential={ess}, null={null}, classes={1+ess}, H1_nonzero=essential, components=OK')

for q in (2,3,4):
    check(q)
print('VERIFY_OK')
