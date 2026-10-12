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

The proof was checked directly from the definition of a signed dominating function. For a barbell \(B_n\), non-bridge vertices yield the clique-sum constraints and the two bridge endpoints yield the two additional endpoint-sign constraints. The even and odd cases were then derived separately from parity.

The embedded `verify_signed_barbell.py` script exhaustively enumerates all \(2^{2n}\) signings for each \(2\le n\le8\), computes the exact weight distribution satisfying the four derived inequalities, and compares it coefficientwise with the closed formulas. It also checks the stated minimum weights and multiplicities. The packaged replay result is:

`VERIFY_OK n_range=2..8 labelings=87376 valid_functions=12123 coefficient_checks=31 minimum_checks=7 max_order=16`

Finite enumeration is not used to establish the all-\(n\) theorem. The unproved limit is bibliographic completeness: the inspected sources and searches do not rule out every unindexed prior statement.
