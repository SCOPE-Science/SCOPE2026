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

# Verification and boundaries

The analytical verification is the stationary-generator calculation and the complete sign analysis of the derivative in `RESULT.md`. The standalone `verify.py` program generates the four affine jump maps in the original opinion coordinates and evaluates stationary equations for the five independent first/second moments, with exact arithmetic for 48 rational parameter triples. It checks symmetry of the resulting variances, the analytic means, nonnegative covariance determinants, the symbolic derivative factorization, and the stationary centered-coordinate moment equations.

Reproduction: install SymPy in a Python 3 environment, then run `python verify.py` in a directory containing this file. The program printed: `PASS: symbolic derivative, stationary z/d identities, and 48 independent exact-rational generator reconstructions.`

The finite tests are not used to infer global monotonicity, the unique maximizer, or uniqueness of the invariant distribution. These follow from the explicit algebra and contraction argument. The claim is restricted to independent Poisson meetings, equal trust fractions, two regular agents, and two opposing fixed opinions; there is no independent audit or empirical validation.
