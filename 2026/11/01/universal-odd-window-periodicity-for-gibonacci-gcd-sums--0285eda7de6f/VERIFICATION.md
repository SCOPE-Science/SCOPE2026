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

# Reproducibility and limits
The standalone script `verify.py` uses the original second-order recurrence, independently recomputes the first \(12\) consecutive window sums and squared-window sums for each test, and compares their gcds with the closed expressions and shifted expressions. Those window-gcd comparisons also rely on the explicitly proved order-two and order-three recurrences to identify the infinite-family gcd. The script checks all nonzero pairs \((a,b)\in[-6,6]^2\) and positive odd lengths less than \(60\): \(168\) seed pairs, \(5{,}040\) window cases, \(5{,}040\) periodic-shift comparisons, and \(9{,}240\) norm identities. All passed in the package construction run. Run `python3 verify.py`. No dependency other than Python 3 is needed.

The argument for every integer pair and every odd length is a symbolic proof in `RESULT.md`. No infinite claim is certified by finite enumeration; no independent review has been performed. The effective bound is not generally the least period. Literature overlap remains a genuine risk because strong previously published gcd formulas are essential ingredients.
