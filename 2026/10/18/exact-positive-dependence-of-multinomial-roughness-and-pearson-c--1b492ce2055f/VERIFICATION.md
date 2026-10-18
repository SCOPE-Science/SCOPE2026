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

The exact theorem is proved in `RESULT.md` using a multinomial factorial-moment identity, Jensen's inequality, local signed-jump enumeration, and the lattice local central limit theorem. This proof applies to all admissible finite \(n,N\) and fixes the periodic \(n=2\) boundary separately.

`verify_covariance.py` requires Python 3 and no nonstandard packages. Running `python verify_covariance.py` reproduces these independent exact-rational finite checks:

- 30 single-edge covariance comparisons, for \(2\le n\le6\), \(2\le N\le7\).
- 54 covariance identities for nonuniform, ternary-uniform, and binary-uniform masses, each against three convex functions, over six sample sizes.
- 15 weighted-graph covariance identities for paths, stars, and a nontrivially weighted graph at five sizes.

All assertions passed. These tests do not enumerate unbounded sample sizes and are not offered as an infinite proof. No external independent audit is asserted.

