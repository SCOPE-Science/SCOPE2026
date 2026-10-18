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

# Reproducible finite verification

Execute `python3 verify.py` with Python 3.9 or newer, without extra dependencies. The script enumerates uniform permutations for all sizes from 2 through 8, checks exact first and mixed moments for every allowed consecutive monotone-run window length, and checks all increasing/increasing and increasing/decreasing overlap identities for lengths 2 through 5. It tests 140 moment assertions and 20 overlap assertions with rational arithmetic; its expected final line is `VERIFY_OK`.

The analytic proof establishes the limit. Exhaustive finite enumeration does **not** prove point-process convergence, independent Gaussian fluctuations, historical novelty, or mathematical value. No independent audit has been performed. The precise scope and limitations are in `RESULT.md`.
