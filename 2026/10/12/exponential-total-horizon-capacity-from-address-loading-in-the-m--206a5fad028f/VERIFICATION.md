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

The proof uses Theorem V.1 of arXiv:2610.02068v1 in its stated regime. The key exact substitutions are \(R=2^{K-T}\), \(T=2\), and \(\min(2,1/p)=2\) for \(0\le p\le1/4\). The infinite profile comparison is analytic: after checking \(T=1,2,3\), the ratio \(f(T+1)/f(T)\) is strictly below one for every integer \(T\ge3\).

The bundled verifier numerically checks representative profile values and constants only. It is not a substitute for the analytic monotonicity proof. The result does not determine the exact split maximizing the true capacity because the source theorem retains unknown multiplicative comparison constants.
