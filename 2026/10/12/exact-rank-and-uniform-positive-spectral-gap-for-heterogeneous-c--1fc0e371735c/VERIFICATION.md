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

Run `python verify.py` using Python 3, NumPy, and SymPy. The script independently constructs the entire adjacency matrix and obtains the average mixing matrix by grouping numerically equal adjacency eigenvalues, squaring their spectral projectors entrywise, and summing. It also constructs the claimed local \(-1\)-projector without using the eigenvectors of the numerical diagonalization.

For six explicit heterogeneous parameter choices, SymPy confirms exactly over the rationals that the claimed projector is idempotent, solves \(AE_{-1}=-E_{-1}\), has rank equal to the multiplicity of \(-1\), and has the stated Schur-square cell eigenvectors and eigenvalues. For 77 independently constructed graph examples, NumPy checks the nullity formula, all predicted difference null directions, the positive-eigenvalue lower bound when the core size is at least two, and the exact \(1/3\) cell-difference eigenmodes when a cell has three vertices.

Observed replay:

`VERIFY_OK exact_projectors=6 independent_graphs=77 max_null_residual=6.106e-16 max_projector_residual=2.220e-16 max_three_clique_mode_residual=1.388e-15`

Floating-point tolerances are numerical comparisons, not exact certificates for infinitely many graphs. The unrestricted claim is established by the six-step analytical proof in RESULT.md. The calculations do not test publication novelty or supply any external validation.
