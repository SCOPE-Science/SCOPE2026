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

# Reproducibility and mathematical limits

The accompanying Python program `verify.py` independently evaluates the Bessel busy-period density, its arrival-rate score and Fisher information using scaled Bessel functions and adaptive quadrature. It tests density normalization, the exact first and second moments, the mean-zero score identity, comparison bounds for the Bessel quotient, likelihood finite differences, service-rate rescaling and the limiting trends at finitely many traffic intensities. The recorded execution completed 275 assertions without failure.

Install the pinned-minimum dependencies in `requirements.txt` and run `python verify.py`. The numerical program deliberately does not assert that a finite collection of parameter values establishes a uniform or infinite limiting result. Those conclusions depend on the analytical argument in `RESULT.md`, especially the light-traffic dominated-convergence bound and heavy-traffic bounded score remainder.

All formulas assume an independently restarted busy period initiated by one customer, a fixed known exponential service rate and \(0<\lambda<\mu\). The likelihood experiment is duration-only or count-only under the fixed-parameter KL covertness definitions. There has been no independent external audit.
