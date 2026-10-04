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

The claim is proved analytically in `RESULT.md`; no numerical experiment or finite search is used as a substitute for proof.

The critical local step is the likelihood-ratio comparison. With an equal-scale history and the normalized rate ratio \(x=\lambda/\lambda_k\), differentiation gives
\[
T_x'(u)=\frac{1-x+xu-u^x}{u^x(1-u)^2}.
\]
For \(x>1\), convexity of \(u^x\) on \((0,1)\) makes the numerator strictly negative; for \(0<x<1\), concavity makes it strictly positive. After the decreasing change of variable \(u=e^{-t}\), this reverses the stochastic ordering of the running maximum conditional on the current observation being a record. Applying the strictly decreasing test function \(e^{-zt}\) gives the exact covariance sign. At \(x=1\), the likelihood ratio is constant and the covariance is zero.

An independent algebraic check is supplied by the exact Laplace transform
\[
L_q(s)=\prod_{j=1}^{q}\frac{j}{s+j},
\]
which yields the three displayed event-probability formulas in `RESULT.md`. Substitution at \(x=1\) gives zero covariance exactly. The formulas also have the correct limits as \(z\downarrow0\) and \(z\to\infty\).

The global classification then requires no additional computation: equal scales through the penultimate observation imply independence by rank/order-statistic separation, while mutual independence plus the local zero-covariance condition forces the scales to agree successively.

Limits not proved here: no sign classification is asserted for a fully heterogeneous history, and no extension to nonexponential or dependent observations is inferred.
