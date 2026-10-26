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

# Verification of the cycle positivity classification

Use `python verify.py` with `sympy` installed (see `requirements.txt`). The exact certificate `coefficients.json` contains numerator and denominator integer coefficient vectors, in ascending polynomial powers, for every symmetry-distance entry of the two-stage Radau IIA transition on each unweighted cycle of size three through ten. The script reconstructs every rational quotient from the cycle Laplacian over the rational function field, compares every vector to the certificate, checks positivity of all denominator coefficients and of the required numerator coefficients, and checks the isolated quintic negative example. No floating-point estimate establishes any sign assertion.

For all larger cycles the proof is independent of finite checking: the fifth Taylor coefficient of the scalar stability function is \(1/108\), and the signed count of shortest walks proves a negative fifth-order transition coefficient at graph distance five. The large-step limit is the rank-one stationary projection. Numerical positioning of the positive root is illustrative only; uniqueness is analytic via one sign change.

This verifies the claims made for the completed-step map, not internal stages, finite-precision implementations, weighted cycles, or a complete positivity set for larger cycles.
