"""Low-degree vanishing H^p(Z_K0;Q)=0 for p<=4 by hand-proof + per-case
computational certification; H^6=0 by case analysis.

Hand-proof skeleton (uses only: every listed minimal non-face has size>=3):
 - All singletons/pairs are faces (full 0-/1-skeleton).
 - Hochster: H^p = (+) over I of H̃^{p-|I|-1}(K_I). For p<=4 and |I|=s:
    s<=2 -> K_I is a simplex (all its subsets of size<=2 are faces) -> 0.
    s>=3 -> q=p-s-1<=3-s<=0: q<=-1 vanishes (K_I has vertices, hence is
      nonempty as a complex); q=0 forces (p,s)=(4,3), and K_I on 3 vertices
      with all 3 edges present is connected -> H̃_0=0.
 - H^6: contributing (s,q): (3,2): 3-vertex complex has no H_2; (4,1) and
    (5,0): certified computationally (all 4-sets H̃_1=0, all 5-sets H̃_0=0);
    s<=2 simplices; s>=6 gives q<=-1 -> 0.
Each class is verified computationally below (512-subset cache, exact Q).
Repro: python3 verify_low_degree.py. Stdlib only.
"""
from itertools import combinations

import verify_target_obstruction as V

N = V.N
# cache all 512 Betti dicts once
CACHE = {}
for mask in range(1 << N):
    I = tuple(i for i in range(N) if mask & (1 << i))
    CACHE[I] = V.reduced_betti(I)

# full 0-/1-skeleton (lemma input)
assert all(V.is_face((i,)) for i in range(N))
assert all(V.is_face(p) for p in combinations(range(N), 2))
print("SKELETON_OK: 9 vertices + 36 edges all faces")

# H^p = 0 for p = 1..4, grouped by reason
for p in (1, 2, 3, 4):
    checked = {"simplex": 0, "neg": 0, "conn": 0}
    for I, b in CACHE.items():
        s = len(I)
        q = p - s - 1
        if not I:
            assert q != -1 or p != 0  # empty set contributes only to H^0
            continue
        if s <= 2:
            assert b == {}, (p, I, b)  # simplex
            checked["simplex"] += 1
        elif q <= -1:
            assert q not in b, (p, I, b)
            checked["neg"] += 1
        elif q == 0:
            assert s == 3 and p == 4
            assert b.get(0, 0) == 0, (p, I, b)  # connected via 3 edges
            checked["conn"] += 1
        else:
            raise AssertionError(f"unclassified case p={p} s={s}")
    # every nonempty I classified
    assert sum(checked.values()) == (1 << N) - 1, checked
    print(f"H^{p}=0 CERTIFIED {checked}")

# H^6 = 0 by cases
for I, b in CACHE.items():
    if not I:
        continue
    s = len(I)
    q = 6 - s - 1
    if s <= 2:
        assert b == {}, ("H6 simplex", I, b)
    elif s == 3:
        assert b.get(2, 0) == 0, ("H6 s=3", I, b)
    elif s == 4:
        assert b.get(1, 0) == 0, ("H6 s=4", I, b)
    elif s == 5:
        assert b.get(0, 0) == 0, ("H6 s=5", I, b)
    else:
        assert q not in b, ("H6 neg", I, b)
print("H^6=0 CERTIFIED (s=3:H_2=0; s=4:H̃_1=0 all; s=5:connected all; else simplex/neg)")
print("LOW_DEGREE_PASS")
