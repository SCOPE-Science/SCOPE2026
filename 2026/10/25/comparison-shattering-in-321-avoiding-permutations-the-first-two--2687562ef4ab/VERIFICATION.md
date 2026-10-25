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

The exact finite claim has two separate executable checks. `build_cert.py` enumerates all 321-avoiding permutations of lengths one through eight and evaluates the exact rank recurrence for binary comparison fibers, with an information-bound pruning rule. `verify_independent.py` enumerates the same families by successive maximum insertion and evaluates the separate depth-existence recurrence. The resulting dimensions agree at every size and are listed in `dimensions.json`.

At eight positions, the finite lower-bound certificate `tree_depth9.json` has 511 internal queries and 512 explicitly recorded distinct permutations at its leaves. The second script verifies that every leaf avoids 321 and realizes all the comparison answers along its nine-edge root-to-leaf route; this is a genuine shattered-tree certificate rather than a sample or randomly generated evidence. Running `python3 build_cert.py` followed by `python3 verify_independent.py` reproduces the two recorded outputs, the latter ending in `ALL_321_AVOIDING_CHECKS_PASS`.

The all-length VC theorem and the direct-sum amplification use the written arguments in RESULT.md, not finite experimentation. These checks establish the quoted small finite ranks and exhibit the unrestricted lower-bound construction. No exact large-size Littlestone formula, exhaustive publication-priority claim, or independent audit is asserted.
