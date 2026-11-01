"""Exact rational Aut(Pappus)-homology character and two full Lefschetz checks.
Only Python standard library required. Run: python3 verify_pappus_character.py
"""
from collections import Counter, defaultdict
from math import lcm

N = 18
JUMPS = (5, 7, -7, 7, -7, -5) * 3
E = {tuple(sorted((i, (i + 1) % N))) for i in range(N)}
E |= {tuple(sorted((i, (i + s) % N))) for i, s in enumerate(JUMPS)}
E = sorted(E)
assert len(E) == 27
A = [0] * N
for u,v in E:
    A[u] |= 1 << v
    A[v] |= 1 << u
assert all(x.bit_count() == 3 for x in A)
EDGE_IDS = {e: i for i,e in enumerate(E)}
V_MASKS = [(1<<u) | (1<<v) for u,v in E]


def find_automorphisms():
    out = []
    def explore(partial, used):
        if len(partial) == N:
            out.append(tuple(partial[i] for i in range(N)))
            return
        # Every extension preserves adjacency AND non-adjacency to the mapped vertices.
        v = max((u for u in range(N) if u not in partial),
                key=lambda u: sum(bool(A[u] & (1 << j)) for j in partial))
        for w in range(N):
            if (used >> w) & 1:
                continue
            if all(bool(A[v] & (1<<x)) == bool(A[w] & (1<<y))
                   for x,y in partial.items()):
                partial[v] = w
                explore(partial, used | (1<<w))
                del partial[v]
    explore({}, 0)
    assert len(out) == 216 and len(set(out)) == 216
    return out


def graph_edge_permutation(p):
    return tuple(EDGE_IDS[tuple(sorted((p[u],p[v])))] for u,v in E)


def order(p):
    cyc = cycle_lengths(p)
    x = 1
    for c in cyc: x = lcm(x,c)
    return x


def cycle_lengths(p):
    seen = set()
    out = []
    for i in range(len(p)):
        if i in seen: continue
        j=i; m=0
        while j not in seen:
            seen.add(j); m+=1; j=p[j]
        out.append(m)
    return tuple(sorted(out))


def orbital_trace(q):
    """Signed Lefschetz sum = independence polynomial of good edge cycles at -1."""
    used=set(); good=[]
    for i in range(len(E)):
        if i in used: continue
        orbit=[]; j=i
        while j not in used:
            used.add(j); orbit.append(j); j=q[j]
        assert j == i
        vset = 0
        for h in orbit:
            if vset & V_MASKS[h]: break
            vset |= V_MASKS[h]
        else:
            good.append(vset)
    def count(i, usedvertices):
        if i==len(good): return 1
        t=count(i+1,usedvertices)
        if not good[i] & usedvertices:
            t-=count(i+1,usedvertices | good[i])
        return t
    return count(0,0)


def all_matchings():
    matchings=[[] for _ in range(10)]
    def rec(i, vertices, edgeset, edge_list):
        if i == len(E):
            matchings[len(edge_list)].append((edgeset,edge_list))
            return
        rec(i+1,vertices,edgeset,edge_list)
        if not vertices & V_MASKS[i]:
            rec(i+1,vertices | V_MASKS[i],edgeset | (1<<i),edge_list+(i,))
    rec(0,0,0,())
    return matchings


def direct_trace(q, matchings):
    """Separate calculation: direct signed simplicial Lefschetz sum."""
    total=0
    for k,layer in enumerate(matchings):
        for mask,src in layer:
            dst=[q[i] for i in src]
            if set(dst) != set(src): continue
            inversions = sum(dst[i]>dst[j] for i in range(k) for j in range(i+1,k))
            total += (-1)**(k+inversions)
    return total


def main():
    aut=find_automorphisms()
    qlist=[graph_edge_permutation(p) for p in aut]
    matchings=all_matchings()
    sizes=[len(layer) for layer in matchings]
    assert sizes==[1,27,297,1719,5643,10557,10737,5319,1026,42], sizes
    orbital=[orbital_trace(q) for q in qlist]
    direct=[direct_trace(q,matchings) for q in qlist]
    assert orbital==direct, [(i,a,b) for i,(a,b) in enumerate(zip(orbital,direct)) if a!=b]
    profiles=defaultdict(list)
    for p,q,t in zip(aut,qlist,orbital):
        profiles[(order(p),cycle_lengths(p),cycle_lengths(q))].append(t)
    assert len(profiles)==11
    assert all(len(set(v))==1 for v in profiles.values())
    assert dict(Counter(orbital))=={-4:18,-2:36,-1:36,0:81,1:12,4:32,40:1}
    assert sum(orbital)==0
    assert sum((-1)**k*s for k,s in enumerate(sizes))==40
    print('AUTOMORPHISMS=216 MATCHINGS=35368 (including empty)')
    print('MATCHING_COUNTS='+','.join(map(str,sizes)))
    print('CHARACTER_DISTRIBUTION='+repr(dict(sorted(Counter(orbital).items()))))
    print('ORDER;VERTEX_CYCLE_LENGTHS;EDGE_CYCLE_LENGTHS;COUNT;TRACE')
    for (o,vc,ec),v in sorted(profiles.items()):
        print('%s;%s;%s;%s;%s'%(o,','.join(map(str,vc)),','.join(map(str,ec)),len(v),v[0]))
    print('INVARIANT_DIM=0, QUOTIENT_REDUCED_RATIONAL_HOMOLOGY=0')
    print('DIRECT_AND_ORBITAL_216_CHECKS_OK')

if __name__=='__main__': main()
