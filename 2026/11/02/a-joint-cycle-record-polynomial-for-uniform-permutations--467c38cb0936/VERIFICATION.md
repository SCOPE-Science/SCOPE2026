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

The complete finite verification is in the accompanying `verify.py`, executable with Python 3 and no additional packages. Its direct enumeration compares each coefficient of the joint generating polynomial against independent counts of cycles and one-line upper records for all sizes from 2 through 8; it also checks exact positional covariances and Ewens probabilities for four parameter values. On execution the program reports `VERIFY_OK` and the number of comparisons.

A finite census does not prove the unrestricted result. The general argument uses (a) contraction of fixed permutation arrows into path components, (b) the weighted-cycle formula for uniform injections, (c) a hypergeometric maximum-rank decomposition, and (d) rising-factorial telescoping. The polynomial holds for every complex evaluation variable, and the Ewens conclusion requires a positive real parameter. Historical-priority risk remains; this verification does not constitute an external independent audit.
