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
# Reproduction and limits

Run `python3 check_cycle.py` and `python3 verify_transfer.py` with Python 3, no third-party packages. The first enumerates all 29 independent subsets of the labeled seven-cycle as possible column states and performs complete cyclic transfer counting for lengths six through fourteen. Its even-length totals are 1316, 7532, 45836, 291144, and 1905876, with maximum code sizes 9, 12, 15, 18, and 21. The odd control at length seven yields maximum size 10 and 980 labeled maxima, which is not part of the accepted claim.

The second program enumerates independent singleton, pair, and triple subsets, verifies every entry of the \(7\times7\) singleton–pair transition matrix, and computes the disjoint family totals through length sixteen. Both scripts were run successfully on their packaged-source counterparts before delivery. The infinite result relies on the complete proof in RESULT.md, not the finite runs. Neither code path performs a literature search or independent external audit.
