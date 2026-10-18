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

# Reproducible verification and its scope

`verify.py` is standalone and requires Python 3.8 or later, with no external data or packages. Run `python3 verify.py` and compare stdout with `verification_output.txt`.

The verifier enumerates every subset of five-cube vertices of sizes one through five (242824 subsets total). No subset of size under five passes the fort predicate; precisely 32 five-subsets pass, and these coincide exactly with the 32 open neighborhoods. It also verifies the five displayed disjoint forts, obtains the maximum open packing of four by examining compatible center subsets through cardinality five, and checks every six-element subset of the 32 cube vertices, finding allowed even-vertex counts 0, 1, 5 and 6 only. The parity-specific six-fort counts are 80, 16, 16 and 80.

This does not enumerate every fort of every size, and such an enumeration is unnecessary: the general upper bound is proved from the minimum-fort and six-fort structure in `RESULT.md`. All finite statements used in the proof are either argued mathematically or exhaustively checked. No external certificate, independent scientific audit, or infinite-dimensional claim is implied.
