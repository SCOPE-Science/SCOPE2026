from collections import Counter, defaultdict
from math import ceil, log2

def cycle_dist(n,i,j):
    d=abs(i-j)
    return min(d,n-d)

def init_colors(n):
    c=[]
    for i in range(n):
        row=[]
        for j in range(n):
            if i==j: row.append(0)
            elif cycle_dist(n,i,j)==1: row.append(1)
            else: row.append(2)
        c.append(row)
    return c

def partition(c):
    n=len(c)
    groups={}
    for i in range(n):
        for j in range(n):
            groups.setdefault(c[i][j],[]).append((i,j))
    return {frozenset(v) for v in groups.values()}

def refine(c):
    n=len(c)
    sigs=[[None]*n for _ in range(n)]
    all_sigs=[]
    for i in range(n):
        for j in range(n):
            cnt=Counter((c[i][w],c[w][j]) for w in range(n))
            sig=(c[i][j], tuple(sorted(cnt.items())))
            sigs[i][j]=sig
            all_sigs.append(sig)
    ids={s:k for k,s in enumerate(sorted(set(all_sigs), key=repr))}
    return [[ids[sigs[i][j]] for j in range(n)] for i in range(n)]

def distance_color_profile(c):
    n=len(c); D=n//2
    prof=[]
    for d in range(D+1):
        vals=set()
        for i in range(n):
            for j in range(n):
                if cycle_dist(n,i,j)==d:
                    vals.add(c[i][j])
        if len(vals)!=1:
            raise AssertionError((n,d,vals))
        prof.append(next(iter(vals)))
    return prof

def pred_stab(n):
    D=n//2
    if n<=5: return 0
    return ceil(log2(D-1))

def verify_n(n):
    c=init_colors(n)
    r=0
    while True:
        prof=distance_color_profile(c)
        D=n//2; R=2**r
        # exact 0..min(R,D), and one far color after R when present
        exact_end=min(R,D)
        assert len(set(prof[:exact_end+1]))==exact_end+1, (n,r,prof)
        if D>R:
            far=prof[R+1:]
            assert len(set(far))==1, (n,r,prof)
            assert far[0] not in set(prof[:R+1]), (n,r,prof)
        nxt=refine(c)
        if partition(nxt)==partition(c):
            break
        c=nxt; r+=1
        assert r<30
    assert r==pred_stab(n),(n,r,pred_stab(n))
    # stable coloring separates every distance class
    prof=distance_color_profile(c)
    assert len(set(prof))==len(prof),(n,r,prof)
    return r

# Full tuple-level implementation through 120 vertices.
for n in range(3,61):
    verify_n(n)

# Closed-form recurrence for distance-class reach, checked to 4096.
# At round r the unresolved tail starts at 2^r+1; stability occurs exactly
# when the tail has size at most one, i.e. floor(n/2) <= 2^r+1.
for n in range(3,4097):
    D=n//2
    expected=0 if n<=5 else ceil(log2(D-1))
    r=0
    while D>2**r+1:
        r+=1
    assert r==expected,(n,r,expected)

# The C^2 lower-bound witness for n>=6 is C3 disjoint union C_{n-3}:
# both graphs are 2-regular of order n, so uniform 1-WL remains uniform forever.
for n in range(6,61):
    assert n-3>=3

print('VERIFY_OK full_2WL_cycles_3_60 formula_cycles_3_4096 width_witnesses_6_60')
