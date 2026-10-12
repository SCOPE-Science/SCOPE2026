#!/usr/bin/env python3
"""Self-contained exact edge-open-packing check for two cubic incidence graphs."""
from collections import Counter
from itertools import combinations, permutations, product


def heawood():
    # Point p and line-normal ell correspond to nonzero vectors in F_2^3.
    # A point lies on a line precisely when their binary dot product is zero.
    return 14, {(p, 7 + ell) for p in range(7) for ell in range(7)
                if (((p + 1) & (ell + 1)).bit_count() % 2 == 0)}


def desargues():
    # Bipartite inclusion graph on the 2- and 3-subsets of a five-set.
    twos = list(combinations(range(5), 2))
    threes = list(combinations(range(5), 3))
    return 20, {(i, 10 + j) for i, a in enumerate(twos)
                for j, b in enumerate(threes) if set(a) <= set(b)}


def adjacency(n, edges):
    adj = [set() for _ in range(n)]
    E = sorted((min(a,b), max(a,b)) for a,b in edges)
    for a,b in E:
        adj[a].add(b)
        adj[b].add(a)
    assert len(E) == 3*n//2 and all(len(x)==3 for x in adj)
    return E, adj


def compatible(E, adj):
    # Two selected edges are compatible exactly when no distinct third edge
    # joins any endpoint of the first to any endpoint of the second.
    C = [set() for _ in E]
    for i, e in enumerate(E):
        for j in range(i+1, len(E)):
            f = E[j]
            for a in e:
                for b in f:
                    if a != b and b in adj[a] and (min(a,b),max(a,b)) not in (e, f):
                        break
                else:
                    continue
                break
            else:
                C[i].add(j)
                C[j].add(i)
    assert all(i not in C[i] for i in range(len(E)))
    assert all((j in C[i]) == (i in C[j]) for i in range(len(E)) for j in range(len(E)))
    return C


def maximal_cliques(C):
    # Bron--Kerbosch with pivot: each maximal clique is returned exactly once.
    found = []
    def recur(R,P,X):
        if not P and not X:
            found.append(tuple(sorted(R)))
            return
        u = max(P|X,key=lambda u: len(P & C[u])) if P|X else None
        for v in sorted(P - (C[u] if u is not None else set())):
            recur(R|{v},P & C[v],X & C[v])
            P.remove(v)
            X.add(v)
    recur(set(),set(range(len(C))),set())
    assert len(set(found)) == len(found)
    return found


def component_sizes(n,E,chosen):
    active=set()
    graph={}
    for i in chosen:
        a,b=E[i]
        active.update([a,b])
        graph.setdefault(a,set()).add(b)
        graph.setdefault(b,set()).add(a)
    components=[]
    while active:
        u=min(active);pending=[u];seen={u}
        while pending:
            for v in graph[pending.pop()]:
                if v not in seen:
                    seen.add(v);pending.append(v)
        active-=seen
        numedges=sum(len(graph[v]) for v in seen)//2
        degree_sequence=tuple(sorted((len(graph[v]) for v in seen),reverse=True))
        assert degree_sequence==(numedges,)+(1,)*numedges
        components.append(numedges)
    return tuple(sorted(components))


def heawood_automorphisms():
    # Invertible binary maps on points induce inverse-transpose maps on lines.
    autos=[]
    for a,b,c in product(range(8), repeat=3):
        def mapvec(v):
            return ((v&1 and a or 0) ^ (v&2 and b or 0) ^ (v&4 and c or 0))
        p=[mapvec(v) for v in range(1,8)]
        if set(p)!=set(range(1,8)):continue
        line=[]
        for ell in range(1,8):
            eligible=[z for z in range(1,8) if all(((v&ell).bit_count()&1)==((mapvec(v)&z).bit_count()&1) for v in range(1,8))]
            assert len(eligible)==1
            line.append(eligible[0])
        regular=tuple([v-1 for v in p]+[7+v-1 for v in line])
        dual=tuple([x+7 if x<7 else x-7 for x in regular])
        autos.extend((regular,dual))
    assert len(autos)==336 and len(set(autos))==336
    return autos


def desargues_automorphisms():
    twos=list(combinations(range(5),2))
    threes=list(combinations(range(5),3))
    lookup={frozenset(s):i for i,s in enumerate(twos+threes)}
    ans=[]
    universe=set(range(5))
    for perm in permutations(range(5)):
        for dual in (False,True):
            m=[]
            for s in twos+threes:
                s2={perm[x] for x in s}
                if dual:s2=universe-s2
                m.append(lookup[frozenset(s2)])
            ans.append(tuple(m))
    assert len(ans)==240 and len(set(ans))==240
    return ans


def optimal_orbit(E, chosen, vertex_automorphisms):
    look={e:i for i,e in enumerate(E)}
    images=set()
    for f in vertex_automorphisms:
        curr=[]
        for i in chosen:
            a,b=E[i]
            curr.append(look[(min(f[a],f[b]), max(f[a],f[b]))])
        images.add(tuple(sorted(curr)))
    return images


def independent_fixed_size_count(C, k):
    # Separate non-pivot clique recursion, independent of maximal-clique search.
    ct=0
    def extend(P, s):
        nonlocal ct
        if s==k:
            ct+=1
            return
        while len(P)>=k-s:
            v=P[0];P=P[1:]
            extend([u for u in P if u in C[v]],s+1)
    extend(list(range(len(C))),0)
    return ct


def run(name,builder,auto_builder,required,number,component,expected_hist):
    n,raw=builder();E,adj=adjacency(n,raw);C=compatible(E,adj)
    maxima=maximal_cliques(C)
    hist=dict(sorted(Counter(map(len,maxima)).items()))
    assert hist==expected_hist,(name,hist)
    largest=max(hist)
    opts={x for x in maxima if len(x)==largest}
    assert largest==required and len(opts)==number
    assert all(component_sizes(n,E,t)==component for t in opts)
    assert largest == n//2-1 # divisibility-bound sharpness; n=14 or 20.
    fixed=independent_fixed_size_count(C,largest)
    assert fixed==number,(name,fixed)
    aut=auto_builder()
    assert all((min(f[a],f[b]),max(f[a],f[b])) in raw for f in aut for a,b in E)
    orbit=optimal_orbit(E,min(opts),aut)
    assert orbit==opts,(name,len(orbit),len(opts))
    example=tuple(E[i] for i in min(opts))
    print(name)
    print('  vertices',n,'edges',len(E),'maximal-clique histogram',hist)
    print('  maximum edge-open-packing size',largest,'number',len(opts))
    print('  exact independent fixed-size count',fixed)
    print('  selected-star edge multiplicities',component)
    print('  automorphisms tested',len(aut),'one-orbit size',len(orbit))
    print('  witness edges',example)


if __name__=='__main__':
    run('Heawood',heawood,heawood_automorphisms,6,14,(2,2,2),{3:14,6:14})
    run('Desargues',desargues,desargues_automorphisms,9,20,(2,2,2,3),{5:132,6:105,8:30,9:20})
    print('ALL_CHECKS_PASSED')
