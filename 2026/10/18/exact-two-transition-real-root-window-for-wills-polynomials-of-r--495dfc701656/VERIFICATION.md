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

# Reproducing the mathematical checks

The proof concerns solid right circular cones with strictly positive radius and height. Read `RESULT.md` for the coefficient normalization and the complete global argument.

In this directory run `python verify.py` after installing the standard packages `sympy` and `mpmath`. The checker verifies exact differentiations of \(Q\) and \(H\), the positive-square formula for both transition derivatives, the cubic discriminant identity, and a rational inequality used in the proof. It then computes both transition parameters to 50 significant digits and checks discriminant signs at four sample aspects.

A successful checker reports `SYMBOLIC_IDENTITIES_OK`, `RATIONAL_BOUND_OK`, the two high-precision thresholds and `NUMERICAL_SIGNATURES_OK`. This checker supplements rather than replaces the proof: numerical signs alone cannot establish uniqueness, whereas positivity of \(F_\pm'\), the global \(m^3>9\pi t\) inequality and component analysis do.

Scientific limitations: dimension 3, Euclidean intrinsic volumes, untruncated right circular cones. The corresponding Steiner polynomial has different coefficients and different thresholds. An independent audit has not been conducted.
