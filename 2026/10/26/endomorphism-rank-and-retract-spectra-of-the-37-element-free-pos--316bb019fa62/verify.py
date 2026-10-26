#!/usr/bin/env python3
from collections import Counter, defaultdict

checks = 0

def ok(cond, msg='assertion failed'):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

# Seven modal iterates from Moraschini Fact 5.2:
# 0=x, 1=Box x, 2=Diamond Box x, 3=Box Diamond Box x,
# 4=Diamond x, 5=Box Diamond x, 6=Diamond Box Diamond x.
# Hasse covers p<q of the seven-element generating poset.
covers = {(1,0),(0,4),(1,3),(3,2),(3,5),(2,6),(5,6),(6,4)}
le = {(i,i) for i in range(7)} | set(covers)
changed = True
while changed:
    changed = False
    for a,b in tuple(le):
        for c,d in tuple(le):
            if b == c and (a,d) not in le:
                le.add((a,d)); changed = True

# Check these really are exactly the covers of the closure.
derived = set()
for a,b in le:
    if a == b:
        continue
    if not any(c not in (a,b) and (a,c) in le and (c,b) in le for c in range(7)):
        derived.add((a,b))
ok(derived == covers)

# Q = isotone maps P -> 2, encoded as upsets of P.
def is_upset_P(U):
    return all(i not in U or all(j in U for j in range(7) if (i,j) in le)
               for i in range(7))
Q = []
for mask in range(1 << 7):
    U = frozenset(i for i in range(7) if (mask >> i) & 1)
    if is_upset_P(U):
        Q.append(U)
Q = tuple(Q)
ok(len(Q) == 14)

# L = Up(Q), the free bounded distributive lattice on P.
def is_upset_Q(S):
    return all(i not in S or all(j in S for j in range(len(Q)) if Q[i] <= Q[j])
               for i in range(len(Q)))
L = []
for mask in range(1 << len(Q)):
    S = frozenset(i for i in range(len(Q)) if (mask >> i) & 1)
    if is_upset_Q(S):
        L.append(S)
L = sorted(L, key=lambda s:(len(s),tuple(sorted(s))))
Lset = set(L)
idx = {s:i for i,s in enumerate(L)}
ok(len(L) == 37)
zero = frozenset()
one = frozenset(range(len(Q)))

# Generator p is {q in Q : p in q}.
gen = tuple(frozenset(k for k,q in enumerate(Q) if p in q) for p in range(7))
for g in gen:
    ok(g in Lset)

# Figure 1 / the Box partition in the proof gives precisely these fixed points.
box_fixed = {zero, gen[1], gen[3], gen[5], one}
dia_fixed = {zero, gen[2], gen[4], gen[6], one}

def box(x):
    cand = [z for z in box_fixed if z <= x]
    mx = [z for z in cand if not any(z < y for y in cand)]
    ok(len(mx) == 1, 'Box fixed-point maximum is not unique')
    return mx[0]

def dia(x):
    cand = [z for z in dia_fixed if x <= z]
    mn = [z for z in cand if not any(y < z for y in cand)]
    ok(len(mn) == 1, 'Diamond fixed-point minimum is not unique')
    return mn[0]

# Check modal S4 behavior directly on the 37-element lattice.
for x in L:
    ok(box(x) <= x)
    ok(x <= dia(x))
    ok(box(box(x)) == box(x))
    ok(dia(dia(x)) == dia(x))
for x in L:
    for y in L:
        ok(box(x & y) == (box(x) & box(y)))
        ok(dia(x | y) == (dia(x) | dia(y)))
ok(box(one) == one)
ok(dia(zero) == zero)

# Modal iterates of the free generator reproduce the seven distinguished generators.
def seven(t):
    return (
        t,
        box(t),
        dia(box(t)),
        box(dia(box(t))),
        dia(t),
        box(dia(t)),
        dia(box(dia(t))),
    )
ok(seven(gen[0]) == gen)

# Every S in Up(Q) has the monotone DNF obtained from its minimal Q-points.
def minimal_q_indices(S):
    return [i for i in S if not any(j in S and Q[j] < Q[i] for j in S)]

def eval_dnf(S, vals):
    out = zero
    for qi in minimal_q_indices(S):
        term = one
        for p in Q[qi]:
            term = term & vals[p]
        out = out | term
    return out

for S in L:
    ok(eval_dnf(S, gen) == S)

# Freeness: for each possible image t of x, evaluate the source's universal-map formula.
endomaps = {}
for t in L:
    vals = seven(t)
    h = tuple(idx[eval_dnf(S, vals)] for S in L)
    endomaps[idx[t]] = h

ok(len(endomaps) == 37)
ok(len(set(endomaps.values())) == 37)

# Full operation-preservation check for every endomorphism.
for ti,h in endomaps.items():
    ok(h[idx[zero]] == idx[zero])
    ok(h[idx[one]] == idx[one])
    for x in L:
        hx = L[h[idx[x]]]
        ok(h[idx[box(x)]] == idx[box(hx)])
        ok(h[idx[dia(x)]] == idx[dia(hx)])
        for y in L:
            hy = L[h[idx[y]]]
            ok(h[idx[x & y]] == idx[hx & hy])
            ok(h[idx[x | y]] == idx[hx | hy])

# Independently close each singleton under the four operations and compare with h[F].
def generated_by(t):
    S = {zero, one, t}
    changed = True
    while changed:
        changed = False
        old = tuple(S)
        additions = {box(x) for x in old} | {dia(x) for x in old}
        additions |= {x & y for x in old for y in old}
        additions |= {x | y for x in old for y in old}
        if not additions <= S:
            S |= additions
            changed = True
    return frozenset(idx[x] for x in S)

images = {}
for ti,h in endomaps.items():
    im = frozenset(h)
    images[ti] = im
    ok(im == generated_by(L[ti]), 'image != singleton-generated subalgebra')

rank_distribution = Counter(len(im) for im in images.values())
expected_rank_distribution = {
    2:2, 4:4, 5:10, 6:2, 8:4, 10:2, 12:2, 13:1,
    16:2, 17:2, 22:1, 23:2, 29:2, 37:1
}
ok(dict(sorted(rank_distribution.items())) == expected_rank_distribution)

# Composition/idempotence census.
def compose(f,g):
    return tuple(f[j] for j in g)

idempotent = {}
nonid = {}
for ti,h in endomaps.items():
    if compose(h,h) == h:
        idempotent[ti] = h
    else:
        nonid[ti] = h
ok(len(idempotent) == 31)
ok(len(nonid) == 6)

idem_rank_distribution = Counter(len(set(h)) for h in idempotent.values())
expected_idem_rank_distribution = {
    2:2, 4:4, 5:6, 6:2, 8:2, 10:2, 12:2, 13:1,
    16:2, 17:2, 22:1, 23:2, 29:2, 37:1
}
ok(dict(sorted(idem_rank_distribution.items())) == expected_idem_rank_distribution)

nonid_transition = Counter()
for ti,h in nonid.items():
    h2 = compose(h,h)
    h3 = compose(h,h2)
    ok(h2 in set(idempotent.values()))
    ok(h3 == h2)
    nonid_transition[(len(set(h)), len(set(h2)))] += 1
ok(nonid_transition == Counter({(5,4):4, (8,6):2}))

# Distinct one-generated subalgebras and retract subalgebras.
all_subalgebras = set(images.values())
retract_subalgebras = {frozenset(h) for h in idempotent.values()}
ok(len(all_subalgebras) == 33)
ok(len(retract_subalgebras) == 27)

subalg_size_distribution = Counter(len(s) for s in all_subalgebras)
expected_subalg = {
    2:1, 4:2, 5:10, 6:2, 8:4, 10:1, 12:2, 13:1,
    16:2, 17:2, 22:1, 23:2, 29:2, 37:1
}
ok(dict(sorted(subalg_size_distribution.items())) == expected_subalg)

retract_size_distribution = Counter(len(s) for s in retract_subalgebras)
expected_retract = {
    2:1, 4:2, 5:6, 6:2, 8:2, 10:1, 12:2, 13:1,
    16:2, 17:2, 22:1, 23:2, 29:2, 37:1
}
ok(dict(sorted(retract_size_distribution.items())) == expected_retract)

nonretract = all_subalgebras - retract_subalgebras
ok(len(nonretract) == 6)
ok(Counter(len(s) for s in nonretract) == Counter({5:4,8:2}))

print('endomorphism_rank_distribution', dict(sorted(rank_distribution.items())))
print('idempotent_rank_distribution', dict(sorted(idem_rank_distribution.items())))
print('one_generated_subalgebras', len(all_subalgebras))
print('retract_subalgebras', len(retract_subalgebras))
print('nonretract_size_distribution', dict(sorted(Counter(len(s) for s in nonretract).items())))
print(f'VERIFY_OK {checks} exact assertions; 37 endomorphisms reconstructed and checked operation-by-operation')
