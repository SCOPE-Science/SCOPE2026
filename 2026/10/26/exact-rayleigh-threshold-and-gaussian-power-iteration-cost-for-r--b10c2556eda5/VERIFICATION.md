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
Run `python3 verify.py` in a fresh Python 3 installation; only the standard library is used. The verifier enumerates vectors with small integer coordinates for dimensions 2, 3 and 4, and condition parameters 2, 3, 7 and 13. Exact fractions check Rayleigh scores, two-plane traces, the globally optimal relative eigen-scaling against a finite comparison grid, and the closed-form sharp contraction rate. It also checks four Gaussian power-initialization probabilities by deterministic-seed Monte Carlo, against closed-form two- and three-dimensional laws.

The analytical proof in RESULT.md, rather than finite enumeration, establishes all stated dimensions, parameters, strict inequalities and asymptotic limits. The finite random checks are not a certificate of tail asymptotics or of infinite-dimensional robustness. The full claim concerns objective-energy contraction with a separately optimizable scalar step; the proof does not establish performance for an externally prescribed step or a general Hessian.
