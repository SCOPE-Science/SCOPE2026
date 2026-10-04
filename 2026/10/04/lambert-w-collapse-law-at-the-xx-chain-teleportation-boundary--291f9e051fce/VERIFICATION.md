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

The source threshold
\[
\sinh x=\cosh(\eta x)
\]
is solved by monotone bisection in `verify_xx_teleportation_boundary.py`.

The checker independently evaluates the source fidelity and concurrence, reproduces all nine published table rows for \(\eta=0.1,0.2,\ldots,0.9\), and verifies the equivalent hyperbolic-tangent equation.

For endpoint values through \(\eta=0.99999\), it evaluates the principal Lambert function by Newton iteration and checks convergence of both asymptotic ratios to one.

These computations are finite checks. Uniqueness and the asymptotic statements are established analytically in `RESULT.md`.

No independent audit has been performed.
