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

# Verification of the count

Execute `python verify_scroll.py` with Python 3 and SymPy. This checks the exact rational objective of genuine rank-\(d\) block-diagonal projector data, verifies noncancellation of all roots of the denominator, computes the derivative numerator, and checks its degree, squarefreeness, and lack of ramification at infinity. It verifies that the derivative has no common root with the cut-locus polynomial and that the denominator degree agrees with the cyclotomic totient count for five separate degree patterns.

The output `verify_scroll_output.txt` records the results of executing the checker from this package. The infinite-family proof is the incidence-divisor argument and Riemann–Hurwitz calculation in RESULT.md, not these finite checks. The scientific review is same-model only. No independent audit or certification is asserted.
