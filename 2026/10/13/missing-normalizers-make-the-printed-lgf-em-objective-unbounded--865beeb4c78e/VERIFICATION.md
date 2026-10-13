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
For a frozen E-step, define
\[
A=\sum_iE(N_i\mid y),\quad
B=\sum_iE(\log Z_i\mid y),\quad
C=\sum_iE(Z_i\mid y),\quad
D=\sum_i y_iE(N_iZ_i\mid y).
\]
The corrected auxiliary function is
\[
Q=A\log\eta-m\log[-\log(1-\eta)]+m\log\theta
+m\{\lambda\log\lambda-\log\Gamma(\lambda)\}
+\lambda(B-C)-\theta D+K.
\]

The packaged checker computes the E-step moments for a positive five-observation sample and verifies the analytic \(\eta\)- and \(\lambda\)-scores by centered finite differences.

It then compares the corrected frailty-shape objective with the literal Eq. (4.5) objective. The corrected objective has a finite numerical maximizer, while the printed objective selects the upper endpoint of successively enlarged search boxes, consistent with its analytic divergence to \(+\infty\).

These finite calculations are reproducibility aids. The unboundedness and coercivity statements are proved analytically.
