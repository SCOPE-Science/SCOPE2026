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
The analytic proof uses only the defining upper bound, compactness of the finite-dimensional unit ball, equality cases in the triangle and quadratic inequalities, and the exposed-edge geometry of the unit hexagon.

`verify.py` uses exact rational arithmetic. It checks eleven admissible endpoint approximants and solves all twenty-four ordered pairs of incident exposed edges by exact three-variable linear-program vertex enumeration. The smallest possible value of \(N(y-z)\) under the limiting double-equality face constraints is exactly \(1\).

The checker does not prove a formula for the subcritical values. Its role is to replay the finite polyhedral lemma and the endpoint construction used by the analytic proof.
