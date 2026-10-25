#!/usr/bin/env python3
"""Exact combinatorial checks for the 27-vertex ternary Hamming Rips complex.

Only the Python standard library is used. Execute: python ternary_wreath_verify.py
"""
from collections import Counter, defaultdict
from itertools import permutations, product

V = list(product(range(3), repeat=3))
assert len(V) == 27
POS = {v: i for i, v in enumerate(V)}
ADJ = []
for a in V:
    bits = 0
    for j,b in enumerate(V):
        if a != b and sum(x != y for x,y in zip(a,b)) <= 2:
            bits |= 1<<j
    ADJ.append(bits)

FACES = []
def enumerate_cliques(current, candidates):
    if current:
        FACES.append(current)
    while candidates:
        low = candidates & -candidates
        candidates -= low
        enumerate_cliques(current | low, candidates & ADJ[low.bit_length()-1])
enumerate_cliques(0, (1<<27)-1)
BY_SIZE = {k: sorted(s for s in FACES if s.bit_count() == k)
           for k in range(1,10)}
assert tuple(map(len,BY_SIZE.values())) == (27,243,945,1728,1620,945,351,81,9)
# An explicit, complete mod-two boundary computation. The resulting ranks
# force the rational Betti numbers by rank comparison and Euler characteristic.
RANKS = {}
for k in range(2,10):
    rowindex = {s:i for i,s in enumerate(BY_SIZE[k-1])}
    pivots = {}
    for s in BY_SIZE[k]:
        vector = 0
        remain = s
        while remain:
            b = remain & -remain
            remain -= b
            vector ^= 1 << rowindex[s^b]
        while vector:
            h = vector.bit_length()-1
            if h not in pivots:
                pivots[h] = vector
                break
            vector ^= pivots[h]
    RANKS[k] = len(pivots)
assert tuple(RANKS.values()) == (26,217,728,954,666,279,72,9)
BETTI = {k-1: len(BY_SIZE[k])-RANKS.get(k,0)-RANKS.get(k+1,0)
         for k in range(1,10)}
assert BETTI == {0:1,1:0,2:0,3:46,4:0,5:0,6:0,7:0,8:0}

P = list(permutations(range(3)))
ID = (0,1,2)
def perm_type(p):
    seen=set(); out=[]
    for a in range(3):
        if a in seen: continue
        b=a; size=0
        while b not in seen:
            seen.add(b); b=p[b]; size+=1
        out.append(size)
    return tuple(sorted(out,reverse=True))
NAME={(1,1,1):'I',(2,1):'T',(3,):'C'}
def group_action(coordinate_perm,symbol_perms):
    out=[]
    for a in V:
        b=[0,0,0]
        for i in range(3):
            j=coordinate_perm[i]
            b[j]=symbol_perms[j][a[i]]
        out.append(POS[tuple(b)])
    assert len(set(out)) == 27
    return out

def class_key(coordinate_perm,symbol_perms):
    seen=set(); result=[]
    for i in range(3):
        if i in seen: continue
        cyc=[]; j=i
        while j not in seen:
            seen.add(j);cyc.append(j);j=coordinate_perm[j]
        composite=ID
        for k in cyc:
            p=symbol_perms[coordinate_perm[k]]
            composite=tuple(p[composite[a]] for a in range(3))
        result.append((len(cyc),NAME[perm_type(composite)]))
    return tuple(sorted(result))

def vertex_cycles(mapping):
    seen=set();out=[]
    for start in range(27):
        if start in seen: continue
        j=start; mask=0
        while j not in seen:
            seen.add(j);mask|=1<<j;j=mapping[j]
        out.append(mask)
    return out

def invariant_orbit_character(mapping):
    # A fixed simplex is a union of full vertex cycles. A selected
    # orbit cycle contributes minus to the alternating cycle count.
    available=[]
    for cyc in vertex_cycles(mapping):
        if all((ADJ[i] | (1<<i)) & cyc == cyc
               for i in range(27) if cyc >> i & 1):
            available.append(cyc)
    answer=0
    def visit(i, mask, sign):
        nonlocal answer
        if i==len(available):
            answer+=sign;return
        visit(i+1,mask,sign)
        nxt=available[i]
        if all((ADJ[j] | (1<<j)) & nxt == nxt
               for j in range(27) if mask >> j & 1):
            visit(i+1,mask | nxt,-sign)
    visit(0,0,1)
    return answer

def direct_signed_lefschetz_character(mapping):
    # Independent calculation from the signed oriented simplicial chains.
    ans=1 # augmented empty face has opposite reduced Lefschetz sign
    for face in FACES:
        im=0; vertices=[]
        t=face
        while t:
            b=t & -t;t-=b
            i=b.bit_length()-1
            vertices.append(i)
            im|=1<<mapping[i]
        if im != face: continue
        # Sign of the induced permutation in increasing-vertex orientation.
        images=[mapping[i] for i in vertices]
        inversions=sum(images[i] > images[j]
                       for i in range(len(images)) for j in range(i+1,len(images)))
        ans-=(-1)**(len(vertices)-1+inversions)
    return ans

def sn_character(partition,cycle_lengths):
    n=sum(partition)
    if n<=1 or partition == (n,): return 1
    if partition == (1,)*n: return (-1)**(n-len(cycle_lengths))
    if partition == (2,1) and n==3: return cycle_lengths.count(1)-1
    raise AssertionError((partition,cycle_lengths))

def wreath_character(key,partitions):
    # Induced Specht-tensor character formula for S3 wreath S3.
    sizes=tuple(sum(part) for part in partitions)
    total=0
    basechars=[{'I':1,'T':1,'C':1},
               {'I':1,'T':-1,'C':1},
               {'I':2,'T':0,'C':-1}]
    for colors in product(range(3),repeat=len(key)):
        if tuple(sum(key[j][0] for j in range(len(key)) if colors[j]==i)
                 for i in range(3)) != sizes:
            continue
        v=1
        for i in range(3):
            cyc=[key[j][0] for j in range(len(key)) if colors[j]==i]
            v*=sn_character(partitions[i],cyc)
        for j,(length,typ) in enumerate(key):
            v*=basechars[colors[j]][typ]
        total+=v
    return total

CLASS_GROUPS=defaultdict(list)
for cp in P:
    for syms in product(P,repeat=3):
        CLASS_GROUPS[class_key(cp,syms)].append((cp,syms))
assert len(CLASS_GROUPS)==22 and sum(map(len,CLASS_GROUPS.values()))==1296
TABLE=[]
for key,items in sorted(CLASS_GROUPS.items()):
    cp,syms=items[0]
    mapping=group_action(cp,syms)
    tr=invariant_orbit_character(mapping)
    assert tr == direct_signed_lefschetz_character(mapping),key
    TABLE.append((key,len(items),tr))
assert sum(size*trace for _,size,trace in TABLE)==0
assert sum(size*trace*trace for _,size,trace in TABLE)==1296*7

PARTS={0:[()],1:[(1,)],2:[(2,),(1,1)],
       3:[(3,),(2,1),(1,1,1)]}
IRREPS=[]
for a in range(4):
    for b in range(4-a):
        for triple in product(PARTS[a],PARTS[b],PARTS[3-a-b]):
            IRREPS.append(triple)
assert len(IRREPS)==22
DECOMPOSITION=[]
for triple in IRREPS:
    ip=sum(sz*trace*wreath_character(key,triple)
           for key,sz,trace in TABLE)
    assert ip%1296==0
    mult=ip//1296
    assert mult>=0
    if mult:DECOMPOSITION.append((triple,mult,wreath_character(((1,'I'),)*3,triple)))
assert len(DECOMPOSITION)==7
assert all(mult==1 for _,mult,_ in DECOMPOSITION)
assert sum(dim for _,_,dim in DECOMPOSITION)==46
expected=[((),(),(1,1,1)),((),(1,),(1,1)),
          ((),(1,1),(1,)),((),(1,1,1),()),
          ((1,),(),(1,1)),((1,1),(),(1,)),
          ((1,1,1),(),())]
assert [lab for lab,_,_ in DECOMPOSITION]==expected
# Certify that the table covers ALL elements, rather than only class reps.
for key,items in CLASS_GROUPS.items():
    trace=next(t for k,_,t in TABLE if k==key)
    for cp,syms in items:
        assert invariant_orbit_character(group_action(cp,syms))==trace
print('TERNARY_HAMMING_WREATH_CHARACTER_VERIFIED',
      len(FACES),len(CLASS_GROUPS),sum(map(len,CLASS_GROUPS.values())),
      len(DECOMPOSITION))
for key,size,trace in TABLE:
    print(key,'size',size,'trace',trace)
print('decomposition',DECOMPOSITION)
