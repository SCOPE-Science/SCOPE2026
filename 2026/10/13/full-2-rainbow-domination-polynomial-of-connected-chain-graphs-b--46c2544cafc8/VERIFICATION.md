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

# Verification procedure and limits

Run `python3 verify_rainbow_chain.py` with only the Python standard library. The script enumerates four-subset-label assignments directly on explicitly constructed adjacency sets and independently evaluates the inclusion–exclusion polynomial. It checks every coefficient for 111 chain degree profiles of order at most eight, comprising 3,843,216 labelings and 1,651 polynomial coefficient comparisons. Two exact named boundary examples and leading coefficient checks are included.

The exhaustive small-graph census checks implementation and combinatorial boundaries. It is not a proof for unbounded graph order. The general argument is the complete disjoint classification and nested-neighborhood coverage equivalence in `RESULT.md`.
