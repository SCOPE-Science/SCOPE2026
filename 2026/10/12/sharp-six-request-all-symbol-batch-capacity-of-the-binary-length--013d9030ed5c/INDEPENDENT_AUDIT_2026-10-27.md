# Independent mathematical audit

## correctness

PASS

The generator g_x=(1,x) is a rank-five affine evaluation generator of RM_2(1,4), with 16 distinct columns. A recovery group avoiding x cannot have one member; any two-column XOR has leading bit 0 and cannot equal g_x, and any subset spanning a target can be shrunk to a nonempty odd-sized sum. Thus at most one set for seven repeated requests meets x, and six other disjoint sets require at least 18 of 15 non-x coordinates: impossible. For sufficiency each x has 1 singleton and 35 three-subsets {a,b,c} with a⊕b⊕c=x. Every six-request multiset is uniquely one nondecreasing tuple (C(21,6)=54264). Independent Python exact-cover backtracking exhaustively chose from those 36 legal supports for each demand and independently recomputed all five-bit generator-column XORs, target multiplicities, group sizes and disjointness for all 54264 valid witnesses. The algorithm's state is (remaining multiplicities, used 16-bit coordinate mask); it branches over all available candidate supports for the selected remaining label, with only the sound prune 'available candidate count < required multiplicity'. Its successful return for every multiset certifies existence and yields exact t=6. The report's histogram is a selection-dependent witness diagnostic, not an access-optimum claim.

## originality

PASS

No identified prior theorem or published table implies the exact six-all-symbol-batch sufficiency for the fixed RM_2(1,4) [16,5,8] code. The 2018 batch theorem proves four requests, and the 2026 all-symbol framework gives a matching upper bound of six without establishing mixed-demand attainability. The finite verification fills that specifically motivated gap. This is a qualified best-of-knowledge assessment, not a claim of exhaustive historical priority.

## value

PASS

The exact all-symbol batch capacity is a natural intrinsic access invariant of a small, standard 16-server code. The literature supplies a four-query mixed-demand property and repeated-target six-query availability but not the collision-free six-mixed-demand assignment. Closing this gap precisely at its natural counting ceiling and using only locality-3 helpers is a worthwhile finite structural benchmark. Full reproducibility and exactness are supporting evidence, not the sole value justification; no generic all-length theorem is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
