from itertools import combinations
from collections import Counter
from math import comb


def half_graph(n):
    # vertices 0..n-1 = a_1..a_n, n..2n-1 = b_1..b_n
    N=2*n
    adj=[set() for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i <= j:
                adj[i].add(n+j)
                adj[n+j].add(i)
    return adj


def induced_paths(adj):
    # all unoriented induced paths with at least 2 vertices
    seen=set(); out=[]
    def extend(path):
        if len(path)>=2:
            key=min(tuple(path),tuple(reversed(path)))
            if key not in seen:
                seen.add(key); out.append(tuple(path))
        u=path[-1]
        for v in adj[u]:
            if v in path: continue
            # v may be adjacent only to the last path vertex
            if any(v in adj[w] for w in path[:-1]): continue
            extend(path+[v])
    for s in range(len(adj)):
        extend([s])
    return out


def direct_mp(paths,S):
    S=set(S)
    return all(sum(v in S for v in p)<=2 for p in paths)


def independent(adj,S):
    S=set(S)
    return all(v not in adj[u] for u,v in combinations(S,2))


def theorem(adj,S):
    return len(S)<=2 or independent(adj,S)


def expected_coeffs(n):
    c=[0]*(2*n+1)
    c[0]=1
    c[1]=2*n
    c[2]=comb(2*n,2)
    for k in range(3,n+1):
        c[k]=(k+1)*comb(n,k)
    return c

subsets=0
path_total=0
for n in range(2,9):
    adj=half_graph(n)
    paths=induced_paths(adj)
    assert max(len(p) for p in paths) <= 4
    path_total += len(paths)
    got=Counter()
    max_sets=[]
    for mask in range(1<<(2*n)):
        S=[v for v in range(2*n) if (mask>>v)&1]
        a=direct_mp(paths,S)
        b=theorem(adj,S)
        assert a==b,(n,S,a,b)
        subsets += 1
        if a:
            got[len(S)] += 1
    coeff=[got[k] for k in range(2*n+1)]
    assert coeff==expected_coeffs(n),(n,coeff,expected_coeffs(n))
    mp=max(got)
    assert mp==n
    if n==2:
        assert got[mp]==6
    else:
        assert got[mp]==n+1
        # direct classification of maximum sets as prefixes of B + suffixes of A
        for t in range(n+1):
            S={n+j for j in range(t)} | {i for i in range(t,n)}
            assert len(S)==n and direct_mp(paths,S)
        max_count=0
        for mask in range(1<<(2*n)):
            if mask.bit_count()!=n: continue
            S={v for v in range(2*n) if (mask>>v)&1}
            if direct_mp(paths,S):
                max_count+=1
                # infer cut t from number of B vertices; must equal prefix/suffix form
                t=sum(v>=n for v in S)
                expected={n+j for j in range(t)} | {i for i in range(t,n)}
                assert S==expected,(n,S,expected)
        assert max_count==n+1

print('VERIFY_OK')
print('half_graphs_checked = 7')
print('n_range = 2..8')
print('vertex_subsets_checked =',subsets)
print('induced_paths_generated =',path_total)
print('all induced paths had at most 4 vertices')
print('all direct monophonic-position tests matched: size <= 2 or independent')
print('all cardinality-enumerator coefficients matched')
print('all maximum-set classifications matched')
