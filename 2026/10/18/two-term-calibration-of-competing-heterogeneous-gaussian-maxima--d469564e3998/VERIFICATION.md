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

The analytical claim is proved in RESULT.md using the exact finite-sample probability identity, the two-term normal Mills formula, a uniform inverse-tail expansion on an explicitly truncated probability-transform interval, an integrated Taylor remainder, and positivity of the calibration derivative. These are universal arguments for each fixed allowed parameter choice.

Run `python verify_gaussian_calibration.py` with Python 3, NumPy and SciPy. On the supplied code, the observed output ended with `PASS: 36 analytic consistency and finite-n quadrature assertions.` Tested \(r\in\{1.44,2,4\}\) and finite sizes \(n\in\{10^6,10^{12},10^{24},10^{48}\}\). The verifier evaluates the exact transformed finite-\(n\) integral, computes the analytic \(F,H,J\) constants, checks the integral derivative with respect to \(\log C\), tests the predicted error scale, and confirms that the optimized correction reduces the deviation in the largest example of each ratio.

The numerical method relies on finite quadrature accuracy, and its large integer sample sizes do not constitute an experiment with that many simulated Gaussian observations. No independent formal or human certification has been performed. The independent audit channel is unperformed.
