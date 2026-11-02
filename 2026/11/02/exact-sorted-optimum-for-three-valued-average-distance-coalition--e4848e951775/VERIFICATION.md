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

`check.py` contains an exact-arithmetic exhaustive verifier for multiplicities from one through seven for each of the three types. It checks 42,189 two-group type-count allocations and five gap pairs, including partitions containing singleton coalitions. It also checks the corresponding one-group inequality.

Command: `python3 check.py`

Observed output:

`VERIFY_OK exact_count_profiles=343 exact_two_group_partitions=42189 gap_pairs=5 singleton_allowed=True`

The proof of the all-size, real-gap statement uses the explicit coefficient identity, concavity for each fixed group size, and exact endpoint inequalities. Finite enumeration alone would not prove it. The main manuscript supplies the universal argument; no external formal proof or independent audit was performed.
