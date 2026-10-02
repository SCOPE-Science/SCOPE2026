# Scientific audit — 2026-10-01

## Final claim assessed

Sharp shortest-edge volume profile for diameter-bounded simplices

## Correctness — PASS

PASS. The coordinate/determinant argument was reconstructed. After placing the distinguished edge symmetrically, the volume equals \(s|\det Y|/n!\). Diameter constraints give \(\|y_i\|^2\le D^2-s^2/4\) and \(\|y_i-y_j\|\le D\). The weighted complete-graph frame operator \(S=YQY^	op\) has a computable determinant and a sharp trace bound; AM--GM on its eigenvalues yields exactly the displayed volume profile. Equality forces every transverse norm and pairwise-distance constraint to be tight, hence every edge except the distinguished one has length \(D\). The converse Gram matrix is positive definite and makes the frame operator scalar. The normalized shortest-edge profile and inverse formula follow algebraically.

## Originality — PASS

PASS to the best of current knowledge. Searches covered the classical largest-small-simplex problem, recent aggregate frame inequalities, prescribed-edge and shortest-edge formulations, and distance-geometry terminology. The full 2025 frame-inequality preprint was inspected: it gives volume bounds from total edge energy and the regular-simplex equality case, but contains no diameter condition and no one-edge-conditioned profile. No located primary source states or mechanically implies the exact formula, equality family, or inverse shortest-edge law.

### equivalent_formulations

Searches: search: maximum volume simplex prescribed edge diameter; search: shortest edge simplex volume diameter inequality; Resultary: shortest-edge volume profile diameter simplex

Evidence: No exact prior theorem was located under prescribed-edge, shortest-edge, edge-ratio or diameter-stability wording.

Reasoning: All such formulations describe the same constrained optimization problem; none of the inspected results supplied the claimed envelope.

### broader_coverage

Searches: arXiv:2202.09920 finite variations on the isoperimetric problem; arXiv:2509.05611 frame inequalities simplex; classical largest-small simplex literature

Evidence: Classical work identifies the regular simplex as the unconstrained diameter extremizer; the frame paper bounds volume through aggregate squared edge lengths.

Reasoning: Neither broader result fixes one edge while keeping only a diameter bound, so neither mechanically yields the sharp conditional profile.

### exact_database_or_table

Searches: Published-record semantic search for prescribed shortest-edge simplex extremum

Evidence: No natural database is relevant and no earlier exact theorem record was found.

Reasoning: The claim is a continuum extremal theorem with a full equality classification.

### claim_vs_prior_implication

Searches: Ledford--Rivera-Ayala--Schroeder 2025 Section 3; Fejes Tóth survey of diameter extremal problems

Evidence: The edge-frame inequality uses total edge energy rather than one prescribed edge and does not imply the profile after only imposing pairwise distances at most \(D\).

Reasoning: The weighted frame/distance constraints used in the assigned proof provide the additional sharp information.

## Scientific value — PASS

PASS. The theorem refines the classical regular-simplex diameter extremum into a sharp one-parameter stability profile valid at every shortest-edge ratio. The equality family and best-possible inverse edge bound are natural geometric information, not an arbitrary finite slice.

## Source inspections

- **A note concerning frames and geometric inequalities** — https://arxiv.org/abs/2509.05611. Material read: Complete primary text in the simplex vertex/edge-frame section and surrounding equality statements. Assessment: AGGREGATE_EDGE_INEQUALITY_NOT_CONDITIONAL_PROFILE. Evidence: The paper proves volume bounds in terms of aggregate frame norms and the regular-simplex equality case; it contains no diameter constraint or one-short-edge extremal theorem.
- **Finite variations on the isoperimetric problem** — https://arxiv.org/abs/2202.09920. Material read: Primary abstract and survey scope describing largest-small-polytope problems. Assessment: BACKGROUND_CLASSICAL_EXTREMAL_CONTEXT. Evidence: The survey provides the classical diameter-extremal context but no inspected statement of the assigned conditional profile.

## Limitations and residual risks

The theorem is Euclidean and simplex-specific. It controls edge lengths rather than stronger intrinsic shape metrics, and it optimizes only one prescribed edge. An equivalent older distance-geometry formulation remains a residual originality risk.

- The proof is elementary enough that an older equivalent result may exist in distance geometry or finite-element shape literature under different terminology.
- No multi-short-edge optimization or non-Euclidean analogue is claimed.

## Disposition

**passed**
