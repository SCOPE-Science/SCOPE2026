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
# Verification

The theorem is analytic. The accompanying checker uses exact rational arithmetic and exhaustive edge-state enumeration.

It tests several base graphs containing isolated triangles, overlapping triangles, chorded structures, and complete graphs. For multiple rational values of \(p\), it enumerates every percolation configuration, computes \(K\), \(T\), and \(R\), and independently computes the triangle-deleted probabilities
\[
\Pr(C_\tau=2)
\quad\text{and}\quad
\Pr(C_\tau=3).
\]

It then verifies the component covariance formula, the cycle-rank covariance formula, and both universal cycle-rank bounds exactly.

The subcritical limits are not inferred from finite computation. They follow from the simple-path union bound and the exact finite identities in `RESULT.md`.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK graph_parameter_checks=18 percolation_states=3888 connectivity_states=4110 triangle_instances=60`.
