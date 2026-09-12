"""Hochster Tor table for TRUE K: MNF = {{0,1},{2,3},{4,5,6,7,8}} (9 verts)."""
from itertools import combinations
import sys
sys.path.insert(0, 'output/artifacts')
from homology_lib import betti_unreduced
from collections import defaultdict, Counter

N = 9
MNF = [{0,1},{2,3},{4,5,6,7,8}]
def is_face(S):
    St = set(S)
    return not any(set(G).issubset(St) for G in MNF)

def reduced_cohom(S):
    S = sorted(S)
    if not S:
        return {-1: 1}
    F = set([()])
    for r in range(1, len(S)+1):
        for T in combinations(S, r):
            if is_face(T):
                F.add(T)
    return dict(betti_unreduced(F, len(S)))

betti = defaultdict(int)
detail = defaultdict(list)
for mask in range(1 << N):
    S = tuple(i for i in range(N) if mask >> i & 1)
    dd = reduced_cohom(S)
    for q, d in dd.items():
        if d:
            i = len(S) - q - 1
            betti[(-i, 2*len(S))] += d
            detail[(-i, 2*len(S))].append((S, q, d))
print("== TRUE bigraded Betti ==")
for k in sorted(betti):
    print(k, betti[k], detail[k])
print("total dim Tor =", sum(betti.values()))
hdeg = Counter()
for (a, b), v in betti.items():
    hdeg[a+b] += v
print("== H^d(Z_K) ==", dict(sorted(hdeg.items())))
