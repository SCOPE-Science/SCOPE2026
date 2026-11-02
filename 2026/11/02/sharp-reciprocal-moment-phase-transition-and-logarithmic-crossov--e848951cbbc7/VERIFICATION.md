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

The reproducible script `checker.py` computes exact probability distributions using rational arithmetic for three discounts and \(1\le n\le34\). It checks total mass one, the exact one-movement probability, a digamma-difference identity with its rational harmonic sum, and three normalized gamma-transform identities. All 612 exact assertions passed. Direct floating-point distributions at \(n=800,1600,3200\) independently corroborated the critical two-term asymptotic with observed-to-predicted ratios 1.0070899, 1.0046655, and 1.0030835, respectively.

The infinite limits, local-mass convergence, boundary-layer interpolation, and cancellation are proved analytically in `RESULT.md`. These are not inferred solely from code. The code requires Python 3 and SciPy for floating-point digamma; exact rational checks use the standard library. The two numerical outputs and exact assertion count were reproduced from the packaged checker.

Independent mathematical audit and independent priority review have not been performed.
