#!/usr/bin/env python3
from itertools import combinations, product, permutations
from collections import Counter, defaultdict

N=5
ALL=range(1<<N)

def parity(x): return x.bit_count() & 1

def span(rows):
    s={0}
    for r in rows:
        s |= {x^r for x in list(s)}
    return frozenset(s)

def span_alt(rows):
    # independent subset-XOR construction used only by Method B
    rows=list(rows); out=set()
    for mask in range(1<<len(rows)):
        x=0
        for j,r in enumerate(rows):
            if (mask>>j)&1: x ^= r
        out.add(x)
    return frozenset(out)

def rank(rows):
    rows=list(rows)
    r=0
    for c in range(N):
        p=next((j for j in range(r,len(rows)) if (rows[j]>>c)&1),None)
        if p is None: continue
        rows[r],rows[p]=rows[p],rows[r]
        for j in range(len(rows)):
            if j!=r and ((rows[j]>>c)&1): rows[j]^=rows[r]
        r+=1
    return r

def rank_alt(rows):
    # independent highest-bit basis insertion used only by Method B
    basis=[0]*N
    for x in rows:
        y=x
        while y:
            b=y.bit_length()-1
            if basis[b]: y ^= basis[b]
            else:
                basis[b]=y; break
    return sum(v!=0 for v in basis)

def all_subspaces_dim(k):
    if k==0: return {frozenset({0})}
    out=set()
    for rows in combinations(range(1,1<<N),k):
        if rank(rows)==k: out.add(span(rows))
    return out

def valid_rowspace(R):
    for i in range(N):
        allowed=(1<<i)|(1<<((i-1)%N))|(1<<((i+1)%N))
        if not any(((r>>i)&1) and not (r & ~allowed) for r in R):
            return False
    return True

def fitting_rows_choices(i):
    e=1<<i; a=1<<((i-1)%N); b=1<<((i+1)%N)
    return [e, e^a, e^b, e^a^b]

def permute_word(x,p):
    y=0
    for i in range(N):
        if (x>>i)&1: y |= 1<<p[i]
    return y

def transform_space(R,p): return frozenset(permute_word(x,p) for x in R)

def dihedral_perms():
    ps=[]
    for a in (1,-1):
        for b in range(N):
            ps.append(tuple((a*i+b)%N for i in range(N)))
    assert len(set(ps))==10
    return list(dict.fromkeys(ps))

def canonical_basis(R):
    # lexicographically smallest independent triple of nonzero words
    for t in combinations(sorted(R-{0}),3):
        if span(t)==R: return t
    raise AssertionError

def bits(x):
    return ''.join(str((x>>i)&1) for i in range(N))

def weight_enum(R):
    c=Counter(x.bit_count() for x in R)
    return tuple(c[i] for i in range(N+1))

# Method A: enumerate all row spaces in F_2^5 and apply the decoding criterion.
subspaces={k:all_subspaces_dim(k) for k in range(6)}
expected_gaussian=[1,31,155,155,31,1]
assert [len(subspaces[k]) for k in range(6)]==expected_gaussian
valid={k:sorted((R for R in subspaces[k] if valid_rowspace(R)), key=lambda R:tuple(sorted(R))) for k in range(6)}
valid_counts=[len(valid[k]) for k in range(6)]
assert valid_counts==[0,0,0,20,16,1], valid_counts
opt=set(valid[3])

# Method B: independently enumerate all 4^5 fitting matrices. Their row spaces are index-code row spaces.
rankdist=Counter(); rank3_spaces=Counter()
for choice in product(range(4), repeat=N):
    rows=[fitting_rows_choices(i)[choice[i]] for i in range(N)]
    r=rank_alt(rows); rankdist[r]+=1
    if r==3: rank3_spaces[span_alt(rows)]+=1
assert rankdist==Counter({3:45,4:537,5:442}), rankdist
assert set(rank3_spaces)==opt and len(rank3_spaces)==20
assert Counter(rank3_spaces.values())==Counter({1:5,2:10,4:5})

# Natural side-information automorphisms: D_10 acting on the five message coordinates.
D=dihedral_perms(); unseen=set(opt); orbits=[]
while unseen:
    R=min(unseen,key=lambda S:tuple(sorted(S)))
    orb={transform_space(R,p) for p in D}
    assert orb<=opt
    orbits.append(orb); unseen-=orb
assert sorted(map(len,orbits))==[5,5,5,5]
reps=[]
for orb in sorted(orbits,key=lambda O:weight_enum(min(O,key=lambda S:tuple(sorted(S))))):
    R=min(orb,key=lambda S:tuple(sorted(S)))
    stabilizer=sum(transform_space(R,p)==R for p in D)
    assert stabilizer==2
    reps.append((R,weight_enum(R),rank3_spaces[R]))
# Four distinct weight enumerators distinguish the four natural orbits.
assert len({w for _,w,_ in reps})==4

# Each 3-space has |GL(3,2)|=(8-1)(8-2)(8-4)=168 ordered bases, i.e. full-rank 3x5 encoders.
assert 20*168==3360

print('SUBSPACES_BY_DIM=' + ','.join(map(str,expected_gaussian)))
print('VALID_BY_DIM=' + ','.join(map(str,valid_counts)))
print('FITTING_RANKS=' + ','.join(f'{r}:{rankdist[r]}' for r in sorted(rankdist)))
print('FITTING_MULTIPLICITIES=' + ','.join(f'{m}:{Counter(rank3_spaces.values())[m]}' for m in sorted(set(rank3_spaces.values()))))
print('DIHEDRAL_ORBITS=' + ','.join(map(str,sorted(map(len,orbits)))))
for j,(R,w,mult) in enumerate(reps,1):
    b=canonical_basis(R)
    print(f'ORBIT_{j}_WEIGHT_ENUM=' + ','.join(map(str,w)) + ';REP_BASIS=' + '/'.join(bits(x) for x in b) + f';FITTING_COUNT={mult}')
print('VERIFY_OK min_linear_length=3 optimal_rowspaces=20 full_rank_3x5_encoders=3360 fitting_rank3=45 dihedral_orbits=4 orbit_sizes=5,5,5,5 stabilizer=2')
