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

The verification is analytic and exact. Starting from the printed profile equation, the upstream characteristic polynomial is
\[
Q(\lambda)=\tau c\lambda^3-D\lambda^2-c\lambda+1.
\]
Its discriminant and the downstream discriminant defining the minimal speed differ, after \(r=\tau/D\) and \(y=c^2/D\), by the positive quantity \(D^3(36ry+8)\). Hence every source-admissible speed has three distinct real upstream roots.

Vieta's formulas give one negative and two positive roots. The positive root of the downstream discriminant satisfies \(y_*>1/r\), so \(c>D/\sqrt\tau\). Evaluating \(Q\) and \(Q'\) at \(1/\sqrt\tau\), together with the fact that \(Q'\) has one positive critical point, proves that both positive roots lie strictly below \(1/\sqrt\tau\).

For either positive root \(\lambda\), the source's Bessel transform is finite and equals \((1-\tau\lambda^2)^{-1}\). Substitution of \(e^{\lambda\xi}\) into the source's limiting convolution equation reduces exactly to \(Q(\lambda)=0\). Thus the displayed exponentials satisfy the source's normalization, positivity, monotonicity, convexity, and decay requirements.

No finite numerical experiment is used as proof. The conclusion is limited to the exact linearized obstruction and the logical consequence for the published proof step.
