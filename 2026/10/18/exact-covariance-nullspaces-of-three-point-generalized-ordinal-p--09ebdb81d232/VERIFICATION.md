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

# Reproducibility checks

Run `python verify.py` with a standard Python 3 interpreter. There are no dependencies beyond the standard library.

The checker enumerates every possible word of lengths three, four and five over alphabets of sizes one through four. It accumulates exact rational probabilities for all ordered pairs of three-point weak-order pattern indicators at lags zero, one and two. It forms the exact symmetric thirteen-by-thirteen asymptotic covariance, computes rational Gaussian-elimination rank, and checks all claimed kernel vectors.

The nine positive-mass test cases include three binary, three ternary and two quaternary mass vectors, as well as the deterministic singleton alphabet. All passed: ranks \(0,3,10\) in the respective regimes, and every specified null direction multiplied to exactly zero.

The mathematical proof is independent of enumeration: the decisive infinite-family argument is the Hoeffding sum-of-squares coboundary characterization, followed by the three-symbol algebraic rigidity argument. The checks do not establish a result for dependent observations, infinitely supported laws or parameter-estimation-adjusted chi-square tests.
