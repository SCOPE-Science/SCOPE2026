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

# Verification details

Run both standalone Python 3 programs in this directory: `python3 check_gp.py` and `python3 check_lcf.py`. Both require only the Python standard library and have been replayed directly from these source files. Compare each printed compact JSON record to `check_gp_output.json` and `check_lcf_output.json`, respectively.

The first program enumerates all perfect matchings from the explicit \(GP(10,2)\) edge list, tests \(36\cdot2^{10}=36864\) candidate matching subsets, evaluates all \(630\) unordered matching pairs for eight-edge symmetric differences, and exhausts all breadth-first distances. The second program independently constructs the same graph by LCF offsets, enumerates exact covers with a different branching heuristic, checks each subset by intersecting all other-match difference families, enumerates legal local replacements on every four-match-edge subset, and independently checks connectivity, eccentricities, degree profiles and subset-polynomial classes.

These are complete finite certificates conditional only on the explicitly proved recursive coverage invariants and reproducible Python execution. No verification claims are made about other fullerenes or inaccessible publications. Independent external audit has not been performed.
