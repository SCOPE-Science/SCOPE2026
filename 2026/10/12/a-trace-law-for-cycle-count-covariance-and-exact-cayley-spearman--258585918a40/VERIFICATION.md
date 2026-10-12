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

The theorem is analytic for every \(n\ge2\) and every deterministic real array.

`checker.py` performs an exact-rational replay. For every \(2\le n\le9\), it exhaustively enumerates all permutations and checks the cycle-count mean and variance, cycle/squared-displacement covariance, Cayley/Spearman covariance, Spearman variance, and the exact correlation-squared formula.

For every \(2\le n\le8\), it separately checks the conditional cycle mean under each event \(\Pi(i)=j\), including the diagonal/off-diagonal distinction that drives the proof. It also evaluates several symmetric and nonsymmetric integer arrays and compares their enumerated cycle-count covariances with the trace-minus-grand-mean formula.

The finite calculations are consistency checks only. The contraction argument proves the universal statement.
