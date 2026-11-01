"""Reproduce the cyclic reflection orbit graphs and bounded mod-two checks.
Python >=3.9, standard library only.
"""
from collections import defaultdict
from itertools import combinations

def mu6(ell):
    V={(j,i) for j in range(1,ell+2) for i in range(6)}|{(-1,-1)}
    E=set()
    def edge(a,b):
        if a!=b: E.add(frozenset((a,b)))
    for j in range(1,ell+1):
        for i in range(6):edge((j,i),(j+1,(i+1)%6))
        for i in range(6):edge((j,i),(j+1,(i-1)%6))
    for i in range(6):
        edge((ell+1,i),(ell+1,(i+1)%6));edge((-1,-1),(1,i))
    return V,E

def orbit_graph(ell, kind):
    V,E=mu6(ell); seen=set();orbits=[]
    perm=lambda u: u if u==(-1,-1) else (u[0],(-u[1])%6 if kind=='vertex' else (1-u[1])%6)
    for u in sorted(V):
        if u in seen:continue
        orbit=frozenset((u,perm(u)));seen|=orbit
        if len(orbit)==2 and orbit in E:continue
        orbits.append(orbit)
    F=set()
    for a,b in combinations(range(len(orbits)),2):
        if any(frozenset((u,v)) in E for u in orbits[a] for v in orbits[b]):F.add(frozenset((a,b)))
    return orbits,F

def model(ell,kind):
    if kind=='vertex':
        nodes=range(4);links={(0,1),(1,2),(2,3)};top_allowed=set(nodes)
    else:
        nodes=range(3);links={(0,0),(0,1),(1,2),(2,2)};top_allowed={1}
    v={(j,a) for j in range(1,ell+1) for a in nodes}|{(ell+1,a) for a in top_allowed}|{(-1,-1)}
    E=set()
    def link(u,w):
        if u!=w:E.add(frozenset((u,w)))
    for j in range(1,ell+1):
        for a,b in links:
            if (j,a) in v and (j+1,b) in v:link((j,a),(j+1,b))
            if (j,b) in v and (j+1,a) in v:link((j,b),(j+1,a))
    for a,b in links:
        if a!=b and (ell+1,a) in v and (ell+1,b) in v:link((ell+1,a),(ell+1,b))
    for a in nodes:link((-1,-1),(1,a))
    return v,E

def quotient_labels(orbit,kind):
    if orbit==frozenset({(-1,-1)}):return (-1,-1)
    j=next(iter(orbit))[0]
    base=([{0},{1,5},{2,4},{3}] if kind=='vertex' else [{0,1},{2,5},{3,4}])
    value_set={u[1] for u in orbit}
    return (j,next(i for i,b in enumerate(base) if b==value_set))

def independent_faces(v,E):
    V=sorted(v);n=len(V);con=[0]*n; lookup={x:i for i,x in enumerate(V)}
    for e in E:
        a,b=sorted(lookup[x] for x in e);con[a]|=1<<b;con[b]|=1<<a
    by=defaultdict(list)
    def rec(mask,slots,cnt):
        if mask:by[cnt-1].append(mask)
        while slots:
            bit=slots&-slots;slots^=bit;idx=bit.bit_length()-1
            rec(mask|bit,slots&~con[idx],cnt+1)
    rec(0,(1<<n)-1,0)
    return by

def rank_gf2(columns):
    piv={}
    for v in columns:
        while v:
            p=v.bit_length()-1
            if p in piv:v^=piv[p]
            else:piv[p]=v;break
    return len(piv)

def betti(by):
    rank={};faces={d:len(s) for d,s in by.items()}
    for d in sorted(by):
        if d<1:continue
        low={f:i for i,f in enumerate(by[d-1])}
        cols=[]
        for f in by[d]:
            col=0;v=f
            while v:
                bit=v&-v;v^=bit;col^=1<<low[f^bit]
            cols.append(col)
        rank[d]=rank_gf2(cols)
    return {d:faces[d]-rank.get(d,0)-rank.get(d+1,0) for d in by if faces[d]-rank.get(d,0)-rank.get(d+1,0)}

def check(ell,kind,homology=False):
    o,E=orbit_graph(ell,kind);Q={quotient_labels(x,kind) for x in o}
    assert len(Q)==len(o)
    eQ={frozenset((quotient_labels(o[a],kind),quotient_labels(o[b],kind))) for a,b in (tuple(e) for e in E)}
    V,F=model(ell,kind);assert Q==V,(ell,kind,'nodes',Q^V)
    assert eQ==F,(ell,kind,'edges',eQ^F)
    if homology:
        b=betti(independent_faces(V,F))
        if kind=='edge':
            k=(ell-1)//3
            expected={}
            if ell%3==2:expected={2*k+1:2**(k+1)}
            if ell%3==0:expected={2*(ell//3):2**(ell//3)}
            positive={d:v for d,v in b.items() if d>0}
            assert positive==expected,(ell,b,expected)
        if kind=='vertex':assert all(d==0 for d in b), (ell,b)
        return len(V),sum(len(x) for x in independent_faces(V,F).values()),b
    return len(V),len(F)

def check_fold(ell):
    V,E=model(ell,'edge');a={(j,b) for j,b in V if j!=-1};e={x for x in E if all(t in a for t in x)}
    # The first layer dominates deletion of each third-layer vertex.
    if ell>=3:
        for b in range(3):
            u=(1,b);w=(3,b)
            Nu={next(t for t in f if t!=u) for f in e if u in f}
            Nw={next(t for t in f if t!=w) for f in e if w in f}
            assert Nu<=Nw,(ell,u,w,Nu,Nw)
        # After the third level is removed, the first two levels form a
        # 6-cycle, and the remaining levels are an identically defined tail.
        survivors=a-{(3,b) for b in range(3)}
        preserved={edge for edge in e if all(x in survivors for x in edge)}
        front={(j,b) for j in (1,2) for b in range(3)}
        tail=survivors-front
        assert len(front)==6
        assert not any(len(edge&front)==1 for edge in preserved)
        front_edges={edge for edge in preserved if edge<=front}
        assert len(front_edges)==6
        assert all(sum(x in edge for edge in front_edges)==2 for x in front)
        if ell==3:
            assert tail=={(4,1)} and not any(edge<=tail for edge in preserved)
        else:
            oldV,oldE=model(ell-3,'edge')
            oldV.discard((-1,-1))
            oldE={edge for edge in oldE if (-1,-1) not in edge}
            mappedV={(j+3,b) for j,b in oldV}
            mappedE={frozenset((j+3,b) for j,b in edge) for edge in oldE}
            assert tail==mappedV,(ell,tail^mappedV)
            assert {edge for edge in preserved if edge<=tail}==mappedE,ell
    if ell==2:
        u=(1,1);w=(3,1)
        Nu={next(t for t in f if t!=u) for f in e if u in f}
        Nw={next(t for t in f if t!=w) for f in e if w in f}
        assert Nu==Nw,(ell,Nu,Nw)

if __name__=='__main__':
    for ell in range(1,12):
        for kind in ('vertex','edge'):
            check(ell,kind,False)
        check_fold(ell)
    samples={}
    for ell in range(1,8):
        samples[ell]=check(ell,'edge',True)
    for ell in range(1,4):check(ell,'vertex',True)
    print('VERIFY_OK',samples)
