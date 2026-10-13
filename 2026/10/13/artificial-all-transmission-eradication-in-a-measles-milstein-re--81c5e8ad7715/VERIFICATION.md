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

# Reproducibility and scope

Execute `python verify.py` with Python 3.8 or later; no packages are required. The script evaluates both intended and printed infected-coordinate drifts at a common positive rational equilibrium, the source disease-free state, exact characteristic polynomials, the one-step infected-mass cancellation, cone preservation for one interior test state, and a source-parameter bound on the Euler step. Its success marker is `VERIFY_OK`.

The proof's general \(\beta\)-uniform extinction result is symbolic, not an inference from those finite tests: the displayed sum of the two printed recurrences is an identity for every nonnegative six-vector with positive total population. The step restriction ensures the positivity hypotheses continue to hold for all iteration indices. The exact full-state endemic equilibrium and positive true invasion eigenvalue demonstrate substantive model disagreement. The code does not validate any stochastic random-increment implementation, prove pathwise convergence for Lévy processes, or certify the publication's simulations.
