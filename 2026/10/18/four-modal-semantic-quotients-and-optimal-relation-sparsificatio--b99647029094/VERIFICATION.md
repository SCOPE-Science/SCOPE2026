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

Run `python3 verify.py` (standard library only) to reproduce `VERIFY_OK`. The program independently evaluates all four semantic quantifier clauses for every upset and every relation through four worlds; compares them to the prefix/suffix profile predictions; counts distinct semantics; and finds actual raw minimum arrow counts. For up to three worlds it independently checks every possible bounded nondecreasing signature against the local feasibility test, constructs witnesses and compares local optimum costs to the exhaustively enumerated minima. At five worlds, it instead enumerates all 1,048,576 extremal-row tuples, a complete class enumeration because of the proved endpoint reduction, and checks the sharp worst-case example.

Expected output:

```text
n=1 classes=2 maximal_edge_minimum=1 raw_and_profile_checks=OK
n=2 classes=16 maximal_edge_minimum=4 raw_and_profile_checks=OK
n=3 classes=279 maximal_edge_minimum=6 raw_and_profile_checks=OK
n=4 classes=7171 maximal_edge_minimum=8 raw_and_profile_checks=OK
n=5 classes=235152 maximal_edge_minimum=10 endpoint_checks=OK
VERIFY_OK
```

The quantifier-table enumeration proves only its finite inspected range; unlimited finite sizes follow from the mathematical proof in `RESULT.md`. There is no independent expert audit and no infinite-frame claim.
