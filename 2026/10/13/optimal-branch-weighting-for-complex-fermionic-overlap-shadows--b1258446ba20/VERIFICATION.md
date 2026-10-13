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

The analytic checks use the exact source identities for the complex-overlap estimator. For \(0<\lambda<1\), the weighted coherent reference changes the desired coherence from \(o_\phi/2\) to \(\sqrt{\lambda(1-\lambda)}o_\phi\), so the estimator coefficient becomes \(d_1/\sqrt{\lambda(1-\lambda)}\). Squaring that coefficient rescales the source's diagonal second-moment operator by \(1/[4\lambda(1-\lambda)]\).

Using the source eigenvalue \(4b_{N,\eta}/(j+1)\) on physical sector \(j\) and \(4b_{N,\eta}\) on the ancillary reference gives
\[
\mathbb E|\widehat o_{\phi,\lambda}|^2
=b_{N,\eta}\left(\lambda^{-1}+S_\phi(1-\lambda)^{-1}\right).
\]
Subtracting \(p_0(\phi)=|o_\phi|^2\) gives the claimed complex variance.

For a target ensemble, differentiation of \(\lambda^{-1}+\bar S(1-\lambda)^{-1}\) gives the unique stationary point \(\lambda_*=1/(1+\sqrt{\bar S})\); strict convexity and endpoint divergence make it the global minimum. Direct substitution gives the gain \(b_{N,\eta}(1-\sqrt{\bar S})^2\).

The minimax claim is checked analytically by the allowed trial-equals-target Slater case, which forces variance \(b_{N,\eta}/[\lambda(1-\lambda)]-1\). This is minimized uniquely at \(\lambda=1/2\), where it equals the source's sharp universal upper bound \(4b_{N,\eta}-1\).

The standalone checker uses exact rational values of \(b_{N,\eta}\) and representative sector distributions to replay these identities. Its finite tests are corroborative and do not establish the all-parameter theorem.
