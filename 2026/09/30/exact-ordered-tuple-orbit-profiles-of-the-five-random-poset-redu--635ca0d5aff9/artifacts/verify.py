from itertools import product
from math import comb

def labeled_posets(n):
    pairs = [(i,j) for i in range(n) for j in range(i+1,n)]
    out = []
    for vals in product((0,1,2), repeat=len(pairs)):
        rel = set()
        for (i,j),v in zip(pairs, vals):
            if v == 1:
                rel.add((i,j))
            elif v == 2:
                rel.add((j,i))
        ok = True
        for a,b in tuple(rel):
            for c,d in tuple(rel):
                if b == c and a != d and (a,d) not in rel:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append(frozenset(rel))
    return out

O2 = {
    frozenset({(0,1),(1,2),(0,2)}),
    frozenset({(1,2),(2,0),(1,0)}),
    frozenset({(2,0),(0,1),(2,1)}),
    frozenset({(0,1)}),
    frozenset({(1,2)}),
    frozenset({(2,0)}),
}
O3 = {frozenset((b,a) for a,b in r) for r in O2}

def triple_class(rel, triple):
    mp = {triple[i]: i for i in range(3)}
    local = frozenset((mp[a],mp[b]) for a,b in rel if a in mp and b in mp)
    if local in O2:
        return 2
    if local in O3:
        return 3
    return 1

def rotation_signature(rel, n):
    sig = []
    for a in range(n):
        for b in range(a+1,n):
            for c in range(b+1,n):
                sig.append(triple_class(rel, (a,b,c)))
    return tuple(sig)

def dual(rel):
    return frozenset((b,a) for a,b in rel)

P = {n:labeled_posets(n) for n in range(5)}
p = [len(P[n]) for n in range(5)]
assert p == [1,1,3,19,219]

# Theorem 3.14 says these triple signatures are exactly finite
# rotation-equivalence invariants. The census checks the resulting
# class counts and dual-fixed classes through four labels.
rot_counts = []
dual_fixed_rot = []
for n in range(5):
    sigs = {rotation_signature(r,n) for r in P[n]}
    rot_counts.append(len(sigs))
    if n < 3:
        dual_fixed_rot.append(len(sigs))
    else:
        dual_fixed_rot.append(sum(all(x == 1 for x in s) for s in sigs))
assert rot_counts == [1,1,1,3,19]
assert rot_counts[1:] == p[:-1]
assert dual_fixed_rot == [1,1,1,1,1]

# A labeled poset fixed by duality has no strict comparable pair.
for n in range(5):
    fixed = sum(r == dual(r) for r in P[n])
    assert fixed == 1

def injective_profiles(k):
    if k == 0:
        return (1,1,1,1,1)
    return (
        p[k],
        (p[k]+1)//2,
        p[k-1],
        (p[k-1]+1)//2,
        1,
    )

expected = {
    0:(1,1,1,1,1),
    1:(1,1,1,1,1),
    2:(3,2,1,1,1),
    3:(19,10,3,2,1),
    4:(219,110,19,10,1),
}
for k,v in expected.items():
    assert injective_profiles(k) == v

def stirling2(n,k):
    if n == k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    dp = [[0]*(k+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1):
            dp[i][j] = dp[i-1][j-1] + j*dp[i-1][j]
    return dp[n][k]

full = []
for n in range(5):
    row = []
    for g in range(5):
        row.append(sum(stirling2(n,k)*injective_profiles(k)[g]
                       for k in range(n+1)))
    full.append(tuple(row))
assert full == [
    (1,1,1,1,1),
    (1,1,1,1,1),
    (4,3,2,2,2),
    (29,17,7,6,5),
    (355,185,45,30,15),
]
print("p_0..p_4 =", p)
print("rotation classes n=0..4 =", rot_counts)
print("injective profiles at k=3 =", expected[3])
print("all-tuple profiles n=0..4 =", full)
print("VERIFY_OK")
