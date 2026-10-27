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

Run `python verify_hapax_runs.py` with Python 3 standard library. The actual checker returned `PASS 1050 exact assertions; witness signs [1, -1, 1, -1]`. It checks the general covariance identity against direct rational enumeration for five alphabet laws and lengths 2–6; tests the binary and uniform formulas exactly; and checks the three-letter rational witness. These tests do not prove the induction for unrestricted alphabet sizes. The complete proof and explicit two-scale estimates are in `RESULT.md`.

Publication priority has only self-review, not independent audit. Exact moment formulas are compatible with classical joint-distribution generating functions, and the main scientific claim is restricted to unbounded sign-reversal counts.
