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

The proof uses the locally uniformly convergent Fourier mask product, an exact modular collision criterion, and arithmetic-progression counting. Every real zero and its analytic order are covered by the arguments in `RESULT.md`.

Run `python3 checker.py` in a directory containing `checker.py`; the script has no nonstandard dependencies. `checker_output.txt` records a completed run with exact rational counts for five representative mask-root angles and three frequency cutoffs each.

The checks verify sample count identities and modular orders, but do not replace the infinite proof. No external mathematical validation was performed. The result does not claim uniform error constants in the digit weight, nor does it classify complex zeros or Fourier bases.
