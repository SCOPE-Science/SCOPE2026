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

The source definition requires \(0<A\le B<\infty\). In the explicit counterexample, \(A=B=4\) is admissible: the original energy is \(|h|^2\), the lower expression is \(4\|K^*h\|^2=|h|^2\), and the upper inequality is \(|h|^2\le4|h|^2\).

For \(\lambda_1=\lambda_2=1/2\), \(\varepsilon=3/2\), and \(K=I/2\), the perturbation inequality reduces to \(|h|\le5|h|/4\). The published smallness expression equals \(1/4\), hence is strictly positive. The perturbed analysis energy is exactly zero for every \(h\), so a positive lower \(K\)-frame bound is impossible because \(K\ne0\).

For the repair, denote the original and perturbed analysis norms by \(X(h)\) and \(Y(h)\). Direct integration of the pointwise hypothesis gives
\[
(1+\lambda_2)Y(h)\ge(1-\lambda_1)X(h)-\varepsilon\|v\|_2\|K^*h\|.
\]
Using \(X(h)\ge\sqrt A\|K^*h\|\) proves the lower coefficient in the finding. The analogous upper triangle inequality and \(X(h)\le\sqrt B\|h\|\) prove the stated upper bound.

The sharpness construction uses only a one-point measure space and scalar operators, so all measurability and domain requirements are automatic. No computational enumeration, timeout argument, or numerical approximation is used.
