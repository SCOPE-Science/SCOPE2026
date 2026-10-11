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

Run `python verify.py` with a standard Python 3 interpreter. The script has no external dependencies.

It checks the published Rudin complex has 41 tetrahedral facets and face vector \((14,66,94,41)\). It then implements the recursive definition of non-evasiveness directly, with a one-vertex complex as the base case and with exact canonical deletion and link operations.

For each of the fourteen vertices it verifies both required first-step branches, \(R-v\) and \(\operatorname{lk}_R(v)\). It then tests every remaining vertex in every first deletion to obtain the exact second-step profile. The expected terminal line is:

`VERIFY_OK facets=41 f=14,66,94,41 roots=14/14 second_profile=11x6,9x4,5x4 second_total=122 memo_states=28708`

The computation is exhaustive. It does not use random choices, approximate arithmetic, external solvers, or timeout-based conclusions. The result proves only the stated first- and second-step admissibility facts; it does not enumerate complete recursion trees.
