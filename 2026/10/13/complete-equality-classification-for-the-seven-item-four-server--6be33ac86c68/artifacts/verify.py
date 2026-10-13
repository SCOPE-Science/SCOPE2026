from itertools import combinations, combinations_with_replacement, permutations
from collections import Counter
from math import factorial

SERVERS=range(4)
SETS=tuple(range(1,16))

def pc(x): return x.bit_count()

def hall_direct(code):
    # Items are positions, so duplicate storage sets are distinct items.
    n=len(code)
    for r in (1,2,3):
        for I in combinations(range(n),r):
            u=0
            for i in I: u |= code[i]
            if pc(u)<r: return False
    return True

def hall_count(code):
    # Equivalent Hall test: every server subset U of size 1 or 2 contains at most |U| stored items.
    # For k=3 only subsets with |U|<3 can violate Hall.
    for U in SETS:
        s=pc(U)
        if s>=3: continue
        c=sum(1 for F in code if F & ~U == 0)
        if c>s: return False
    return True

def perm_mask(x,p):
    y=0
    for i in SERVERS:
        if x>>i & 1: y |= 1<<p[i]
    return y

def perm_code(code,p): return tuple(sorted(perm_mask(x,p) for x in code))

# Exhaustive ambient census: C(15+7-1,7)=116280 multisets.
best=10**9
opts=[]
valid_count=0
for code in combinations_with_replacement(SETS,7):
    a=hall_direct(code)
    b=hall_count(code)
    if a != b:
        raise AssertionError(('predicate mismatch',code,a,b))
    if not a: continue
    valid_count += 1
    s=sum(pc(x) for x in code)
    if s<best: best=s; opts=[code]
    elif s==best: opts.append(code)
assert best==12
assert len(opts)==46
S=set(opts)

# Four canonical types on labeled servers {1,2,3,4} encoded by bits 0..3.
# T1/T2: three singleton items on 1,2,3; star pairs to 4; triple either 123 or 124.
T1=tuple(sorted([1,2,4, 1|8,2|8,4|8, 1|2|4]))
T2=tuple(sorted([1,2,4, 1|8,2|8,4|8, 1|2|8]))
# T3: singletons 1,2 and every allowed pair except 12.
T3=tuple(sorted([1,2, 1|4,1|8,2|4,2|8,4|8]))
# T4: singletons 1,2, pair 34 doubled, and one cross-edge omitted (here 24 omitted).
T4=tuple(sorted([1,2, 1|4,1|8,2|4,4|8,4|8]))
REPS=(T1,T2,T3,T4)

perms=list(permutations(SERVERS))
orbits=[]
for rep in REPS:
    orb={perm_code(rep,p) for p in perms}
    orbits.append(orb)
assert [len(o) for o in orbits]==[4,12,6,24]
assert len(set().union(*orbits))==46
assert set().union(*orbits)==S
assert [24//len(o) for o in orbits]==[6,2,4,1]

# Structural proof conditions for every optimum.
def profile(code):
    return tuple(sum(pc(F)==j for F in code) for j in (1,2,3,4))
profiles=Counter(profile(c) for c in opts)
assert set(profiles)=={(3,3,1,0),(2,5,0,0)}
assert profiles[(3,3,1,0)]==16
assert profiles[(2,5,0,0)]==30

# Labeled-item count: each storage multiset has 7!/prod multiplicity! labelings.
def item_labelings(code):
    den=1
    for v in Counter(code).values(): den*=factorial(v)
    return factorial(7)//den
labeled=sum(item_labelings(c) for c in opts)
assert labeled==171360

# Published optimum formula specializes to 12: 2n-floor((2*C(m,2)-n)/(m-2)).
from math import comb
n,k,m=7,3,4
formula=(k-1)*n - ((k-1)*comb(m,k-1)-n)//(m-k+1)
assert formula==12

# Independent hand-structure checks encoded as assertions.
# At storage 12, let a_j be the number of j-server items. Algebra gives a1=a3+2a4+2.
for code in opts:
    a=profile(code)
    assert a[0]==a[2]+2*a[3]+2
    # singleton items are on distinct servers
    sing=[F for F in code if pc(F)==1]
    assert len(sing)==len(set(sing))

print('VERIFY_OK ambient=116280 valid=%d optimum=12 unlabeled_server_fixed=46 orbit_sizes=4,12,6,24 stabilizers=6,2,4,1 profiles=3-3-1-0:16,2-5-0-0:30 labeled_incidence=171360 predicates_agree=true structural_union=true' % valid_count)
