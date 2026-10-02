# Independent audit — Block-nuclear lower bounds and exact low-rank regularizers for quadratic neural networks

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** The block-nuclear lower bound was reconstructed atom by atom. Each signed neuron contributes a rank-one block with nuclear norm \(2|\alpha|\) and a quadratic block with nuclear norm \(|\alpha|\), giving \(R\ge\Omega\). Dualizing the off-diagonal block yields \(\Omega\ge\|z\|_2\). Pure quadratic and pure linear axes realize the nuclear and Euclidean norms exactly; for aligned rank-one aggregates the two signed atoms give \(R=\max\{|s|,|t|\}\). For orthogonal rank-one data, the three-atom construction has cost \((S^2+2ST+2T^2)/(S+2T)\), and an independently re-derived feasible quadratic dual polynomial attains the same value. The committed numerical script is only corroborative.

## Originality

**PASS.** The complete motivating preprint was inspected. It gives separate nuclear/Euclidean lower bounds and a regularized least-squares surrogate, but not the full block-nuclear bound or the exact induced atomic norms on the aligned and orthogonal families.

### Equivalent formulations

The closest convex-lift and atomic-gauge formulations were compared at statement level.

Evidence: The 2026 source's Theorem 3.3 lower-bounds the regularizer by a combination of \(\|Z\|_*\) and \(\|z\|_2\), while Theorem 3.4 isolates \(\|Z\|_*\). The neural-spectrahedra framework supplies the exact semidefinite aggregate representation but not the audited block-nuclear gauge formulas.

### Broader coverage

Broader optimization frameworks do not mechanically cover these exact regularizer values.

Evidence: The exact convex SDP framework is broader for training, but it does not state the stronger closed-form lower bound or low-rank gauge classifications. No inspected source gave the orthogonal rank-one formula or the scalar \(\ell_\infty\) regularizer.

### Exact database or table

The claim concerns explicit convex-gauge formulas, so exact-formula searching is the appropriate database check.

Evidence: No earlier exact match was located.

### Claim versus prior implication

The audited formulas are not immediate restatements of the prior lower bound.

Evidence: The source inequalities imply only the weaker separate lower bounds; taking the nuclear norm of the full signed block is a stronger certificate. The exact aligned and orthogonal values require explicit primal decompositions and matching dual certificates not supplied by the inspected sources.

### Source inspections

- **Regularized Least Squares Training of Quadratic Neural Networks with Applications to System Identification** — DIRECT_COMPARISON_NOT_COVERING.
  Identifier: arXiv:2609.17654
  Material read: Complete 11-page paper, including the convex QNN formulation, Lemmas 3.1--3.2, Theorems 3.3--3.4, Remarks 3.5--3.6, and conclusions.
  Evidence: The source proves separate nuclear/Euclidean lower bounds and nuclear-norm surrogates but does not state the full block-nuclear certificate or the exact low-rank atomic-gauge formulas.
- **Neural Spectrahedra and Semidefinite Lifts** — FOUNDATIONAL_NOT_COVERING.
  Identifier: arXiv:2101.02429
  Material read: Open abstract and detailed accessible scientific summary of the SDP lift and neural decomposition.
  Evidence: It provides the exact semidefinite lift/decomposition framework, but the searched material does not state the audited block-nuclear or rank-one regularizer identities.

### Residual risks

- The full 2021 neural-spectrahedra paper was not available in the same text interface during this audit; a gauge identity implicit in its proofs remains a residual prior-art risk, though the direct 2026 source was read completely.

## Scientific value

**PASS.** The result strengthens a current QNN regularization bound and computes exact induced regularizers on natural low-rank families, including a strict gap example. These formulas clarify what the convex relaxation actually penalizes and are mathematically reusable.

## Final assessment

The final claim survives unchanged on all three scientific axes. No claim text or slogan change is proposed.

This review does not constitute formal verification or a guarantee against undiscovered prior art.
