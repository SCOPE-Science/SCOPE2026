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

The central proof is exact and finite. It uses no numerical integration or asymptotic inference.

For a putative nonnegative equilibrium with \(I_c=I_{ck}=0\):

1. The \(S\)-equation excludes \(S=0\) because \(\Lambda>0\).
2. With \(S>0\), \(\beta_c>0\), \(N>0\), and \(0\le\varepsilon_v\le1\), the \(I_c\)-equation forces \(H=0\).
3. With \(H=I_c=I_{ck}=0\), the \(H\)-equation and \(\zeta_k>0\) force \(I_k=0\).
4. With \(I_k=H=I_c=I_{ck}=0\), the \(I_k\)-equation becomes \(0=\lambda_kS\), contradicting \(\lambda_k>0\) and \(S>0\).

The bundled `verifier.py` evaluates the source's baseline displayed candidate with exact rational arithmetic. It checks
\[
S^0=\frac{356000}{360017}
\]
and
\[
\left.\dot I_k\right|_{E_0}=\frac{20826}{9000425}>0.
\]
It also checks positivity of the baseline transmission and CKD-hospitalization coefficients used by the theorem.

The verification does not certify a repaired model, a replacement reproduction number, or any claim on parameter axes where \(\lambda_k\), \(\zeta_k\), or \(\beta_c\) vanishes.
