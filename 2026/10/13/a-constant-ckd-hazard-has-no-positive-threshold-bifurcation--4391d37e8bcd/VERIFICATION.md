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

The verification target is the CKD-only affine subsystem printed in DOI 10.3934/math.2026707. The packaged `verify.py` performs exact symbolic checks of the following points:

- the identity \(D=\zeta_k(\mu_h+\mu)+(\mu_k+\mu)(\gamma_h+\mu_h+\mu)>0\);
- exact substitution of \(S^*\), \(I_k^*\), and \(H^*\) into all three equilibrium equations;
- factorization of the homogeneous characteristic polynomial as \((r+\lambda_k+\mu)[r^2+(\phi_k+\psi)r+D]\);
- evaluation at the source's \(C_k=1\) hazard, where the actual \(I_k^*\) remains positive and the characteristic polynomial has no zero root;
- exact positive derivatives of \(I_k^*\) and, when \(\zeta_k>0\), \(H^*\) with respect to \(\lambda_k\).

The checker returns `VERIFY_OK`. No numerical trajectory experiment is used to establish the theorem. The conclusion is limited to the printed three-dimensional affine subsystem.
