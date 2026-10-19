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

The displayed stationary states are obtained by sector-projecting the faithful diagonal invariant density matrix. A direct Lindblad-adjoint dissipation identity establishes the absence of all other stationary or oscillatory modes; the full proof is in `RESULT.md`.

The standalone `check.py` (NumPy and SciPy) was executed on the actual included source and reported **PASS: 306 numerical assertions across thermal ratios and initial states**. It checks the two-dimensional zero eigenspace and remaining negative spectral real parts, exact stationarity, trace and positivity, spin-swap conservation, concurrence for 21 singlet weights at each of 5 positive thermal ratios, and asymptotic agreement of a separable initial state with the predicted limit at 3 ratios.

Finite numerical assertions are not a proof of universal convergence. The analytical argument covers all strictly positive rates, every nonzero equal hopping, every real on-site frequency and every initial three-spin density matrix. A separate independent scientific audit has not been performed.
