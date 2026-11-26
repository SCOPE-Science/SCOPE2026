# Independent mathematical audit

## correctness

PASS

A prefix dominates the union of its occupied rows and columns; until one side is full, legality is exactly introducing at least one new label. The first edge introduces two, so the prefix before the last edge has at most m+n−2 labels but at least as many labels as the full sequence length. Equality forces the prefix to use exactly m−1 rows and n−1 columns, introducing one new label at every step after the first. Its incidence graph is a tree. The last edge must introduce the missing column only (a column leaf), the missing row only (a row leaf), or both (a detached single edge). Conversely prune a leaf on the full side, or omit the detached edge, grow the remaining nonempty tree, then append the pruned edge: this is legal and dominating, including the one-edge prefix on 2×2. The weighted bipartite matrix-tree identity gives the degree-minus-one enumerator (∑x)^(b−1)(∑y)^(a−1). With the row variables set to 1, the full-support column monomials have total weight a^(b−1)b!S(a−1,b), so subtracting them gives exactly A; transpose for B. C uses the unconstrained bipartite tree count and has a unique detached edge except on 2×2, where there are two matchings, not four endpoint choices. Fresh exhaustive legal-order testing via actual closed neighborhoods on 2×2, 2×3 and 3×3 yielded (A,B,C) counts (2,2,2), (2,12,6), and (36,36,36).

## originality

PASS

Pass for the exact three-type classification and census of unordered maximum supports. Do not credit the known m+n−2 construction or the rook-to-incidence-graph correspondence. The closest catalog and primary results change legality, the family of minimal sets, or the observable, and do not determine this classification.

## value

PASS

Answers the natural extremizer question left by a length construction. It provides both a test for whether a given unordered support can attain that length and a uniform count by three distinct mechanisms, including the duplicated matching parametrization at the smallest board. The 3×3 discrepancy with ordinary domination shows that the sequential constraint contributes actual structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
