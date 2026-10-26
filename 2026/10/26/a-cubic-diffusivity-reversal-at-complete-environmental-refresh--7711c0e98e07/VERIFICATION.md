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

The analytical proof uses iid regeneration blocks, explicit four-step static-walk moments, an absolutely convergent power series, and a closed generating function in the fair-arrow specialization. Its uniform remainder follows from the deterministic bound \(|Z_n|\le n\).

To reproduce: install `requirements.txt` and execute `python verify.py`. This exact symbolic checker enumerates all \(2^n\) step sequences for each \(1\le n\le4\), integrates their environmental weights in terms of \(\mathbb EB\) and \(\mathbb EB^2\), checks the moment table and cubic coefficients, and algebraically checks the fair-arrow generating function and rational variance. It completed successfully.

Finite path enumeration alone is not a proof of asymptotic expansion or of global all-\(p\) formulas. Those deductions, as well as the uniform tail estimate and the two-cycle decomposition, are written in `RESULT.md`. The exact crossover boundary coefficient vanishes and its next term is not determined here. Independent validation has not been performed.
