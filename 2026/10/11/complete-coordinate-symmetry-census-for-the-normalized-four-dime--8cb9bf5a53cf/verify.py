import itertools, collections

N = 4
PERMS = list(itertools.permutations(range(N)))
ID = tuple(range(N))
U = [v for v in itertools.product((0,1), repeat=N) if v != (1,1,1,1)]

def compose(a,b):
    return tuple(a[b[i]] for i in range(N))

def inverse(a):
    r = [0]*N
    for i,x in enumerate(a):
        r[x] = i
    return tuple(r)

def parity(a):
    invs = sum(a[i] > a[j] for i in range(N) for j in range(i+1,N))
    return -1 if invs % 2 else 1

def act_v(g,v):
    r = [0]*N
    for i in range(N):
        r[g[i]] = v[i]
    return tuple(r)

def generated(gens):
    G = {ID}
    frontier = [ID]
    while frontier:
        x = frontier.pop()
        for s in gens:
            for y in (compose(s,x), compose(x,s)):
                if y not in G:
                    G.add(y)
                    frontier.append(y)
    return frozenset(G)

# Generate the full subgroup lattice without a stored list.
SUBGROUPS = {frozenset([ID])}
changed = True
while changed:
    changed = False
    for H in list(SUBGROUPS):
        for g in PERMS:
            if g not in H:
                K = generated(list(H) + [g])
                if K not in SUBGROUPS:
                    SUBGROUPS.add(K)
                    changed = True

assert len(SUBGROUPS) == 30
assert collections.Counter(map(len,SUBGROUPS)) == {
    1:1, 2:9, 3:4, 4:7, 6:4, 8:3, 12:1, 24:1
}

def fixed_count(H):
    seen = set()
    total = 1
    for v in U:
        if v in seen:
            continue
        orb = {act_v(g,v) for g in H}
        seen |= orb
        v0 = min(orb)
        stab = [g for g in H if act_v(g,v0) == v0]
        if v0 == (0,0,0,0):
            opts = [ID]
        else:
            need = 1 if sum(v0) % 2 == 0 else -1
            opts = [
                p for p in PERMS
                if parity(p) == need
                and all(compose(p,g) == compose(g,p) for g in stab)
            ]
        total *= len(opts)
    return total

FIX = {H:fixed_count(H) for H in SUBGROUPS}

def cycle_type(p):
    seen = [False]*N
    lengths = []
    for i in range(N):
        if not seen[i]:
            j=i
            m=0
            while not seen[j]:
                seen[j]=True
                j=p[j]
                m+=1
            if m>1:
                lengths.append(m)
    return tuple(sorted(lengths, reverse=True)) or (1,)

def subgroup_type(H):
    o = len(H)
    c = collections.Counter(cycle_type(g) for g in H if g != ID)
    if o == 1: return "trivial"
    if o == 2: return "C2_trans" if c[(2,)] else "C2_double"
    if o == 3: return "C3"
    if o == 4:
        if c[(4,)] == 2: return "C4"
        if c[(2,)] == 2: return "V4_split"
        return "V4_normal"
    if o == 6: return "S3"
    if o == 8: return "D8"
    if o == 12: return "A4"
    if o == 24: return "S4"
    raise AssertionError((o,c))

expected_fixed = {
    "trivial": (1, 12**14),
    "C2_trans": (6, 1327104),
    "C2_double": (3, 47775744),
    "C3": (4, 0),
    "V4_split": (3, 768),
    "C4": (3, 6912),
    "V4_normal": (1, 9216),
    "S3": (4, 0),
    "D8": (3, 32),
    "A4": (1, 0),
    "S4": (1, 0),
}

for typ,(number,value) in expected_fixed.items():
    hs = [H for H in SUBGROUPS if subgroup_type(H) == typ]
    assert len(hs) == number
    assert {FIX[H] for H in hs} == {value}

# Every subgroup containing a three-cycle has no invariant assignment.
for H in SUBGROUPS:
    if any(cycle_type(g) == (3,) for g in H):
        assert FIX[H] == 0

# Burnside average directly over the 24 group elements.
burnside_sum = 0
for g in PERMS:
    burnside_sum += fixed_count(generated([g]))
TOTAL_ORBITS = burnside_sum // 24
assert burnside_sum % 24 == 0
assert TOTAL_ORBITS == 53496608995008

# Exact stabilizers by descending subgroup-lattice subtraction.
EXACT = {}
for H in sorted(SUBGROUPS, key=len, reverse=True):
    EXACT[H] = FIX[H] - sum(EXACT[K] for K in EXACT if H < K)
    assert EXACT[H] >= 0
assert sum(EXACT.values()) == 12**14

expected_exact_aggregate = {
    "trivial": 1283918313282048,
    "C2_trans": 7958016,
    "C2_double": 143276736,
    "C3": 0,
    "V4_split": 2208,
    "C4": 20640,
    "V4_normal": 9120,
    "S3": 0,
    "D8": 96,
    "A4": 0,
    "S4": 0,
}
for typ,expected in expected_exact_aggregate.items():
    got = sum(EXACT[H] for H in SUBGROUPS if subgroup_type(H) == typ)
    assert got == expected, (typ,got,expected)

expected_orbits = {
    "trivial": 53496596386752,
    "C2_trans": 663168,
    "C2_double": 11939728,
    "V4_split": 368,
    "C4": 3440,
    "V4_normal": 1520,
    "D8": 32,
}
for typ,expected in expected_orbits.items():
    hs = [H for H in SUBGROUPS if subgroup_type(H) == typ]
    aggregate = sum(EXACT[H] for H in hs)
    got = aggregate * len(hs[0]) // 24
    assert aggregate * len(hs[0]) % 24 == 0
    assert got == expected, (typ,got,expected)

nontrivial_assignments = sum(
    EXACT[H] for H in SUBGROUPS if subgroup_type(H) != "trivial"
)
nontrivial_orbits = sum(
    expected_orbits[typ]
    for typ in expected_orbits if typ != "trivial"
)
assert nontrivial_assignments == 151266816
assert nontrivial_orbits == 12608256

print("VERIFY_OK")
print("subgroups=30")
print("normalized_assignments=1283918464548864")
print("S4_orbits=53496608995008")
print("nontrivial_symmetry_assignments=151266816")
print("nontrivial_symmetry_orbits=12608256")
print("three_cycle_fixed_sets=0")
