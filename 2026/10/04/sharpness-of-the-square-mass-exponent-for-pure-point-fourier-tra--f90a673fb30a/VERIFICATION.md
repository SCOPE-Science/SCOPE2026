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

`verify_q_threshold.py` performs exact finite checks of the Rudin--Shapiro recurrence through order ten. For each checked order it verifies that all coefficients are signs, that the nonzero autocorrelations of the complementary pair cancel exactly, and that the constant square-sum coefficient is \(2N\). This is the coefficient form of
\[
|P_r(z)|^2+|Q_r(z)|^2=2^{r+1}
\]
on the unit circle.

The script also verifies the exact logarithmic block-mass formula
\[
\log_2 \nu_q(B(L_m,1))=m^2(1-q/2)-q(m+5)
\]
for representative rational exponents below \(2\), the square-mass identity \(\nu_2(B(L_m,1))=2^{-2m-10}\), and the positive lower bound
\[
1-\frac{\sqrt2}{16}>0.91
\]
for the constructed density. The replay output is stored in `verification_output.txt` and ends with `VERIFY_OK`.

These checks are supplementary. They do not replace the analytic proof of the infinite construction, distributional Fourier-transform identity, or the all-\(q\) threshold.
