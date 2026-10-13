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

# Reproducibility and limits

With Python 3 and no third-party packages, run `python3 verify.py` beside this document. The script checks the full operator-level support semantics of the fixed formula against its functional-dependency/subteam characterization on all 258 teams over domains of size one or two, plus 180 sparse three-element-domain teams. It verifies the proposed 2-SAT algorithm against exhaustive 97,336 three-element-domain teams with at most two rows per first-coordinate fibre, plus 1,400 randomized four-element-domain teams admitting non-Boolean third coordinates. It separately checks 5,180 source three-CNF instances against the target's full-cover functional-assignment characterization, including exact three-tuples-per-fibre and padding constraints. The checked execution printed `VERIFY_OK direct_teams= 258 sparse_teams= 180 two_fiber_multi_value_cases= 1400 three_value_exhaustive_two_fiber= 97336 sat_bridge_cases= 5180`.

Finite tests neither certify the unrestricted mathematical proof nor establish literature originality. The symbolic argument handles arbitrary finite domain sizes, all teams meeting the stated size restrictions, and the general complexity bounds. This record has received only self-review; independent audit has not been performed.
