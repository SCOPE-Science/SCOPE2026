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

# Verification of the two-by-two RJD restart-moment calculation

Execute `python verify.py` using Python 3; no third-party packages or data files are required. Successful output begins with `VERIFY_OK` and includes the number of independently checked rational instances.

The checker verifies the exact two-matrix eigenbasis loss equality for 2,100 rational parameter/coefficient combinations, independently reconstructs 1,872 explicit eigenbases and checks their directly measured matrix residuals, and checks that ranking coefficients by the unsigned Gaussian angle agrees with ranking by the computed loss. Deterministic Simpson integration tests the exact single-trial expectation against \(2\varepsilon\) at four nonzero choices of \(\varepsilon\) and compares the third-trial limit integral with \(48\log2/\pi^2\).

These are finite algebra and quadrature checks; they do not certify the uniform asymptotic error in the two-trial logarithmic law, the order-statistic distribution, or the dominance argument for arbitrary integers \(L\ge3\). Those steps are justified analytically in `RESULT.md`. Eigenvalues are assumed computed exactly and numerical floating-point effects are outside the result.

No independent audit, proof assistant certification, or external validation has been performed.
