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

# Verification of the cone-sidewall chord-moment theorem

The analytic proof appears in `RESULT.md`. `verify_cone.py` is a standard-library standalone checker whose exact rational expansion independently reproduces the second, fourth and sixth chord moment polynomials. It checks derivative identities and negative discriminants, sample exact ambiguity pairs, endpoint constants, and a direct three-variable midpoint quadrature with 15 moment/shape comparisons.

Actual execution: `VERIFY_OK exact_polynomial_and_rational_checks= 38 independent_quadratures=15 max_absolute_quadrature_error= 7.29849565e-05`. Reproduction command: `python3 verify_cone.py`. The quadrature tolerances are finite and do not certify any universal result; the proof's symbolic polynomial and mean-value arguments give universal validity.

No independent mathematical audit or external validation has been performed. Historical priority remains provisional because a potentially relevant general-moment paper could not be inspected in full.
