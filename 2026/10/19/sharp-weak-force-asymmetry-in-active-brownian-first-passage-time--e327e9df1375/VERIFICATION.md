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

# Reproducibility

The accompanying `verify.py` is a standalone script using Python with `numpy`, `scipy`, and `mpmath`. Invoke `python verify.py` from the directory containing this file. No network access or external datasets are needed.

At each of six diffusivities, the code evaluates the exact susceptibility from its closed rational-hyperbolic form and independently from explicit Dirichlet Green quadratures. The largest relative discrepancy in the tested values is much smaller than numerical precision (55 decimal digits in the high-precision path). At four positive diffusivities it also directly solves the first-passage and time-moment backward boundary problems with angular modes zero, one and two, and checks the small-force, small-propulsion prediction. Relative deviations in that finite-parameter test are approximately 0.49%–1.20%, consistently decreasing when the perturbation parameters are further reduced.

For a further asymptotic check, the script evaluates the exact expression at \(\varepsilon=10^{-6}\), finding agreement with \(1/(12\varepsilon)+1/(4\sqrt\varepsilon)\) to the recorded numerical precision. All numerical comparisons pass. The proof is the stopped-path response identity and the exactly evaluated Green/resolvent system in `RESULT.md`; the computations are corroborating finite tests only. No external mathematical audit or infinite certification has occurred.
