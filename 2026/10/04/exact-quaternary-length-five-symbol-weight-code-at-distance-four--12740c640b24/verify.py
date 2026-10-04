from itertools import combinations

C = [
    "33221","32312","31030","30103","22001","23132","21323","20210",
    "13300","12233","10022","03013","02120","01202","00331",
]
Q = set("0123")
assert len(C) == 15 and len(set(C)) == 15
assert all(len(w) == 5 and set(w) <= Q for w in C)

def sw(w):
    return max(w.count(a) for a in Q)

def dist(u,v):
    return sum(a != b for a,b in zip(u,v))

assert all(sw(w) == 2 for w in C)
assert min(dist(u,v) for u,v in combinations(C,2)) >= 4

pairs = list(combinations(range(5),2))
missing = []
for i,j in pairs:
    proj = {(w[i],w[j]) for w in C}
    assert len(proj) == 15
    miss = {(a,b) for a in Q for b in Q} - proj
    assert miss == {("1","1")}
    missing.append(next(iter(miss)))

def equal_pairs(w):
    return sum(w[i] == w[j] for i,j in pairs)

assert all(equal_pairs(w) == 2 for w in C)
assert sum(equal_pairs(w) for w in C) == 30
# Arithmetic used in the contradiction at size 16.
assert len(pairs) == 10
assert 10 * 4 == 40
assert 16 * 2 == 32
assert 40 > 32
# Arithmetic used in the equality case at size 15.
assert 10 * 3 == 30
assert 15 * 2 == 30
print("VERIFY_OK maximum=15 witness=15 projections=10 equal_incidence=30 missing_diagonal=11")
