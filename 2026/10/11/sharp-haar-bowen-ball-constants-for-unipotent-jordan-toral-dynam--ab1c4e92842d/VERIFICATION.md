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

# Verification of the sharp Bowen-ball volume law

The proof uses exact integer iterates of the full unipotent Jordan block and a triangular polynomial change of variables. Its decisive non-computational points are a modulo-one no-wrapping induction for radii strictly below one quarter, uniform Markov interpolation for the degree-\(d-1\) coefficient body, and the exact integral of the allowable quadratic curvature interval. They yield an analytical limit with relative error \(O_d(1/n)\) for every fixed dimension and permitted radius.

Run `python3 verify.py` from the directory containing this file. The standard-library checker performs 5,950 exact-rational orbit-identity comparisons in dimensions two through six, checks the exact fractions \(272/9\) and \(544/9\), and numerically integrates the independently derived quadratic curvature interval on three successive midpoint grids. The expected terminal marker is `CHECKS_OK`. These diagnostics confirm implementation-level algebra and a finite quadrature sanity check, not the infinite convergence proof.

This package does not contain a computer-assisted infinite certificate; no independent audit has been performed. The polynomial-entropy exponent for the underlying map was known previously, and the asserted new component is the exact Haar-volume coefficient.
