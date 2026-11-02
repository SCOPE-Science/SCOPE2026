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

# Exact computational checks and scope
The included `verify_even_quartic_graph.py` is standalone Python 3 code using only the standard library. It implements explicit residue-field multiplication, including quotient-polynomial fields, forms the full graph of \(t^4+at^2\), and enumerates all ordered pair sums. It compares **the complete histogram including zero-representation targets** with a separately coded closed-form prediction for every chosen coefficient.

Command: `python verify_even_quartic_graph.py`

Expected terminal line: `VERIFY_OK finite_fields=41 coefficient_cases=618`.

The field orders include 31 prime fields through 127, as well as nonprime fields of orders 4, 8, 16, 9, 27, 81, 25, 125, 49, and 121. All coefficient values are checked in fields of size at most 49; representative values are checked for larger fields. The verifier independently checks that each predicted spectrum counts exactly \(q^2\) target points and accounts for exactly \(q^2\) ordered input pairs, and it compares the full tuple multiplicities directly rather than merely matching sumset sizes. Numerical checks cannot establish universal correctness or historical originality; those require the mathematical proof and source analysis.
