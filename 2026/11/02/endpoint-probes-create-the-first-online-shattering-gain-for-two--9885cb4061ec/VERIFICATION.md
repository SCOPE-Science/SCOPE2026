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
# Reproducibility

Execute `python verify_lattice_paths.py` in the directory holding `depth6_tree.json` using Python 3 and the standard library only.

Verified exact recurrence outputs, listed in order of heights one through ten:

- Full vertex-incidence Littlestone dimensions: `1,2,3,3,4,4,4,5,5,6`.
- Middle-only Littlestone dimensions: `1,2,3,3,4,4,4,5,5,5`.
- Hypothesis counts: `3,6,10,15,21,28,36,45,55,66`.
- Exhaustive VC census for heights one through six: `1,2,2,2,2,2`.

The recurrence enumerates every query on every reachable exact version-space mask; ranks are therefore exhaustive for the finite domains. The program also generates all monotone paths independently by east-step positions, confirms full ranks, and verifies the 63-node depth-six adaptive tree on 64 distinct consistent witnesses. A successful run ends with `ALL_TWO_EAST_STEP_PATH_CHECKS_PASS`.

The universal VC dimension and logarithmic online bounds are mathematical arguments supplied in `RESULT.md`; the finite experiments by themselves do not prove them. Historical priority and independent scientific audit are not established by this computation.
