# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260919-1fa8a4cea945`

## Correctness — PASS

The central representation-theoretic correction reconstructs exactly. Writing an equivariant linear map columnwise reduces every coefficient map on the ambient \(\mathbb R^d\) factor to a scalar multiple of the identity, so the commutant is precisely right multiplication \(X\mapsto XB\). Thus even entry-diagonal equivariant maps can have one scalar per column. The stated covariance rule transforms by conjugation under a right frame rotation, matrix functional calculus gives the corresponding inverse-square-root covariance, and the embedded Stiefel projector satisfies both left and right covariance identities. Frobenius capping and polar retraction preserve the same symmetry. The package's exact two-column example and random bi-equivariance script were read in full; the reported errors are only floating-point roundoff and are corroborative rather than the proof.

### Correctness sources

- assigned RESULT.md at frozen Git tree
- artifacts/verify_equivariance.py and verification_output.txt
- standard commutant fact for the defining real orthogonal representation
- arXiv:2609.19363 public abstract and source summaries

### Correctness risks

- The source paper's complete proof text was not obtainable through the available arXiv/OA routes during this run; the mathematical correction itself does not depend on its numerical experiments.
- Full matrix preconditioning is not steepest descent in the source's fixed embedded metric.

## Originality — PASS

The abstract commutant theorem and adaptive matrix covariance methods are prior art and are not credited as new. The surviving claim is source-specific: under the left ambient \(O(d)\) action actually used for Stiefel frames, scalar second moments are not forced by equivariance, and even diagonal right-column scaling is a counterexample. Fresh published-finding searches located only the audited correction. The 2019 RASA and 2023 Stiefel-attention optimizer literature narrows algorithmic novelty but does not remove the source-specific correction.

### equivalent_formulations

Searches:
- Resultary search for Stiefel equivariance, scalar moments and matrix-valued preconditioning
- web searches for the source's scalar-moment/equivariance formulation

Evidence:
- The exact current record was the only theorem-level Resultary match.
- The source abstract publicly describes one scalar second moment per frame and exact \(O(d)\)-equivariance.

Reasoning:
The comparison was made at the level of the represented group action and its commutant, not by optimizer names.

### broader_coverage

Searches:
- Kasai–Jawanpuria–Mishra RASA 2019
- Kong–Wang–Tao 2023 Stiefel optimizer
- 2026 Stiefel-AdamW

Evidence:
- Matrix-valued and coordinatewise Stiefel adaptivity already existed as algorithms.

Reasoning:
Those broader algorithmic precedents are explicitly excluded from the novelty claim; they strengthen the need for the correction but do not themselves state it against this source's left-action uniqueness rationale.

### exact_database_or_table

Searches:
- current Resultary Stiefel/adaptive-manifold findings

Evidence:
- No database/table entry settles a representation-commutant statement.

Reasoning:
This is a structural theorem, not a lookup invariant.

### claim_vs_prior_implication

Searches:
- claim-to-prior implication comparison

Evidence:
- RASA shows non-scalar adaptive matrix-manifold preconditioning exists, while the elementary commutant calculation shows why it is compatible with the left action.

Reasoning:
The prior algorithms do not by themselves correct the exact claimed symmetry implication; the direct commutant argument does.

### source_inspections

- **Stiefel Attention: When the Geometry of Transformer Projection Matrices Dominates Optimizer Choice—and When It Does Not** — https://arxiv.org/abs/2609.19363. Trigger: Primary source whose symmetry rationale is being corrected. Material read: Public arXiv abstract plus multiple indexed source summaries; full primary PDF text was unavailable through attempted arXiv/OA access in this run. Method: Statement-scope comparison with access limitation recorded. Assessment: The accessible source confirms the scalar-moment method and exact left \(O(d)\)-equivariance; the package supplies the precise uniqueness statement it corrects. Evidence: The abstract explicitly says the optimizer carries one scalar second moment per frame and proves exact \(O(d)\)-equivariance.
- **Riemannian adaptive stochastic gradient algorithms on matrix manifolds** — https://proceedings.mlr.press/v97/kasai19a.html. Trigger: Prior matrix-valued adaptive-manifold optimization. Material read: Published algorithm scope as cited and described in the package. Method: Prior-art comparison. Assessment: Prior algorithmic coverage, not coverage of the source-specific correction. Evidence: RASA uses left/right covariance preconditioning on matrix manifolds.
- **Assigned equivariance verifier** — artifacts/verify_equivariance.py. Trigger: Exact finite counterexample and symmetry checks. Material read: Complete source and saved output. Method: Line-by-line inspection plus analytic reconstruction. Assessment: Correct corroboration. Evidence: The two-column preconditioned direction is non-collinear and the left/right equivariance residuals are at roundoff scale.

### checked_sources

- https://arxiv.org/abs/2609.19363
- https://proceedings.mlr.press/v97/kasai19a.html
- https://arxiv.org/abs/2205.14173
- assigned RESULT.md and verifier
- fresh Resultary search

### residual_risks

- The exact uniqueness wording in the very recent source could change in a later revision; the primary full text was inaccessible in this run.

## Scientific value — PASS

This is a substantive source correction rather than a generic observation: it changes the admissible design space under the paper's stated ambient coordinate symmetry from one scalar to an entire positive-definite column covariance, while preserving the source's valid scalar method and isolating steepest-direction preservation as the condition that truly forces scalar rescaling.

### Value sources

- source scalar Stiefel optimizer
- commutant classification
- RASA and prior Stiefel adaptive optimization

### Value risks

- No empirical or convergence improvement is established for the matrix-valued alternative.

## Limitations

- The abstract commutant theorem and matrix-valued adaptation are prior art.
- Full source text was not accessible through the attempted routes in this run; the exact source wording is therefore a residual attribution risk.
- No convergence-rate or transformer-accuracy improvement is claimed.

## Disposition

**PASSED**
