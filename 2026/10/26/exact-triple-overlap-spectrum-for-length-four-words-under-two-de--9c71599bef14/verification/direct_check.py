"""Independent direct ordered-subsequence check and polynomial moment identity."""
from itertools import combinations, product
from math import comb, prod

A = {
    2: (672, 432, 132, 12),
    3: (28038, 7200, 1466, 72),
    4: (113890, 11868, 1936, 18),
    5: (114600, 4304, 688, 0),
    6: (39720, 384, 64, 0),
    7: (5184, 0, 0, 0),
    8: (216, 0, 0, 0),
}

def falling(q,k):
    return prod(range(q-k+1,q+1)) if q>=k else 0

def predicted(q):
    hs = [sum(A[k][s-1]*falling(q,k) for k in A)//6 for s in range(1,5)]
    return [comb(q**4,3)-sum(hs)]+hs

for q in (2,3,4,5):
    words = list(product(range(q), repeat=4))
    # This mask is computed directly from all six index pairs per center.
    shadows = []
    for x in words:
        shadows.append(0)
        for i,j in combinations(range(4),2):
            shadows[-1] |= 1<<(q*x[i]+x[j])
    obs = [0]*7
    for i,j,k in combinations(range(len(words)),3):
        obs[(shadows[i] & shadows[j] & shadows[k]).bit_count()] += 1
    expected = predicted(q)
    assert obs == expected + [0,0], (q,obs,expected)
    print(f"q={q}: {obs[:5]}; checked {comb(q**4,3)} triples")

# First moment: each length-two output has exactly 1+4(q-1)+6(q-1)^2
# distinct four-letter supersequences. Thus sum_s s H_s = q^2 binom(U,3).
for q in range(2,15):
    h = predicted(q)
    u = 1+4*(q-1)+6*(q-1)**2
    assert sum(s*h[s] for s in range(5)) == q*q*comb(u,3)
    assert sum(h)==comb(q**4,3)
print("first-moment checks q=2..14: all passed")
print("VERIFY_OK")
