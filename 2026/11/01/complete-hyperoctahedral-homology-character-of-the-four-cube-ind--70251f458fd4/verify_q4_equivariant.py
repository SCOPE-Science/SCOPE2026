#!/usr/bin/env python3
"""Finite verification of the topological and symmetry assertions for Ind(Q4).

Only Python's standard library is needed. A face is a 16-bit integer mask;
bit v indexes the binary cube vertex v, for 0 <= v < 16.
"""
from collections import Counter, defaultdict, deque
from itertools import permutations

D = 4
N = 1 << D
ADJ = tuple(sum(1 << (v ^ (1 << i)) for i in range(D)) for v in range(N))
FACES = tuple(s for s in range(1 << N)
              if all(not (s & ADJ[v]) for v in range(N) if s & (1 << v)))
NONEMPTY = set(FACES) - {0}
assert len(FACES) == 743
assert [sum(s.bit_count() == k for s in NONEMPTY) for k in range(1, 9)] == [16,88,208,228,128,56,16,2]

# The 367 pairs are independently reconstructed, rather than supplied as logs.
remaining = set(NONEMPTY)
pairs = []
per_pivot = []
for v in range(N):
    bit = 1 << v
    current = []
    for s in sorted(remaining):
        t = s | bit
        if not (s & bit) and s in remaining and t in remaining:
            remaining.remove(s); remaining.remove(t)
            current.append((s,t))
    pairs.extend(current)
    per_pivot.append(len(current))
assert per_pivot == [176,134,10,4,5,5,13,4,0,3,4,3,3,1,1,1]
assert len(pairs) == 367
assert sorted(remaining) == [1,1680,2400,10370,17028,24600,33064,33096]
assert Counter(s.bit_count()-1 for s in remaining) == {0:1,3:7}

# Every covering relation in the nonempty-face poset is oriented,
# downwards unless matched, when upwards. Kahn's DAG test exhausts it.
matched = set(pairs)
indegree = {s:0 for s in NONEMPTY}
arrows = {s:[] for s in NONEMPTY}
edge_count=0
for high in NONEMPTY:
    for v in range(N):
        if high & (1 << v):
            low = high ^ (1 << v)
            if low == 0: continue
            tail, head = (low,high) if (low,high) in matched else (high,low)
            arrows[tail].append(head)
            indegree[head] += 1
            edge_count += 1
assert edge_count == 2816
queue = deque([s for s in NONEMPTY if indegree[s] == 0]); reached=0
while queue:
    u=queue.popleft();reached += 1
    for w in arrows[u]:
        indegree[w] -= 1
        if indegree[w] == 0: queue.append(w)
assert reached == 742

# Independent check: mod-two ranks of unreduced simplicial boundaries.
fs = {k:sorted(s for s in NONEMPTY if s.bit_count()==k+1) for k in range(8)}
ranks=[]
for k in range(1,8):
    index={s:i for i,s in enumerate(fs[k-1])}
    basis={}
    for s in fs[k]:
        col=0
        for v in range(N):
            if s & (1 << v): col ^= 1 << index[s^(1<<v)]
        while col:
            p=col.bit_length()-1
            if p not in basis:
                basis[p]=col;break
            col ^= basis[p]
    ranks.append(len(basis))
assert ranks == [15,73,135,86,42,14,2]


def sgn_perm(p):
    return -1 if sum(p[i] > p[j] for i in range(D) for j in range(i+1,D)) % 2 else 1

def image_vertices(p,b):
    """g(x) has coordinate p(i) equal to coordinate i of x XOR bit i of b."""
    return tuple(sum((((x >> i) & 1) ^ ((b >> i) & 1)) << p[i] for i in range(D)) for x in range(N))

def signed_face_trace(g):
    """Reduced Euler-Lefschetz, negated for H3 (the only reduced homology)."""
    result = 1  # the empty simplex contributes reduced degree -1
    for s in FACES[1:]:
        f = [i for i in range(N) if s & (1 << i)]
        img = [g[i] for i in f]
        if set(f) != set(img): continue
        inversions = sum(img[i] > img[j] for i in range(len(img)) for j in range(i+1,len(img)))
        result -= (-1) ** (len(f)-1 + inversions)
    return result

def orbit_trace(g):
    """Alternative fixed-orbit independence-polynomial calculation."""
    unseen=set(range(N)); orbits=[]
    while unseen:
        z=min(unseen);cyc=[];x=z
        while x in unseen:
            unseen.remove(x);cyc.append(x);x=g[x]
        assert x==z
        orbits.append(cyc)
    good=[]
    for cyc in orbits:
        if all(not (ADJ[x] & sum(1<<y for y in cyc if y!=x)) for x in cyc):
            good.append(cyc)
    masks=[sum(1<<x for x in cyc) for cyc in good]
    ans=0
    for s in range(1<<len(good)):
        taken=0;ok=True
        for j,M in enumerate(masks):
            if s&(1<<j):
                if any(ADJ[x]&taken for x in good[j]):ok=False;break
                taken |= M
        if ok: ans += (-1)**s.bit_count()
    return ans

def signed_cycle_type(p,b):
    unseen=set(range(D));out=[]
    while unseen:
        i=min(unseen); cyc=[];j=i
        while j in unseen:
            unseen.remove(j);cyc.append(j);j=p[j]
        out.append((len(cyc),sum((b>>j)&1 for j in cyc)%2))
    return tuple(sorted(out))

all_records=[]
for p in permutations(range(D)):
    for b in range(1<<D):
        g=image_vertices(p,b)
        direct=signed_face_trace(g)
        alternative=orbit_trace(g)
        fixed=[i for i in range(D) if p[i]==i]
        predicted=sgn_perm(p)*(len(fixed)-1 + sum((-1)**sum((b>>j)&1 for j in range(D) if j!=i) for i in fixed))
        assert direct == alternative == predicted, (p,b,direct,alternative,predicted)
        all_records.append((p,b,direct,signed_cycle_type(p,b)))
assert len(all_records)==384
bytype=defaultdict(list)
for p,b,tr,t in all_records:bytype[t].append(tr)
assert len(bytype)==20
assert all(len(set(v))==1 for v in bytype.values())
assert sum(tr for _,_,tr,_ in all_records)==0
byb={b:tr for p,b,tr,_ in all_records if p==tuple(range(D))}
weight_multiplicities=defaultdict(set)
for a in range(1<<D):
    mult=sum(byb[b]*(-1)**((a&b).bit_count()) for b in range(1<<D))//(1<<D)
    weight_multiplicities[a.bit_count()].add(mult)
assert dict(weight_multiplicities)=={0:{3},1:{0},2:{0},3:{1},4:{0}}
print('faces=743 nonempty=742 pairs=367 incidence_arrows=2816 critical=1x0+7x3')
print('mod2_boundary_ranks='+str(ranks))
print('group=384 signed_cycle_types=20 character_agrees_on_all=384')
print('translation_multiplicities_by_weight=0:3,1:0,2:0,3:1,4:0')
print('full_group_fixed_h3=0')
print('signed_cycle_type (length, parity) ; class_size ; H3_trace')
for key in sorted(bytype):
    print(str(key)+' ; '+str(len(bytype[key]))+' ; '+str(bytype[key][0]))
print('VERIFY_OK')
