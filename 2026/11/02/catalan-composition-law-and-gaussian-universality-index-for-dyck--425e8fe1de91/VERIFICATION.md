---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Greedy binary arch-factorization index counts completed shortest mixed-letter prefixes. Each arch is 0^{s+1}1 or 1^{s+1}0, subject to Dyck nonnegativity; terminal unfinished suffix must be forced 1^h. Semilength calculation yields n−index=total positive arch increments. First-step recurrences for arch-height F_h solve a quadratic and lead to exact F0=C(z(1-z)/(1-x)); substitution z=tu, x=t yields the stated composition. Independently enumerated all Dyck words n<=10 and compared exact coefficients. Dominant square-root singularity ρ(u)=(4u+1−sqrt(8u+1))/(8u²), unique near u=1, gives mean 2/3 and variance 4/27 via quasi-powers; independent rational derivative checks passed. Normality is an infinite singularity-analysis deduction, not established by finite counts.

## originality

PASS

Schnoebelen–Veron prove general greedy arch-factorization/subword-universality theory, used as PRIOR. The previously published fixed-defect Dyck rationality framework and low-defect coefficients are acknowledged as PRIOR. A distinct published Resultary record gives binary *unrestricted* word index law (1+z)/(1-z−2uz²), not the Dyck Catalan joint composition. Neither inspected general arch algorithm nor fixed-defect rationality alone states the single uniform all-defect Catalan composition with large-index Gaussian law.

## value

PASS

A global bivariate generating function and exact normal fluctuations for a natural Dyck statistic connects Catalan paths to subsequence-universality theory. It is not merely another fixed-defect coefficient: it simultaneously determines every defect and macroscopic scaling, a useful exact combinatorial statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
