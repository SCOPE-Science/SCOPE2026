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

The supplied `verify_diam4.py` is a standalone Python 3 script requiring only the standard library. It constructs all 240 canonical diameter-four trees (multiplicity vector in `range(4)^4`, with at least two nonzero-depth branches), evaluates two independently coded complete rank-three first-order signatures, and compares all nine minimal representatives under a third, literal three-round Ehrenfeucht–Fraïssé minimax recursion. The output file `verification_output.txt` records 240 canonical inputs, 9 types, the exact representative list and orders, 81 cross-check games, and `VERIFY_OK`.

The symbolic three-round truncation argument in RESULT.md is required to pass from those 240 finite cases to the unrestricted class. The program alone is not evidence of equivalence for arbitrary orders. The test gives a complete finite enumeration only within the mathematically justified canonical family. Checks did not include a formal proof assistant or independent external audit.
