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

# Reproduction

Run `python verify.py` using Python 3 and its standard library. The rational checker verifies the precision-dependent representability of each synthetic addend, strict one-ulp accumulator advance, exact total sum and both analytic inequalities for precision 3 through 10 and endpoint exponent 1 through 5. It additionally tests thousands of independent positive representable additions under a local rounding implementation. All comparisons use exact rational arithmetic. The algorithm is not an infinite proof; the result follows from the midpoint-gap and geometric series derivations in RESULT.md.

No floating hardware subnormal behavior, finite exponent range, mixed-sign cancellation, or independent assessment is verified or claimed.
