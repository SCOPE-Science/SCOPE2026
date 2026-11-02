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

# Verification and reproducibility

Execute `python check.py` with Python 3, NumPy, SciPy and SymPy. The packaged run passed 2,390 finite/symbolic assertions, covering symbolic response derivatives and integration, numerical tangency and integral identities at eight parameter pairs, finite-support clock comparisons, asymptotically sharp positive two-point examples, and Poisson recovery.

The all-clock inequality and equality classification rely on the analytic derivative sign, regenerative reward identity, concave majorant and Jensen equality conditions in `RESULT.md`, not on finitely sampled clocks. The root \(\xi=1.7932821329008\ldots\) and the \(19.37\%\) gain are numerical illustrations rather than rigorously interval-certified constants.

No independent scientific audit has been performed. The theorem is restricted to instantaneous exogenous complete renewal resets, positive confinement and heading-decorrelation rates, and signed long-run alignment.
