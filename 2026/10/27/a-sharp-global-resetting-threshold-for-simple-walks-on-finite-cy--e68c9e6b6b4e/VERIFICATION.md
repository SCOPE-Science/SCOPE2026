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

# Reproducibility and limits

The self-contained `verify.py` checks the claimed polynomial identities and the global nonnegativity certificate over a finite integer range by exact rational arithmetic. It independently solves exact linear mean-hitting-time equations and compares their output with the rational polynomial formula. Invoke `python verify.py` with Python 3 and no nonstandard dependencies.

The infinite parameter claim is proved by the coefficient comparison in `RESULT.md`; finite checks are not an exhaustive proof. The source comparisons use published primary papers, and historical priority remains subject to independent evaluation.
