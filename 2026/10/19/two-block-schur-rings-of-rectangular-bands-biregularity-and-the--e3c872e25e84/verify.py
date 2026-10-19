"""Exact checks for two-block Schur partitions of rectangular bands.

All computations use integer arithmetic and exhaustive finite loops.
"""
from itertools import combinations, permutations, product
from collections import Counter
from math import factorial


def direct_closed(a, b, mask):
    cells = [(i, j) for i in range(a) for j in range(b)]
    block = lambda i, j: (mask >> (i * b + j)) & 1
    rs = [[sum(block(i,j) == z for j in range(b)) for i in range(a)] for z in range(2)]
    cs = [[sum(block(i,j) == z for i in range(a)) for j in range(b)] for z in range(2)]
    for z in (0,1):
        positions = [(i,j) for i,j in cells if block(i,j) == z]
        if not positions: return False
        for x,y in product(range(2),repeat=2):
            values = {rs[x][i]*cs[y][j] for i,j in positions}
            if len(values) > 1: return False
    return True


def classified(a, b, mask):
    rs = [sum((mask>>(i*b+j))&1 for j in range(b)) for i in range(a)]
    cs = [sum((mask>>(i*b+j))&1 for i in range(a)) for j in range(b)]
    return (all(v in (0,b) for v in rs) or
            all(v in (0,a) for v in cs) or
            (0<rs[0]<b and 0<cs[0]<a and len(set(rs))==1 and len(set(cs))==1))


def automorphic(a, b, mask):
    group=[]
    for p in permutations(range(a)):
        for q in permutations(range(b)):
            if all(((mask>>(i*b+j))&1)==((mask>>(p[i]*b+q[j]))&1)
                   for i in range(a) for j in range(b)):
                group.append((p,q))
    for color in (0,1):
        pos = [(i,j) for i in range(a) for j in range(b) if ((mask>>(i*b+j))&1)==color]
        seed=pos[0]
        orb={(p[seed[0]],q[seed[1]]) for p,q in group}
        if len(orb)!=len(pos): return False
    return True

# Independent direct multiplication check of the structural characterization.
for a,b in ((2,2),(3,3),(3,4),(4,4)):
    good=0
    for mask in range(1, (1<<(a*b))-1):
        d=direct_closed(a,b,mask)
        c=classified(a,b,mask)
        assert d==c, (a,b,mask,d,c)
        if d:
            good+=1
            assert automorphic(a,b,mask), (a,b,mask)
    print('direct',a,b,'ordered colorings',good,'two-block partitions',good//2)

# The 4x6 witness, with columns indexing the edges of a 3-regular multigraph.
columns=((0,1),(0,1),(2,3),(2,3),(0,2),(1,3))
mask=sum(1<<(i*6+j) for j,p in enumerate(columns) for i in p)
assert direct_closed(4,6,mask) and classified(4,6,mask)
assert not automorphic(4,6,mask)

# Every 4x6 nontrivial biregular case has row degree 3, column degree 2.
# Enumerate 6^6 possible columns, not 2^24 arbitrary matrices.
pairs=tuple(combinations(range(4),2))
ps=tuple(permutations(range(4)))
counts=Counter()
profiles=Counter()
for seq in product(range(6),repeat=6):
    deg=[0]*4
    for t in seq:
        u,v=pairs[t]; deg[u]+=1; deg[v]+=1
    if deg != [3]*4: continue
    prof=tuple(seq.count(i) for i in range(6))
    good=[p for p in ps if all(prof[i]==prof[pairs.index(tuple(sorted((p[u],p[v]))))]
                                for i,(u,v) in enumerate(pairs))]
    # Complete edge and nonedge flags for one representative of each column type.
    red={(i,u) for i,pair in enumerate(pairs) if prof[i] for u in pair}
    blue={(i,u) for i,pair in enumerate(pairs) if prof[i] for u in range(4) if u not in pair}
    def orbit(seed):
        i,u=seed
        return {(pairs.index(tuple(sorted((p[pairs[i][0]],p[pairs[i][1]])))),p[u]) for p in good}
    is_auto=(len(orbit(next(iter(red))))==len(red)
             and len(orbit(next(iter(blue))))==len(blue))
    counts[is_auto]+=1
    profiles[tuple(sorted(prof,reverse=True))]+=1
assert counts=={True:780,False:1080},counts
assert profiles=={(3,3,0,0,0,0):60,(2,2,1,1,0,0):1080,(1,1,1,1,1,1):720},profiles
assert sum(counts.values())==1860
assert 2**3-1 + 2**5-1 + 1860//2==968
assert 38 + 780//2==428
assert 1080//2==540
print('4x6',dict(counts),'profiles',dict(profiles),
      'two-block total=968 automorphic=428 nonautomorphic=540')
print('VERIFY_OK')
