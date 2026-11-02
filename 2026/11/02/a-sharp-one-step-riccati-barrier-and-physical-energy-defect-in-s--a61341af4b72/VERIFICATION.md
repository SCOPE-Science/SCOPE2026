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

Run `python3 verify.py` alongside this file. It uses rational fractions and separately implements the cold-state five-stage updates. It compares the derived midpoint values, exact second-Riccati denominator, conserved modified energy, physical-energy defect, scaled-field consistency discrepancy and the Riccati pole-time inequality. Additional exact evaluation at the threshold checks that the denominator vanishes while the auxiliary variable remains positive.

The proof is the algebra in `RESULT.md`, not an inference from tests. Numerical floating-point tests are not needed for the claims. All results concern exact arithmetic, the specified one-cell periodic homogeneous model and winding-aware current deposition. Independent mathematical audit has not been conducted.
