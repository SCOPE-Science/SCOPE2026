---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For the autonomous source-theory recurrence, the optimum satisfies \(s_\star=\varepsilon/(1-\beta_2)\). The residual square has zero differential at the optimum and the denominator perturbation is multiplied by a zero numerator, so the Jacobian is block triangular with eigenvalue \(\beta_2\) and optimization block determinant \(\beta_1\), trace \(1+\beta_1-(1-\beta_1)\chi\). The second-order Jury conditions reduce exactly to \(0<\chi<2(1+\beta_1)/(1-\beta_1)\). At the upper boundary the roots are \(-1\) and \(-\beta_1\). The discriminant gives the stated complex-root interval, and constant product \(\beta_1\) forces modulus \(\sqrt{\beta_1}\). For the debiased algorithm, the optimum reference orbit has constant corrected second moment and an exponentially convergent first-moment factor, so the same strict asymptotic frontier follows away from equality.

## originality

PASS

The full AdaBelief primary text confirms the source epsilon convention, explicitly says bias correction is omitted in the theoretical analysis, discusses curvature qualitatively, and experimentally studies epsilon sensitivity. The later Aida paper explicitly analyzes how AdaBelief's epsilon placement suppresses its adaptive-step range. Neither inspected source gives a scalar quadratic Schur frontier, the \(-1\) crossing, or the exact momentum-root plateau. Targeted Resultary and literature searches for AdaBelief quadratic/local/Jury stability found no equivalent theorem.

## value

PASS

The defining paper emphasizes both curvature adaptation and epsilon sensitivity, so the exact scalar curvature ceiling is a motivated stability invariant. The theorem identifies a sharp unit-root boundary and a nontrivial constant-modulus momentum plateau, explaining a qualitative mechanism not captured by the global convergence bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
