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

The finite exact-rational checker `VERIFY.py` enumerates each integer occupancy composition, weighting it by the full multinomial probability, and independently computes the Pearson statistic and occupancy-frequency covariances. It compares against both the binomial second-difference and explicit quadratic closed form. On the specified \(m=2,\ldots,7\) and \(n=2,\ldots,10\) bounded composition grid, it also tests two arbitrary nonlinear box-score functions to exercise the universal curvature identity, plus six integer instances of the doubleton Pell equation.

Run from the extracted directory with `python3 VERIFY.py`. The script is deterministic, needs no internet or external package, and prints its test counts. The analytic proof is responsible for the unbounded \(m,n\), general real \(f\), complete arithmetic classification, and Poisson scaling; no finite enumeration substitutes for those arguments.

Independent scientific assessment was not performed. Historical priority cannot be certified by targeted database and primary-literature comparisons alone.
