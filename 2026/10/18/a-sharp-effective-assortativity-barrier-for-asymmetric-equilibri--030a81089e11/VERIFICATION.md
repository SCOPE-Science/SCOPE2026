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

# Reproducibility and scope of verification

Execute `python3 checks/verify_fold.py` from the package root. The Python standard-library `fractions.Fraction` tests 324 exact rational identities for the source vector field and the reduced common-pressure equations, verifies both zero residuals of the asymmetric stationary witness, tests the signed derivative, and samples elementary monotone-parameter cases. All stated exact identities and finite checks passed when packaged. The analytical cubic-boundary and whole-domain quantifiers depend on the proof in `RESULT.md`; the finite tests alone do not establish them.

The independently unperformed audit channel has no evidence. No numerical experiment or computer-assisted finite grid is represented as a proof of absence of additional fixed points. The literature comparison remains subject to an unindexed-equivalence risk.
