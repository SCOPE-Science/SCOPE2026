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

The analytical proof uses two strict Cauchy–Schwarz inequalities on exponential-rate moments. The first bounds the positive function \(Q\); the second proves \(Q'<0\), which makes the cut-off slope's derivative switch sign at most once. Equality at the critical cutoff is treated as a boundary with no interior minimum. The implicit-function theorem establishes the critical onset; a two-slowest-rate expansion proves the finite-mixture limit.

Reproduce the numeric checks with `python verify.py` using Python 3 and the standard library. The verification run completed: exact two-rate cutoff and minimum calculations; 3,000 finite mixtures each tested at two cutoffs; 6,000 derivative-vs-finite-difference comparisons; and finite-support large-cutoff checks. Numerical sampling is not a proof for all rate laws. Finite third moments, a fixed conditioning cutoff, and finite-support hypotheses for the asymptotic formula are indispensable. No independent validation has been performed.
