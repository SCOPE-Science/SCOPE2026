# Independent mathematical audit

## correctness

PASS

Ringel's orientable genus formula gives ceil(2*7/4)=4. A connected cellular embedding then has 17 faces and 72 total face sides. Bipartiteness forces even facial walk lengths; a length-two walk in this simple graph would immediately reverse the sole edge between its vertices, impossible under rotations at vertices of degrees 4 and 9. Thus the excess over 17 quadrangles is 4, split as 2+2 or 4. Both printed rotations were independently parsed and checked against the snapshot's witness data, then traced as permutations of all 72 darts. Each yielded 17 cycles and Euler characteristic -6. A gave 15 quadrangles and the two cyclic words (0,11,2,8,1,7), (1,12,2,9,3,11); B gave 16 quadrangles and the octagon (0,10,1,7,2,9,3,5). The rotation-system construction gives orientable cellular embeddings; there is no assumption that facial walks of arbitrary competing embeddings are simple cycles. Replay: python3 /workspace/replay/02-trace.py. The snapshot retains witness data, but its old verifier hardcodes scratch/witnesses.json and was not executed or treated as fresh verification.

## originality

PASS

The excess exclusion is prior art and the octagonal profile also follows from a standard quadrangulation by deletion. The distinct step is a two-hexagon realization in this small case, which completes the classification. The October 25 catalog result supplies independent mathematical coverage of that step via a general extension argument; combined with the classical octagon deduction it covers the classification today. The available evidence does not show that extension or an equivalent K(4,9) realization available before the September finding. This is bounded best-of-knowledge credit for the September contribution, not a claim of priority or of present-day non-overlap.

## value

PASS

The complete-bipartite minimum-genus face census is an established problem. K(4,9) is the first n>7 in the fixed K(4,n) family with nonzero orientable minimum-genus excess, naturally just beyond the cited small-part census. The substantive witness realizes two hexagons and establishes that the excess can be spent in a different way from the octagon obtained by deleting a vertex of K(4,10). It closes the exact finite census question at that boundary; the Euler calculation or the deletion construction alone would not suffice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
