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

The standalone Python 3 program `verify_eop.py` independently builds the rook graph from cell adjacency and tests the original definition that two selected edges must have no third connecting edge. It enumerates all EOP sets for 12 labeled boards and compares the exact maximum sizes and optimizer counts with the stated closed forms; its recorded output is `verification_output.txt`. The 12 boards contain 30,977 nonempty EOP sets in total, and all tests passed.

The enumeration is exhaustive **only for the listed finite boards**. The infinite classifications, parity bound, factorial formulas, and asymptotic are established by the case proof in `RESULT.md`, not by extrapolating finite data. This verification does not check unindexed publication records or provide independent audit evidence.
