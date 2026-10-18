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

Execute `python3 verify.py` with Python 3 and its standard library. The script enumerates every increasing labeled recursive tree for sizes 2–9 and attachment weights 1/3, 1/2, 1, 2, 5, computes its probability by multiplying exact rational parent-selection weights, and independently calculates leaf count and root-to-node depth sum. Its assertions check exact leaf/path means, exact covariance, the sign boundary, and the uniform-tree specialization. A successful run displays `VERIFY_OK parameter_size_pairs=40 trees=231165 exact_assertions=208`.

This checks finitely many cases only; infinite correctness is based on the recurrences and analytic induction in RESULT.md. No independent audit has yet been conducted. The external variance inputs and the implicitly covered uniform model are identified in RESULT.md.
