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

The proof is analytic. The source equation for the relevant root is specialized only after fixing \(\omega=\pi/2\) and \(x=\lambda_0^L+1/2\in(0,1/2)\), which removes the absolute values without a sign ambiguity. The positive quadratic root lies in \((1/2,1/\sqrt2)\), so it maps back to the required \(x\in(1/3,1/2)\) and \(\lambda_0^L\in(-1/6,0)\).

For the local regularity claim, the source gives both the exact singular generator \(u_0^L=\phi r^{\lambda_0^L}f_0^L\) and the decomposition of the distinguished domain into an \(H^1\) minimal-domain part plus its span. On a bounded neighborhood the \(H^1\) part lies in \(W^{1,p}\) for \(p\le2\). The singular part has gradient size comparable to \(r^{\lambda_0^L-1}\) on a nonzero angular set, so the radial convergence test is necessary and sufficient. At \(p=p_c\) the exponent is exactly \(-1\), giving logarithmic divergence.

`verify.py` checks the closed-form root against the angular equation at representative couplings and checks the endpoint exponent algebra numerically. Sampling is not used as proof.

Limit: no exact \(W^{1,p}\) transfer to a general curvilinear corner is asserted.
