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

# Reproduce the finite proof

Run `python3 check_gp.py > gp_replayed.json` and `python3 check_lcf.py > lcf_replayed.json` from the directory containing the programs. Compare each resulting JSON object against `gp_output.json` and `lcf_output.json`. Only Python 3 standard-library modules are needed.

`check_gp.py` constructs \(GP(8,3)\), checks all \(\binom{16}{k}\) seeds for \(0\le k\le6\) by deterministic synchronous mask closure, generates all legal six-set exchanges, and computes BFS from each of the 1704 minimum states. `check_lcf.py` independently builds the graph via the LCF notation `[5,-5]^8`, verifies an explicit graph isomorphism, applies sequential forces, constructs exchanges by shared five-subsets, and performs independent all-origin BFS. The programs assert the exact census, 16560 jump edges, zero slide edges, and radius and diameter equal to six. The first checks a concrete sharp witness route.

Because the vertex universe consists of sixteen vertices and the programs traverse all candidate subsets through cardinality six, all minimum sets are considered. The reconfiguration graph construction is complete because every one-vertex replacement is tested; a breadth-first search computes exact shortest-path distances in the resulting unweighted graph. No timeout or sampled partial search substitutes for exhaustive enumeration.

This is computational verification for one finite graph, not a proof for all generalized Petersen graphs. No independent external audit is asserted.
