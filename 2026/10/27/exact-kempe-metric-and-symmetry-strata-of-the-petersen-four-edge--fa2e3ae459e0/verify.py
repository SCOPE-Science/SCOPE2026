"""Exact, standard-library certificate for the 4-edge-coloring Kempe graph of Petersen graph.
Run with Python 3.9+: python verify.py. All instances are fully enumerated.
"""
from collections import Counter, deque
from itertools import combinations

N=5
EDGES=sorted({tuple(sorted((a,b))) for i in range(N) for a,b in ((i,(i+1)%N),(i,N+i),(N+i,N+(i+2)%N))})
assert len(EDGES)==15
incident=[set() for _ in range(10)]
for e,(a,b) in enumerate(EDGES):
    incident[a].add(e);incident[b].add(e)
edge_neighbours=[(incident[a]|incident[b])-{e} for e,(a,b) in enumerate(EDGES)]


def canonical(coloring):
    ren={};out=[]
    for c in coloring:
        if c not in ren:ren[c]=len(ren)
        out.append(ren[c])
    return tuple(out)


def enumerate_states():
    """Canonical-first-occurrence branching; exactly one state per S4-color orbit."""
    current=[-1]*len(EDGES);found=[]
    def visit(k,largest):
        if k==len(EDGES):
            found.append(tuple(current));return
        for c in range(min(3,largest+1)+1):
            if not any(current[j]==c for j in edge_neighbours[k]):
                current[k]=c
                visit(k+1,max(largest,c))
                current[k]=-1
    visit(0,-1)
    return found


def enumerate_fixed_star():
    """Independent enumeration after fixing a vertex star to colors 0,1,2.

    All four colors must occur, and S4 acts freely on four used colors, so
    each orbit admits exactly one representative with first star fixed
    after using all global color relabelings. Normalization therefore
    checks the entire canonical enumeration independently.
    """
    star=sorted(incident[0]);assert len(star)==3
    cur=[-1]*15
    for e,c in zip(star,(0,1,2)):cur[e]=c
    rest=[e for e in range(15) if e not in star]
    got=set();labeled_count=[0]
    def visit(k):
        if k==len(rest):
            labeled_count[0]+=1
            got.add(canonical(cur))
            return
        e=rest[k]
        for c in range(4):
            if all(cur[f]!=c for f in edge_neighbours[e]):
                cur[e]=c;visit(k+1);cur[e]=-1
    visit(0)
    return got,labeled_count[0]


def edge_kempe_successors(s):
    """Kempe components in the line graph of edges."""
    result=set()
    for c,d in combinations(range(4),2):
        unseen={e for e in range(15) if s[e]==c or s[e]==d}
        while unseen:
            a=unseen.pop();component={a};q=[a]
            for e in q:
                for f in edge_neighbours[e]&unseen:
                    unseen.remove(f);component.add(f);q.append(f)
            t=list(s)
            for e in component:t[e]=c+d-t[e]
            result.add(canonical(t))
    result.discard(s)
    return result


def vertex_kempe_successors(s):
    """Independent Kempe component traversal through vertices, not edges."""
    result=set()
    for c,d in combinations(range(4),2):
        unseen={e for e in range(15) if s[e] in (c,d)}
        while unseen:
            e=unseen.pop();seen={e};q=deque([e])
            while q:
                f=q.popleft();a,b=EDGES[f]
                for v in (a,b):
                    for j in incident[v]:
                        if j in unseen:
                            unseen.remove(j);seen.add(j);q.append(j)
            t=list(s)
            for f in seen:
                t[f]=d if t[f]==c else c
            result.add(canonical(t))
    result.discard(s)
    return result


def all_automorphisms():
    neighbors=[set() for _ in range(10)]
    for a,b in EDGES:
        neighbors[a].add(b);neighbors[b].add(a)
    result=[]
    def rec(mapping,used):
        if len(mapping)==10:
            result.append(tuple(mapping[v] for v in range(10)));return
        u=max((i for i in range(10) if i not in mapping),key=lambda v:(len(neighbors[v]&mapping.keys()),-v))
        for image in range(10):
            if image in used:continue
            if all((u in neighbors[v])==(image in neighbors[mapping[v]]) for v in mapping):
                mapping[u]=image;used.add(image)
                rec(mapping,used)
                used.remove(image);del mapping[u]
    rec({},set())
    return result


def main():
    states=enumerate_states()
    assert len(states)==2080 and len(set(states))==2080
    assert all(len(set(s))==4 for s in states)
    by_star,nstar=enumerate_fixed_star()
    assert len(by_star)==2080 and by_star==set(states),(nstar,len(by_star))
    assert nstar==2080, nstar # one normalized representative per color permutation orbit
    index={s:i for i,s in enumerate(states)}
    adjacency=[]
    for s in states:
        a=edge_kempe_successors(s)
        assert a==vertex_kempe_successors(s)
        assert a<=index.keys()
        adjacency.append({index[t] for t in a})
    assert all(i not in adj and all(i in adjacency[j] for j in adj) for i,adj in enumerate(adjacency))
    degree=Counter(map(len,adjacency))
    assert degree==Counter({12:1840,13:240}),degree
    assert sum(map(len,adjacency))//2==12600
    eccentricities=[]
    for i in range(len(states)):
        distances=[-1]*len(states);distances[i]=0;q=deque([i])
        while q:
            v=q.popleft()
            for w in adjacency[v]:
                if distances[w]==-1:
                    distances[w]=distances[v]+1;q.append(w)
        assert -1 not in distances
        eccentricities.append(max(distances))
    ecc=Counter(eccentricities)
    assert ecc==Counter({5:60,6:1860,7:160}),ecc
    automorphisms=all_automorphisms()
    assert len(automorphisms)==120
    edge_map={e:i for i,e in enumerate(EDGES)}
    perms=[]
    for aut in automorphisms:
        p=[edge_map[tuple(sorted((aut[u],aut[v])))] for u,v in EDGES]
        assert len(set(p))==15
        perms.append(p)
    pending=set(range(2080));orbit_ecc=Counter()
    while pending:
        v=min(pending);s=states[v]
        orbit=set()
        for perm in perms:
            transformed=[-1]*15
            for k,dk in enumerate(perm): transformed[dk]=s[k]
            orbit.add(index[canonical(transformed)])
        assert orbit<=pending and len({eccentricities[w] for w in orbit})==1
        pending-=orbit
        orbit_ecc[(len(orbit),eccentricities[v])]+=1
    expected=Counter({(20,6):1,(40,6):1,(40,7):1,(60,5):1,(60,6):2,(120,6):14,(120,7):1})
    assert orbit_ecc==expected,(orbit_ecc,expected)
    assert sum(orbit_ecc.values())==21
    print('VERIFY_OK: canonical states=2080, fixed-star states=2080, four colors used')
    print('VERIFY_OK: Kempe moves agree under edge/vertex component traversals')
    print('VERIFY_OK: undirected edges=12600, degree profile=',sorted(degree.items()))
    print('VERIFY_OK: radius=5, diameter=7, eccentricity profile=',sorted(ecc.items()))
    print('VERIFY_OK: graph automorphism order=120; state orbit count=21; orbit-ecc=',sorted(orbit_ecc.items()))


if __name__=='__main__':
    main()
