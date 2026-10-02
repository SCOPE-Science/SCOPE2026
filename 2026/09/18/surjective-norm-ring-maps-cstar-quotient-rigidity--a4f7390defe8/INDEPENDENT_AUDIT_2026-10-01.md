# Independent mathematical audit — SCOPE-20260918-a4f7390defe8

Final disposition: **PASS**.

## Correctness
**PASS.** The proof was reconstructed without using injectivity. Surjective Fischer-Muszely rigidity supplies additivity. If \(u=T(1)\) and \(p=(1+u)/2\), then any \(x\in pB(1-p)\) has \(x^2=0\); taking a preimage \(a\), the product-norm identity gives \(T(a^2)=0\), while additivity still gives \(T(1-a^2)=u\). The resulting norm equalities \(\|1\pm2x\|=1\) force \(x=0\), so \(u\) is central. After normalization \(\Phi=uT\), the positivity argument gives contractivity. Its kernel is closed, two-sided, involution-stable, and complex-linear; the induced quotient map is bijective and satisfies Matsuzaki's hypotheses, so it is a real *-isomorphism. The converse and the quotient norm identity then follow.

## Originality
**PASS.** Matsuzaki's September 2026 primary theorem is explicitly stated for bijections. The audited argument is not a mere quotient restatement: before quotienting it must show centrality, positivity, continuity, and that the noninjective kernel is a C*-ideal using only the norm identities. Resultary searches found the assigned theorem but no earlier or later published quotient classification under these exact hypotheses. Full text of the very recent Matsuzaki preprint could not be obtained through the lawful routes tried, so hidden discussion of the surjective case remains a residual risk.

### Equivalent formulations
The quotient formulation was treated as the theorem's conclusion, not assumed as a prior equivalence.

### Broader coverage
No inspected stronger theorem dominates the noninjective surjective case.

### Exact database or table
There is no relevant finite table; this check specifically targeted an already-published equivalent theorem.

### Claim versus prior implication
The final surjective classification is not mechanically implied by simply deleting the word bijective from the prior theorem.

## Value
**PASS.** Removing injectivity from a new rigidity theorem and replacing it by an exact quotient-kernel classification is a natural and useful extension. The theorem determines all norm loss by distance to the kernel and immediately resolves the simple-domain case. The noninjective evaluation/quotient examples show that this is not a vacuous restatement of the bijective theorem.

## Source inspections
- **Involution-preserving ring isomorphisms in norm between unital C*-algebras** (https://arxiv.org/abs/2609.18121): primary abstract, which states the full bijective theorem; full-text retrieval was attempted through open and authorized routes but no verified PDF was obtained Assessment: BIJECTIVE_PREDECESSOR_WITH_ACCESS_RISK. Evidence: The primary abstract assumes a bijection and concludes a central symmetry times a real *-isomorphism.
- **Stability of the Fischer-Muszely functional equation** (https://doi.org/10.5486/PMD.2003.2725): indexed theorem description and the exact corollary as cited by the package Assessment: SUPPORTING_INPUT_NOT_COVERING_QUOTIENT_CLASSIFICATION. Evidence: The exact surjective norm-additive case supplies additivity only.

## Residual risks
- The directly preceding Matsuzaki preprint was not available in verified full text during this run, so an unindexed surjective remark remains possible.
- Older nonlinear-preserver literature is broad and may contain an equivalent quotient formulation under different terminology.
