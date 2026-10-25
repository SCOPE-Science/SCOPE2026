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

The Python standard-library file `verify.py` was run successfully. It performs 132 deterministic finite diagnostics: two exact planar moment equalities, 24 integer-exact even-sign-moment identities, 100 comparisons of convex hull areas formed from independently projected octahedral vertices against the facet formula, and six asymptotic-scale numerical comparisons.

Analytic evidence is the five-part proof in `RESULT.md`: a facet-projection identity; a spherical beta integral; a bivariate Gaussian absolute-product identity; exact sign moments with a uniform Taylor remainder and gamma asymptotics; and fiberwise translation-volume integration.

Finite diagnostics cannot establish the all-dimensional variance limit by themselves. No formal theorem prover or independent external reviewer was used. Priority relative to unpublished or unindexed work is not certified. The independent audit remains not performed.
