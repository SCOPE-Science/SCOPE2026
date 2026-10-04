from itertools import product, combinations, permutations

# Eisenstein integers a+b*w, w^2+w+1=0, represented as pairs (a,b).
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    a,b=x; c,d=y
    # (a+bw)(c+dw)=ac + (ad+bc)w + bd w^2, w^2=-1-w
    return (a*c-b*d, a*d+b*c-b*d)
def smul(n,x): return (n*x[0],n*x[1])
def iszero(x): return x==(0,0)
ZERO=(0,0); ONE=(1,0); W=(0,1); W2=(-1,-1)
ROOTS=(ONE,W,W2)
PTS=[(ONE,x,y,z) for x in ROOTS for y in ROOTS for z in ROOTS]

def det3(rows, cols):
    s=ZERO
    for p in permutations(range(3)):
        inv=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        t=ONE
        for i in range(3): t=mul(t, rows[i][cols[p[i]]])
        s=add(s, neg(t) if inv&1 else t)
    return s

def nullvec3(rows):
    out=[]
    for j in range(4):
        cols=[k for k in range(4) if k!=j]
        d=det3(rows,cols)
        if j&1: d=neg(d)
        out.append(d)
    return tuple(out)

def dot(p,c):
    s=ZERO
    for x,y in zip(p,c): s=add(s,mul(x,y))
    return s

def rank_ge3(rows4):
    # enough to find a nonzero 3x3 minor among any three rows and any three cols
    for ridx in combinations(range(4),3):
        rs=[rows4[i] for i in ridx]
        for cols in combinations(range(4),3):
            if not iszero(det3(rs,cols)):
                return True
    return False

# 1) No four evaluation rows have rank <=2.
lowrank4=0
for inds in combinations(range(27),4):
    if not rank_ge3([PTS[i] for i in inds]):
        lowrank4 += 1
assert lowrank4==0

# 2) Enumerate every rank-3 triple. For unique hyperplanes with all four coefficients nonzero,
#    total grid-zero count is 3 or 5 only.
counts={}
triple_total=0
rank3_nonzero_coeff=0
maxzeros=0
for inds in combinations(range(27),3):
    rows=[PTS[i] for i in inds]
    c=nullvec3(rows)
    if all(iszero(x) for x in c):
        continue  # rank <=2 triple
    triple_total += 1
    if any(iszero(x) for x in c):
        continue
    rank3_nonzero_coeff += 1
    z=tuple(i for i,p in enumerate(PTS) if iszero(dot(p,c)))
    k=len(z)
    counts[k]=counts.get(k,0)+1
    maxzeros=max(maxzeros,k)
assert set(counts)=={3,5}, counts
assert maxzeros==5

# 3) Exact witnesses for each possible zero count.
witnesses={
    0: ((1,0),(1,0),(1,0),(1,0)),
    1: ((-3,0),(-1,0),(2,0),(2,0)),
    2: ((-3,0),(-3,0),(-2,0),(-1,0)),
    3: ((-3,0),(-2,0),(2,0),(3,0)),
    5: ((-1,0),(-1,0),(1,0),(1,0)),
}
for k,c in witnesses.items():
    assert all(not iszero(x) for x in c)
    z=sum(iszero(dot(p,c)) for p in PTS)
    assert z==k,(k,z)

print('lowrank4=',lowrank4)
print('rank3_triples=',triple_total)
print('rank3_all_nonzero_coeff=',rank3_nonzero_coeff)
print('intersection_counts=',sorted(counts.items()))
print('witness_zero_counts=',sorted(witnesses))
print('VERIFY_OK')
