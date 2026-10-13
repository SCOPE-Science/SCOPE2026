# Scientific review: rectangular rook-graph power domination

## Correctness

**PASS.** The full unseen-cell set after initial observation is the Cartesian rectangle of empty rows and columns. An observed cell has exactly zero, the number of empty rows, or the number of empty columns as unseen neighbors. This proves both the no-force obstruction when both numbers exceed one and the one-round propagation when either equals one. The support-threshold equivalence is therefore exact for every pair of dimensions at least two. Inclusion–exclusion counts each set uniquely by row and column support. A deletion-witness argument classifies all inclusion-minimal sets; the Stirling-number sum counts surjections in the non-square case, and an explicit overlap correction counts partial permutations in the square case. The companion exhaustive checker independently reconstructs forcing and matches every coefficient and minimal-set count for all nine boards with dimensions two through four and the board \(3\times5\).

## Originality

**PASS, subject to stated residual risk.** The 2008 graph-product work treats different products/factors, not an all-set enumerator for complete-by-complete Cartesian products. Soh and Koh's 2014 paper already proves the minimum size, and that value is expressly excluded from the novelty claim. The indexed lemma/theorem passages inspected from it do not state the new all-set or inclusion-minimal-set counts, but its unavailable complete text remains a risk. The 2015/2018 graph-product study concerns numerical bounds and forcing for other products; the 2018 general polynomial paper computes other graph families, not this full Cartesian-product family. Ordinary rook domination is strictly more restrictive and not equivalent. Other previously recorded results on crown, book, and threshold graphs do not cover these objects/invariants. Searches under rook, Cartesian, power-domination polynomial, inclusion-minimal, upper parameter, and row/column support aliases identified no dominating prior statement; nonhits alone were not treated as originality proof.

## Value

**PASS.** The new structural theorem provides the complete cardinality distribution of viable sensor placements and the exact inclusion-minimal spectrum on every rectangular board. A square board has a single possible inclusion-minimal cardinality, whereas rectangular boards with short side at least three admit two separated cardinalities; the gap grows without bound on \(R_{3,n}\). This distinguishes optimum-size monitoring from configurations where no individual sensor can be deleted, an intrinsic combinatorial and network-placement distinction. The count of every viable and every irreducible configuration is substantially stronger than the known minimum-number formula.

## Sources and limitations

Closest primary comparison: K. W. Soh and K. M. Koh (2014), DOI 10.1080/09728600.2014.12088762, Theorem 3.3 (minimum number only in accessible excerpt). Also inspected Dorbec et al. (2008), DOI 10.1137/060661879, the available complete author-hosted text; Benson et al. arXiv:1510.02421, graph-product scope; Brimkov et al. arXiv:1805.10984v1, complete HTML body; and ordinary rook domination. The full 2014 text could not be accessed, and differently indexed older specializations may exist. Full mathematical proof is supplied; finite enumeration is corroboration only. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
