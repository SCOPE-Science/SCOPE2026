"""Independent check of the A* lemma: for all forbidden triples, minimum is at rank 1.
Also verify: appending n+1 at end creates 1324 iff pi contains 132-pattern with first element = global min... just characterize."""
from itertools import permutations
for t in [(1,3,2,4),(1,2,4,3),(1,4,3,2)]:
    assert min(t)==t[0]==1, t
print("A* lemma holds: all three forbidden patterns start with value 1.")
# Verify key structural fact: pi+(n+1) contains forbidden ending at n+1 iff pi contains a 132-subsequence starting at a left-to-right minimum... check on data instead.
