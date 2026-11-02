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

# Verification record

The mathematical proof uses a bijection that prunes a marked set of pendant vertices from a uniform labeled Cayley tree. The remaining tree is again uniform; its noncentral leaf count is the number of unoccupied Prüfer-word letters outside the marked center. The exact probability-generating function follows by inclusion–exclusion. The proof of strict ordering uses the explicit derivative of the vacancy probability, and the final equality follows from the core-size-one and core-size-two boundary cases.

Run `python verify.py` with Python 3 standard library to enumerate every Prüfer word of lengths one through six (orders three through eight). The test compares the actual enumerated leaf/bouquet cross-moments with the formula as exact rational numbers, and checks positivity and the ordering with the proper endpoints. The tested script returned `95 exact rational assertions passed`. These finite tests do not certify a theorem for larger sizes, which is supplied by the analytic proof.

No independent audit has been performed. No external infinite formal certification is claimed. Historical publication priority beyond the documented comparisons is not independently certified.
