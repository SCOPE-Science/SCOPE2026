"""Independent check from nine incidence triples, set signatures, and factor graph."""
from itertools import combinations
from collections import Counter, deque

# Points p0..p8, lines l0..l8. Each triple lists the points of one line.
LINES = ((0,8,2), (0,1,6), (1,2,7), (2,3,5), (3,4,0),
         (4,5,1), (5,6,8), (6,7,3), (7,8,4))
P = list(range(9)); L = list(range(9,18)); V = P + L
neighbors = {v: set() for v in V}
for j,line in enumerate(LINES):
    for p in line:
        neighbors[p].add(j+9); neighbors[j+9].add(p)
assert len({tuple(sorted(neighbors[v])) for v in V})==18
assert all(len(neighbors[v])==3 for v in V)
# Explicit isomorphism with the usual 18-cycle LCF presentation:
# point p_i corresponds to vertex 2i+1, line l_j to vertex 2j.
shifts=(5,7,-7,7,-7,-5)*3
edges=set()
for v in range(18):
    for w in ((v+1)%18,(v-1)%18,(v+shifts[v])%18):
        edges.add(frozenset((v,w)))
assert edges=={frozenset((2*i+1,2*j)) for j,line in enumerate(LINES) for i in line}


def check(C, kind):
    if kind == 'LD':
        targets = [v for v in V if v not in C]
        vectors = [frozenset(neighbors[v]&C) for v in targets]
    elif kind == 'ID':
        vectors = [frozenset((neighbors[v]|{v}) & C) for v in V]
    else:
        vectors = [frozenset(neighbors[v] & C) for v in V]
    return all(vectors) and len(vectors) == len(set(vectors))


def find_first(kind):
    for k in range(19):
        codes = [frozenset(t) for t in combinations(V,k) if check(set(t),kind)]
        if codes:
            return k,codes
    assert False


def make_graph(C):
    index={c:i for i,c in enumerate(C)}
    H=[set() for c in C]
    for i,c in enumerate(C):
        for a in c:
            t=c-{a}
            for b in V:
                if b not in c:
                    j=index.get(t|{b})
                    if j is not None and i!=j:
                        H[i].add(j)
    return H


def dfs_components(H):
    seen=set();out=[]
    for i in range(len(H)):
        if i not in seen:
            q=[i];seen.add(i);n=0
            while q:
                u=q.pop();n+=1
                for v in H[u]:
                    if v not in seen:seen.add(v);q.append(v)
            out.append(n)
    return sorted(out,reverse=True)


def bfs(H,a):
    dist={a:0};q=deque([a])
    while q:
        v=q.popleft()
        for w in H[v]:
            if w not in dist:dist[w]=dist[v]+1;q.append(w)
    return dist


def main():
    answers={}
    for kind in ('LD','ID','OLD'):
        k,C=find_first(kind)
        H=make_graph(C)
        answers[kind]=(k,len(C),sum(len(x) for x in H)//2,dfs_components(H))
        print(kind,answers[kind])
        if kind=='LD':
            assert len(C)==18 and all(len(neighbors[v]&c)==0 for c in C for v in c)
        if kind=='ID':
            # No exchange ever crosses between the two strict-majority point classes.
            groups=[frozenset(i for i,c in enumerate(C) if len(c & set(P))<=4),
                    frozenset(i for i,c in enumerate(C) if len(c & set(P))>=5)]
            assert list(map(len,groups))==[514,514]
            assert all(not(H[i] & groups[1]) for i in groups[0])
            assert all(len(bfs(H,min(g)))==514 for g in groups)
            print('ID partition counts',dict(sorted(Counter(len(c & set(P)) for c in C).items())))
        if kind=='OLD':
            # In a bipartite graph the nonempty open signatures of its two sides
            # are disjoint. Thus every OLD set is one side-choice plus the other.
            Fp=[frozenset(a) for a in combinations(P,5) if all((neighbors[v]&set(a)) for v in L) and len({frozenset(neighbors[v]&set(a)) for v in L})==9]
            Fl=[frozenset(a) for a in combinations(L,5) if all((neighbors[v]&set(a)) for v in P) and len({frozenset(neighbors[v]&set(a)) for v in P})==9]
            assert len(Fp)==len(Fl)==45
            # An explicit point-line duality of this incidence structure.
            alpha=(0,3,4,8,6,5,2,7,1)
            beta=(0,2,3,4,8,5,1,7,6)
            assert all(((i in line) == (beta[j] in LINES[alpha[i]]))
                       for j,line in enumerate(LINES) for i in P)
            assert set(Fl)=={frozenset(9+alpha[i] for i in f) for f in Fp}
            # The 5-point sets admit only four incidence patterns; exactly
            # two patterns give nine distinct nonempty line signatures.
            patterns=Counter()
            goodpatterns=Counter()
            for points in combinations(P,5):
                ss=set(points)
                occup=tuple(sum(len(ss&set(line))==r for line in LINES) for r in range(4))
                patterns[occup]+=1
                if frozenset(ss) in Fp:goodpatterns[occup]+=1
            assert patterns==Counter({(1,2,5,1):54,(0,4,4,1):27,(0,5,2,2):27,(0,3,6,0):18})
            assert goodpatterns==Counter({(0,5,2,2):27,(0,3,6,0):18})
            assert set(C)=={a|b for a in Fp for b in Fl}
            Efp=[{j for j,t in enumerate(Fp) if len(s&t)==4} for s in Fp]
            Efl=[{j for j,t in enumerate(Fl) if len(s&t)==4} for s in Fl]
            assert sum(map(len,Efp))//2 == sum(map(len,Efl))//2 ==153
            assert dfs_components(Efp)==dfs_components(Efl)==[45]
            ecc=Counter(max(bfs(Efp,i).values()) for i in range(45))
            assert dict(ecc)=={3:27,4:18}
            assert Counter(max(bfs(Efl,i).values()) for i in range(45))==ecc
            assert all(len(Efp[i])==(6 if sum(len(set(LINES[j])&set(s))==3 for j in range(9))==2 else 8)
                       for i,s in enumerate(Fp))
            assert Counter(map(len,Efp))==Counter({6:27,8:18})
            # Each factor move changes exactly one selected side; no mixed move.
            assert sum(map(len,H))//2 == 45*153*2
            for c,ns in zip(C,H):
                assert all((len(c & C[j])==9 and ((c&set(P)) == (C[j]&set(P)) or (c&set(L))==(C[j]&set(L)))) for j in ns)
            print('OLD factor', 'vertices',len(Fp),'edges',153,'eccentricities',dict(sorted(ecc.items())))
    assert answers=={
     'LD':(6,18,0,[1]*18),
     'ID':(9,1028,3780,[514,514]),
     'OLD':(10,2025,13770,[2025])}
    print('ALL_INCIDENCE_CHECKS_PASS')

if __name__=='__main__':main()
