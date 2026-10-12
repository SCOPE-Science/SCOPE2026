import itertools
from collections import Counter

# Permutations are tuples p with p[i] equal to the image of i.
G=list(itertools.permutations(range(3)))
idx={p:i for i,p in enumerate(G)}

def compose(p,q):
    return tuple(p[q[i]] for i in range(3))

def inverse(p):
    out=[0]*3
    for i,j in enumerate(p):
        out[j]=i
    return tuple(out)

mul=[[idx[compose(p,q)] for q in G] for p in G]
inv=[idx[inverse(p)] for p in G]
e=idx[(0,1,2)]

def conj(a,h):
    return mul[mul[a][h]][inv[a]]

def is_averaging(A):
    for g in range(6):
        ag=A[g]
        for h in range(6):
            left=conj(ag,A[h])
            right=A[conj(ag,h)]
            if left!=right:
                return False
    return True

def generated_subgroup(elements):
    H={e}|set(elements)
    while True:
        old=set(H)
        H|={inv[x] for x in list(H)}
        H|={mul[x][y] for x in list(H) for y in list(H)}
        if H==old:
            return frozenset(H)

def subgroup_equivariant(A):
    H=generated_subgroup(A)
    for k in H:
        for h in range(6):
            if A[conj(k,h)]!=conj(k,A[h]):
                return False
    return True

all_maps=itertools.product(range(6),repeat=6)
accepted=[]
for A in all_maps:
    avg=is_averaging(A)
    equiv=subgroup_equivariant(A)
    assert avg==equiv
    if avg:
        accepted.append(A)

assert len(accepted)==129
pointed=[A for A in accepted if A[e]==e]
assert len(pointed)==51

by_order=Counter(len(generated_subgroup(A)) for A in accepted)
assert by_order==Counter({1:1,2:45,3:80,6:3}),by_order

pointed_by_order=Counter(len(generated_subgroup(A)) for A in pointed)
assert pointed_by_order==Counter({1:1,2:21,3:26,6:3}),pointed_by_order

# Every automorphism of S3 is inner.  Conjugation by k represents it.
def transform(A,k):
    kinv=inv[k]
    return tuple(
        conj(k,A[conj(kinv,x)])
        for x in range(6)
    )

def orbit_partition(maps):
    pool=set(maps)
    orbits=[]
    while pool:
        A=next(iter(pool))
        orb={transform(A,k) for k in range(6)}
        assert orb <= set(maps)
        orbits.append(orb)
        pool-=orb
    return orbits

orbits=orbit_partition(accepted)
assert len(orbits)==60
sizes=Counter(len(O) for O in orbits)
assert sizes==Counter({1:6,2:39,3:15}),sizes

orbit_strata=Counter()
for O in orbits:
    orbit_strata[len(generated_subgroup(next(iter(O))))]+=1
assert orbit_strata==Counter({1:1,2:15,3:41,6:3}),orbit_strata

porbits=orbit_partition(pointed)
assert len(porbits)==25
psizes=Counter(len(O) for O in porbits)
assert psizes==Counter({1:6,2:12,3:7}),psizes

porbit_strata=Counter()
for O in porbits:
    porbit_strata[len(generated_subgroup(next(iter(O))))]+=1
assert porbit_strata==Counter({1:1,2:7,3:14,6:3}),porbit_strata

# Independent conceptual-count checks.
assert 1 + 3*(2**4-1) + (3**4-1) + 3 == 129
assert 1 + 3*(2**3-1) + (3**3-1) + 3 == 51
assert 1 + 15 + (80+2)//2 + 3 == 60
assert 1 + 7 + (26+2)//2 + 3 == 25

print({
    "averaging_maps":len(accepted),
    "pointed_maps":len(pointed),
    "generated_image_counts":dict(sorted(by_order.items())),
    "pointed_generated_image_counts":dict(sorted(pointed_by_order.items())),
    "automorphism_orbits":len(orbits),
    "pointed_automorphism_orbits":len(porbits),
    "orbit_sizes":dict(sorted(sizes.items())),
    "pointed_orbit_sizes":dict(sorted(psizes.items())),
})
print("VERIFY_OK")
