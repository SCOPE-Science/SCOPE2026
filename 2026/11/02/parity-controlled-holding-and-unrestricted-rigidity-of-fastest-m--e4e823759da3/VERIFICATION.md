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

# Reproducibility and limits

Run `python verify_torus.py` with Python 3, NumPy and SciPy installed. The script was run from the final candidate package contents and printed `PASS: 3138 numerical and analytic consistency assertions across 28 torus shapes.`

The finite verifier compares closed formulas against tensor Fourier eigenvalues, solves symmetrized linear programs independently using a linear optimization routine, checks full matrix spectra and saturated coordinate Fourier eigenvectors, and tests feasible nonsymmetric perturbations. It explicitly exercises the holding boundary of three triangular cycles, zero-holding with four odd factors, and positive holding when one of three odd factors is length five.

A finite numerical run does not prove global uniqueness or the statement for unbounded cycle lengths. Those assertions follow from the variational inequalities and Fourier equality-case argument in RESULT.md. Unrestricted independent mathematical validation has not occurred. No separate external audit was conducted.
