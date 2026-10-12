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

# Verification

The symbolic proof checks two distinct mechanisms: a positive-series transfer ratio strictly greater than one for every factor count at least two, and the product-of-consecutive-ratios proof that splitting a prime exponent strictly increases the count. Their strictness implies the equality cases of the fixed-support bounds. The supporting polynomial identity makes both constants finite and exactly evaluable.

The accompanying `verify.py` separately implements the original recursive definition as a divisor-lattice recurrence and evaluates the binomial-polynomial forward-difference expression, then checks every positive exponent partition of total multiplicity at most 11. It verifies transfers, splits, endpoints, and prime-power/squarefree formulas; see `verification_output.txt` for actual results.

The finite test range does not prove the unbounded theorem. This record does not claim a machine-verified formal proof, an external review, or any independent audit.
