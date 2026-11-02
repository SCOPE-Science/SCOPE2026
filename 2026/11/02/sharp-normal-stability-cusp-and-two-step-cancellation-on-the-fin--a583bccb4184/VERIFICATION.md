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

The standalone script `check_incoherent.py` requires Python 3 with NumPy and SymPy. Execute `python check_incoherent.py`. It constructs the Jacobian directly from the finite phase map (including the diagonal mean-field derivative), compares its eigenvalues with the exact rank-two formula on 750 antipodal phase configurations for several network sizes, checks 120 Schur threshold configurations, and verifies the exceptional square-zero matrix symbolically with exact trigonometric values. Two nonlinear iterations at the exceptional configuration confirm the nonzero quadratic remainder outside the linearization.

Expected summary: `PASS exact nilpotent example; random spectral comparisons: 750 max eigen residual: 1.1111108480574222e-14 Schur cases: 120`.

The verified exact normal matrix is
\[
\begin{pmatrix}0&0\\-2\sqrt3&0\end{pmatrix},
\]
which is nonzero but has square zero. Finite tests do not certify universal assertions: the determinant, Jury criterion, and monotonicity arguments in `RESULT.md` establish those analytically. Boundary criticality is spectral only, with no nonlinear bifurcation classification. The motivating source's full text was not accessible for exhaustive historical comparison.
