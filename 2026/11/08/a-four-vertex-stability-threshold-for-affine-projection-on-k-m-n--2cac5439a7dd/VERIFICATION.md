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

The symbolic checker `verify_tripartite_affine_projection.py` constructs the exact three-class Gram inverse and the vertex kernel integrals. It produces universal positive-coefficient certificates for the competitor row comparisons in both sign regions and for the amplification-two threshold. It also checks the fixed-smaller-part limiting formula. Independent rational Gram inversions and edgewise absolute kernel integrations were carried out for 28 parameter pairs; these finite tests corroborate, but do not replace, the coefficient-based universal proof.

Exact reported checks:

```
THREE_CLASS_GRAM_INVERSE_AND_EXPLICIT_NORM_FORMULA_OK
UNIVERSAL_VERTEX_DOMINANCE_POSITIVE_COEFFICIENT_CERTIFICATES_OK [('low', 'BminusA', 189, 225), ('low', 'BminusC', 99, 115), ('high', 'BminusA', 143, 156), ('high', 'BminusC', 104, 105)]
EXACT_TWO_THRESHOLD_AND_LIMIT_CERTIFICATES_OK
INDEPENDENT_DENSE_EXACT_GRAM_KERNEL_INTEGRATIONS_OK 28
ALL_TRIPARTITE_AFFINE_PROJECTION_CHECKS_OK
```

No external independent audit was performed. An unexamined potentially relevant paper on weighted finite-element projection is an originality-review limitation.
