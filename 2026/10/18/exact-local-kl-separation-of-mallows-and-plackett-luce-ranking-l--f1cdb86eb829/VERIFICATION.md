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

Run `python3 verify.py` from the extracted package directory. The checker enumerates all permutations on two through six alternatives, computes score moments as exact rational numbers, and independently compares the claimed coefficient to the rank-score orthogonal projection. Expected output is a success message with the number of checked dimensions. The mathematical expansion uses an analytic implicit-function/Taylor argument; enumeration alone cannot prove an infinite family. A separate finite optimization probe at perturbations 0.01 and 0.05 produced curvature ratios approaching \(5/168\) for three items and the stated coefficient for four and five items. No independent external audit has been performed.
