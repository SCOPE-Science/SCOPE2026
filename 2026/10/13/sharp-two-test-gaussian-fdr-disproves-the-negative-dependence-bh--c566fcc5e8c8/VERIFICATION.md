---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The exact BH two-test rejection partition gives FDR=P(U<=alpha/2,V>alpha)+0.5 P(U<=alpha,V<=alpha)=alpha/2+0.5[P(alpha/2<U<=alpha,V<=alpha)-P(U<=alpha/2,V<=alpha)] <=3alpha/4 for U uniform. Set mu=-Phi^-1(alpha/2)-Phi^-1(alpha)>0, with Y1=-Z,Y2=Z+mu at rho=-1; V<=alpha iff U>=alpha/2, making the FDR exactly 3alpha/4. The corresponding rho>-1 positive-definite normal laws converge almost surely in threshold indicators, so the supremum holds for nonsingular rho<0. At alpha=1/20 and rho=-99999999/100000000, coupling with boundary normal yields P(alternative threshold changes)<epsilon+2*10^-8/epsilon^2=29/5000 for epsilon=1/200; hence FDR>=317/10000. The originating conjecture in Chi et al Section 7 is FDR<=tilde_s_2(alpha)/2; Eq.(26) bounded by e<3 and pi>2 gives <30307/1088000. Exact independent rational arithmetic verified strict gap; neither numerical integration nor singular covariance is used as the final counterexample.

## originality

PASS

PASS best-of-knowledge for negative resolution of the precisely named one-sided shifted-Gaussian BH conjecture. The classic universal 3alpha/4 upper bound is credited prior work and is not claimed new. The additional fact is near-attainability *inside* nonsingular negative Gaussian null/nonnull models and the explicit conjecture violation.

## value

PASS

A concrete rigorously verified counterexample to an explicitly stated statistical open problem is valuable, especially with exact worst-case sharpness and an entirely nonsingular Gaussian witness; it identifies how a shifted nonnull can align with a BH step boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
