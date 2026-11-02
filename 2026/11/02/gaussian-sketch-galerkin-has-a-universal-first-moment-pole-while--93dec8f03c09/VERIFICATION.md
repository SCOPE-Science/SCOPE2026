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
# Verification of the one-step Gaussian-sketch comparison

The self-contained `verify.py` may be executed with `python verify.py` from this package. It uses only Python's standard library and has been executed from its packaged source. It checks, for sketch row counts one through ten, normalization of the explicit Gaussian/chi ratio density; for counts three through ten, the second-moment integral; for each row count, convergence of the reciprocal-pole tail coefficient by finite deterministic integration; and for 1,050 Gaussian sketch draws, agreement of the direct sketched Galerkin/minimal-residual algebra with orthogonal-coordinate formulae. Exact rational checks reproduce the two-dimensional example's energy error. A successful run prints `VERIFY_OK` with counts.

These are finite and numerical corroborations, **not** proofs of moment divergence or asymptotic tail constants. The rigorous argument is the density integration and positive density at the Galerkin denominator's zero, which appear in `RESULT.md`. The test's deterministic integration tolerance is documented in source. No other external code, stored data or certificates are required.

The scope excludes conditioned sketches and finite precision. Independent audit has not been performed.
