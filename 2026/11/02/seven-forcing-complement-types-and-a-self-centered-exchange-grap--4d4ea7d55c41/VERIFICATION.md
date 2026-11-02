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

# Exact checks and limits

The following two standalone Python 3 verification programs were run against their actual included source files, and both returned successfully:

- `python3 kg62_direct_check.py`: checks absence of all nine-seed zero forcing sets, enumerates all 3,003 ten-seed sets, constructs every token-jump edge, then executes breadth-first search from all 1,662 optimal states. Result begins `DIRECT_PASS`.
- `python3 kg62_orbit_check.py`: independently recursively searches individual forcing sequences, partitions the 3,003 white five-sets into all fifteen full permutation orbits, and verifies all seven accepted orbits, with breadth-first searches from orbit representatives. Result begins `ORBIT_PASS`.

Both agree on: zero forcing number 10; minimum sets 1,662; exchange edges 24,270; eccentricities all five; degree histogram `{26:450,29:360,30:432,32:420}`; and unordered pair counts `{1:24270,2:202320,3:557820,4:477855,5:118026}`. The standard Python 3 interpreter is the only dependency.

The proof is a finite exhaustive classification, and the checkers constitute its repeatable certificates for the specified labeled graph. An external independent scholarly audit has not been performed; no assertion is made about other Kneser parameters or about priority over inaccessible historical computations.
