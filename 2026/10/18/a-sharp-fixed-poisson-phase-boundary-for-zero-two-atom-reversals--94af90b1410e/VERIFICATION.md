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

# Verification evidence and scope

The analytic proof is in `RESULT.md`. Its decisive identity is the exact change in the zero–two point-probability ratio when two positive Bernoulli probabilities are merged without altering their sum. It provides a direct sign criterion and supplies the equality cases.

Run `python verify.py` from the directory containing the documents. The executable uses Python `fractions.Fraction`, exhaustive rational grids for up to four independent coins, and direct exact comparisons of odds polynomials, merging formulas, threshold cases, and equality configurations. The completed execution passed 10,390 exact rational assertions.

The finite enumerations do not establish universality. The proof covers every fixed positive Poisson rate and every finite Bernoulli vector through the merging argument, and includes the endpoint \(\lambda=\sqrt2\). It does not establish a sharp global envelope for Bernoulli mean at least one or for other pairs of atoms.

Independent mathematical audit has not been performed.
