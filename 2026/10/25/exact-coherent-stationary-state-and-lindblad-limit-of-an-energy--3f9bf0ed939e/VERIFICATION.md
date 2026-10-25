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

The mathematical argument appears in `RESULT.md`, including the explicit generator decomposition, all-offset stationary recurrences, phase-mixture positivity, purity summation, and trace-class convergence bound. To rerun the accompanying finite-section checks, use `python verify.py` after installing NumPy. The verification script checks five parameter sets, exercises the incoherent and pure endpoints, and computes an exact rational purity witness.

Finite cutoffs are not represented as closed physical upper boundaries: the script inspects only the interior matrix entries for which the infinite-ladder shifts are unchanged. Finite eigenvalue and residual checks are not certificates for infinite dimension. No independent audit or external certification has been performed. The proof does not cover trace-norm convergence of arbitrary initial states or fixed-step Lindblad embeddability.
