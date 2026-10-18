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

# Reproduction and limitations

Run `python3 verify.py` in a standard Python 3 environment (no third-party packages). The first check explicitly enumerates all functions whose source root is fixed, constructs principal upsets from the full ancestor relations, and tests the exact back condition at each source point; it agrees with the closed counting formula on 50 profile pairs including 16 zero-count pairs. A canonical JSON encoding of the exhaustive table has SHA-256 `ba693d7d1c74b658e6560606d13fe8c3baed6344fe2e388d96ead118ddbc171b`. The second check, implemented independently as a subset-of-covered-target-branches dynamic program, agrees with inclusion–exclusion on 13,260 parameter pairs (10,521 positive); its largest exact count is 70,543,872.

These are finite consistency checks, not an exhaustive investigation of all input sizes. For unbounded profiles, correctness rests on the branchwise bijection and inclusion–exclusion proof in `RESULT.md`. This check does not establish bibliographic uniqueness. No independent mathematical audit has been performed.
