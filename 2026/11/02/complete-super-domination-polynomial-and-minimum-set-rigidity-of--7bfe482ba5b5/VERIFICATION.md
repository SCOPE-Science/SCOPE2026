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
# Reproducible finite checks

Run `python3 verify_rook.py` from the extracted package. The script constructs graph neighborhoods independently, tests the original unique-neighbor requirement for every chosen omitted subset, and compares the entire cardinality polynomial against a recurrence enumerating labeled star forests by a distinguished row and inclusion-exclusion for isolated rows and columns.

Exhaustively checked boards and valid complements: \((2,2):9\), \((2,3):24\), \((2,4):47\), \((3,3):88\), \((3,4):272\), \((3,5):774\), and \((4,4):1161\). It also independently enumerates all \(\binom{25}{6}=177100\) size-six omitted subsets of the five-by-five board and finds exactly \(400\) feasible, all described by the two-star templates. The extremal formula is compared against the symbolic recurrence at five larger board profiles without exhaustive full-board enumeration. The included `verification_output.txt` records one successful execution.

No finite computation proves the general coefficient-extraction theorem, which is proved by the local-witness partition and labeled exponential formula in `RESULT.md`. No independent audit has been performed.
