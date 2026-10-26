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

# Verification details

Execute `python verify.py` with Python 3. It cross-checks permutation enumeration and an independently constructed subset dynamic program for all \(2\le n\le8\), all positional records, and all feasible descent counts. The exact unique positive determinant is 3043 and the probability difference is \(3043/1060371\). Only the descent boundary is finite; the global inversion statement follows from the independent-uniform insertion code and convolution log-concavity proved in RESULT.md. The computation uses exact Python integers and fractions. Independent audit has not been performed.
