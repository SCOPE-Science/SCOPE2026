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

The mathematical proof establishes the theorem for every finite set and every nonempty refinement-closed family. The accompanying finite checker is a corroborating experiment, not an infinite proof.

Run from the extracted package directory:

```
python3 verify_partition_rank.py > replay.txt
cmp replay.txt verify_partition_rank_output.txt
```

The program enumerates all \(1099\) labeled simple graphs through five vertices and tests exact VC/Littlestone/graph-chromatic identities. It also checks \(12070\) compatible graph/query-history combinations on four vertices against the quotient chromatic formula. Expected final line:

```
ALL_PARTITION_SHATTERING_CHECKS_PASS 1099
```

Only finite cases are enumerated. No independent audit or external certification has been performed. Published-priority searches may miss relevant unindexed literature.
