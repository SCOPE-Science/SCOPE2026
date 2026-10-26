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

# Computational verification and scope

Run `python3 verify.py` with the standard Python interpreter. The script checks all binary necklaces of circumferences 2 through 14, comparing two independent membership algorithms: (a) greedy subsequence search through every source rotation and (b) exhaustive size-\(m\) selection of source positions with all rotations of the selected target. The algorithms agree on all instances. Exactly one of the 1,182 necklaces at circumference 14 fails the bound, and none at smaller circumferences does. The exact exception and a shortest missing target are printed, together with explicit position witnesses for all length-six target necklaces. Representative larger family members are also checked.

The finite exhaustive search establishes only the finite cutoff. The universal upper bound and the infinite obstruction family have separate combinatorial proofs in `RESULT.md`. No independent audit is claimed.
