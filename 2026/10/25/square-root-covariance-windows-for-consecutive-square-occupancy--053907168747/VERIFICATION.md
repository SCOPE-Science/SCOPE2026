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

# Verification summary

Run `python verify_occupancy_boundary.py` with Python 3 and `mpmath` installed. The checker directly enumerates small occupancy assignments for \((r,s)=(1,4)\), compares exact rational mixed moments, verifies the finite one-step normalized-ratio identity for four successive-square pairs, and compares 65-digit evaluations to the predicted second-order profile. The observed result was `PASS 3242 finite exact/high-precision checks`.

The exact recurrence in equation (4) and the Taylor expansion with uniform remainder in equations (5)--(8) supply the unrestricted mathematical proof. Bounded tests do not prove infinitely many parameter cases or settle the boundary sign at critical \(z\) values. No independent external audit was performed.
