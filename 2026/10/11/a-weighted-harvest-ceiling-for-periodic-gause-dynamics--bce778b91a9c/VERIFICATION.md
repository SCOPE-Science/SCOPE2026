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
The proof was replayed from the packaged source equations. Differentiating \(x+q(t)y\) with \(q=s/p\) gives the exact cancellation of the Holling-III terms and the sign-correct residual \(-qby^2-(qc-\dot q)y\). The period average is therefore exact.

For \(0<m<K\), differentiation of \(u(K-u)(u-m)\) gives \(-3u^2+2(K+m)u-Km\); its larger root is the unique critical point in \((m,K)\), so it is the global nonnegative maximizer because the cubic is negative outside \((m,K)\).

The mean-predator bound uses only \(\overline{y^2}\ge\overline y^2\), positivity, and coefficient minima. The included `verify.py` checks the algebraic cancellation, critical root, and quadratic inversion symbolically and prints `VERIFY_OK`.

Limits: this verification does not establish existence of a positive cycle, does not treat \(qc-\dot q<0\), and does not replace the literature comparison recorded in the review.
