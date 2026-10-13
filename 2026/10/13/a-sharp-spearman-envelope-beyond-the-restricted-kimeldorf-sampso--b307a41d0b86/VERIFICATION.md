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
The standalone `verify_ks.py` uses symbolic simplification to check
\[
\rho_S=\frac\alpha3+\frac{3\beta}4,
\quad
24t_*^2-18t_*+1=0,
\quad
2(1-3t_*^2)=\frac94(1-2t_*).
\]
It verifies the proposed exact parameter formulas, the sharp value
\[
\frac{\sqrt{57}-3}{12},
\]
and the edge identity
\[
c_{\alpha_*,\beta_*}(u,1)=6\beta_*(u-t_*)^2.
\]
It also verifies the positive lower-edge endpoint formulas and the uniqueness derivative condition.

A finite grid diagnostic checks the sign pattern; it is **not** used as proof of global nonnegativity. Global positivity is proved by concavity on sections when either coordinate is at most \(1/\sqrt3\), together with a direct sign bound when both are larger.

This verification does not establish a full analytic description of the two-dimensional admissible region or a general Pearson-correlation bound for arbitrary transformed margins.
