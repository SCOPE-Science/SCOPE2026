#!/usr/bin/env python3
"""Exact integral magnitude-homology check for the Tutte--Coxeter graph.

Requires Python 3 and SymPy. This reconstructs the graph, both localized
length-five chain complexes, Smith invariant factors, and the orbit reduction.
"""
from collections import Counter, deque
from itertools import combinations, permutations
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

V = tuple(range(6))
points = list(combinations(V, 2))

def matchings(rem):
    if not rem:
        yield ()
        return
    a = rem[0]
    for b in rem[1:]:
        for other in matchings(tuple(v for v in rem if v not in (a,b))):
            yield tuple(sorted(((a,b),)+other))

lines = sorted(set(matchings(V)))
assert len(points) == len(lines) == 15
p_index = {p:i for i,p in enumerate(points)}
l_index = {line:i+15 for i,line in enumerate(lines)}
adj = [set() for _ in range(30)]
for p,i in p_index.items():
    for line,j in l_index.items():
        if p in line:
            adj[i].add(j); adj[j].add(i)
assert all(len(neighbors) == 3 for neighbors in adj)
assert sum(map(len, adj)) // 2 == 45

dist = []
for a in range(30):
    d = [-1] * 30
    d[a] = 0
    queue = deque([a])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if d[v] < 0:
                d[v] = d[u] + 1
                queue.append(v)
    assert -1 not in d
    dist.append(d)
assert max(max(row) for row in dist) == 4

def girth():
    answer = 100
    for a in range(30):
        for b in adj[a]:
            d = [-1] * 30
            d[a] = 0
            queue = deque([a])
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if {u,v} == {a,b}: continue
                    if d[v] < 0:
                        d[v] = d[u] + 1
                        queue.append(v)
            answer = min(answer, d[b]+1)
    return answer
assert girth() == 8

def chain_tuples(x,z,k,rem=5):
    prefix = [x]
    def grow(left):
        if len(prefix) == k:
            last_distance = dist[prefix[-1]][z]
            if 0 < last_distance == left:
                yield tuple(prefix + [z])
            return
        for v in range(30):
            gap = dist[prefix[-1]][v]
            if 0 < gap < left:
                prefix.append(v)
                yield from grow(left-gap)
                prefix.pop()
    yield from grow(rem)

def boundary(t):
    out = {}
    for i in range(1,len(t)-1):
        if dist[t[i-1]][t[i]] + dist[t[i]][t[i+1]] == dist[t[i-1]][t[i+1]]:
            s = t[:i] + t[i+1:]
            out[s] = out.get(s,0) + (-1)**i
    return {s:v for s,v in out.items() if v}

def matrix(source,target):
    indices = {t:i for i,t in enumerate(target)}
    mat = Matrix.zeros(len(target),len(source))
    for col,t in enumerate(source):
        for s,v in boundary(t).items():
            assert s in indices
            mat[indices[s],col] += v
    return mat

def smith_profile(mat):
    smith = smith_normal_form(mat, domain=ZZ)
    return Counter(abs(int(smith[i,i])) for i in range(min(smith.shape)) if smith[i,i])

def compute_case(x,z):
    C2=list(chain_tuples(x,z,2)); C3=list(chain_tuples(x,z,3)); C4=list(chain_tuples(x,z,4))
    B3 = matrix(C3,C2); B4 = matrix(C4,C3)
    assert B3*B4 == Matrix.zeros(len(C2),len(C4))
    S3, S4 = smith_profile(B3), smith_profile(B4)
    rank3,rank4 = sum(S3.values()), sum(S4.values())
    h3 = len(C3)-rank3-rank4
    if dist[x][z]==1:
        assert (len(C2),len(C3),len(C4),rank3,rank4,h3)==(8,36,56,8,28,0)
        assert S3=={1:8} and S4=={1:28}
    else:
        assert dist[x][z]==3
        assert (len(C2),len(C3),len(C4),rank3,rank4,h3)==(14,45,40,14,27,4)
        assert S3=={1:14} and S4=={1:27}
    print(f'd={dist[x][z]} C2/C3/C4={len(C2)}/{len(C3)}/{len(C4)} ranks={rank3}/{rank4} SNF_B4={dict(S4)} H3=Z^{h3}')

base_point = p_index[(0,1)]
incident = next(l_index[M] for M in lines if (0,1) in M)
nonincident = next(l_index[M] for M in lines if (0,1) not in M)
compute_case(base_point,incident)
compute_case(base_point,nonincident)

# Every permutation of six underlying symbols preserves incidence.
# Check that these symmetries cover both point->line orbit types.
def act_edge(p,perm):
    return tuple(sorted((perm[p[0]],perm[p[1]])))
def act_matching(line,perm):
    return tuple(sorted(act_edge(p,perm) for p in line))
for target in (incident,nonincident):
    starting = (base_point,target)
    orbit = {
        (p_index[act_edge(points[starting[0]],pi)],
         l_index[act_matching(lines[starting[1]-15],pi)])
        for pi in permutations(V)
    }
    expected = 45 if dist[base_point][target]==1 else 180
    assert len(orbit)==expected
    assert all(dist[p][l]==dist[base_point][target] for p,l in orbit)
    print('S6 orbit',dist[base_point][target],len(orbit),'ordered point-to-line pairs')

# Bipartite parity makes same-side endpoints impossible for odd length five.
assert all(not list(chain_tuples(i,j,k))
           for k in (2,3,4) for i in (0,15) for j in range(15) if i<15)
assert all(not list(chain_tuples(i,j,k))
           for k in (2,3,4) for i in (0,15) for j in range(15,30) if i>=15)
assert 2*180*4==1440
print('PASS: integral MH_(3,5) = Z^1440; all relevant Smith factors are units')
