#!/usr/bin/env python3
"""Exact finite proof checks for folded-five-cube independence topology and symmetry.

Requires only Python 3.10+. Outputs exact integer invariants and assertions.
The graph is the degree-five, not the degree-ten, Clebsch graph.
"""
from itertools import permutations
from collections import Counter,deque

N=5
V=tuple(x for x in range(1<<N) if x.bit_count()%2==0)
assert len(V)==16
idx={x:i for i,x in enumerate(V)}
ADJ=[]
for x in V:
    ADJ.append(sum(1<<j for j,y in enumerate(V) if (x^y).bit_count()==4))
assert all(a.bit_count()==5 for a in ADJ)
assert sum(a.bit_count() for a in ADJ)//2==40
for i in range(16):
    for j in range(i+1,16):
        common=(ADJ[i]&ADJ[j]).bit_count()
        assert common==(0 if ADJ[i]>>j&1 else 2)

# Independent faces by increasing-bit dynamic programming.
F={0}
for s in range(1,1<<16):
    b=s&-s
    i=b.bit_length()-1
    t=s^b
    if t in F and not (ADJ[i]&t):F.add(s)
assert len(F)==393
fvec=tuple(sum(s.bit_count()==d+1 for s in F) for d in range(5))
assert fvec==(16,80,160,120,16)
assert not any(s.bit_count()>5 for s in F)

# Independent second enumeration from recursive inclusion/exclusion on remaining vertices.
def rec(allowed,used,out):
    if not allowed:
        out.add(used);return
    bit=allowed&-allowed
    v=bit.bit_length()-1
    rec(allowed^bit,used,out)
    rec((allowed^bit)&~ADJ[v],used|bit,out)
second=set()
rec((1<<16)-1,0,second)
assert second==F

# Lexicographic matching on the face poset (including empty face).
remaining=set(F);pairs=[]
for v in range(16):
    bit=1<<v
    for s in sorted(remaining):
        if s not in remaining or s&bit:continue
        t=s|bit
        if t in remaining:
            remaining.remove(s);remaining.remove(t)
            pairs.append((s,t))
assert (0,1) in pairs
critical=remaining|{1}
assert len(pairs)==192
assert Counter(s.bit_count()-1 for s in critical)=={0:1,3:9}
assert set(s for s in critical if s.bit_count()==4)=={0xf0,0xf00,0x3300,0x5500,0x6900,0x9600,0xaa00,0xcc00,0xf000}

# Verify the FULL oriented Hasse diagram on nonempty faces: ordinary
# incidences are down, matched incidences up. Require a global DAG.
matched={(a,b) for a,b in pairs if a}
nonempty=F-{0}
indeg={s:0 for s in nonempty}
out={s:[] for s in nonempty}
incidences=0
for s in nonempty:
    bits=s
    while bits:
        bit=bits&-bits;bits^=bit
        t=s^bit
        if t==0:continue
        incidences+=1
        a,b=(t,s) if (t,s) in matched else (s,t)
        out[a].append(b);indeg[b]+=1
assert incidences==1200
queue=deque(s for s in nonempty if indeg[s]==0)
visited=0
while queue:
    s=queue.popleft();visited+=1
    for t in out[s]:
        indeg[t]-=1
        if indeg[t]==0:queue.append(t)
assert visited==392
assert len(nonempty)==1+9+2*191
print('MORSE_OK faces_including_empty=393 fvector=(16,80,160,120,16)')
print('MORSE_OK ordinary_pairs=191 critical=(one_vertex,nine_3_cells) incidences=1200 Hasse_DAG=392')

# The full automorphism group is E_even (translations) semidirect S5.
# Check all 16*120 affine permutations separately.
perms=list(permutations(range(5)))
assert len(perms)==120

def perm_mask(x,p):
    y=0
    for i in range(N):
        if x>>i&1:y|=1<<p[i]
    return y

def image_perm(p,a):
    return tuple(idx[perm_mask(x,p)^a] for x in V)

seen=set();tracehist=Counter();subgroup_class=Counter();indep_orbit_traces=Counter()

# Direct chain-Lefschetz trace on the 393 faces, reducing to H3
# using Morse proof (all other reduced homology zero).
def chain_trace(P):
    z=1  # contribution of degree -1 reduced chain
    for s in F:
        if not s:continue
        orig=[];img=[];im=0;bits=s
        while bits:
            bit=bits&-bits;bits^=bit
            i=bit.bit_length()-1
            orig.append(i);img.append(P[i]);im|=1<<P[i]
        if im!=s:continue
        inversions=sum(img[i]>img[j] for i in range(len(img)) for j in range(i+1,len(img)))
        z-=(-1)**(len(img)-1+inversions)
    return z

# Independent character computation: invariant faces are independent
# unions of graph-vertex orbits; orientation signs cancel the orbit lengths.
def orbit_trace(P):
    unseen=set(range(16));cycles=[]
    while unseen:
        s=min(unseen);c=[];t=s
        while t in unseen:
            unseen.remove(t);c.append(t);t=P[t]
        assert t==s
        mask=sum(1<<u for u in c)
        if all(not (ADJ[u]&(mask^(1<<u))) for u in c):cycles.append(mask)
    k=len(cycles)
    conflicts=[0]*k
    for i in range(k):
        for j in range(i+1,k):
            if any(ADJ[u]&cycles[j] for u in range(16) if cycles[i]>>u&1):
                conflicts[i]|=1<<j;conflicts[j]|=1<<i
    from functools import lru_cache
    @lru_cache(None)
    def evaluate(rem):
        if not rem:return 1
        b=rem&-rem;i=b.bit_length()-1
        return evaluate(rem^b)-evaluate((rem^b)&~conflicts[i])
    return evaluate((1<<k)-1)

for p in perms:
    inv=sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))
    sign=(-1)**inv
    fixed=[i for i in range(5) if p[i]==i]
    for a in V:
        P=image_perm(p,a)
        assert P not in seen
        seen.add(P)
        assert all((bool(ADJ[i]>>j&1)==bool(ADJ[P[i]]>>P[j]&1)) for i in range(16) for j in range(i+1,16))
        predicted=sign*((len(fixed)-1)+sum((-1)**(a>>i&1) for i in fixed))
        actual=chain_trace(P)
        independent=orbit_trace(P)
        assert actual==predicted==independent,(p,a,actual,predicted,independent)
        tracehist[actual]+=1
        subgroup_class[(len(fixed),sign)]+=1
assert len(seen)==1920
assert tracehist==Counter({-5:20,-3:60,-1:884,1:865,3:80,5:10,9:1})
assert sum(t*c for t,c in tracehist.items())==0
print('ACTION_OK affine_automorphisms=1920 signed_Lefschetz_and_orbit_independence_agree')
print('ACTION_OK trace_multiplicities='+str(sorted(tracehist.items())))
print('ACTION_OK formula=sign(pi)*(fixed(pi)-1+sum_fixed_i((-1)^a_i))')

# Verify translation-Fourier ranks 4 on the trivial character and 1 on
# each of the five weight-one characters; zero on ten weight-two chars.
T0=tuple(range(5))
translation_trace={a:chain_trace(image_perm(T0,a)) for a in V}
for q in range(16):
    m=sum(translation_trace[a]*(-1)**((a&q).bit_count()%2) for a in V)
    assert m%16==0
    m//=16
    expected=4 if q==0 else (1 if min(q.bit_count(),5-q.bit_count())==1 else 0)
    assert m==expected,(q,m,expected)
print('FOURIER_OK E_even_multiplicities=(trivial:4,weight_one:1_each,weight_two:0)')

# Determine the S5 representation on the four-dimensional E_even-fixed
# summand by the explicit 16-element averaging projector.
for p in perms:
    inv=sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))
    sign=(-1)**inv
    f=sum(p[i]==i for i in range(5))
    projected=sum(chain_trace(image_perm(p,a)) for a in V)
    assert projected==16*sign*(f-1)
print('PROJECTOR_OK E_even_fixed_module=sign_tensor_standard4')
print('RESULT_OK wedge_of_9_S3 and rational_H3=sign_tensor_standard4 plus sign_tensor_weight1_module5')
