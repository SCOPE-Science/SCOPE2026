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

# Verification record

The accompanying `verify.py` is an independent lattice-hopping approximation, not a repetition of the continuous-state Poisson-equation derivation. It implements an exact finite-state generator with motion inward at rate proportional to mesh inverse and orientation changes at the specified Poisson rate. It then computes stationary probabilities, two separate wall-contact Green–Kubo integrals, and the leading eigenvalue of generators tilted by their signed wall contact. Four mesh refinements were used at each of three parameter triples; all three contact-covariance discrepancies decrease with mesh size. Six tilted finite-generator eigenchecks also approach the analytical telegraph value with mesh refinement.

The program checks symbolic rational-function identities for the signed and total covariance and for the derivative of the total-contact variance coefficient. Execution with `python verify.py` (requiring NumPy, SciPy and SymPy) completed successfully with `FINITE_VOLUME_CHECKS_PASSED` and `SYMBOLIC_IDENTITIES_AND_TILTED_CHECKS_PASSED`.

The infinite-time limits, large-deviation principle, exact wall-density normalization and boundary conditions are established by the written analytical proof. Finite discretization checks only corroborate the claimed formulas; they neither establish infinite-dimensional convergence nor validate research originality. No independent external audit was performed.
