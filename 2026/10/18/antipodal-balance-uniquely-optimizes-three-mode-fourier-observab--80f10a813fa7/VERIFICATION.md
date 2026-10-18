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

# Verification of analytic and finite claims

The exact proof is in `RESULT.md`. The frequency basis is orthonormal in the ambient probability Haar measure. The observation norm is **not** renormalized to make the arcs total measure one.

The Gram has entries \(t,c u,v\), and diagonalization into its antisymmetric one-dimensional sector and symmetric two-dimensional sector yields eigenvalues \(t-v\) and \(t+(v\pm H)/2\). The branch-selection inequality and the identity
\[
H^2-(v+2d)^2=8u^2(c^2-d^2)
\]
establish the sharp least-squared-singular-value bound for every admissible width and center separation. At \(u=0\) the sharp three-element spectrum and inverse norm follow immediately. Second-order Taylor expansion of the displayed **exact** deficit gives the local coefficient.

The included `checker.py` independently verifies finite numerical evaluations of the eigenvalue trace, determinant, rationalized deficit, nonnegativity, equality example, and local curvature for six arc widths and 101 relative positions per width. These are **finite** consistency checks; they cannot independently prove the all-parameter theorem or originality. No separate external scientific validation has been conducted.
