---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

The source's Lemma B.1 reduces positive endemic equilibria to positive roots of the scalar function \(F\). Direct differentiation shows strict monotonicity in both \(\beta_1\) and \(\beta_2\) for every positive \(I\). A fresh symbolic calculation verified the package derivative simplification and, after substituting the source thresholds, verified identically that the cleared corner value equals a negative positive-prefactor times \(I^2(C_0+C_1I)\). Under \(0<\sigma\le1\), both \(C_0\) and \(C_1\) are positive. Thus the corner is strictly negative for all \(I>0\), and monotonicity propagates this to the claimed rectangle.

## originality

PASS

The full primary paper explicitly labels the \(\beta_2\le\beta_2^\ast\), \(R_0<1\) equilibrium-exclusion observation as Numerical Finding 7.1, while its proved subcritical two-equilibrium theorem treats \(\beta_2>\beta_2^\ast\). The audited monotonicity-plus-corner factorization promotes exactly the unproved equilibrium sentence to a theorem and strengthens it to the boundary \(R_0=1\). Resultary found no later covering result.

## value

PASS

The theorem closes an explicit gap between the source's proved backward-bifurcation regime and its numerical complementary regime. It sharply separates the existence of endemic equilibria from the stronger, still-unproved global-convergence claim and settles the threshold boundary as well.

The dated certificate retains the supplied scientific assessment, sources and limitations.
