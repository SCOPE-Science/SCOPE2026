#!/usr/bin/env python3
from collections import Counter, defaultdict, deque

# Petersen graph: outer 5-cycle 0..4, inner pentagram 5..9, five spokes.
EDGES=set()
def add(a,b): EDGES.add(tuple(sorted((a,b))))
for i in range(5):
    add(i,(i+1)%5)
    add(i,5+i)
    add(5+i,5+((i+2)%5))
EDGES=sorted(EDGES)
ADJ=[set() for _ in range(10)]
for a,b in EDGES:
    ADJ[a].add(b); ADJ[b].add(a)

def is_ind2(mask):
    vertices=[i for i in range(10) if (mask>>i)&1]
    seen=set()
    for s in vertices:
        if s in seen:
            continue
        stack=[s]; seen.add(s); size=0
        while stack:
            u=stack.pop(); size+=1
            for w in ADJ[u]:
                if ((mask>>w)&1) and w not in seen:
                    seen.add(w); stack.append(w)
        if size>2:
            return False
    return True

FACES=[m for m in range(1,1<<10) if is_ind2(m)]
FACESET=set(FACES)
assert len(FACES)==260
assert Counter(m.bit_count()-1 for m in FACES)==Counter({0:10,1:45,2:90,3:80,4:30,5:5})

# Staged vertex-toggle matching. At stage v, pair each still-unmatched face not
# containing v with its v-extension when that extension is also still unmatched.
order=tuple(range(10))
unmatched=set(FACESET)
pairs=[]
for v in order:
    bit=1<<v
    for m in sorted(tuple(unmatched)):
        if m not in unmatched or (m&bit):
            continue
        u=m|bit
        if u in unmatched:
            unmatched.remove(m); unmatched.remove(u); pairs.append((m,u))
assert len(pairs)==128
critical=sorted(unmatched)
assert critical==[1,82,116,402]
assert Counter(m.bit_count()-1 for m in critical)==Counter({0:1,2:1,3:2})

# Verify that every pair is a codimension-one face relation and all cells occur once.
seen=set()
for lo,hi in pairs:
    assert lo in FACESET and hi in FACESET
    assert hi.bit_count()==lo.bit_count()+1
    assert lo & hi == lo
    assert lo not in seen and hi not in seen
    seen.add(lo); seen.add(hi)
assert seen.isdisjoint(critical) and len(seen)+len(critical)==len(FACES)

# Verify acyclicity of the Forman matching by orienting unmatched Hasse edges downward
# and matched edges upward, then performing a topological sort.
up={lo:hi for lo,hi in pairs}
down={hi:lo for lo,hi in pairs}
out=defaultdict(list); indeg={m:0 for m in FACES}
for hi in FACES:
    if hi.bit_count()<=1:
        continue
    bits=[i for i in range(10) if (hi>>i)&1]
    for v in bits:
        lo=hi & ~(1<<v)
        if lo==0:  # empty face is not part of this nonempty-face matching
            continue
        if up.get(lo)==hi:
            a,b=lo,hi
        else:
            a,b=hi,lo
        out[a].append(b); indeg[b]+=1
q=deque([m for m in FACES if indeg[m]==0]); count=0
while q:
    a=q.popleft(); count+=1
    for b in out[a]:
        indeg[b]-=1
        if indeg[b]==0: q.append(b)
assert count==len(FACES)

# Incidence number [hi:lo] for the standard increasing-vertex orientation.
def incidence(hi,lo):
    hs=[i for i in range(10) if (hi>>i)&1]
    los=set(i for i in range(10) if (lo>>i)&1)
    k=next(k for k,x in enumerate(hs) if x not in los)
    return -1 if k%2 else 1

# Exact gradient-path recursion for the Morse boundary between critical dimensions 3 and 2.
# When a path enters a matched upper cell, the matched lower face is excluded from the next step.
from functools import lru_cache
@lru_cache(None)
def morse_coeff(cell,target):
    total=0
    bits=[i for i in range(10) if (cell>>i)&1]
    for k,v in enumerate(bits):
        face=cell & ~(1<<v)
        x=-1 if k%2 else 1
        if face==down.get(cell):
            continue
        if face==target:
            total += x
        elif face in up:
            mate=up[face]
            a=incidence(mate,face)
            total += -x*a*morse_coeff(mate,target)
    return total

crit2=[m for m in critical if m.bit_count()==3]
crit3=[m for m in critical if m.bit_count()==4]
assert crit2==[82] and crit3==[116,402]
coeffs=[morse_coeff(c,crit2[0]) for c in crit3]
assert coeffs==[-1,-1]

# The Morse CW complex therefore has one 0-cell, one 2-cell, and two 3-cells,
# with the two 3-cell attaching degrees both -1. One degree-one attachment forms
# a contractible subcomplex; the remaining 3-cell is then attached to a contractible
# space, yielding S^3 up to homotopy.
print('PETERSEN_IND2_VERIFY_OK')
print('faces=260 f_vector=(10,45,90,80,30,5)')
print('critical_masks=(1,82,116,402) critical_dimensions=(0,2,3,3)')
print('morse_boundary_C3_to_C2=(-1,-1)')
