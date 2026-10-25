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

The included `verify.py` was executed using Python 3 with SymPy and NumPy, and completed without assertions. It independently reconstructs the cycle map from alternating coordinate refreshes and checks its matrix, characteristic polynomial and three factored Schur–Jury expressions, followed by 500 exact-rational direct-cycle comparisons and 3,000 numerical root-location checks, plus limiting cases. These finite checks supplement but do not establish the infinite-parameter proof.

The full stability classification uses the explicit characteristic polynomial and strict cubic Schur–Jury conditions. At the exact stability boundary, strict inequality fails, and the argument using \(E+TE=\mathbb R^3\) shows nonconvergence from some zero-buffer initial positions. Supremum \(3\) is not attained because \(|c|<1\). The analysis does not cover arbitrary Hessians, noise, nonlinear objectives, or transient objective monotonicity.
