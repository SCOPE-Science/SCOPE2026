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

# Verification of signed-tree obstruction classification

Run the included standalone program with `python3 verify.py` (Python 3 standard library only). It constructs 15 trees with odd branch counts three, five and seven, and leaf level two through six. For each, it verifies graph connectivity and tree size, every incident signed sum, the exact integer matrix equality \(Kd=(k+1)\mathbf1\), every individual signed cut and the total negative-edge count. Three finite-angle checks per tree confirm the scalar invariant-circle update within stated floating-point tolerance. Integer-only tests cover the least-common-multiple exclusion for all smaller bipartitions and the unique feasible cardinality/sign parameter choice at nine vertices.

Actual program output:

```
VERIFY_OK: 15 family instances; 9-node sharp witness; exact signed cuts;
          exact Kd vectors; scalar invariant-line evaluations; n<=8 arithmetic obstruction.
```

The tree incidence lemma, all-order size lower bound, unique nine-vertex signed topology, and tangent-space conclusion are proved in `RESULT.md` for all stated parameters. Finite computations do not substitute for those proofs. The script uses a conservative positive step based on the Laplacian bound; it does not numerically certify arbitrary-parameter manifold transversality, which follows analytically. Independent audit has not been performed.
