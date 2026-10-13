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
# Verification record

The analytic theorem was checked by deriving the CDF derivative and the exact logarithmic-curvature identity directly from the displayed density. The all-real-parameter sufficiency requires the monotonicity argument for the inverse-hyperbolic auxiliary function given in the proof; numerical samples cannot replace that argument.

Reproduce the symbolic and exact-rational diagnostics with `python verify_concrete.py` (requires Python 3 and SymPy). The checks include the polynomial identity for the second derivative, six CDF derivative specializations, the 100-to-1 midpoint counterexample, the correspondence with the unit-logistic median parameterization and 76 exact finite curvature signs. Expected output begins with `PASS`. All code and derivations concern the scalar binary Concrete density; higher-dimensional and general optimization assertions were not checked.

This scientific self-review is not an independent audit. A historical original article on the equivalent distribution could not be compared in full and remains a bibliographic priority risk.
