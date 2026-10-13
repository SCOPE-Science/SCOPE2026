import itertools
from collections import Counter

# Fano plane: points 0..6, lines 7..13.
LINES = [
    {0,1,2}, {0,3,4}, {0,5,6}, {1,3,5},
    {1,4,6}, {2,3,6}, {2,4,5},
]
LINE_IDS = list(range(7,14))
LINE_PTS = dict(zip(LINE_IDS, LINES))

def is_point(x):
    return x < 7

def incident(a,b):
    if not is_point(a):
        a,b=b,a
    return is_point(a) and not is_point(b) and a in LINE_PTS[b]

def join(p,q):
    assert p != q and is_point(p) and is_point(q)
    vals=[l for l in LINE_IDS if p in LINE_PTS[l] and q in LINE_PTS[l]]
    assert len(vals)==1
    return vals[0]

def meet(l,r):
    assert l != r and not is_point(l) and not is_point(r)
    vals=LINE_PTS[l] & LINE_PTS[r]
    assert len(vals)==1
    return next(iter(vals))

def closure(tup):
    s=set(tup)
    while True:
        old=len(s)
        pts=[x for x in s if is_point(x)]
        ls=[x for x in s if not is_point(x)]
        for p,q in itertools.combinations(pts,2):
            s.add(join(p,q))
        for l,r in itertools.combinations(ls,2):
            s.add(meet(l,r))
        if len(s)==old:
            return s

def canonical_marked_closure(tup):
    s=closure(tup)
    pts=sorted(x for x in s if is_point(x))
    ls=sorted(x for x in s if not is_point(x))
    best=None
    # Canonicalize the finite incidence structure while retaining tuple positions as marks.
    for pp in itertools.permutations(range(len(pts))):
        mp={pts[i]:pp[i] for i in range(len(pts))}
        for ll in itertools.permutations(range(len(ls))):
            ml={ls[i]:len(pts)+ll[i] for i in range(len(ls))}
            m={**mp, **ml}
            invp={m[x]:x for x in pts}
            invl={m[x]:x for x in ls}
            inc=[]
            for i in range(len(pts)):
                for j in range(len(pts),len(pts)+len(ls)):
                    inc.append(int(incident(invp[i],invl[j])))
            key=(len(pts),len(ls),tuple(inc),tuple(m[x] for x in tup))
            if best is None or key < best:
                best=key
    return best

expected={1:2,2:8,3:48}
for n in (1,2,3):
    reps={}
    for tup in itertools.product(range(14), repeat=n):
        key=canonical_marked_closure(tup)
        reps[key]=len(closure(tup))
    assert len(reps)==expected[n], (n,len(reps))
    print(f"S_{n}_marked_closure_types={len(reps)}")
    print(f"S_{n}_closure_size_distribution={dict(sorted(Counter(reps.values()).items()))}")

inj={}
for tup in itertools.permutations(range(14),3):
    key=canonical_marked_closure(tup)
    inj[key]=len(closure(tup))
assert len(inj)==28
assert Counter(inj.values())==Counter({3:6,4:14,5:6,6:2})
print("injective_S_3_types=28")
print("injective_S_3_closure_size_distribution={3: 6, 4: 14, 5: 6, 6: 2}")
print("VERIFY_OK")
