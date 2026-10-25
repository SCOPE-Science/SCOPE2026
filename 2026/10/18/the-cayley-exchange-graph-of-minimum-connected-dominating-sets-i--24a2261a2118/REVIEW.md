# Independent mathematical audit

## correctness

PASS

On Q4 with 16 labeled binary vertices, exhaustive direct independent enumeration of all subsets k=1,...,6 proved zero connected dominating sets for k<6 and exactly 192 of size6, all induced P6. All 192 optimum sets arise from direction words (a,b,c,d,a); source verify_group.py independently builds connected subsets and a free transitive 192-element affine-even-permutation group action on the state set. Exhaustive one-vertex replacements give degree4 and 384 jump edges; zero replacements use a cube-adjacent moved token, so slide exchange graph is empty. The four displayed H=F2^4⋊A4 generators act as all neighbors and give an inverse-closed Cayley graph; BFS distance levels (1,4,10,23,45,76,30,3) show diameter7 and connectedness. Independent reimplementation directly rebuilt state jump graph and parity-double BFS, obtaining odd girth11, matching source group method and explicit 11-letter odd identity word. This is exhaustive for Q4 only; no higher-dimensional extrapolation.

## originality

PASS

Past work on γ-graphs moves unrestricted minimal dominating sets by slides, at-most-k dominating-set reconfiguration permits add/delete, and general connected-domination papers enumerate minimal solutions, not this exact optimal connected jump graph. A 2003 primary paper about paths and cycles dominating hypercubes has plausible overlap with minimum size and induced P6 descriptions, which the current assessment does not assert uniquely new. Its full text could not be retrieved through lawful OA or authorized institutional retrieval (VPN disconnected), but no evidence of the much more specific affine Cayley token-jump exchange theorem was found. Best-of-knowledge PASS applies to the full exchange graph and its metrics, retaining source risk.

## value

PASS

Q4 is a natural canonical finite hypercube, and minimum connected dominating sets are optimal connected coverage backbones. An exact classification of their reconfiguration graph, affine regular action, diameter, shortest odd cycle, and obstruction to all local token slides exposes meaningful reachability/dynamics structure, not just an arbitrary catalogued integer. The contrast that all optimal states are connected by jumps within seven steps but isolated by slides is a motivated qualitative boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
