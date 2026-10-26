# Self-review

## Correctness — PASS
The theorem is reconstructed from the exact covariance operator \(T=I+D^*(\Sigma-I)D\) on the real Hermitian Hilbert space; the identity holds even for singular \(\Sigma\). Differentiating equivariance at every diagonal matrix unit forces each Lie-algebra off-block entry to vanish unless the respective rows of \(\Sigma-I\) agree. Explicit block-trace factorization gives the converse. Normalizing the entire connected block-unitary subgroup forces any disconnected symmetry to permute coordinate blocks, and exact permutation invariance is equivalent to preserving \(\Sigma\). Both necessity and sufficiency and all normalization boundary cases are proved. The finite verification script passed 102 exact-rational checks, but the analytic proof, not the checks, establishes the infinite theorem.

## Originality — PASS, with literature limitations
The exact matching 2026 primary paper was inspected through its full available HTML text, particularly the model and symmetry definitions, Proposition 2.2, and Remark 2.3(ii). Its theorem requires positive definiteness and excludes \(1\) from the covariance spectrum. Its remarks explicitly leave the exceptional eigenspace case open to further analysis and show two full-unitary special families. The present theorem resolves every exceptional covariance by a row-partition criterion and describes the entire identity component and finite quotient. The prior generic theorem and special full-unitary examples are credited. Targeted web and mathematical-record searches found no directly encompassing formula. A general classical covariance-stabilizer classification might yield the present explicit formula, and literature search is not exhaustive; these are genuine residual novelty risks.

## Mathematical value — PASS
The new result closes an explicit structural classification gap for a natural Gaussian random-matrix model, rather than giving a small parameter variation. It gives a computable characterization of every possible intermediate symmetry group, a precise criterion distinguishing a generic spectrum degeneracy from an actual enlargement, and covers singular diagonal covariance not handled in the source's generic theorem. The block-group dimension and component quotient are useful for symmetry reductions of Gaussian ensembles.

## Limitations and source comparison
Houdré–Kidonakis (arXiv:2610.12950v1, Proposition 2.2 and Remark 2.3) is the closest primary work. Only distributional conjugation symmetries of the stated independent-off-diagonal Gaussian law are covered. Finite computations support but do not replace proof. Independent literature and mathematical auditing may uncover an equivalent statement not retrieved by the targeted searches.

Self-review: passed. Independent audit: not yet performed.
