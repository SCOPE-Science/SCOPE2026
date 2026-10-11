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
# Verification of the contained ellipsoid formula

Run `python verify.py` with Python 3 and SymPy installed. The bundled source reproduces two distinct levels of checks:

1. Symbolically, the row-face quadratic form equals its claimed support square, the entry-face quadratic form differs by the explicit degree-two polynomial factor, and the positive proposed multipliers satisfy all three shape stationarity equations. The positive quadratic root is also verified exactly for \(2\le n\le30\).
2. Numerically, the source applies the shape operator directly to matrix units and row/column indicator normals, obtains the exact Frobenius supporting widths, and constructs contact points for all \(n^2+2n\) facets for \(2\le n\le9\). Each contact is tested against every displayed defining inequality with a bound to accommodate floating-point rounding.

The concrete run returned `ALL CHECKS PASSED` (\(372\) facet/contact cases in the second verification). It is not a formal all-dimensional software proof. The mathematical basis for arbitrary \(n\ge2\) is the complete symbolic containment/KKT derivation and convex global-optimality proof in `RESULT.md`. No higher-level or independent audit is reported.
