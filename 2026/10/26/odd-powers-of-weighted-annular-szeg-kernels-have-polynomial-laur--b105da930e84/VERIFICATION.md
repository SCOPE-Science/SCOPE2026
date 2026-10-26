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

The exact result is proved by theta quasi-periodicity, a finite triangular principal-part calculation, and uniqueness of a globally holomorphic quasi-periodic Laurent function. No numerical finite check is used as a proof of an infinite identity.

The accompanying `verification/check_odd_powers.py` uses 80-digit `mpmath` and separately forms the Laurent powers and their predicted polynomial-coefficient sums. Executed successfully with 123 numerical kernel/cubic comparisons, plus positivity and leading-term checks, for several positive weights and odd powers through seven. The analytic proof handles every admissible parameter. The thin-annulus constant follows from a dominated midpoint Riemann sum; three finite-width numerical ratios are corroborative only.

Boundary cases \(q=0\), \(q=1\), \(r=0\), nonpositive weights, and even exponent powers are outside the theorem. Coefficient positivity is asserted on integer indices, not on all real inputs. Absolute historical priority, new zero-process formulas, and independent audit are not established.
