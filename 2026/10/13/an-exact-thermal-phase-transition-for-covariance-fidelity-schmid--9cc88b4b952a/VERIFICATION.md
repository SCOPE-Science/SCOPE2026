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

The analytic proof uses the exact TMST formulas of arXiv:2610.03113v1. The critical steps are:

1. eliminate \(s_{\mathrm{opt}}\) by \(e^{\operatorname{arsinh}x}=x+\sqrt{1+x^2}\);
2. rationalize \(\widetilde R_{\mathrm{opt}}^2\) and use \(\sqrt{1+u^2\sinh^2(2r)}<u\cosh(2r)\);
3. take \(r\to\infty\) to obtain \((u^2-1)/2\) and solve the equality to obtain \(\beta_c=\log(2+\sqrt3)\);
4. sum the geometric Schmidt spectrum to obtain \(B_k=1-\tanh^{2k}(s_{\mathrm{opt}})\);
5. use \(s_{\mathrm{opt}}=r+\tfrac12\log u+o(1)\) and \(h(z)=1-\log(4z)+o(1)\) for the two exponential laws.

`artifacts/verify.py` evaluates both forms of \(\widetilde R_{\mathrm{opt}}^2\), checks the critical constant, confirms subcritical zero fidelity at representative points, and checks convergence of both asymptotic ratios. These finite calculations only guard against algebraic and implementation mistakes; they do not replace the displayed proof.
