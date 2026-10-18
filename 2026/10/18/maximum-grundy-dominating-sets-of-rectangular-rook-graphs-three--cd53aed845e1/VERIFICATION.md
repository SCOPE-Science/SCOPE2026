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

The executable `verify.py` was run from the extracted package's contents. It independently computes legal domination by testing closed-neighborhood increments for every candidate set of size \(m+n-2\), compares against the exact three-forest structural predicate, and compares both counts with the closed Stirling-number expression. It checks nine boards from \(2\times2\) through \(4\times4\). See `verification_output.txt` for actual counts and `VERIFY_OK`.

These finite cases do not prove the all-size theorem; the proof is in `RESULT.md`. No external independent audit or certification has been performed.
