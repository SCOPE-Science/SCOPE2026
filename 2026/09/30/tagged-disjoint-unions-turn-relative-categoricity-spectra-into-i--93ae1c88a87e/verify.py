from itertools import product, permutations

N = 2
PAIRS = [(i, j) for i in range(N) for j in range(N)]
RELS = []
for bits in product((0, 1), repeat=len(PAIRS)):
    RELS.append({p for p, bit in zip(PAIRS, bits) if bit})


def iso_count(R, S):
    count = 0
    for p in permutations(range(N)):
        image = {(p[i], p[j]) for i, j in R}
        if image == S:
            count += 1
    return count


def tagged_union_iso_count(A, B, C, D):
    # The four-point domains are 0,1 for the first tag and 2,3 for the second.
    count = 0
    for p0 in permutations(range(N)):
        for p1 in permutations(range(N)):
            image_a = {(p0[i], p0[j]) for i, j in A}
            image_b = {(p1[i], p1[j]) for i, j in B}
            if image_a == C and image_b == D:
                count += 1
    return count

checked = 0
for A in RELS:
    for C in RELS:
        ac = iso_count(A, C)
        for B in RELS:
            for D in RELS:
                bd = iso_count(B, D)
                tagged = tagged_union_iso_count(A, B, C, D)
                assert tagged == ac * bd
                checked += 1

assert checked == 65536
for A in RELS:
    for B in RELS:
        tagged_aut = tagged_union_iso_count(A, B, A, B)
        rigid_components = iso_count(A, A) == 1 and iso_count(B, B) == 1
        assert (tagged_aut == 1) == rigid_components

print("VERIFY_OK", checked)
