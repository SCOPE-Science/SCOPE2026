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

The accompanying self-contained Python 3 `check.py` has been executed in a local Python runtime using rational arithmetic. It reported `EXACT_ASSERTIONS_PASSED 2607` across three exact rational annulus parameters and six finite block lengths, including pointwise verification of the weighted displacement identity and finite lower-bound inequalities. Diagnostic values are printed for the scaled residuals. No downloaded third-party paper is included.

The analytical proof handles every real \(0<q<1\) and all sufficiently large block sizes, and it establishes exact norm distance to the full displacement kernel rather than relying on a finite experiment. The finite checks are non-exhaustive and cannot independently verify the asymptotic theorem or publication priority. Independent audit and validation have not been performed.
