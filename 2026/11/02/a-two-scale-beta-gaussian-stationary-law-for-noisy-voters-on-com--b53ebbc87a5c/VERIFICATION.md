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

# Reproducibility and verification

Run `python checker.py` using Python's standard library; no network, random seed, precomputed output, external data, or additional package is required. The script forms the lumped continuous-time generator, solves the stationary linear system with exact fractions and checks 409 assertions over 49 independent small systems. It tests probability normalization and positivity, both class mean fractions, all applicable within-part pair correlations, cross-part pair correlations, and the exact interpart variance; it also computes an independent finite-size fourth moment.

Separately evaluated numerical stationary systems with \(a=b=8,16,32\) and \(\theta=1/a\) gave respective scaled-difference variances approximately \(0.0900000,0.0867347,0.0850515\), and excess kurtoses approximately \(0.4736873,0.5243643,0.5587221\). The proven critical \(\lambda=1\) limit is variance \(1/12\) and excess kurtosis \(3/5\). These numerical figures are convergence checks only; they are not evidence of an infinite theorem by themselves.

The infinite result is obtained analytically from the generator and stationarity. The key quantitative controls are exact \(\mathbb E(P_A-P_B)^2=O(h)\); a rate-weighted third-jump bound of \(O(h)\) for the slow generator after scaling by \(h^{-1}\); a rate-weighted third-jump bound of \(O(\sqrt h)\) for the fast generator; and \(O(\sqrt h)\) for cross-observable jumps. Tightness and second-moment control justify the stationary subsequence argument. The complete proof and its limiting restrictions are in `RESULT.md`.

No external independent audit or external mathematical certification has been performed. Historical priority is not definitive.
