---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The proof expands the full power-distance quadratic form on the zero-sum subspace into core and peripheral block-contrast squares plus a rank-one form on peripheral block sums. Its necessary-and-sufficient inequality, monotone root, critical null vector, strict Schur-concavity of the size-profile function, and equal-size boundary cases are derived analytically in RESULT.md.

The standalone artifact `verify_multicore.py` independently builds the specified graph, computes shortest-path distances, projects to zero-sum coordinates, compares eigenvalues on both sides of the predicted threshold, confirms the endpoint equality vector, and verifies the closed form and balancing inequality on bounded samples. Running `python verify_multicore.py` succeeded with `PASS multicore supplementary checks: 6570`. Numerical experiments are finite and supplement, rather than certify, the infinite-parameter theorem.

Known limitations: the proof assumes unit edges, complete core and peripheral cliques, integer parameters with at least two core and peripheral blocks, and real Hilbert-space target geometry. Historical equivalence outside inspected accessible literature has not been excluded. Independent mathematical validation has not been performed.
