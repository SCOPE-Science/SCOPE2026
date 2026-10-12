# Self-review

## Correctness — PASS
For binary LCD \(C\) with \(n=20\), \(k=8\), the decomposition \(\mathbb F_2^{20}=C\oplus C^\perp\) forces every listed marginal equality, and pair orthogonality and minimum distance force the pattern zeros. The 2015 joint MacWilliams identity and standard code-dual MacWilliams identity yield the remaining linear equations. The self-contained exact-rational checker reconstructs the full integer Hadamard transform of degree 20, then verifies all \(686\) allowed coefficient inequalities and the negative rational right-hand side. A violated constraint would invalidate the proof; no approximation is used. This proves distance \(\le6\), not existence at 6.

## Originality — PASS
Kang–Xiong (arXiv:2609.08662v2, §5.3 and Table 4) identify the exact \((20,8)\) reverse comparison but say the joint enumerator endpoint is only numerical screening, while their other four comparisons are certified. Alahmadi–Deza–Dutour Sikirić–Solé (arXiv:1511.08889v1) supply the original model and tabulate through length 16, not this exact point. Focused exact-parameter, equivalent-formulation, dominating-bound, research-index and table searches did not locate this particular rational certificate. The original numerical observation is properly credited; published or differently named coverage not reached by these searches remains a residual risk.

## Value — PASS
An exact certificate for the one explicitly uncertified reverse-direction benchmark converts a numerical observation into a finite mathematical separation between competing LCD linear-programming relaxations. Its object and cutoff are motivated by the source's Table 4, and the proof's exact arithmetic can be reproduced using only Python 3 standard library. No general distance hierarchy, optimal code construction, or broad LP dominance is asserted.

Self-review: passed. Independent audit: not yet performed.
