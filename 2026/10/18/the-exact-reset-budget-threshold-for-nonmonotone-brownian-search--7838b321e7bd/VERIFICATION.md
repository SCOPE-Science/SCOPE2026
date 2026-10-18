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

The standalone `verify.py` reconstructs the exact rational degree-28 certificate from the stated finite sums; it does not import any generated coefficient table. On each of four rational subintervals it computes the 29 degree-28 Bernstein coefficients by exact fractions, checks all are strictly positive, and verifies the four stated minima. It separately establishes the exact positive rational witness at \(q=6/7\) for 22 attempts. An independent numerical check differentiates the original finite renewal formula by central differences at 42 parameter pairs, comparing with the analytic derivative. The latter finite test is diagnostic, not the proof of the infinite-parameter theorem.

The script was run from its containing directory with `python verify.py` and completed without exceptions. The theorem requires the normalizing convention that the Brownian generator is \(D\partial_{xx}\), rather than \(D\partial_{xx}/2\). The statement is about unconditional time to target absorption **or** budget exhaustion. The source's renewal formula is acknowledged as prior work; the new item is the exact monotonicity boundary and its complete rational sign certificate. Independent validation remains unperformed.
