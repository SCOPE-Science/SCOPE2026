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

# Reproducibility and verification

Run `python verify_tripartite.py` with Python 3.9+ and its standard library. The program independently constructs every edge of a labeled complete tripartite graph and computes the exact jamming-law distribution by rational recursion over vacant-vertex bitmasks. It compares that computation with a separately programmed count-state recursion using only the three remaining part sizes.

Six finite graphs undergo exact rational distribution comparison, while twenty further parameter pairs undergo exact normalization, parity/support and total-variation-bound checks. Fourteen algebraic product checks, nine larger-limit comparisons, and two binomial-law checks complete 117 assertions. A verified invocation returned `PASS 117 independent finite-state, rational, limit-support, and bound checks`.

At \(n=100\) the computed probability of two remaining vacancies for \(r=2\) is approximately \(0.49286074\), compared with limiting value \(1/2\). For \(r=3\) the three-vacancy probability is approximately \(0.23958725\), compared with limiting value \(1/4\). These finite calculations check applications of the all-size proof but do not establish asymptotics on their own.

The mathematical proof is given in `RESULT.md`, including the marked-impurity race inequality, its telescoping product, the summation-by-parts step and the coupling bound. No external solver, unprovided data, or formal proof system is required. Self-review is complete; an independent audit has not been performed.
