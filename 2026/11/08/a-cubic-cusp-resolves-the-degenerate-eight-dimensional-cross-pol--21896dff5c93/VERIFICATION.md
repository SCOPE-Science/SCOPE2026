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

The bundled `verify_saddle.py` was executed from its real package path with installed SymPy and mpmath, returning `SADDLE_EXACT_OK`. It symbolically checks the two tangent-unit vectors, the base integral \(\pi\sqrt2/4\), exact cancellation of the collective quadratic coefficient, the beta-integral reduction to \(3003\pi/512\), the normalized positive cubic coefficient \(1001\sqrt3/3072\), and the normalized negative quadratic coefficient \(-3/2\). Supplementary high-precision quadrature at three perturbation magnitudes confirms the predicted signs and leading coefficients.

The exact cancellation and integral values are not a computer substitute for the asymptotic argument: the latter follows from the displayed uniform remainder estimates, the bounded and tail-region split, and dominated convergence. Neither enumeration nor numerical observations assert a global maximum or comprehensive classification of critical points. This is a self-review only; independent audit has not been performed.
