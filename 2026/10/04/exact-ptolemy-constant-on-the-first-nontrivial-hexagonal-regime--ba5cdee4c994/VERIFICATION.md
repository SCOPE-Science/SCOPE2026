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

The exact-family source was checked at the displayed definition and extreme-point formula. The proof was then replayed independently from those definitions.

For \(H_\gamma(x,y)=\sqrt{x^2+(1-\gamma^2)y^2}\), all six vertices of the \(N_\gamma\)-unit ball have \(H_\gamma\)-norm one, hence \(H_\gamma\le N_\gamma\). Weighted Cauchy--Schwarz gives the sharp bound
\[
|x|+(1-\gamma)|y|\le\sqrt{\frac{2}{1+\gamma}}\,H_\gamma(x,y).
\]
The branch \(|y|\) has comparison factor \((1-\gamma^2)^{-1/2}\), which is strictly smaller than \(\sqrt{2/(1+\gamma)}\) exactly when \(0<\gamma<1/2\).

Applying Hilbert-space Ptolemy therefore yields
\[
C_{\mathrm{Pt}}(X_\gamma)\le\frac{2}{1+\gamma}.
\]
For
\[
x=(-1,0),\qquad y=(\gamma,1),\qquad z=(-(1+\gamma),1),
\]
direct substitution gives numerator \(4\) and denominator \(2+2\gamma\), so the ratio is exactly \(2/(1+\gamma)\).

No finite experiment, numerical search, or external certificate is used to justify the infinite quantified claim. Access-limited literature is not used as a correctness premise.
