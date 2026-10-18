"""Exact integral-topology premise and rational symmetry-character verifier.

Run: python verify.py
Only Python's standard library is required.
"""
from itertools import combinations, permutations
from functools import lru_cache
from collections import Counter, deque
from math import factorial

N = 6
DUADS = list(combinations(range(N), 2))

def make_matchings(rem):
    if not rem:
        yield ()
        return
    a=rem[0]
    for b in rem[1:]:
        for rest in make_matchings(tuple(t for t in rem if t not in (a,b))):
            yield tuple(sorted(((a,b),)+rest))

SYNTHEMES = sorted(set(make_matchings(tuple(range(N)))))
assert len(DUADS) == len(SYNTHEMES) == 15
VERTICES = [('duad', a) for a in DUADS] + [('syntheme', a) for a in SYNTHEMES]
POSITION = {a:i for i,a in enumerate(VERTICES)}
EDGES = {(i,15+j) for i,p in enumerate(DUADS) for j,m in enumerate(SYNTHEMES) if p in m}
assert len(EDGES)==45
ADJ = [0]*30
for i,j in EDGES:
    ADJ[i]|=1<<j
    ADJ[j]|=1<<i
assert all(x.bit_count()==3 for x in ADJ)

# Color-interchanging involution in the above lexicographic vertex order.
DUAL = [15,22,20,28,24,27,25,19,23,16,26,18,21,29,17,
        0,9,14,11,7,2,12,1,8,4,6,10,5,3,13]
assert sorted(DUAL)==list(range(30))
assert all(DUAL[DUAL[i]]==i for i in range(30))
assert all(DUAL[i]>=15 for i in range(15))

def automorphism_check(g):
    assert sorted(g)==list(range(30))
    assert all((min(g[i],g[j]),max(g[i],g[j])) in EDGES for i,j in EDGES)

automorphism_check(DUAL)

def action(pi):
    q=[]
    for typ,obj in VERTICES:
        if typ=='duad':
            image=('duad',tuple(sorted(pi[k] for k in obj)))
        else:
            image=('syntheme',tuple(sorted(tuple(sorted(pi[k] for k in p)) for p in obj)))
        q.append(POSITION[image])
    return q

def perm_cycles(g):
    seen=set()
    orbits=[]
    for k in range(len(g)):
        if k in seen:continue
        orb=[];cur=k
        while cur not in seen:
            orb.append(cur);seen.add(cur);cur=g[cur]
        assert cur==k
        orbits.append(tuple(orb))
    return orbits

def trace_by_invariant_faces(g):
    """Reduced Hopf trace when homology is concentrated in even degree 8.

    A g-fixed independent face is a union of g-orbits. Each eligible orbit
    contributes minus one to the signed reduced cellular Euler trace;
    the empty union contributes minus one as an augmented simplex.
    """
    good=[]
    for orb in perm_cycles(g):
        b=sum(1<<x for x in orb)
        if all((ADJ[x]&b)==0 for x in orb):
            good.append(b)
    conf=[]
    for i,b in enumerate(good):
        incompat=sum(1<<j for j,c in enumerate(good) if j!=i and any(ADJ[x]&c for x in range(30) if b>>x&1))
        conf.append(incompat)
    @lru_cache(None)
    def signed_independent_count(active):
        if not active:return 1
        pivot=active&-active
        idx=pivot.bit_length()-1
        return signed_independent_count(active^pivot)-signed_independent_count(active&~(pivot|conf[idx]))
    return -signed_independent_count((1<<len(good))-1)

def inversion_parity(pi):
    return -1 if sum(pi[i]>pi[j] for i in range(6) for j in range(i+1,6))%2 else 1

def topological_cycle_type(pi):
    return tuple(sorted((len(o) for o in perm_cycles(pi)),reverse=True))

def cycle_type_on_30(g):
    return tuple(sorted((len(o) for o in perm_cycles(g)),reverse=True))

def enumerable_faces():
    allfaces=set()
    def visit(i,mask,forbidden):
        if i==30:
            if mask:allfaces.add(mask)
            return
        visit(i+1,mask,forbidden)
        if not (forbidden>>i)&1:
            visit(i+1,mask|(1<<i),forbidden|ADJ[i]|(1<<i))
    visit(0,0,0)
    return allfaces

def morse_check(faces):
    unmatched=set(faces)
    lower_to_upper={};upper_to_lower={}
    for v in range(30):
        bit=1<<v
        for face in list(unmatched):
            if face&bit:continue
            upper=face|bit
            if upper in unmatched:
                unmatched.remove(face);unmatched.remove(upper)
                lower_to_upper[face]=upper;upper_to_lower[upper]=face
    critical=Counter(x.bit_count()-1 for x in unmatched)
    assert critical=={0:1,8:9},critical
    assert len(lower_to_upper)==238088
    # Orient all nonempty-face Hasse covers down except matched covers up.
    indeg={m:0 for m in faces}
    covers=0
    for upper in faces:
        bits=upper
        while bits:
            b=bits&-bits;bits-=b
            lower=upper^b
            if lower:
                covers+=1
                if lower_to_upper.get(lower)==upper:indeg[upper]+=1
                else:indeg[lower]+=1
    assert covers==3461400, covers
    ready=deque(x for x,d in indeg.items() if d==0)
    processed=0
    while ready:
        face=ready.popleft();processed+=1
        upp=lower_to_upper.get(face)
        if upp is not None:
            indeg[upp]-=1
            if indeg[upp]==0:ready.append(upp)
        bits=face
        while bits:
            b=bits&-bits;bits-=b
            lower=face^b
            if lower and upper_to_lower.get(face)!=lower:
                indeg[lower]-=1
                if indeg[lower]==0:ready.append(lower)
    assert processed==len(faces),(processed,len(faces))
    return critical,covers

def main():
    faces=enumerable_faces()
    f=Counter(s.bit_count()-1 for s in faces)
    expected=[30,390,2890,13515,41736,86610,120690,111225,66090,
              24948,6420,1370,240,30,2]
    assert [f[k] for k in range(15)]==expected
    assert len(faces)==476186
    assert sum((-1)**k*f[k] for k in f)==10
    critical,covers=morse_check(faces)
    print('INTEGRAL_MORSE_OK',len(faces),covers,critical)

    character={}; outer=Counter(); s6=Counter(); count=0
    signtwist=Counter()
    for pi in permutations(range(6)):
        g=action(pi);automorphism_check(g)
        t=trace_by_invariant_faces(g)
        fixed_letters=sum(pi[i]==i for i in range(6))
        fixed_duads=sum(set(pi[k] for k in e)==set(e) for e in DUADS)
        expected=inversion_parity(pi)*(fixed_duads-fixed_letters)
        assert t==expected,(pi,t,expected)
        typ=topological_cycle_type(pi)
        if typ in character:assert character[typ]==t
        character[typ]=t
        s6[typ]+=1
        outer_action=[DUAL[g[i]] for i in range(30)]
        automorphism_check(outer_action)
        otyp=cycle_type_on_30(outer_action)
        outertrace=trace_by_invariant_faces(outer_action)
        if otyp in outer:assert outer[otyp][0]==outertrace
        if otyp not in outer:outer[otyp]=[outertrace,0]
        outer[otyp][1]+=1
        count+=1
    assert count==720 and len(character)==11 and len(outer)==4
    assert character[(1,)*6]==9
    assert sum(s6[t]*character[t]*character[t] for t in character)==720
    assert outer[(8,8,8,4,2)]==[1,360]
    assert outer[(4,4,4,4,4,4,2,2,2)]==[-1,180]
    assert outer[(10,10,10)]==[-1,144]
    assert outer[(2,)*15]==[-1,36]
    assert trace_by_invariant_faces(DUAL)==-1
    print('S6_CHAR', sorted(character.items()))
    print('DUAL_CHAR',sorted(outer.items()))
    print('S6_IRREDUCIBLE_OK')
    print('VERIFY_OK')

if __name__=='__main__':main()
