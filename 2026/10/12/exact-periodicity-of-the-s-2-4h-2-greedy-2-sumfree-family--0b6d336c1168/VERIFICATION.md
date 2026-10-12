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

The exact verifier is `artifacts/verify_greedy_2_4hplus2.py` (Python 3 standard library only). It checks all residue and distinct-sum interval formulas and their exhaustive coverage for the affine endpoint stability window; it separately checks circular gap uniqueness and raw greedy generation for small parameters. The affine-bound calculation proves the finite check sufficient for every permitted parameter, subject to the elementary endpoint-order argument given in `RESULT.md`. Run the script from the package root and compare its stdout with `artifacts/verification_output.txt`. No independent review is represented by this file.
