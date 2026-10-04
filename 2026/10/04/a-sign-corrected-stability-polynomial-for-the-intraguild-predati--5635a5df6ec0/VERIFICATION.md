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

The universal coefficient identity is checked by direct determinant expansion: for any \(3\times3\) Jacobian \(J\), the coefficients of \(\det(\lambda I-J)\) are \(-\operatorname{tr}J\), the sum of principal \(2\times2\) minors, and \(-\det J\). With the source's definitions this is exactly \(-\sigma_2,-\sigma_1,-\sigma_0\).

`verifier.py` supplies an exact model-internal witness using `fractions.Fraction`. It verifies that \((R,C_1,C_2)=(1/2,1,1)\) is a positive equilibrium for the displayed positive parameters, reconstructs the exact Jacobian, reproduces the source \(\sigma\)-values, and checks the true characteristic polynomial \(\lambda^3+(23/36)\lambda^2+(139/216)\lambda+4/27\). It then verifies the exact Hurwitz margin \(2045/7776>0\), confirms that the source's stated supplement criterion rejects the witness, and confirms the corrected source-notation inequalities.

No finite experiment is used to prove the universal sign identity. No claim is made about nonlinear homoclinic existence, Lyapunov exponents, or ecological calibration.
