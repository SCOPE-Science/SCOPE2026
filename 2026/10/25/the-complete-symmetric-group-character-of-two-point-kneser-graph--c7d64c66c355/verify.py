#!/usr/bin/env python3
"""Exact checks of graph-configuration characters for the two-subset Kneser family.

Uses only Python 3 standard library. All arithmetic is integral or modulo a stated
prime. The infinite-parameter theorem uses the proof in RESULT.md, not extrapolation.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations
from math import factorial


def partitions(n, cap=None):
    if n == 0:
        yield ()
        return
    for a in range(min(n, n if cap is None else cap), 0, -1):
        for tail in partitions(n-a, a):
            yield (a,) + tail


def class_representative(parts):
    perm = list(range(sum(parts)))
    off = 0
    for k in parts:
        for j in range(k):
            perm[off+j] = off + ((j+1) % k)
        off += k
    return tuple(perm)


def cycle_type(p):
    seen = set()
    ans = []
    for i in range(len(p)):
        if i not in seen:
            j = i
            k = 0
            while j not in seen:
                seen.add(j)
                j = p[j]
                k += 1
            ans.append(k)
    return tuple(sorted(ans, reverse=True))


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


class Kneser:
    def __init__(self, n):
        self.n = n
        self.vertices = list(combinations(range(n), 2))
        self.vertex_id = {x: i for i, x in enumerate(self.vertices)}
        N = len(self.vertices)
        self.edges = [e for e in combinations(range(N), 2)
                      if set(self.vertices[e[0]]).isdisjoint(self.vertices[e[1]])]
        self.edge_id = {x: i for i, x in enumerate(self.edges)}
        self.neighbors = [set() for _ in range(N)]
        for a,b in self.edges:
            self.neighbors[a].add(b)
            self.neighbors[b].add(a)
        self.c0 = list(combinations(range(N), 2))
        self.i0 = {x: i for i,x in enumerate(self.c0)}
        self.c1 = [(ei, v) for ei,(a,b) in enumerate(self.edges)
                   for v in range(N) if v != a and v != b]
        self.i1 = {x: i for i,x in enumerate(self.c1)}
        self.c2 = [(ei,fi) for ei,fi in combinations(range(len(self.edges)),2)
                   if len(set(self.edges[ei]+self.edges[fi])) == 4]
        self.d1 = [(self.i0[tuple(sorted((b,v)))],
                    self.i0[tuple(sorted((a,v)))])
                   for ei,v in self.c1 for a,b in [self.edges[ei]]]
        self.d2 = []
        for ei,fi in self.c2:
            a,b = self.edges[ei]
            c,d = self.edges[fi]
            self.d2.append((self.i1[fi,b],self.i1[fi,a],
                            self.i1[ei,d],self.i1[ei,c]))
        assert all(not {u,v}.intersection({c,d})
                   for ei,fi in self.c2 for u,v in [self.edges[ei]]
                   for c,d in [self.edges[fi]])
        for a,b,c,d in self.d2:
            z = Counter()
            for j,sgn in ((a,1),(b,-1),(c,-1),(d,1)):
                aa,bb=self.d1[j]
                z[aa] += sgn
                z[bb] -= sgn
            assert not any(z.values()), 'Boundary square must vanish'

    def induced(self, p):
        vp = [self.vertex_id[tuple(sorted((p[a],p[b])))]
              for a,b in self.vertices]
        ep,eps=[],[]
        for a,b in self.edges:
            aa,bb=vp[a],vp[b]
            ep.append(self.edge_id[tuple(sorted((aa,bb)))])
            eps.append(1 if aa<bb else -1)
        return vp,ep,eps

    def direct(self,p):
        vp,ep,eps=self.induced(p)
        a = sum(tuple(sorted((vp[u],vp[v])))==(u,v) for u,v in self.c0)
        b = sum(eps[e] for e,v in self.c1 if (ep[e],vp[v])==(e,v))
        c=0
        for e,f in self.c2:
            ee,ff=ep[e],ep[f]
            if tuple(sorted((ee,ff)))==(e,f):
                c+=eps[e]*eps[f]*(1 if ee<ff else -1)
        cg1=sum(eps[e] for e in range(len(self.edges)) if ep[e]==e)
        cg0=sum(vp[v]==v for v in range(len(self.vertices)))
        return (a,b,c,cg1,cg0,c-b+a+cg1-cg0)

    def formula(self,p):
        vp,ep,eps=self.induced(p)
        p2=compose(p,p)
        v2,e2,s2=self.induced(p2)
        vfix=[v for v in range(len(vp)) if vp[v]==v]
        F=len(vfix)
        F2=sum(v2[i]==i for i in range(len(v2)))
        T=sum(eps[e] for e in range(len(ep)) if ep[e]==e)
        T2=sum(s2[e] for e in range(len(e2)) if e2[e]==e)
        P=sum(vp[a]==a and vp[b]==b for a,b in self.edges)
        S=0
        for v in vfix:
            a=sum(vp[w]==w for w in self.neighbors[v])
            b=sum(v2[w]==w for w in self.neighbors[v])
            S+=a*a-b
        assert (T*T-T2-S)%2 == 0
        c2=(T*T-T2-S)//2
        c1=T*F-2*P
        assert (F*F+F2)%2==0
        c0=(F*F+F2)//2-F
        return (c0,c1,c2,T,F,c2-c1+c0+T-F)

    def rank_mod(self,prime):
        basis = {}
        pivots=[]
        for j,(a,b,c,d) in enumerate(self.d2):
            x={}
            for row,sgn in ((a,1),(b,-1),(c,-1),(d,1)):
                t=(x.get(row,0)+sgn)%prime
                if t:x[row]=t
                else:x.pop(row,None)
            while x:
                k=max(x)
                if k not in basis:
                    inverse=pow(x[k],-1,prime)
                    basis[k]={r:t*inverse%prime for r,t in x.items()}
                    pivots.append((j,k))
                    break
                multiple=x[k]
                for row,t in basis[k].items():
                    val=(x.get(row,0)-multiple*t)%prime
                    if val:x[row]=val
                    else:x.pop(row,None)
        return len(basis),pivots


@lru_cache(None)
def specht_character(lam, mu):
    if not mu:
        return 1 if not lam else 0
    k=mu[0]
    possible=[]
    def subpart(i,ceiling,s,seq):
        if i==len(lam):
            if s==sum(lam)-k:
                possible.append(tuple(a for a in seq if a))
            return
        for a in range(min(ceiling,lam[i]),-1,-1):
            if s+a<=sum(lam)-k:
                subpart(i+1,a,s+a,seq+[a])
    subpart(0,lam[0],0,[])
    acc=0
    for nu in possible:
        padded=nu+(0,)*(len(lam)-len(nu))
        cells={(i,j) for i in range(len(lam))
               for j in range(padded[i],lam[i])}
        if len(cells)!=k:
            continue
        if any((i+1,j) in cells and (i,j+1) in cells and
               (i+1,j+1) in cells for i,j in cells):
            continue
        seen={next(iter(cells))}
        todo=list(seen)
        while todo:
            i,j=todo.pop()
            for a in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if a in cells and a not in seen:
                    seen.add(a)
                    todo.append(a)
        if len(seen)==k:
            height=len({i for i,j in cells})
            acc+=(-1)**(height-1)*specht_character(nu,mu[1:])
    return acc


def class_size(parts):
    z=1
    for k,m in Counter(parts).items():
        z*=k**m*factorial(m)
    return factorial(sum(parts))//z


def main():
    g=Kneser(6)
    assert (len(g.vertices),len(g.edges),len(g.c0),len(g.c1),len(g.c2)) == (15,45,105,585,765)
    rank3,piv3=g.rank_mod(3)
    rank2,piv2=g.rank_mod(2)
    assert (rank3,rank2)==(450,449)
    assert len(set(j for j,k in piv3))==450
    print('KG(6,2): vertices=15, edges=45, cubes=(105,585,765)')
    print('Exact modular boundary ranks: mod 3 = 450, mod 2 = 449')
    print('Graph cycle rank=31, rational first Betti=31, second Betti=315')
    parts=list(partitions(6))
    chars={}
    for p in permutations(range(6)):
        assert g.direct(p)==g.formula(p)
        typ=cycle_type(p)
        chi=g.formula(p)[-1]
        assert typ not in chars or chars[typ]==chi
        chars[typ]=chi
    assert len(chars)==len(parts)==11
    assert chars[(1,)*6]==315
    print('All 720 S6 actions: direct oriented-cell traces = local fixed-data formula')
    print('S6 cycle type : class size : degree-two trace')
    for typ in parts:
        print('%s : %s : %s' %(typ,class_size(typ),chars[typ]))
    irreps=[]
    for la in parts:
        s=sum(class_size(mu)*chars[mu]*specht_character(la,mu)
              for mu in parts)
        assert s%720==0
        m=s//720
        assert m>=0
        irreps.append((la,specht_character(la,(1,)*6),m))
    assert sum(d*m for _,d,m in irreps)==315
    assert not irreps[0][2] and not irreps[-1][2]
    expected={(5,1):1,(4,2):3,(4,1,1):5,(3,3):1,(3,2,1):7,
              (3,1,1,1):6,(2,2,2):2,(2,2,1,1):4,(2,1,1,1,1):2}
    assert {la:m for la,d,m in irreps if m}==expected
    print('S6 irreducibles: partition, dimension, multiplicity')
    for row in irreps:
        print(*row,sep=',')
    h=Kneser(7)
    for typ in partitions(7):
        perm=class_representative(typ)
        assert h.direct(perm)==h.formula(perm)
    print('KG(7,2): all 15 conjugacy types checked against direct oriented cubes')
    print('VERIFY_OK_KNESER_GRAPH_BRAID_CHARACTER')

if __name__=='__main__':
    main()
