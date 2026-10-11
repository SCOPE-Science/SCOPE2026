---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For the source's logistic maturation weights, \(Y_A\le y_1/2+y_2\) and \(Y_J\ge y_1/2\). Integrating the age equation with the renewal boundary condition and differentiating \(V=x+cy\) gives the exact upper bound with cross coefficients \(s+c(k-g)/2\) and \(-b+ck\). A positive constant \(c\) makes both nonpositive exactly when \(c(g-k)\ge2s\) and \(ck\le b\), equivalently \(g>k\) and \(2sk\le b(g-k)\) under the source's positive-parameter regime (with no upper bound when \(k=0\)). Then \(V'\le\max\{r,\|\widetilde B\|_\infty\}V\), so Gronwall bounds \(x+\|u\|_1\) on each finite horizon. The source's local Lipschitz construction on bounded balls and finite-horizon compact age support then give continuation. Concentrating age mass near the juvenile cutoff or far in the adult tail verifies sharpness only within the constant-weight \(x+c\int u\) family.

## originality

PASS

The motivating paper was freshly inspected in full open-access text at the exact model equations, Theorem 1 local existence, its numerical blow-up convention, and its later saturated modification. It proves only local existence for the original unsaturated system and discusses boundedness after changing the birth term; it does not state the audited source-specific weighted-mass criterion. The finite-dimensional Li--Liu--Wei predecessor has different stage equations and does not imply the smooth age-renewal estimate. Fresh Resultary search found only other age-structured models, not an implication-equivalent criterion.

## value

PASS

The source itself treats apparent blow-up as a modeling concern and introduces saturation to tame it. The audited theorem identifies a nontrivial exact region where the original unsaturated equations already cannot undergo mathematical finite-time norm blow-up, and it separates that statement from the paper's operational simulation threshold. The exact feasibility boundary for constant weighted mass is a useful structural criterion, not merely a routine estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
