# Self-review

## Correctness

PASS. The claim covers every \(n\ge2\), \(1\le a\le\lfloor n/2\rfloor\), and every unordered-pair query support. A cycle with one negative edge is an unconditional obstruction. Every edge labeling on a forest has exactly two compatible choices per component; those choices contribute either \(c_i\) or \(t_i-c_i\) vertices to the size-\(a\) block. The coefficient condition is therefore necessary and sufficient, not merely a relaxation. The balanced component assignments prove the upper bound, while the explicit star labeling argument proves the matching lower bound in the stated range. The finite verifier compared this criterion with independently enumerated cut responses for 100,490 parameter/support cases. Finite enumeration is corroboration rather than a replacement for the unrestricted proof.

## Originality

PASS under the identified primary literature and published-record comparisons, with residual historical-priority uncertainty. The 2020/2021 closure-bounds paper studies universal Boolean aggregation, and the 2022/2023 inapproximability paper studies general explicit concept-class hardness. Neither supplies or logically forces the precise cardinality-constrained forest profile, its polynomial coefficient characterization, or the sharp eventual value. Earlier graph-cut learning concerns vertex-label cuts or bounds by the number of crossed edges, not an edge-query set system with one side of prescribed vertex cardinality. A fixed-size edge-hit system uses the Boolean OR of endpoint membership and has star-forest shattering supports, whereas the present cut system uses endpoint XOR and admits general forests subject to cardinality arithmetic; neither earlier classification implies the other. The local fixed-block-size cases known from prior work are implied by this theorem, not vice versa. The searched records could miss synonyms or inaccessible publications; this is not a claim of priority certification.

## Mathematical value

PASS. Fixed-cardinality bipartitions arise naturally in balanced clustering and cut learning, where transitivity and the exact side size interact. The result replaces a general exponential family of vertex subsets and arbitrary support graphs by a graph-theoretic forest test plus arithmetic of component-size profiles, and proves a dimension saturation phenomenon: increasing the ambient vertex set past \(3a+1\) no longer increases the largest statically shattered edge-query support. It also explains why allowing the block sizes to vary gives a different classification. Both the structural theorem and all-parameter sharp bound remain useful outside any small-instance census.

## Closest literature and limitations

Ghazi et al., arXiv:2007.03668; Manurangsi, arXiv:2211.01443; Gärtner and Garriga, *The Cost of Learning Directed Cuts*. The conclusion does not provide a closed expression for every \(n<3a+1\), the exact smallest saturation order for each \(a\), or adaptive Littlestone dimensions. Relevant synonyms in old or unindexed cut-learning literature could conceal prior coverage.

Self-review: passed. Independent audit: not yet performed.
