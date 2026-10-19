# Mathematical review

## Correctness — PASS
The graph and impurity normalization are explicit, and the determinant identity is established by deleting the impurity vertex. The Chebyshev sign intervals give a complete real-root count, including an exterior root and an additional even-order root. For fixed size and strong nonreciprocity the unique minima of the complete lobes yield the exact cutoff; the critical lobe gives the residue-three correction, while ordering and local antinode expansions give the other residue classes. All root crossings are counted algebraically. The standalone `verify.py` reproduces exact characteristic polynomials at six sizes, 24 full-matrix threshold configurations, and selected correction laws. Finite checks corroborate rather than prove all-dimensional statements.

## Originality — PASS
Liu, Zeng, Li and Chen (arXiv:2106.03420v1) derive the exact characteristic equation and a simpler large-system realification bound; the finite-size exact threshold is explicitly lower, but its residue-dependent asymptotic prefactor and the exceptional correction are not given in the inspected main paper and Appendix A. Guo et al. (arXiv:2102.03781v2) and Li, Lee and Gong (arXiv:2008.05501v1) instead perturb boundary hoppings, not a positive real on-site defect. Searches of published findings and public scientific literature yielded no directly dominating assertion. This is a self-review, not independent proof that no equivalent statement exists elsewhere.

## Scientific value — PASS
Quantifying the smallest on-site impurity capable of fully realifying the finite nonreciprocal ring is directly motivated by the impurity-induced transition in the 2021 source. A finite-order, congruence-dependent cutoff ratio and exceptionally small bound defect are structural information unavailable from a universal sufficient bound; the effects persist in each fixed size's strong-nonreciprocity limit. Explicit four- and five-site factors and the large-size spacing law make the arithmetic boundary experimentally and numerically interpretable.

## Closest literature, conditions, and risks
The existing exact secular equation and finite-size sufficient bound are prior art. The novelty claim is restricted to the asymptotic classification of the true all-real cutoff, not the impurity effect itself. The limit order is essential. External priority checking may still find an equivalent formulation, and no independent validation was conducted.

Self-review: passed. Independent audit: not yet performed.
