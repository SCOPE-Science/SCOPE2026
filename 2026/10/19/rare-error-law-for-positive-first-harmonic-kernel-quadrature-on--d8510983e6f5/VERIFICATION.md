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

The source `verify.py` is standalone, requires only Python 3 standard libraries and has a fixed deterministic random seed. Run `python3 verify.py` from the extracted package. The inspected program completed with `all checks passed 5746`.

Its tests covered polygon distance computations against the exact isotropic missing-gap identity, scale bounds for anisotropic features, independent numerical integrations of the conditional beta law, direct sampling of the conditional rare-failure geometry without exponential rejection, and normalizations of the exact circular second-moment integral. The conditional sampling Monte Carlo tolerances are loose and explicitly coded; statistical agreement is corroboration, not a proof of any universal statement.

The analytical proof in RESULT.md is the evidence for the results for all sample sizes and the asymptotic conditional law. Its critical nonstandard step is the uniform small-deficit supporting-chord projection and its determinant expansion; the midpoint Lipschitz bound is the required moment-dominating estimate. This verification makes no claim of independent auditing or certification.
