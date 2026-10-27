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

# Reproduction and scope

Run `python verify_phase_leakage.py` with NumPy and mpmath installed. The recorded run produced `PASS: 418 finite and special-function assertions`.

The checker constructs independent finite Fock sections for several dimensions, squeezing parameters and phase slopes; differentiates the full finite GKSL master equation through third order; compares with the predicted \(\gamma(\phi'(0)+4\omega)^2\)-weighted norm; and evaluates hypergeometric derivatives against explicit positive Fock sums. It also checks exact rotating-frame phase tracking and the zero-balanced strong-squeezing asymptotic at high precision.

These checks verify finite-dimensional algebra and sample the special-function identities; they do **not** certify an infinite-dimensional error bound, a universal norm-convergent quantum dynamical semigroup, or independently confirm originality. The analytic argument in `RESULT.md` is required for the general statement. The claim only concerns the sequential strong-squeezing coefficient, not a joint asymptotic for finite \(t\).
