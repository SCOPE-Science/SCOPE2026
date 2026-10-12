from itertools import product, permutations
from collections import Counter
import hashlib

Q=3
N=4
WORDS=list(product(range(Q), repeat=N))
INDEX={w:i for i,w in enumerate(WORDS)}

def deletion_shadow(w):
    return frozenset(w[:i]+w[i+1:] for i in range(N))

SHADOW=[deletion_shadow(w) for w in WORDS]
ADJ=[]
for i in range(len(WORDS)):
    mask=0
    for j in range(len(WORDS)):
        if i != j and SHADOW[i].isdisjoint(SHADOW[j]):
            mask |= 1 << j
    ADJ.append(mask)

max_size=0
maximal_count=0
maxima=[]
size_distribution=Counter()

def bron_kerbosch(R,P,X):
    global max_size,maximal_count,maxima
    if not P and not X:
        maximal_count += 1
        s=R.bit_count()
        size_distribution[s] += 1
        if s > max_size:
            max_size=s
            maxima=[R]
        elif s == max_size:
            maxima.append(R)
        return
    U=P|X
    if U:
        best=-1
        best_count=-1
        T=U
        while T:
            b=T & -T
            u=b.bit_length()-1
            c=(P & ADJ[u]).bit_count()
            if c > best_count:
                best_count=c
                best=u
            T ^= b
        candidates=P & ~ADJ[best]
    else:
        candidates=P
    while candidates:
        b=candidates & -candidates
        v=b.bit_length()-1
        bron_kerbosch(R|b, P & ADJ[v], X & ADJ[v])
        P ^= b
        X |= b
        candidates ^= b

bron_kerbosch(0,(1<<len(WORDS))-1,0)

def count_k_cliques(k):
    total=0
    def rec(P,depth):
        nonlocal total
        need=k-depth
        if need == 0:
            total += 1
            return
        while P:
            if P.bit_count() < need:
                return
            b=P & -P
            v=b.bit_length()-1
            P ^= b
            rec(P & ADJ[v],depth+1)
    rec((1<<len(WORDS))-1,0)
    return total

count11=count_k_cliques(11)
count12=count_k_cliques(12)
assert max_size == 11
assert len(maxima) == 6
assert count11 == 6 and count12 == 0

def code_from_mask(mask):
    return frozenset(WORDS[i] for i in range(len(WORDS)) if (mask>>i)&1)

MAX_CODES=[code_from_mask(m) for m in maxima]
for C in MAX_CODES:
    assert len(C)==11
    shadows=[SHADOW[INDEX[w]] for w in C]
    assert all(shadows[i].isdisjoint(shadows[j]) for i in range(11) for j in range(i))

CORE=set.intersection(*(set(C) for C in MAX_CODES))
EXPECTED_CORE={(a,a,b,b) for a in range(Q) for b in range(Q)}
assert CORE == EXPECTED_CORE
SPECIAL=sorted(set.union(*(set(C) for C in MAX_CODES))-CORE)
EXPECTED_SPECIAL={(a,b,c,a) for a,b,c in permutations(range(Q),3)}
assert set(SPECIAL) == EXPECTED_SPECIAL
EDGES={tuple(sorted(set(C)-CORE)) for C in MAX_CODES}
assert len(EDGES)==6
special_degree=Counter()
for u,v in EDGES:
    special_degree[u]+=1
    special_degree[v]+=1
assert len(special_degree)==6 and set(special_degree.values())=={2}

PERMS=list(permutations(range(Q)))
def transform_word(w,p,reverse):
    z=tuple(p[a] for a in w)
    return z[::-1] if reverse else z

def transform_code(C,p,reverse):
    return frozenset(transform_word(w,p,reverse) for w in C)

GROUP=[(p,r) for p in PERMS for r in (False,True)]
assert len(GROUP)==12
REP=MAX_CODES[0]
ORBIT={transform_code(REP,p,r) for p,r in GROUP}
STAB=[(p,r) for p,r in GROUP if transform_code(REP,p,r)==REP]
assert ORBIT == set(MAX_CODES)
assert len(ORBIT)==6 and len(STAB)==2

def wstr(w):
    return ''.join(str(x) for x in w)
CANON=sorted(' '.join(sorted(wstr(w) for w in C)) for C in MAX_CODES)
CENSUS=('\n'.join(CANON)+'\n').encode('utf-8')
CENSUS_SHA256=hashlib.sha256(CENSUS).hexdigest()
assert CENSUS_SHA256 == '0fdfab77f115f24f9c37c8cf153819f8d380b7e269ae7be3a039a018133a0a16'
print('VERIFY_OK')
print('vertices',len(WORDS))
print('maximal_cliques',maximal_count)
print('maximal_size_distribution',','.join(f'{k}:{size_distribution[k]}' for k in sorted(size_distribution)))
print('maximum',max_size)
print('maximum_codes',len(MAX_CODES))
print('count11',count11)
print('count12',count12)
print('core_size',len(CORE))
print('special_cycle_vertices',len(SPECIAL))
print('special_cycle_edges',len(EDGES))
print('natural_group',len(GROUP))
print('orbits',1)
print('orbit_size',len(ORBIT))
print('stabilizer',len(STAB))
print('census_sha256',CENSUS_SHA256)
