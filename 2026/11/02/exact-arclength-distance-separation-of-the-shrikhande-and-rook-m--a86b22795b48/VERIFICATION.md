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

# Reproducibility

Execute `python3 verify.py` with standard Python 3; no third-party dependency is required. The code constructs the labeled \(4\times4\) rook graph and the specified \(\mathbb Z_4^2\) Shrikhande graph, verifies degree and pair-common-neighbor data, and exhaustively classifies each of the \(1128\) unordered distinct-edge pairs. Rational polygon clipping computes the exact area where all four endpoint routes exceed a specified radius. Eighteen rational control points on six half-unit radius intervals determine the quadratic spline, since the active clipping configuration can only change at half-integers. The code checks the exact upper-tail geometry and the \(1/96\) diagnostic difference. Finite exact enumeration proves the two explicit graph claims when combined with the half-integer-breakpoint proof. The all-graphs statement uses the independent analytic disjoint-edge route bound in RESULT.md.

Known limits: this test is not an external independent audit; it neither checks every possible graph nor establishes historical publication priority. It does not address arbitrary edge lengths or vertex diameter above two.
