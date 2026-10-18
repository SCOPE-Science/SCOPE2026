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
The result follows from the two-sided multiplication law and a complete orbit–stabilizer derivation. In each of eleven finite test cases, `checker.py` independently computes group multiplication, centralizer orders, element-count strata, and class counts, and compares these with the predicted graph sum. The tests include fields of orders 2, 3, 4 and 5, multiple and oppositely oriented arrows, loops and disconnected quivers. It also evaluates the six-vertex bridge witness and verifies equality of total group order and class number and inequality of the class-size-3 coefficients.

Run: `python3 checker.py`.
Expected last line: `ALL_QUOTIENT_UNIT_CLASS_TESTS_PASSED 11`.
The checker exhausts only the displayed finite cases, not all quivers or all fields. No independent audit or external certification is claimed.
