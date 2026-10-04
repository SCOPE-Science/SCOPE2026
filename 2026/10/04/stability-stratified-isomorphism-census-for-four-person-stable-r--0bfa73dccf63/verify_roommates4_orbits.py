#!/usr/bin/env python3
import itertools, collections

N = 4
V = tuple(range(N))
PERMS = tuple(itertools.permutations(V))
PREFS = {i: tuple(itertools.permutations([j for j in V if j != i])) for i in V}
MATCHINGS = (
    ((0,1),(2,3)),
    ((0,2),(1,3)),
    ((0,3),(1,2)),
)

def profiles():
    for choices in itertools.product(range(6), repeat=4):
        yield tuple(PREFS[i][choices[i]] for i in V)

def stable_rank(profile, matching):
    partner = {}
    for a,b in matching:
        partner[a]=b; partner[b]=a
    rank = tuple({x:k for k,x in enumerate(profile[i])} for i in V)
    for i in V:
        for j in range(i+1,N):
            if partner[i] == j:
                continue
            if rank[i][j] < rank[i][partner[i]] and rank[j][i] < rank[j][partner[j]]:
                return False
    return True

def stable_prefix(profile, matching):
    partner = {}
    for a,b in matching:
        partner[a]=b; partner[b]=a
    above = {}
    for i in V:
        row = profile[i]
        above[i] = set(row[:row.index(partner[i])])
    for i in V:
        for j in range(i+1,N):
            if partner[i] == j:
                continue
            if j in above[i] and i in above[j]:
                return False
    return True

def nstable(profile):
    a = sum(stable_rank(profile,m) for m in MATCHINGS)
    b = sum(stable_prefix(profile,m) for m in MATCHINGS)
    assert a == b
    return a

def relabel(profile, sigma):
    out = [None]*N
    for i in V:
        out[sigma[i]] = tuple(sigma[j] for j in profile[i])
    return tuple(out)

def canonical(profile):
    return min(relabel(profile,s) for s in PERMS)

def cycle_type(sigma):
    seen=set(); parts=[]
    for i in V:
        if i not in seen:
            j=i; n=0
            while j not in seen:
                seen.add(j); n+=1; j=sigma[j]
            parts.append(n)
    return tuple(sorted(parts, reverse=True))

all_profiles = list(profiles())
assert len(all_profiles) == 6**4 == 1296

# Method A: direct orbit partition by canonical representative.
labeled = collections.Counter()
reps = {}
for p in all_profiles:
    k = nstable(p)
    labeled[k] += 1
    reps.setdefault(canonical(p), k)
assert all(reps[c] == nstable(c) for c in reps)
orbits_A = collections.Counter(reps.values())

# Orbit-size/stabilizer refinement.
orbit_size_dist = collections.Counter()
for c,k in reps.items():
    stab = sum(relabel(c,s) == c for s in PERMS)
    assert 24 % stab == 0
    orbit_size_dist[(k,24//stab)] += 1

# Method B: stability-stratified Burnside calculation.
fixed_by_type = collections.defaultdict(lambda: collections.Counter())
num_elements = collections.Counter()
for s in PERMS:
    ct = cycle_type(s)
    num_elements[ct] += 1
    for p in all_profiles:
        if relabel(p,s) == p:
            fixed_by_type[ct][nstable(p)] += 1
orbits_B = collections.Counter()
for k in range(4):
    total_fixed = sum(fixed_by_type[ct][k] for ct in fixed_by_type)
    assert total_fixed % 24 == 0
    orbits_B[k] = total_fixed // 24

assert labeled == collections.Counter({1:1098, 2:150, 0:48})
assert orbits_A == collections.Counter({1:51, 2:7, 0:2})
assert orbits_B == collections.Counter({1:51, 2:7, 0:2, 3:0})
assert sum(orbits_A.values()) == 60
assert labeled[0] == 48 and (labeled[1]+labeled[2]) * 27 == 26 * 1296
assert orbit_size_dist == collections.Counter({
    (0,24):2,
    (1,24):42,
    (1,12):6,
    (1,6):3,
    (2,24):6,
    (2,6):1,
})

# Burnside fixed-count table by conjugacy class, per group element.
expected_per_element = {
    (1,1,1,1): {0:48, 1:1098, 2:150, 3:0},
    (2,1,1):   {0:0, 1:0, 2:0, 3:0},
    (2,2):     {0:0, 1:34, 2:2, 3:0},
    (3,1):     {0:0, 1:0, 2:0, 3:0},
    (4,):      {0:0, 1:4, 2:2, 3:0},
}
for ct, exp in expected_per_element.items():
    e = num_elements[ct]
    got = {k: fixed_by_type[ct][k]//e for k in range(4)}
    assert got == exp, (ct, got, exp)

# The two unsolvable orbit representatives are exactly the two orientations
# of the classical 3-cycle obstruction, written canonically in zero-based labels.
uns = sorted(c for c,k in reps.items() if k == 0)
expected_uns = [
    ((1,2,3),(2,0,3),(0,1,3),(0,1,2)),
    ((1,2,3),(2,0,3),(0,1,3),(0,2,1)),
]
assert uns == expected_uns

print('VERIFY_OK')
print('labeled_by_stable_count', dict(sorted(labeled.items())))
print('orbits_by_stable_count', dict(sorted(orbits_A.items())))
print('orbit_size_distribution', sorted((k,s,n) for (k,s),n in orbit_size_dist.items()))
print('burnside_per_element', {str(ct): expected_per_element[ct] for ct in expected_per_element})
print('unsolvable_representatives', uns)
