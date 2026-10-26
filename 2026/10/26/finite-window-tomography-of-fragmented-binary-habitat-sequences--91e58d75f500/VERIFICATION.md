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

# Verification scope

The general theorem is proved algebraically in `RESULT.md`. All inversion denominators are nonzero on the stated strict-interior feasibility region. Exact arithmetic checks are implemented in `verify_fragmentation.py` using `fractions.Fraction` and explicit enumeration of binary sequences for \(1\le n\le8\). Execute `python verify_fragmentation.py` in the directory containing the script, and compare its sorted, indented JSON standard output with `verification_certificate.json`.

The packaged verifier reports 1,350 parameter triples, 10,800 full probability-generating polynomial comparisons, 688,500 enumerated binary strings summed, 278 stationary examples (counted within the grid), and an exact two-cell nonidentifiability witness. The certificate is a finite computation record, not an independently certified or exhaustive infinite-parameter argument. The original mathematical assumptions—especially shared initial law across window sizes, homogeneity, strict positivity, and the spatial window boundary convention—must be maintained.

There has been no independent scientific audit; published sources provide contextual and overlapping forward methods but not external validation of this theorem.
