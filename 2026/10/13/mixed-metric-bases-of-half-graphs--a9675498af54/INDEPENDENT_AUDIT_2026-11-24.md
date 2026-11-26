# Independent mathematical audit

## correctness

PASS

A vertex at a leaf is the unique separator of its incident edge from the other endpoint, forcing a_n and b_1. For the prefix list (a_1,a_1b_2,…,a_1b_i), only indices 2 through i affect the list: each selected a-coordinate cuts at one threshold, and each selected b-coordinate can isolate only one item. Thus i distinct codes require at least i−1 effective landmarks. The reflected suffix list gives the n−i bound on indices i through n−1. At total size n the two internal counts overlap only at index i; their sum forces at least one at every internal pair, then exactly one. For sufficiency, the (b_1,a_n) signatures separate types except within individual shores, within internal edges and within each boundary star together with its center. Distinct A-vertices are distinguished at their smaller index, distinct B-vertices at their larger index. For edges with different A-index the smaller A-index works; otherwise the larger B-index works. A star edge is distinguished from its center at the leafward endpoint's index. At n=2 the seven signatures are already distinct and the forced landmarks give the lower bound. The frozen verifier and output were read, not executed. An independently written BFS/mixed-code check exhausted subsets of size at most n for 2≤n≤6 and found no smaller solutions and exactly 1,2,4,8,16 bases with the stated form; the frozen output reports the longer n≤8 enumeration, which is not a general proof.

## originality

PASS

The closest earlier exact catalogue result is edge metric bases of the same graph. Reversing indices converts its pairs to {a_{k+1},b_k}, k=1,…,n−1, and its dimension is n−1. Its proof already uses threshold/singleton counting on edge stars. Those results do not yield the mixed dimension or its diagonal transversals: adding the star center as a competing element changes which landmarks are effective, forces the leaves, and shifts the two critical ranges. Even the simple edge lower bound does not combine additively with the two leaves, which can themselves contribute to edge resolution. Neither the published mixed-family formulas nor the other inspected half/chain resolving invariants cover this exact mixed classification. The Bhat–Hanif–Sudhakara full text remains an explicit limitation, not negative evidence.

## value

PASS

Mixed dimension is a standard invariant, and the canonical twin-free nested bipartite family is a natural family on which vertex–edge resolution is not captured by the previously solved edge or vertex variants. The exact all-n family of optimal witnesses exposes a different pairing structure from edge resolution and supplies both sharp dimension and a complete basis count. The value is the structural classification, not a new general resolving proof technique or finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
