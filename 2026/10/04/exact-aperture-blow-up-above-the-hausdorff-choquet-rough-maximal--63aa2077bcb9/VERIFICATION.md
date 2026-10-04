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

For the normalized cap kernel
\[
u_{\theta,r}=\frac{\mathbf 1_{B(\theta,r)}}{\sigma(B(\theta,r))},
\]
the primary source proves
\[
\|\mathcal M_{u_{\theta,r}}f\|_{L^{1,\infty}}
\le C_n\|f\|_1
\]
with \(C_n\) independent of \(\theta\) and \(r\).

The same source proves
\[
\|u_{\theta,r}\|_{\mathcal{HC}_\alpha}
\asymp_{n,\alpha}
r^{2\alpha-(n-1)}.
\]

For the lower weak norm, take
\[
f=\mathbf 1_{B_{\mathbb R^n}(0,2)}.
\]
On \(B_{\mathbb R^n}(0,1)\), the radial scale \(R=1\) yields
\[
\mathcal M_{u_{\theta,r}}f\ge c_n
\]
uniformly in the cap. Hence
\[
\|\mathcal M_{u_{\theta,r}}f\|_{L^{1,\infty}}
\ge c'_n\|f\|_1.
\]
Therefore the unnormalized cap operator norm is comparable to one, and division by the cap quasi-norm gives
\[
\mathfrak C_{n,\alpha}(r)
\asymp_{n,\alpha}
r^{n-1-2\alpha}.
\]

For \(\alpha>(n-1)/2\), this is exactly
\[
r^{-(2\alpha-(n-1))}.
\]
No computation or asymptotic fitting is used; the conclusion is an algebraic quotient of two verified two-sided estimates.
