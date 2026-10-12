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

# Reproducibility and verification

Run `python verify.py` using Python 3 with NumPy and SymPy. The script is standalone, reconstructing its own graphs and analytic formulas. An actual successful run produced:

`VERIFY_OK exact_cases=4 exact_projector_samples=24 independent_numeric_cases=144 max_matrix_error=4e-15 max_kernel_residual=3.11e-15 double_star_2_2_rank=3/6 full_rank_3_4=9/9`

The four exact examples are \((p,q)=(1,1),(1,2),(2,2),(2,3)\). In each, the script computes spectral projectors as polynomials in the adjacency matrix and compares 24 selected entries against the independent squared-eigenvector formula with symbolic radical simplification. Each kernel vector is checked symbolically. The 144 numerical examples cover every ordered pair \(1\le p,q\le12\) by independent real-symmetric diagonalization and compare complete mixing matrices, predicted ranks and explicit kernel vectors. The maximum matrix difference and kernel residual were recorded above in double precision.

The program is finite verification rather than a certification of the infinite theorem. The unrestricted result follows from the characteristic polynomial \(s^2-(p+q+1)s+pq\), the explicit spectral-projector decomposition, and an exhaustive rank argument given in `RESULT.md`. No finite test establishes originality or mathematical significance.
