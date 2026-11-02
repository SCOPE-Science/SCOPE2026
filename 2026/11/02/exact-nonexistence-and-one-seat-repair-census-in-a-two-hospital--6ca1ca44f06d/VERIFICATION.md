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

# Reproduction

From a directory containing the embedded files, run `python3 verify_structural.py` and `python3 verify_direct.py`. Both require only the Python standard library. The structural program implements the proved original-capacity criterion; the direct program instead enumerates every feasible allocation and explicitly tests every S1 and S2 coalition at original and expanded capacities. They each assert the five original nonexistence counts `0,128,128,192,192`, and the direct program asserts all 640 failing profiles are stable at each of the two separate expansion choices. The full 11,520-case Cartesian product is processed, not sampled.

The result is strictly limited to the listed finite family; there is no extrapolation to larger markets, correlated preferences, joint placements within a single hospital, or different stability concepts. The two supplied scripts are independently structured computational checks, not an independent external scientific audit.
