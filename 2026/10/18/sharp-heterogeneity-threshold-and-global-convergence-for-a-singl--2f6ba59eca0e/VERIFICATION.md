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

The exact theorem is proved analytically in RESULT.md. The diagnostic program `verify.py`, using only Python 3 standard library, completed successfully for all five specified parameter vectors. It checked the unique scalar fold through monotone bracketing, finite-dimensional stationary identities for both branches, the strict heterogeneous geometric-mean comparison, Jacobian reduction, envelope derivative by finite differences, and the analytic potential-gradient equality by centered differences. A separate symbolic calculation over independent three-variable symbols simplified each component of the gradient identity to zero.

The verified reference values are \(\lambda_*=4\) for three equal ratios and \(\lambda_*\approx4.586911204889\) for \(b=(1/4,1,4)\), with common geometric mean one; at four equal ratios the fold is \(27/4\), compared with \(8.383037599343\) for \(b=(1/4,1/2,2,4)\).

These tests do not enumerate all parameter choices, compute stochastic-chain fixation probabilities, or replace the proof of convergence for arbitrary initial states. The proof's key nonstandard steps are the scalar equilibrium correspondence, the rank-one inertia computation, and the coercive gradient potential. The model is continuous time and deterministic; no external certification or independent audit has been performed.
