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

# Reproducible checks

Run `python3 checker.py` with Python 3 and no external packages. For each \(1\le n\le6\), the checker enumerates all \(n^n\) functions on the involutive chain. For \(7\le n\le10\), it enumerates every nondecreasing function (all candidates that could meet (M)). It evaluates the original universally quantified (M), (Pos), and (Con) axioms directly and independently compares them with the monotonic/threshold/plateau characterization and the exact total and top-preserving formulas.

The completed execution reported `EXHAUSTIVE_CHECK_OK`. Exact outputs for \(n=1,\ldots,10\) are total counts \(1,2,5,13,40,115,415,1281,4956,16086\) and top-preserving counts \(1,2,3,9,21,70,210,735,2485,8946\). All together the program evaluates 174,908 candidate functions. The proof in `RESULT.md`, rather than the finite computations, establishes the statements for unbounded chain sizes and the limiting density.

The historical relationship to Celani–Menchón–Miguelez is not independently validated: only the public abstract and a detailed secondary overview were accessible, not the full original manuscript. The relevant equations are restated explicitly in the result so that the mathematical statement is self-contained. No external audit has been performed.
