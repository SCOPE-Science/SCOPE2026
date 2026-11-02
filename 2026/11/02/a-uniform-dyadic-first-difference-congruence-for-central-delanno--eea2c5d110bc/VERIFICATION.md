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

The standalone `verify.py` uses exact integer arithmetic and the exact three-term central Delannoy recurrence to check 512 first-difference cases with increments \(32,64,96,128\) and numerous dyadic-difference cases with odd multipliers and both shift residues. It confirms the low-degree weight coefficients, the parity of the cubic expression for all four residues modulo four, and the analytic tail-index inequalities through \(10000\). The all-index theorem follows from the written Vandermonde and polynomial-coefficient bounds, not from these finite checks. The periodic difference quotient is interpreted in \(\mathbb Z_2\), allowing non-integral rational quotients with odd denominators. No independent audit was performed.
