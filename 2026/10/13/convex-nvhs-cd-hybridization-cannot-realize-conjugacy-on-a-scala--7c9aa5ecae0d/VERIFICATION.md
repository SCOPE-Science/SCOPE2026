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

The proof is symbolic. Starting from the published formulas on \(f(x)=\frac{a}{2}x^2\), it derives \(\tau=a\alpha_0\), \(r=1-\tau\), the exact strong-Wolfe restriction \(|r|\le\sigma\), the conjugacy target \(\beta_{\rm conj}=-r\), and the two endpoint coefficients. The strict convex-hull comparison is then elementary in the two sign cases.

`artifacts/verify.py` is a finite exact-rational consistency replay. It checks representative rational values on both sides of the exact line-search point, confirms the strong-Wolfe inequalities, reconstructs the source coefficients, confirms that the conjugacy target lies outside their convex hull, and verifies \(\theta_{\rm raw}=-1/|r|\). Its saved output is `VERIFY_OK`.

The finite replay is not used to prove the universal quantifier over all admissible nonexact steps. That conclusion is supplied by the analytic inequalities in `RESULT.md`.
