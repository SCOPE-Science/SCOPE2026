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

# Verification of the terminal-gap theorem

Running `python3 verify_reflexive.py` performs direct exhaustive ideal membership and double-dual checks in both families for each integer \(3\le m\le13\). Its terminal line is `VERIFY_OK: 22 exhaustive semigroup families; independent ideal and double-dual membership`. Every normalized ideal is enumerated from the full finite gap set, retained only if its closure condition is satisfied, then tested for the defining bidual equality by direct finite-conductor membership. In particular, the code does not treat a binary-word run test as its definition of reflexivity.

The infinite theorem does **not** follow from these finite tests: its proof is the general gap partition, colon formula, and binary-word combinatorics in `RESULT.md`. No external independent mathematical audit or certification is asserted.
