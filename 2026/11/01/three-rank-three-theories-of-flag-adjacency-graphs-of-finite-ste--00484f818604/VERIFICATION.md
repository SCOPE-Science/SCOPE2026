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
# Verification record

The mathematical proof is in `RESULT.md`. Run the standalone checks with Python 3 and only the standard library:

```
python3 verify_designs.py
python3 verify_ef3.py
```

The captured outputs are `verify_designs.out` and `verify_ef3.out`. The direct checker validates each finite design's \(2\)-design property, enumerates full third-vertex equality/adjacency profiles for all ordered pairs, and checks all three claimed classes against examples with \(6,12,20,21,36,52,105,150,186\) flags. The independent checker computes exact first-order three-round types recursively through all ordered triples on six representative graphs. Both compare the universal design class with the Johnson graph \(J(7,3)\); the direct checker also identifies an explicit induced-claw witness in that Johnson graph.

These computations are corroboration, not a proof of the infinite all-design claim. The proof uses the design identities and game lemma to establish every quantifier. Program executions have not been independently audited; external validation is unperformed.
