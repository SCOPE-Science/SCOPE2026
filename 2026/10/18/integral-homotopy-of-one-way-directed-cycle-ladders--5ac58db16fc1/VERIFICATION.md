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

The all-parameter theorem is proved by an exact arc-conflict description and two finite good-cover nerve arguments in RESULT.md. This verification script is an independent, finite check only, not an infinite proof.

Execute from a directory containing the delivered `verify_multipath.py`:

```sh
python3 verify_multipath.py
```

The script uses only the standard Python library. In five directed graphs with three, four, or five vertices per rim, it constructs faces both by explicit indegree/outdegree and Kahn directed-cycle tests and by independently constructed local restrictions. It asserts equality of these face sets, the formula for all enumerated faces, and reduced mod-two homology in exactly the two predicted dimensions. It prints `FINITE_CHECKS_OK` on success.

Integral torsion-freeness and the homotopy wedge are proved by the homotopy pushout and do not follow solely from finite mod-two ranks. The result does not address other orientations, partial matchings, additional cross-arcs, or unequal cycle lengths.
