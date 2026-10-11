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

The exact algebraic check is implemented in `verify.py`. It clears the denominator in \(W=z-gx^2/(2a)\) and verifies symbolically, over the integer polynomial ring in the parameters and state variables, that
\[
2a\dot W=-b(2az-gx^2)+\bigl(2a(f+g)-bg\bigr)x^2.
\]
The checker is finite only because it compares exact polynomial coefficients; it is not being used to infer an infinite-time dynamical statement from samples.

The infinite-time step is proved analytically: for bounded complete trajectories and \(b>0\), variation of constants sends the backward homogeneous term to zero. Positivity of the kernel and \(\kappa>0\) then gives \(W\ge0\); equality at one time forces the origin trajectory by continuity, boundedness backward in the scalar \(z\)-equation, and uniqueness.

The result does not certify existence of chaos, a compact attractor, or any non-equilibrium recurrent trajectory.
