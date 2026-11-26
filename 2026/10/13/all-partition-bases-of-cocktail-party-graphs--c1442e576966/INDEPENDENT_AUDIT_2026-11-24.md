# Independent mathematical audit

## correctness

PASS

For a block not containing v, distance is 2 iff the block is the singleton mate of v; otherwise it is 1. In the same block, distinct vertices therefore collide exactly when neither mate is singleton. For s singleton blocks among k blocks, each nonsingleton block of size r needs at least r−1 distinct singleton mates, so s≥2n−k. Equality k=n would make all blocks singleton and leave vertices uncovered. With k=n+1, s is n or n−1. In the first case the one size-n block has at most one endpoint from each pair (an internal pair would create two exceptions), hence is a transversal; its complement gives the singleton blocks. In the second case tightness forces exactly one exception in each of the two large blocks and requires all singleton vertices to have nonsingleton mates. The exceptions must be mated across the two blocks, leaving the remaining n−1 mates to distribute with both blocks receiving one. These forms are sufficient by the same distance criterion. Canonically naming a large block by which endpoint of the exceptional pair it contains avoids a spurious division by two, giving 2^n+n2^(n−1)(2^(n−1)−2) on labeled vertices with unordered blocks; ordering multiplies by (n+1)!. The finite independent replay `python3 /workspace/branches/independent-checks.py 2` enumerated restricted-growth strings for n=3,4,5 (203,4140,115975 partitions) and tested distance vectors, giving optimum values 4,5,6 and counts 32,208,1152. This corroborates, but does not replace, the proof for n≥3. Read the frozen checker and expected output without executing the uploaded code.

## originality

PASS

The scalar dimension is credited to prior work; the supported contribution is the complete classification and enumeration of all minimizers, explicitly the narrower claim of the frozen record. The strongest same-graph comparison, Zafari–Alikhani, verifies the scalar dimension and exhibits constructions rather than describing all minimizers. The old complete-multipartite scan could not be read and is an explicit residual risk, not negative evidence.

## value

PASS

This resolves a natural extremal gap for a standard complete-multipartite family. The classification exposes a second family that a proof by a single construction can miss and describes every optimum at all n, with an exact count for labeled vertices. The already-known scalar partition dimension is not the basis for this assessment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
