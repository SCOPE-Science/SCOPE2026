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

Writing \(s_i=\sqrt{V_i+\eta^{-2}}\) converts each boundary exactly to \(s_i\sqrt{\log(\eta^2/(a_i/s_i)^2)}\). For \(0<\alpha<e^{-1/2}\), every feasible \(a_i/s_i\) lies in the strict-convexity region of this scalar function, so weighted Jensen gives the unique common-ratio allocation \(a_i=\alpha s_i/S\) and the displayed minimum. The fixed-allocation coverage extension uses only a union bound. Expanding the equal-split logarithms around \(L_t=\log(\eta^2S(t)^2/\alpha^2)\) gives the stated KL coefficient. An independent numerical reconstruction reproduced the closed-form objective on a three-clock example.

## originality

PASS

Best-of-knowledge comparison found the motivating paper to combine two arm-level confidence sequences by a union bound but did not find the boundary-specific optimal error split, exact minimized summed width, or KL/entropy equal-split penalty. Generic weighted Bonferroni procedures establish admissible fixed weights, not this optimizer. The full PMLR PDF could not be text-inspected in this runtime because the public PDF endpoint was exposed as unsupported binary content; that access limitation is retained as a residual risk rather than treated as negative evidence.

## value

PASS

The source setting has a concrete design choice—how to prespecify a familywise error budget across arm-level anytime-valid intervals when target variance clocks are imbalanced. The theorem solves that natural finite-clock optimization exactly, gives a simple square-root-rate prescription, quantifies the cost of equal splitting by a KL term, and states the validity boundary against data-dependent reallocation. This is more than a normalization check or arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
