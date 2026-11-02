---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

A=diag(1/2,sqrt(3)/2) and orthogonal Q with entries ±1/sqrt2 give B=QA and Gram diag(1/4,3/4). For M=1,beta=2/3, H(P)=[[I-P,I],[-P/3,I]], and E[P] equals the same Gram for both row distributions, so the signed means have the same stable 2x2 spectral blocks (squared moduli 5/6 and 1/2). For diagonal A, the W=diag(1/10,1) weighted moment increases by >=101/100: independent exact symbolic multiplication gave the surplus D with positive leading entry and determinant 163/1800000; the state-to-adjacent-error bound gives the 1/41 growth lower bound. For mixed B, the displayed 4x4 C is positive definite with rational 2x2 block determinants and E[H^T C H]=C-I_4; tr(C)=532/5 implies decay <=(527/532)^k and initial energy <=34/5 ||x0||^2. Hence divergent second moments of A (for e1) and uniform contraction on B coexist with identical signed mean. Verified exact identities independently using SymPy, not sample path simulation.

## originality

PASS

Best-of-knowledge PASS. Alderman–Luikart–Marshall original KGSM arXiv:2401.09415 derives expected signed error along singular vectors, not an invariance law for second moments; identical Gram forces that same first moment but does not fix distribution of projectors. A previously published exact KGSM mean-square frontier treats uniform orthonormal A=I2 and cannot imply a same-Gram counterexample with unequal row probabilities and non-axis projectors. Broader stochastic momentum theory may contain related generic representation dependence, but no direct coverage was established.

## value

PASS

Orthogonal left multiplication preserves the deterministic least-squares Gram matrix, singular values, and mean error recurrence. The exact opposite stability under unchanged KGSM parameters proves singular-value-based first-moment tuning can fail decisively for mean-square convergence; a concrete positive definite certificate on each side makes the small counterexample reproducible and reusable for stochastic numerical method design. The example has a clear structural obstruction and is not merely a tiny-instance negative without motivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
