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

# Verification notes

For reproducible exact computations, run `python3 verify_pell_cubic.py` using Python 3 and no nonstandard dependencies. The script calculates four consecutive cubic Pell-window sums for all integer half-lengths from \(1\) to \(120\), checks the proposed GCD, the algebraic initial-window formula, the reversible recurrence, the Pell norm, and the modulus-\(16\) residue calculation. Four windows suffice for the infinite GCD because the order-four recurrence has leading and constant coefficients equal to \(1\).

Finite calculations do not prove an unbounded theorem. The proof is the symbolic prime-by-prime argument in RESULT.md. The exceptional valuation at \(7\) is established by the nonvanishing of the initial-window brackets modulo \(7\); the extra \(3\) is derived separately. This document does not assert an independent audit.
