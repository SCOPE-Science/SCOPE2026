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

# Verification of the exact endpoint-noise allocation result

The analytic result assumes a Hermitian three-site tridiagonal Hamiltonian with unit coherent hopping, arbitrary real central detuning, right-end sink rate strictly positive, and fixed positive total pure dephasing divided only between the two endpoints. The initial state is the left-end projector.

The independent nine-dimensional complex Lindblad superoperator construction, run directly from `check_endpoint_noise.py`, verified 900 seeded parameter points against the closed rational mean-absorption formula. Symbolic checks confirmed all nine integrated-density linear relations, the trace identity and the second derivative. The program also checked 1,200 strict-convexity/derivative comparisons, 650 global minimizations, and representative settings on both endpoints and inside the allocation interval.

The decisive non-numerical steps are: total absorption by positivity and finite-dimensional irreducibility along the chain; the unique solution of the integrated master equation; strict positivity of the analytic second derivative at nonzero detuning; and endpoint slope comparisons. Uniform sampling does not prove these statements; the proof does. The numeric comparisons are illustrative tests under finite arithmetic precision. No independent audit was performed.
