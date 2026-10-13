#!/usr/bin/env python3
from itertools import combinations, permutations
from collections import Counter, defaultdict
import hashlib, json, math

N=7
Q=5

# Restricted-growth-string set partitions of seven labelled codewords,
# with at most five blocks because the alphabet has size five.
def partitions_rgs(n, max_blocks):
    a=[0]*n
    out=[]
    def rec(i,mx):
        if i==n:
            if mx+1<=max_blocks:
                out.append(tuple(a))
            return
        for v in range(mx+2):
            if v>=max_blocks: break
            a[i]=v
            rec(i+1,max(mx,v))
    rec(1,0)
    return out

parts=partitions_rgs(N,Q)
assert len(parts)==855
pidx={p:i for i,p in enumerate(parts)}
triples=list(combinations(range(N),3))
pairconds=[]
for quad in combinations(range(N),4):
    a,b,c,d=quad
    pairconds += [((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c))]
assert len(triples)==35 and len(pairconds)==105

# For each coordinate partition, bit j is one exactly when that coordinate
# certifies the corresponding IPP1 (35) or IPP2 (105) condition.
masks=[]
for p in parts:
    m=0
    for j,t in enumerate(triples):
        if len({p[x] for x in t})==3:
            m |= 1<<j
    for j,(ab,cd) in enumerate(pairconds):
        if {p[ab[0]],p[ab[1]]}.isdisjoint({p[cd[0]],p[cd[1]]}):
            m |= 1<<(35+j)
    masks.append(m)
ALL=(1<<140)-1
cover=[]
for bit in range(140):
    s=0
    for i,m in enumerate(masks):
        if (m>>bit)&1:
            s |= 1<<i
    cover.append(s)
FULL=(1<<len(parts))-1

# Coordinate order is irrelevant for equivalence, so enumerate i<=j<=k.
valid=[]
for i,m1 in enumerate(masks):
    for j in range(i,len(parts)):
        missing=ALL ^ (m1|masks[j])
        cand=FULL
        mm=missing
        while mm and cand:
            b=mm & -mm
            cand &= cover[b.bit_length()-1]
            mm -= b
        if not cand:
            continue
        cand &= ~((1<<j)-1)
        while cand:
            b=cand & -cand
            k=b.bit_length()-1
            valid.append((i,j,k))
            cand -= b
assert len(valid)==210
assert all(len(set(t))==3 for t in valid)

# Canonicalize under relabelling the seven codewords. Coordinate permutations
# are already handled by sorting the partition-index triple.
perms=list(permutations(range(N)))
def canon_rgs(seq):
    mp={}; nxt=0; out=[]
    for x in seq:
        if x not in mp:
            mp[x]=nxt; nxt+=1
        out.append(mp[x])
    return tuple(out)

def transform_part(p,perm):
    q=[None]*N
    for old in range(N):
        q[perm[old]]=p[old]
    return pidx[canon_rgs(q)]

classes=defaultdict(list)
for t in valid:
    best=None
    for perm in perms:
        x=tuple(sorted(transform_part(parts[idx],perm) for idx in t))
        if best is None or x<best:
            best=x
    classes[best].append(t)
assert len(classes)==2
class_items=sorted(classes.items())
assert sorted(len(v) for _,v in class_items)==[105,105]

expected_codes={
    tuple(sorted(['000','011','022','103','204','330','440'])),
    tuple(sorted(['000','011','022','133','234','343','444'])),
}

def code_from_tuple(t):
    ps=[parts[i] for i in t]
    return tuple(sorted(''.join(str(ps[c][v]) for c in range(3)) for v in range(N)))
rep_codes={code_from_tuple(t) for t,_ in class_items}
assert rep_codes==expected_codes

# Direct descendant-definition verification on representatives.
def descendants(coal):
    out={()}
    for pos in range(3):
        vals={w[pos] for w in coal}
        out={prefix+(v,) for prefix in out for v in vals}
    return out

def is_ipp(code):
    words=[tuple(map(int,w)) for w in code]
    coalitions=[]
    for r in (1,2):
        for idxs in combinations(range(len(words)),r):
            coal=tuple(words[i] for i in idxs)
            coalitions.append((set(idxs),descendants(coal)))
    ys=set().union(*(d for _,d in coalitions))
    for y in ys:
        parents=[idxs for idxs,d in coalitions if y in d]
        common=set.intersection(*parents)
        if not common:
            return False
    return True
assert all(is_ipp(code) for code in expected_codes)
assert all(is_ipp(code_from_tuple(t)) for t in valid)

# Stabilizer in (S_5)^3 semidirect S_3 equals the automorphism count of the
# full five-block partition structure, since every representative uses all
# five symbols in every coordinate.
coordperms=list(permutations(range(3)))
def aut_count(t):
    ps=[parts[i] for i in t]
    ans=0
    for perm in perms:
        tr=[transform_part(p,perm) for p in ps]
        for cp in coordperms:
            if all(tr[cp[c]]==t[c] for c in range(3)):
                ans+=1
    return ans
stabs=sorted(aut_count(t) for t,_ in class_items)
assert stabs==[48,48]
G=math.factorial(5)**3*math.factorial(3)
orbits=[G//s for s in stabs]
assert orbits==[216000,216000]
assert sum(orbits)==432000

# Every coordinate has five blocks; profiles distinguish the two classes.
def profile(code):
    hp=Counter()
    words=[tuple(map(int,w)) for w in code]
    for a,b in combinations(words,2):
        hp[sum(x!=y for x,y in zip(a,b))]+=1
    return tuple(hp.get(d,0) for d in (1,2,3))
profiles=sorted(profile(code) for code in expected_codes)
assert profiles==[(0,7,14),(0,9,12)]
for t,_ in class_items:
    assert all(len(set(parts[idx]))==5 for idx in t)

valid_blob='\n'.join(','.join(map(str,t)) for t in valid).encode()
summary={
    'partitions':len(parts),
    'ipp1_conditions':len(triples),
    'ipp2_conditions':len(pairconds),
    'valid_unordered_partition_triples':len(valid),
    'equivalence_classes':len(classes),
    'class_partition_counts':sorted(len(v) for v in classes.values()),
    'natural_group_order':G,
    'orbit_sizes':orbits,
    'stabilizers':stabs,
    'literal_maximum_codes':sum(orbits),
    'distance_profiles':profiles,
    'representatives':sorted(','.join(c) for c in expected_codes),
    'valid_triples_sha256':hashlib.sha256(valid_blob).hexdigest(),
}
print('VERIFY_OK '+json.dumps(summary,sort_keys=True,separators=(',',':')))
