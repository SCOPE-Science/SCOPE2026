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

Run `python3 verify.py` from the directory containing this document; Python 3.10+ and its standard library suffice. The program uses exact `Fraction` arithmetic to derive the first \(d\) moments of a Dirichlet quadratic form and reconstructs \(\prod_i(1-b_i z)\) independently for four test spectra in dimensions \(2,3,4,5\). It verifies the first-moment ambiguity for two different planar spectra. It also calculates four true three-dimensional ellipsoid sections from the restriction of the defining quadratic form to an orthonormal section-plane basis and compares them against the proposed codimension-one Jacobian formula, with a relative tolerance of \(2\times10^{-14}\).

Observed program output: `VERIFY_OK: exact moments in dimensions 2-5, sharp 2D ambiguity, four independent 3D section-area checks`.

The proof, not the finite tests, establishes arbitrary dimension, all semiaxis multiplicities, and the local sharpness statements. The inputs are exact population moments; no finite-sample statistical estimator or root-conditioning bound is verified here.
