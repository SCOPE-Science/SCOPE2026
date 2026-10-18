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
# Verification record
The identity \(f(x)^3=x^3g(x^2)^3\) and the coefficient rule \(M_{ij}=\gamma_{7i-j}\) give the four-by-four matrix in the proof. The two nonzero two-by-two blocks have determinant \(AB-D=P(s,t)\); because each contains an entry equal to \(1\), their possible ranks are exactly \(1\) and \(2\). This establishes the geometric \(a\)-number assertion without relying on numerical samples.

Run `python3 checks/cartier_rank_check.py` in the extracted package. The script symbolically checks the coefficients of \(g(z)^3\), the whole matrix and the determinant polynomial in \(\mathbf F_7[s,t]\). A separate convolution computes \(f(x)^3\) for all \(49\) parameter pairs and then checks the smoothness discriminant, the rank stratification, and the two square-zero exceptional matrices. Expected lines are `SYMBOLIC_IDENTITY_OK`, `F7_CENSUS_OK`, `P_RANK_ZERO_CHECK_OK`.

The condition \(\Delta(s,t)\ne0\) excludes repeated roots and is indispensable. The \(31\) finite-field objects are counted as parameter pairs; no claim of geometric or arithmetic inequivalence is made. Over \(\overline{\mathbf F}_7\), the rank-stratification claim is proved symbolically, whereas the zero stable rank is shown only for the two specified \(\mathbf F_7\) models. Independent external validation has not been performed.
