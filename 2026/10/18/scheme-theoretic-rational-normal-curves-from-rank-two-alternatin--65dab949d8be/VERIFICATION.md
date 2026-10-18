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

# Verification record

An exact standalone Python checker, `skew_toeplitz_verify.py`, uses only the standard library. Running `python3 skew_toeplitz_verify.py` reconstructs recurrence polynomials in two homogeneous variables and directly substitutes them into every four-index Pfaffian for matrix sizes \(n=4,5,6,7,8,9,10\). It also computes exact rational ranks of the selected quadratic coefficient vectors, verifying \(\binom{n-2}{2}\) independent quadrics at each size. It prints `VERIFY_OK` upon success.

This finite computation does not establish any case beyond \(n=10\); the unrestricted and all-characteristic assertions follow instead from the triangular coordinate change, universal polynomial identity, weighted independence argument, and quadratic generation of the rational normal curve ideal, as proved in RESULT.md. No separate external mathematical audit has been carried out.
