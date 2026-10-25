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

# Verification of the sharp finite linear-extension formula

The proof is self-contained in `RESULT.md`: symmetry-averaging reduces arbitrary extensions to one real parameter, all five target-pair orbit contributions are computed by exact coefficient-sum duality, and two affine lower bounds meet at an admissible strictly positive optimizer. The \(n=3\) case lacks disjoint midpoint pairs and has a separate sharp value. The remaining orbit inequalities at the proposed optimizers reduce to elementary inequalities, notably \(\sqrt6\ge1+\sqrt2\) in dimensions \(n\ge4\).

With NumPy and SciPy installed, execute `python verify_simplex_midpoint.py`. Its finite unsymmetrized LP optimizations agree with the formula for \(n=3,4,5,6\) (120, 720, 3360, 13440 inequalities, respectively). The script also checks the closed formulas for \(3\le n\le10\). Numerical optimization does not provide an all-dimensional proof; that role belongs exclusively to the analytical argument in `RESULT.md`. No independent audit was conducted.
