# Review of the exact star-conditioned elliptope–cut comparison

## Correctness

**PASS.** Permutation averaging retains the objective and every feasible convex set. The Schur-complement eigenvalues of the resulting two-parameter Gram matrix give the exact bare-SDP envelope. The four triangle inequalities on every three vertices reduce to two additional scalar bounds, producing all three sharp branches with explicit feasible constructions. The cut-polytope calculation reduces to a concave interpolation of the exact integer clique-cut profile. Its interpolation deficit is exactly \(\alpha(1-\alpha)\) on the PSD-controlled branch. The analytical argument treats every real tolerance, all dimensions, and boundary points. The bundled `verify.py` reproduced 7,804 exact-rational checks and 95 optional small linear programs; these are supplementary, not infinite proofs.

## Originality

**PASS with residual risk.** The primary September 2026 spanning-tree paper proves *exact* correlation-integrality propagation, not the support-function values under positive star tolerances. The 2026 volume comparison of the cut, metric, and elliptope bodies includes the already-known first separation at five vertices, but its results concern volumes, not this whole star-conditioned objective phase diagram. Fixed-rank MaxCut integrality bounds concern Gram rank; cardinality-constrained MaxCut concerns deterministic cut sizes, not the intersection of the cut polytope with marginal bounds. No covering statement arose in the inspected primary texts, published-result searches, or existing-claim comparisons. A full historical cut-polytope monograph was not verified, and equivalent parameterized moment inequalities remain possible. The known cut-profile formula is credited as an input, not advertised independently as new.

## Value

**PASS.** The gap under uniform near-integral star correlations is a natural quantitative refinement of exact spanning-tree integrality. Its complete all-size phase diagram identifies the precise one-leaf-flip threshold, the sharp universal additive defect \(1/4\), and the first dimension where triangle cuts fail to match the cut-polytope slice for this objective. It supplies a benchmark for semidefinite bounds at partly decided star branches. It does not claim arbitrary-graph applicability, deterministic-constraint equivalence, or improved solver run time.

## Unresolved scientific and literature limits

The gap is for the **cut-polytope moment slice**, which is not an integer feasible-set hull under literal positive tolerance. The analysis does not extend automatically to nonuniform tolerances, general tree topologies, other objective weights, or stronger inequalities. General geometric separation between metric and cut polytopes is prior art, and exhaustive equivalence against historical monographs is not established.

Self-review: passed. Independent audit: not yet performed.
