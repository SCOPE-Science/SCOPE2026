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
The defining Cayley--Dickson multiplication and the standard elements \(p_0=E_{11}\), \(n_0=E_{12}\) were checked against arXiv:2610.04466v1. The proof was then reconstructed directly from that multiplication law.

For arbitrary \(x,y\), the quaternion part of \(p_0(xy)-n_0(yx)\) has zero second row, and the whole value lies in \((Fp_0+Fn_0)\oplus M_2(F)\omega\). For \(x_0=E_{11}+E_{21}\), the fixed-slice matrix has rank \(6\); the minor on rows and columns corresponding to \(E_{11},E_{12},E_{11}\omega,E_{12}\omega,E_{21}\omega,E_{22}\omega\) has determinant \(1\). This proves surjectivity of that slice over every field and supplies the reverse inclusion.

Running `python verify.py` from the package directory reconstructs these formulas symbolically and terminates with `VERIFY_OK`. The script is supplementary; the proof itself is the displayed algebraic calculation and determinant-one argument.
