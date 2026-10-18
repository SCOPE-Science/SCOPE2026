# Scientific review: cyclic binary trimer-composition profiles

## Correctness — PASS

The theorem covers every positive length, including length-one and length-two circular windows defined by periodic indexing. The proof separates constant words from words having alternating cyclic runs. Exact mixed-trimer identities \(p=2(r-s_0)+s_1\) and \(q=2(r-s_1)+s_0\), together with the excess-length formulas for the pure trimers, give the necessary congruence and boundary conditions. For sufficiency, the explicit choice \(r=\lceil\max((2p+q)/3,(p+2q)/3)/2\rceil\) yields valid singleton-run counts and sufficient nonsingleton runs for distributing the required lengths. The generating series is an exhaustive sum over these feasible quadruples. Coefficient extraction justifies the exact quasipolynomial and asymptotic ratio. Two independent finite procedures check the full feasible sets, not just their cardinalities: brute-force circular words through length 16 and a de Bruijn-state recurrence through length 48. Finite checks do not replace the proof.

## Originality — PASS, subject to stated risk

Ye and Elishco (arXiv:2208.14963, especially Section VIII) study a linear length-at-most-\(r\) composition observation and a code construction; the source does not claim the exact image or count of cyclic, exactly-three-window composition histograms. Gupta and Mahdavifar (arXiv:2201.09955) study the full linear composition multiset and corresponding reconstruction algorithms; their statements do not imply the present fixed-trimer cyclic histogram count without a new analysis. Ota and Manada (DOI:10.1587/transfun.2023TAP0015) use ordered substring frequencies and minimal absent words for uniquely reconstructing circular binary input; their main theorem is a reconstruction criterion, not an enumeration of unordered-composition output vectors, and assumes input without a smaller period. Indexed adjacent-pair multispectra, linear three-length-limited composition profiles, and directed cyclic pair matrices have different domains and observation maps, so their exact counts neither state nor immediately imply this theorem. Source and parameter searches located no equivalent all-length characterization or rational formula. Residual risk: an unindexed equivalent enumeration or a specialized projected-flow count could predate this result. This is not independent novelty certification.

## Mathematical value — PASS

The four-coordinate observation is a natural mass/composition version of a circular length-three read channel. The theorem determines exactly which histogram outputs can occur—not simply how to reconstruct a word from richer observations—and gives the complete image size for every length. The modular obstruction \(p\equiv q\pmod3\), together with two sharp boundary inequalities, produces a nontrivial exact cubic quasipolynomial and the limiting fraction \(1/3\) of realizable candidate histograms. The count is also the exact noiseless zero-error code cardinality for this observation channel. No polynomial-growth claim is made for arbitrary alphabet sizes or other window lengths.

## Sources and residual limits

Closest primary sources inspected: Z. Ye and O. Elishco, arXiv:2208.14963 (introductory definitions and Section VIII); U. Gupta and H. Mahdavifar, arXiv:2201.09955 (problem setup and principal reconstruction statements); T. Ota and A. Manada, DOI:10.1587/transfun.2023TAP0015 (definitions, main reconstruction theorem, algorithm and conclusion). See the original theorem for exact model boundaries and a reproducible finite verification program. Unindexed equivalent work may exist, and no independent audit is included.

Self-review: passed. Independent audit: not yet performed.
