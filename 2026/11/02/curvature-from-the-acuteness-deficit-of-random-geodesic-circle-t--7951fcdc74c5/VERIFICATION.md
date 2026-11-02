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
# Verification of the curvature–acuteness asymptotic

The analytic proof gives the universal quantifiers and the exact \(O_p(r^3)\) limitation. The reproducible `CHECK.py` file requires Python 3 with SymPy and mpmath; run `python CHECK.py` in the directory containing this document. It verifies the half-angle identity, the right-angle threshold's exact first variation, cyclic Dirichlet-gap density normalization, and high-precision integrals on positive- and negative-curvature space forms. The program prints `ALL_CHECKS_PASSED` on success.

Numerical integration is a finite diagnostic, not proof on nonhomogeneous surfaces. The extension to any smooth surface uses the quadratic normal-coordinate metric jet, polar arclength Jacobi expansion, smooth dependence of minimizing geodesics, and the transverse right-angle boundary in the two-dimensional gap simplex. No finite-radius probability formula, confidence interval, or independent mathematical audit is claimed.
