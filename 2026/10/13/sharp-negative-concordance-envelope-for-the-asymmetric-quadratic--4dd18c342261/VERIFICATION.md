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
The theorem applies to genuine continuous copulas. Its proof uses the necessary boundary limit \(\phi(v)\to1\) as \(v\uparrow1\); assigning \(\phi(1)=1\) alone does not force this condition under interior differentiability.

The exact proof requires no finite search to establish the infinite-class bound. The accompanying script independently reproduces the algebra behind
\[
\rho_S=-2\int_0^1v[1-\phi(v)]\,dv,
\qquad \tau_K=\frac23\rho_S.
\]
It verifies the analytic envelope integral
\[
\int_0^{e^{-1}}v\,dv+\int_{e^{-1}}^1(-v\log v)\,dv
=\frac{1-e^{-2}}4,
\]
checks the closed form of \(v\phi_\varepsilon'(v)\) for the proposed soft-maximum CDF, and evaluates the Spearman integral at high precision for decreasing positive \(\varepsilon\).

The limiting envelope is not differentiable at \(v=e^{-1}\), so it is not a valid attained member. The smooth approximants all satisfy the source's derivative condition and approach that envelope; this nonattainment/sharpness statement is proved analytically in the result, not inferred from numerical convergence.
