"""Independent finite checks of girth-five four-cut complexes (Python 3 stdlib only)."""
from itertools import combinations
from collections import Counter
from math import comb
import random


def connected_subset(vs, adj):
    todo={vs[0]}; seen=set()
    S=set(vs)
    while todo:
        x=todo.pop()
        if x in seen: continue
        seen.add(x)
        todo.update((adj[x]&S)-seen)
    return len(seen)==len(S)


def girth_at_least_five(adj):
    n=len(adj)
    for root in range(n):
        dist={root:0}; parent={root:-1}; queue=[root]
        for u in queue:
            for v in adj[u]:
                if v not in dist:
                    dist[v]=dist[u]+1;parent[v]=u;queue.append(v)
                elif parent[u]!=v and dist[u]+dist[v]+1<5:
                    return False
    return True


def construct(n,edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        assert u!=v and 0<=u<n and 0<=v<n
        adj[u].add(v);adj[v].add(u)
    assert girth_at_least_five(adj)
    if n<9: raise ValueError('requires n>=9')
    fours={frozenset(z) for z in combinations(range(n),4) if connected_subset(z,adj)}
    fives={frozenset(z) for z in combinations(range(n),5) if all(frozenset(y) in fours for y in combinations(z,4))}
    # Check the five-sets are precisely the induced pentagons.
    for z in fives:
        assert all(len(adj[v]&z)==2 for v in z)
    for z in combinations(range(n),5):
        z=frozenset(z)
        if all(len(adj[v]&z)==2 for v in z): assert z in fives
    degree_count=sum(comb(len(a),3) for a in adj)+sum((len(adj[u])-1)*(len(adj[v])-1) for u in range(n) for v in adj[u] if u<v)
    assert len(fours)==degree_count,(len(fours),degree_count)
    assert not any(all(frozenset(t) in fives for t in combinations(s,5)) for s in combinations(range(n),6))
    return adj,fours,fives


def collapse(adj,fours,fives):
    n=len(adj)
    active=set(fours)
    removed_triangles=set()
    for Q in sorted(fives,key=lambda x:tuple(sorted(x))):
        tet=min((frozenset(S) for S in combinations(sorted(Q),4)),key=lambda x:tuple(sorted(x)))
        # A 4-set cannot be a face of two 5-simplices (girth >= 5).
        assert sum(tet < Z for Z in fives)==1
        assert tet in active
        active.remove(tet)
    counts=Counter(T for U in active for T in (frozenset(S) for S in combinations(sorted(U),3)))
    steps=[]
    while active:
        available=[(tuple(sorted(U)),tuple(sorted(T)),U,T)
                   for U in active for T in (frozenset(S) for S in combinations(sorted(U),3))
                   if counts[T]==1 and T not in removed_triangles]
        assert available,'no free triangles: collapse failed'
        _,_,U,T=min(available)
        assert counts[T]==1 and T in [frozenset(S) for S in combinations(sorted(U),3)]
        active.remove(U)
        removed_triangles.add(T)
        for S in combinations(sorted(U),3):
            counts[frozenset(S)]-=1
        steps.append((U,T))
    assert len(steps)==len(fours)-len(fives)
    assert len(removed_triangles)==len(steps)
    return steps


def rank_gf2(columns):
    piv={}
    for x in columns:
        while x:
            i=x.bit_length()-1
            if i in piv:x^=piv[i]
            else:piv[i]=x;break
    return len(piv)


def mod_two_homology_x(n,fours,fives):
    fs=[list(map(frozenset,combinations(range(n),k))) for k in (1,2,3)]
    fs += [sorted(fours,key=lambda x:tuple(sorted(x))), sorted(fives,key=lambda x:tuple(sorted(x)))]
    ranks=[]
    for i in range(1,5):
        idx={T:j for j,T in enumerate(fs[i-1])}
        cols=[]
        for U in fs[i]:
            b=0
            for z in combinations(sorted(U),i):b^=1<<idx[frozenset(z)]
            cols.append(b)
        ranks.append(rank_gf2(cols))
    betti=[len(fs[i])-(ranks[i-1] if i else 0)-(ranks[i] if i<len(ranks) else 0) for i in range(5)]
    return betti,ranks


def mod_two_homology_delta(n,adj):
    allbits=(1<<n)-1
    facets=[]
    for U in combinations(range(n),4):
        if not connected_subset(U,adj):
            excluded=sum(1<<u for u in U)
            facets.append(allbits ^ excluded)
    faces={0}
    for F in facets:
        T=F
        while T:
            faces.add(T)
            T=(T-1)&F
    fs=[[T for T in faces if T.bit_count()==k] for k in range(1,n-3)]
    fs=[sorted(s) for s in fs]
    ranks=[]
    for i in range(1,len(fs)):
        ix={F:j for j,F in enumerate(fs[i-1])}
        cols=[]
        for F in fs[i]:
            b=0
            for v in range(n):
                if (F>>v)&1:b^=1<<ix[F ^ (1<<v)]
            cols.append(b)
        ranks.append(rank_gf2(cols))
    betti=[len(fs[i])-(ranks[i-1] if i else 0)-(ranks[i] if i<len(ranks) else 0) for i in range(len(fs))]
    betti[0]-=1
    return betti


def analyze(label,n,edges,direct=True):
    adj,fours,fives=construct(n,edges)
    moves=collapse(adj,fours,fives)
    mu=comb(n-1,3)-len(fours)+len(fives)
    assert mu>=0
    if direct:
        betti,ranks=mod_two_homology_x(n,fours,fives)
        assert betti==[1,0,mu,0,0],(label,betti,mu)
        assert ranks[3]==len(fives) and ranks[2]==len(fours)-len(fives)
        if n<=10:
            primal=mod_two_homology_delta(n,adj)
            assert primal==[mu if i==n-5 else 0 for i in range(n-4)],(label,primal,mu)
    return (label,n,len(edges),len(fours),len(fives),mu,len(moves))


def cycle(n):return [(i,(i+1)%n) for i in range(n)]

def petersen():
    pairs=list(combinations(range(5),2))
    return 10,[(i,j) for i in range(10) for j in range(i+1,10) if not (set(pairs[i])&set(pairs[j]))]

def generalized_petersen(n,k):
    return 2*n,[(i,(i+1)%n) for i in range(n)]+[(i,i+n) for i in range(n)]+[(n+i,n+(i+k)%n) for i in range(n)]


def main():
    examples=[]
    examples.append(('pentagon with four isolated vertices',9,cycle(5)))
    examples.append(('two pentagons sharing a vertex',9,cycle(5)+[(4,5),(5,6),(6,7),(7,8),(8,4)]))
    examples.append(('two disjoint pentagons',10,cycle(5)+[((a+5),(b+5)) for a,b in cycle(5)]))
    examples.append(('pentagon plus five leaves',10,cycle(5)+[(i,i+5) for i in range(5)]))
    examples.append(('pentagon plus pendant chain',12,cycle(5)+[(i,i+1) for i in range(4,11)]))
    examples.append(('nine-cycle',9,cycle(9)))
    examples.append(('twenty-cycle',20,cycle(20)))
    n,e=petersen();examples.append(('Petersen',n,e))
    n,e=generalized_petersen(10,2);examples.append(('dodecahedral',n,e))
    n,e=generalized_petersen(8,3);examples.append(('Mobius-Kantor',n,e))
    checks=[]
    for title,n,e in examples:checks.append(analyze(title,n,e))
    assert next(x for x in checks if x[0]=='Petersen')[3:6]==(70,12,26)
    assert next(x for x in checks if x[0]=='dodecahedral')[3:6]==(140,12,841)
    rng=random.Random(1729)
    good=0
    for n in range(9,15):
        for i in range(130):
            p=rng.uniform(.08,.27)
            e=[(u,v) for u in range(n) for v in range(u+1,n) if rng.random()<p]
            adj=[set() for _ in range(n)]
            for u,v in e:adj[u].add(v);adj[v].add(u)
            if not girth_at_least_five(adj):continue
            checks.append(analyze(f'random_{n}_{i}',n,e,direct=False))
            good+=1
    assert good>=75,good
    print('CUT4_GIRTH_FIVE_ELEMENTARY_COLLAPSE_OK')
    print('named examples',len(examples),'random graph examples',good)
    for row in checks[:len(examples)]:print('graph',*row)
    print('each test independently checked connected four sets, induced five-cycles, degree formula, absence of dual six-faces, and every elementary free-face collapse')
    print('direct dual full mod-two boundary ranks checked for all ten named examples')
    print('direct primal four-cut mod-two boundary ranks checked for each named graph of at most ten vertices')

if __name__=='__main__':main()
