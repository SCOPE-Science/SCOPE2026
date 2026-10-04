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

The focal full text was checked at the harmonic mesh, the amplitude recurrence, the Gaussian inner-product formula, and Example 7.4. These give
\[
\rho_n=\exp(-\delta^2H_{n-1}^{(2)}),\qquad
\rho_n\to e^{-\delta^2\pi^2/6},
\]
and
\[
\langle x_i,x_j\rangle=\rho_i\rho_j
\exp\!\left(-\delta^2(H_{i-1}-H_{j-1})^2\right).
\]

The amplitude replacement is controlled by
\[
\frac1{n^2}\sum_{i,j=1}^n|\rho_i\rho_j-\rho_\infty^2|
\le\frac2n\sum_{i=1}^n|\rho_i-\rho_\infty|\to0.
\]
For each fixed \(\varepsilon>0\), the harmonic-number asymptotic is uniform for \(i,j\ge\varepsilon n\), while the complementary boundary strips occupy normalized mass at most \(2\varepsilon\). This proves the full-kernel Riemann-sum limit without an unproved interchange of infinite limits.

The limiting integral was independently reduced by symmetry and substitutions:
\[
\int_0^1\!\int_0^1 e^{-\delta^2(\log(s/t))^2}\,ds\,dt
=\int_0^1e^{-\delta^2(\log r)^2}\,dr
=\frac{\sqrt\pi}{2\delta}e^{1/(4\delta^2)}
\operatorname{erfc}\!\left(\frac1{2\delta}\right).
\]
At \(\delta=1/8\), finite double sums numerically approach the predicted norm \(0.960538\ldots\); this is only a sanity check and is not part of the proof.

The literature comparison inspected the focal source in full, checked the earliest public version date, compared the broader Krengel–Lin nonlinear mean-ergodic counterexample, searched indexed published mathematical findings using source, alias, formula, and implication language, and compared the claim against the returned statements for overlap. A differently phrased unindexed derivation remains the principal originality risk.
