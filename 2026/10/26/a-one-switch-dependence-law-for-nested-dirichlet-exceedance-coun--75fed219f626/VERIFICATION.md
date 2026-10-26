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

# Scientific verification and limits

The standalone `verify.py` enumerates 139,672 exact-rational covariance sign checks for uniform-simplex dimensions and selected-coordinate counts, checks the explicit negative three-point graph example, and brackets exact crossing roots on either side. The same script uses standard-library seeded independent gamma draws to corroborate five unequal-threshold covariance signs at Dirichlet parameters outside \(\alpha=1\). Its output is stored as `verification_results.txt`.

The invariant proof is analytic: exchangeability yields an exact covariance reduction, Dirichlet neutrality and the beta density establish a strictly decreasing conditional tail, the equal-threshold variance anchors the positive side, and the disjoint-threshold boundary anchors the negative side. The all-\(n\) asymptotic follows from deterministic expansion of the exact finite formula. Finite tests cannot establish strictness or unique crossings for every real parameter. No independent external validation has been performed.
