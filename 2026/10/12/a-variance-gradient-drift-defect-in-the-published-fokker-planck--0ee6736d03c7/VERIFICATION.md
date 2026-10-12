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

Running `python verification/verify.py` in a directory containing the bundled files prints `VERIFY_OK`. The checker needs `sympy` and reconstructs the strong residuals of both printed equations using exactly rational \(1/50\) instead of decimal floating-point algebra. It verifies
\[
L_8f-L_6f=-\frac12\sum_j\partial_j\big((\partial_jD_j)f\big)
\]
for the source-specific controlled drift and \(D_j=\tfrac1{50}(1-\alpha)^2 S^2I^2\), including a general smooth polynomial test density.

It separately verifies the exact generator shift on each coordinate and checks the constant-diffusion witness \(f=1+S-2t\), \(F=(2,0)\), \(D_j=1\). For the positive test function \(\varphi=S(1-S)I(1-I)\) on the unit square (a convenient \(H_0^1\) polynomial replay), the published weak residual integrates to \(-1/36\); compactly supported interior smooth approximations retain nonzero residual, as explained in the proof. No finite experiment is used as a substitute for the general differential identities.

The review is same-model only and does not assess independent validation or hidden numerical implementation.
