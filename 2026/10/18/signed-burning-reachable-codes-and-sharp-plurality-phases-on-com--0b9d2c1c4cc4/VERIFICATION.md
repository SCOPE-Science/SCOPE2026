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

# Verification of the stated balanced signed-burning theorem

The self-contained Python 3 file `verify_burning_multipartite.py` implements the spread-before-ignition burning game directly. Its actual recursive process never reads the proposed closed formula or invokes a switching trick in order to generate terminal outcomes; each unburned vertex receives the strict majority of signed colours from already-burned neighbours, followed by one freely selected ignition. The model's termination is handled when all vertices have burned in the spread step.

For all 37 integer-partition multipartite graph types on two to seven vertices with at least two parts, the program independently enumerates the reachable terminal signed vectors for all 1,354 balanced edge-signing classes (using a first-coordinate normalization only to avoid double counting). The enumerator's 14,772 terminal-state appearances agree exactly with the theorem's proposed antipodal code. Each instance's computed minimum green count, the maximum distance over its balanced signings, and the count of signings attaining that maximum agree with the stated arithmetic expressions.

**Reproduction:** run `python3 verify_burning_multipartite.py` in the directory containing this document. Expected stdout:

```
VERIFY_OK graph_types=37 signings=1354 terminal_states=14772 max_order=7
```

**What is not certified:** computational enumeration terminates at graph order seven. No independent audit or general-order computer proof has been performed. The all-order theorem is justified by the complete three-round and Hamming-distance arguments in `RESULT.md`; the script is a bounded consistency check.
