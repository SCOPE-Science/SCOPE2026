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

# Reproducibility

The standard-library-only `verify.py` contains independent finite tests for the theorem. Run `python3 verify.py` in the same directory as this document. The expected terminal output is `VERIFY_OK`; the recorded output for this package appears in `verify_output.txt`.

The checker tests both forbidden classical patterns on every permutation through length nine by enumerating index quadruples, computes the maximum product over all avoiding outcomes, and checks the exact values. An independent simulation generates every preference sequence of lengths one through five, parks its cars physically, and compares every successful outcome's fiber size to the product formula. Integer dynamic programming independently evaluates the complete exact composition recurrence through order 150, checks its agreement with the closed form, and verifies the eventual five-step multiplier over the checked range. The strict part-splitting inequality is also independently checked over a finite range.

**Scope of verification:** All mathematical claims for unbounded order require the proof in RESULT.md. Finite checks do not prove avoidance of an arbitrary pattern or an infinite recurrence identity by themselves. Originality rests on bounded scientific literature comparison, not on executing this checker. External independent audit was not performed.
