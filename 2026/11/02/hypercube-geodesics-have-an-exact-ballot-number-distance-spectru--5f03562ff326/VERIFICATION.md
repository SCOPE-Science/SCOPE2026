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

The binary-hypercube distance-shell formula is proved by a path automorphism reduction, a reflected-walk counting argument, and the factorization of untouched coordinate contributions. A complete proof appears in RESULT.md. A standalone finite checker enumerates distances in every dimension up to 12 for canonical geodesics, all rooted oriented paths up to dimension 6, and checks optimal path counts through dimension 10. The source must be run with Python 3.10+ via `python verify.py`; no third-party packages are needed.

Finite checks cannot establish infinite-dimensional quantifiers. They are cross-checks of the mathematical proof. Priority remains qualified because relevant older literature on dominating hypercube paths was not accessible in full text. No independent mathematical audit has been performed.
