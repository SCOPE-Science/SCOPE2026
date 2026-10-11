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

Let
\[
s=\frac1{\sqrt3}\sum_{i=1}^3\sqrt{w_i}\,\gamma_i,
\qquad
P=\sum_{i=1}^3w_i(1-\gamma_i^2)+s^2,
\]
where the \(\gamma_i=\cos\theta_i\) are independent phase variables. The exact source integrand is
\[
(1-t^2P)^{3/2}(1+ts)^{-3}.
\]

The checker expands this expression through degree eight and averages monomials using
\[
\mathbb E[\gamma_i^{2m}]=\frac{\binom{2m}{m}}{4^m},
\qquad
\mathbb E[\gamma_i^{2m+1}]=0.
\]
It then imposes
\[
w_1+w_2+w_3=1
\]
and verifies exactly
\[
[t^2]=0,
\]
\[
[t^4]=\frac{2\Sigma_2-1}{16},
\]
\[
[t^6]=\frac{105\Sigma_2-41-690\Pi}{1728},
\]
\[
[t^8]=\frac{-382+1440\Sigma_2-555\Sigma_2^2-11400\Pi}{27648}.
\]

At
\[
\Sigma_2=\frac12
\]
the checker verifies
\[
[t^6]=\frac{23-1380\Pi}{3456}.
\]
At the secondary value
\[
\Pi=\frac1{60}
\]
it verifies
\[
[t^8]=\frac{37}{110592}>0.
\]

The feasible threshold examples are checked exactly:
\[
\left(\frac12,\frac12,0\right)
\]
has \(\Pi=0\), and
\[
\left(\frac23,\frac16,\frac16\right)
\]
has \(\Pi=1/54\). The cubic
\[
z^3-z^2+\frac14z-\frac1{60}
\]
has discriminant \(1/1200>0\) and sign changes in three positive disjoint intervals, proving that the secondary threshold is attained.

All coefficient identities and sign conclusions are exact symbolic statements. Numerical roots are not used as proof.
