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

The accepted statement was checked from the exact operator identities, without treating finite numerical spectra as proof.

For the Gaussian operator \(B_{\beta,d}\), the eigenvalues are \(c_\beta q^{|\nu|}\) with \(c_\beta=(1-q)^d\). Therefore
\[
\operatorname{tr}(B_{\beta,d}^r)=\left\{\frac{(1-q)^r}{1-q^r}\right\}^{d}.
\]
The finite-rank correction is positive, so with \(R_{\beta,d}=B_{\beta,d}-A_{\beta,d}\),
\[
\|R_{\beta,d}\|_1=1-\operatorname{tr}(A_{\beta,d})=O_d(\beta^{-d}),
\qquad
\|A_{\beta,d}\|\le\|B_{\beta,d}\|=O_d(\beta^{-d}).
\]
The telescoping expansion of \(B_{\beta,d}^r-A_{\beta,d}^r\) then gives
\[
\left|\operatorname{tr}(B_{\beta,d}^r)-\operatorname{tr}(A_{\beta,d}^r)\right|
=O_{d,r}(\beta^{-dr}).
\]
This proves the leading power-sum constant. At \(r=2\), it reproduces \(\operatorname{tr}(A_{\beta,d}^2)\sim2^{-d}\beta^{-d}\), which is an external consistency check against the motivating source.

The standardized cumulant constant was simplified algebraically. At \(r=4\),
\[
2^{(d+1)r/2-1}(r-1)!r^{-d}=12,
\]
so the excess kurtosis is \(12\beta^{-d}(1+o(1))\). For the Berry--Esseen step, the numerator is \(\mathbb E|N_1^2-1|^3\sum_j\lambda_j^3\) and the variance denominator is \(\{2\sum_j\lambda_j^2\}^{3/2}\), yielding order \(\beta^{-d/2}\).

Unproved limits: no claim of a sharp Berry--Esseen constant, no uniformity when \(d\) or \(r\) grows, and no theorem for a finite-sample statistic with a diverging smoothing parameter.
