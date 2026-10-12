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
# Verification

The analytic proof uses the source's exact equilibrium and characteristic-polynomial formulas.

With
\[
B=b\gamma_E,\qquad
c=\alpha_3+\alpha_4+\gamma_L,\qquad
t=\frac{\mathcal R_0-1}{\mathcal R_0},
\]
direct substitution of the explicit \(A^*\) gives
\[
\eta_1=e_1,\qquad
\eta_2=e_2+B,\qquad
\eta_3=e_3+Bc,\qquad
\eta_4=t e_4.
\]
Expanding \(\Delta_3\) yields the positive decomposition given in `RESULT.md`.

The bundled `verification/verify.py` reconstructs these coefficients for deterministic positive parameter vectors, checks the exact reduction numerically, compares the direct and expanded determinant formulas, and verifies every sign inequality used in the proof. It prints `VERIFY_OK` on success.

Unproved limits: no global convergence theorem is added, and no statement is made for altered recruitment laws, delays, or discrete-time stage models.
