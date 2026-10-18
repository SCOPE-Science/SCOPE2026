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

The included standalone `verify.py` performs exact finite-field arithmetic in polynomial quotient models of orders 4, 8, and 16. It enumerates unordered support pairs, checks Sidon uniqueness and character halfspace sizes, and compares flat and phase-coded nonvanishing counts with the two rank formulas. The encoded root phases are handled symbolically using the odd-order root noncancellation argument; no floating-point tolerance is used. The results are in `verify_output.txt`. The proof in RESULT.md establishes the statements for all finite binary Sidon supports with odd support size; the finite examples are not claimed to certify all parameters.
