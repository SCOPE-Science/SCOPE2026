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

The face vector read from Theorem 3.3.1 of arXiv:2512.21190v1 is \((21,120,420,480,192)\). The script `verify_euler.py` uses exact integer arithmetic to compute the alternating sum and confirms \(\chi=33\ne3\). The comparison value \(3\) is the Euler characteristic of \(\mathbb{CP}^{2}\), with one cell in each of dimensions \(0,2,4\).

This check verifies only the stated numerical incompatibility. It does not reconstruct the dual complex, inspect every geometric stratum, infer a corrected face vector, or independently validate the cited theorem's applicability to the stack construction.
