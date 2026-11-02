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

# Reproducibility notes

Run `python verify.py` with NumPy and SciPy. On the checked code, the program reports 72 full-matrix spectral comparisons (\(m=1,2,3,4,5,7\), three transmission rates, four residence times), a numerical switching transition at approximately 3.034908427660, and nonlinear phase-locked endemic orbits at three group sizes. Both half-period exchange symmetry and the inactive-to-active leaf ratio are checked with stringent ODE integration tolerances.

The analytic proof establishes all-size assertions. Matrix tests at finitely many sizes do not certify the infinite family, and 180 iterations of the return map are not by themselves a convergence proof. The mathematical theorem is restricted to continuous-time deterministic NIMFA and the explicitly specified periodic star pattern. No independent validation has been performed.
