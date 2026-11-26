# Independent mathematical audit

## correctness

PASS

PASS is for the repaired claim only. The frozen torsion formula is false: with its last pair (10,13), the evaluations on oriented product tori (0,7,6,1,9)×(2,4,3,5,8) and (0,7,6,2,8)×(1,5,3,4,9) are −1 and +1. Frozen verify.py lines 75 and 164 select row[8], which is instead the lexicographic chord pair (10,14). The independent exact reconstruction at /workspace/branches/08a3c15a-8c4e-488e-adf7-6249df9df778/independent_check.py confirmed the false pairing, the graph-cell counts (45,120,75), cokernel Smith factors of 69 ones and a two, and full cup-plus-coboundary column lattice; it did not run the uploaded verifier. The repair isolates the realization of the torsion by a single cup, (α8+α10)∪(α14−α10). The square cochain for this product follows from the cellular map into the torus, with support (8,10),(8,14),(10,14) and signs (−1,1,1). The two-particle discretization hypotheses hold (girth five and the essential-vertex path bound). The separate repaired package reconstructs the cells from the graph, checks an explicit integral D u=2c certificate and an F2 cycle with ⟨c,z⟩=1. This proves exact order two, not merely rational invisibility. The unique torsion subgroup follows from the known H_1 and the universal coefficient theorem. Replay: python3 /workspace/repairs/4/verify.py, observed PRODUCT_ORDER_TWO_OK integral_double_boundary=True mod2_cycle_pairing=1.

## originality

PASS

PASS is restricted to the corrected explicit single product of two specified integral total-motion classes. The abstract group and even generation by degree-one cups are covered or directly implied by prior results. The strongest exact Petersen records inspected give homology and integral pairings against tori, which cannot certify that a rationally zero cup is a nonzero torsion class, or exhibit a decomposable pair with that property. No equivalent pair or subsuming explicit result was established in the bounded checks.

## value

PASS

Realizability of a torsion class by a single pair of ordinary integral motion classes is stronger than additive generation. This is an explicit, short witness for a natural nonplanar graph, useful for detecting integral multiplication that all rational and integral top-cycle evaluations miss. The proof certifies both halves of exact order without a routine rank-only comparison; no general classification or support minimality is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
