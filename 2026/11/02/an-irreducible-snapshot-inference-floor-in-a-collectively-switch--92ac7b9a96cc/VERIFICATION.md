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

# Verification of stationary snapshot inference

The proof derives the exact joint signal/state stationary density from the Markov forward equations, the independent Gaussian conditional distribution, the Bayes-optimal threshold and the threshold-local \(N^{-1}\) expansion. The numerical file `verify.py` calculates the full beta-Gaussian likelihood and its root without assuming the limiting threshold. It validates fifteen (shape, noise-level) combinations; checks the exact uniform-beta CDF formula, symmetric incomplete-beta representation, and both symmetric extreme-switching limits. Run with Python 3, NumPy and SciPy using `python verify.py`. All assertions passed in the recorded local execution.

Quadrature and finitely many samples cannot establish the theorem for all parameters or certify bibliographic priority. The conditional-state beta law appears already in the cited Herbach work. Independent scientific audit is not performed.
