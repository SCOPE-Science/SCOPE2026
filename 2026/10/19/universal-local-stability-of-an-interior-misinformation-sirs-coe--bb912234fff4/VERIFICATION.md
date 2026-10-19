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

# Verification of the all-time-scale local stability theorem

The standalone `verify.py` reconstructs the six-dimensional nonlinear ODE symbolically from its stated equations, verifies the exact positive coexistence equilibrium, checks the reduced four-dimensional Jacobian, and factors the full characteristic polynomial into the two normal modes and the tangent characteristic polynomial. It independently derives the rational Schur-complement characteristic identity and checks that the tangent Jacobian has nonzero determinant.

An exact positive rational specimen is included. Additional rational parameter points are tested with exact Routh–Hurwitz inequalities to catch sign errors. The script uses symbolic rational arithmetic, not approximate floating-point eigenvalue calculations. These finite tests establish reproducibility of the algebra, not universal stability.

The universal result instead follows from the analytically proved strict positive-real inequality in `RESULT.md`: every right-half-plane spectral candidate violates the Schur complement, for every positive time-scale parameter. The assertion requires \(0<K<1\), \(b_1>b_2\), positive equilibrium coordinates and positive demographic and infection rates. No global dynamical conclusion, independence certification, or exhaustive bibliographic novelty proof is inferred.
